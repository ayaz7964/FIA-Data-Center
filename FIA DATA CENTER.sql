DROP DATABASE IF EXISTS FIA_DATA_CENTER;

CREATE DATABASE IF NOT EXISTS FIA_DATA_CENTER;
use FIA_DATA_CENTER;

-- Create Person table
CREATE TABLE IF NOT EXISTS Person (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    l_name VARCHAR(25),
    date_of_birth DATE,
    place_of_birth VARCHAR(100),
    age INT,
    gender VARCHAR(25),
    nationality VARCHAR(25),
    religion VARCHAR(25),
    cnic_number VARCHAR(25),
    Family_id INT
);

-- Create Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_uname VARCHAR(25),
    password VARCHAR(25),
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Emails table
CREATE TABLE IF NOT EXISTS Emails (
    person_id INT,
    email_address VARCHAR(100),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Phone_numbers table
CREATE TABLE IF NOT EXISTS Phone_numbers (
    person_id INT,
    phone_number VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Addresses table
CREATE TABLE IF NOT EXISTS Addresses (
    person_id INT,
    address VARCHAR(255),
    adr_city VARCHAR(25),
    adr_state VARCHAR(25),
    adr_country VARCHAR(25),
    address_status VARCHAR(25),
    adr_date_in DATE,
    adr_date_out DATE,
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Education table
CREATE TABLE IF NOT EXISTS Education (
    person_id INT,
    degree_name VARCHAR(100),
    edu_reg_id VARCHAR(25),
    edu_institute VARCHAR(100),
    edu_date_in DATE,
    edu_date_out DATE,
    Education_status VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Employment table
CREATE TABLE IF NOT EXISTS Employment (
    person_id INT,
    employment_company VARCHAR(100),
    company_address VARCHAR(100),
    hired_date DATE,
    leave_date DATE,
    job_name VARCHAR(50),
    employment_status VARCHAR(25),
    job_id VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Property table
CREATE TABLE IF NOT EXISTS Property (
    person_id INT,
    property_type VARCHAR(50),
    property_address VARCHAR(100),
    property_reg_id VARCHAR(25),
    property_value_amount INT,
    buy_date DATE,
    sell_date DATE,
    property_status VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create Vehicles table
CREATE TABLE IF NOT EXISTS Vehicles (
    person_id INT,
    vehicle_maker VARCHAR(25),
    vehicle_model VARCHAR(25),
    vehicle_year DATE,
    vehicle_color VARCHAR(25),
    vehicle_reg_number VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Crimes (
    crime_id INT AUTO_INCREMENT PRIMARY KEY,
    crime_name VARCHAR(50),
    crime_details VARCHAR(255),
    punishment VARCHAR(255),
    fine INT
);

-- Create CrimeRecord table
CREATE TABLE IF NOT EXISTS CrimeRecord (
    crime_record_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    crime_id INT,
    crime_date DATE,
    crime_status VARCHAR(25),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (crime_id) REFERENCES Crimes(crime_id)
);

CREATE TABLE IF NOT EXISTS Jail_Details (
    jail_id INT AUTO_INCREMENT PRIMARY KEY,
    jail_name VARCHAR(50),
    jail_location VARCHAR(100)
);

-- Create Jail_Record table
CREATE TABLE IF NOT EXISTS Jail_Record (
    jail_record_id INT AUTO_INCREMENT PRIMARY KEY,
    jail_id INT,
    person_id INT,
    crime_record_id INT,
    jailed_date_in DATE,
    jailed_date_out DATE,
    jailed_status VARCHAR(25),
    FOREIGN KEY (jail_id) REFERENCES Jail_Details(jail_id),
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (crime_record_id) REFERENCES CrimeRecord(crime_record_id) ON UPDATE CASCADE ON DELETE CASCADE
);
