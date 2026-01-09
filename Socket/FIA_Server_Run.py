import socket
import json
import mysql.connector
from datetime import datetime
from IP import get_ip_address

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def send_data(client_socket, data):
    # Convert data to JSON
    json_data = json.dumps(data, default=str)

    # Send data length first
    client_socket.sendall(str(len(json_data)).encode('utf-8'))

    # Wait for acknowledgement
    client_socket.recv(1024)

    # Send data in chunks
    chunk_size = 1024
    for i in range(0, len(json_data), chunk_size):
        client_socket.sendall(json_data[i:i + chunk_size].encode('utf-8'))

    # Wait for acknowledgement
    client_socket.recv(1024)


def handle_client(client_socket):
    # Receive query from client
    query = client_socket.recv(1024).decode('utf-8')
    print("Received query from client:", query)
    config = load_config()

    # Execute query in MySQL database
    try:
        connection = mysql.connector.connect(
            host=config["HOST"],
            user=config["USER"],
            password=config["PASSWORD"],
            database=config["DATABASE"]
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()

        # Convert date format to string before serialization
        for row in results:
            for key, value in row.items():
                if isinstance(value, datetime):
                    row[key] = value.strftime('%Y-%m-%d %H:%M:%S')

        cursor.close()

        connection.commit()
        connection.close()

        # Send data to client
        send_data(client_socket, results)
    except Exception as e:
        print("Error executing query:", e)
        error_response = {'error': str(e)}
        send_data(client_socket, error_response)

    # Close connection
    client_socket.close()


def main():
    config = load_config()
    # Define host and port
    host = get_ip_address()
    config["IP"] = host
    port = config["PORT-1"]
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
        handle_client(client_socket)


if __name__ == "__main__":
    main()
