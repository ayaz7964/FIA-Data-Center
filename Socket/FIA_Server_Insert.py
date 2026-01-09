import socket
import json
import mysql.connector
import threading
from datetime import datetime
from IP import get_ip_address


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)


config = load_config()


def receive_data(client_socket):
    # Receive data length
    data_length = int(client_socket.recv(1024).decode('utf-8'))

    # Acknowledge data length
    client_socket.sendall(b'ACK')

    # Receive data in chunks
    received_data = b""
    while len(received_data) < data_length:
        chunk = client_socket.recv(1024)
        received_data += chunk

    return received_data.decode('utf-8')


def handle_client(client_socket):
    # Receive JSON data from client
    json_data = receive_data(client_socket)
    data_dict = json.loads(json_data)

    # Extract query and data from JSON
    query = data_dict.get('query')
    data = data_dict.get('data')

    # Get current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"[{current_time}] Received query from client:", query)
    print(f"[{current_time}] Received data from client:", data)

    try:
        connection = mysql.connector.connect(
            host=config["HOST"],
            user=config["USER"],
            password=config["PASSWORD"],
            database=config["DATABASE"]
        )
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()

        # Send "True" back to client if insertion was successful
        client_socket.sendall(b'True')
    except Exception as e:
        print("Error executing query:", e)
        # Send "False" back to client if insertion failed
        client_socket.sendall(b'False')

    # Close connection
    client_socket.close()


def main():
    # Define host and port
    host = get_ip_address()
    config["IP"] = host
    port = config["PORT-2"]
    save_config(config)
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening on port", port, " and host ", host)

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        # Handle client connection in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    main()
