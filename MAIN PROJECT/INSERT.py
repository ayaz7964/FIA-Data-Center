import socket
import json


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def send_data(client_socket, data):
    # Convert data to JSON
    json_data = json.dumps(data)

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


def Insert_Query(query, data):
    # Define server address and port
    ip_data = load_config()
    server_address = ip_data["IP"]
    server_port = ip_data["PORT-2"]

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect((server_address, server_port))

    # Construct JSON object
    json_data = {'query': query, 'data': data}

    # Send JSON data to server
    send_data(client_socket, json_data)

    # Receive server response
    response = client_socket.recv(1024).decode('utf-8')

    # Close connection
    client_socket.close()

    return response == 'False'



def Insert_Into_Person(data):
    query = "INSERT INTO person ( f_name, l_name, date_of_birth, place_of_birth, age, gender, nationality, religion, cnic_number, Family_id) values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Phone_Number(data):
    query = "INSERT INTO phone_numbers (person_id, phone_number) values (%s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Address(data):
    query = "INSERT INTO addresses (person_id, address, adr_city, adr_state, adr_country, address_status, adr_date_in, adr_date_out) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Email(data):
    query = "INSERT INTO emails (person_id, email_address) values (%s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Education(data):
    query = "INSERT INTO education (person_id, degree_name, edu_reg_id, edu_institute, edu_date_in, edu_date_out, Education_status) values (%s, %s, %s, %s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Employment(data):
    query = "INSERT INTO employment (person_id, employment_company, company_address, hired_date, leave_date, job_name, employment_status, job_id) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Property(data):
    query = "INSERT INTO property (person_id, property_type, property_address, property_reg_id, property_value_amount, buy_date, sell_date, property_status) values (%s, %s, %s, %s, %s, %s, %s ,%s)"
    return Insert_Query(query, data)


def Insert_Into_Vehicle(data):
    query = "INSERT INTO vehicles (person_id, vehicle_maker, vehicle_model, vehicle_year, vehicle_color, vehicle_reg_number) values (%s, %s, %s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Crime_Record(data):
    query = "INSERT INTO crimerecord ( person_id, crime_id, crime_date, crime_status) values (%s, %s, %s, %s)"
    return Insert_Query(query, data)


def Insert_Into_Crimes(data):
    query = "INSERT INTO crimes (crime_name, crime_details, punishment, fine) VALUES (%s, %s, %s, %s);"
    return Insert_Query(query, data)


def Insert_Into_Jail_Record(data):
    query = "INSERT INTO jail_record (jail_id, person_id, crime_record_id, jailed_date_in, jailed_date_out, jailed_status) values (%s, %s, %s, %s, %s ,%s)"
    return Insert_Query(query, data)


def Insert_Into_Jail_Details(data):
    query = "INSERT INTO jail_details (jail_name, jail_location) values (%s, %s)"
    return Insert_Query(query, data)


def main():
    # Sample query and data
    query = "INSERT INTO users (user_uname, password, user_type, person_id) VALUES (%s, %s, %s, %s);"
    data = ["user1", "user1", "user1", 3]

    # Call Insert_Query method
    success = Insert_Query(query, data)
    print("Insertion status:", success)


if __name__ == "__main__":
    data = [22, "name", "details", "punishment", 1000]
    print(Insert_Into_Crimes(data))
