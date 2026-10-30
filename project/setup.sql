-- Run this file in MySQL Workbench or the MySQL command line.
CREATE DATABASE IF NOT EXISTS car_rental_db;
USE car_rental_db;

CREATE TABLE IF NOT EXISTS customers (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(150) NOT NULL DEFAULT '',
    licence VARCHAR(30) NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS cars (
    number VARCHAR(15) PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    rate DECIMAL(10, 2) NOT NULL,
    seats INT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Available'
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_username VARCHAR(50) NOT NULL,
    car_number VARCHAR(15) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Booked',
    final_total DECIMAL(10, 2) NULL,
    returned_date DATE NULL,
    CONSTRAINT fk_booking_customer FOREIGN KEY (customer_username)
        REFERENCES customers(username),
    CONSTRAINT fk_booking_car FOREIGN KEY (car_number)
        REFERENCES cars(number),
    INDEX idx_booking_car_dates (car_number, start_date, end_date),
    INDEX idx_booking_customer (customer_username)
);
