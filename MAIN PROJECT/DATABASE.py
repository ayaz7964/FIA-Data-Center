import socket
import json


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def receive_data(client_socket):
    json_length = int(client_socket.recv(1024).decode('utf-8'))
    client_socket.sendall(b'ACK')
    received_data = ""
    while len(received_data) < json_length:
        chunk = client_socket.recv(1024).decode('utf-8')
        received_data += chunk
    client_socket.sendall(b'ACK')
    return received_data


def RunQuery(query):
    ip_data = load_config()
    host = ip_data["IP"]
    port = ip_data["PORT-1"]
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    client_socket.sendall(query.encode('utf-8'))
    response = receive_data(client_socket)
    data = json.loads(response)
    return data

    client_socket.close()


if __name__ == "__main__":
    result = RunQuery("select * from person where person_id = 1")
    print("Received data : " + str(result))
