import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "dhiraj.1163",
    "database": "car_rental_db",
}


def connect():
    """Connect to the selected MySQL database."""
    return mysql.connector.connect(**DB_CONFIG)


def prepare_database():
    """Create the tables if they are not there yet."""
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
        number VARCHAR(15) PRIMARY KEY,
        model VARCHAR(50) NOT NULL,
        rate INT NOT NULL,
        seats INT NOT NULL
    )""")

    # Remove the old car-type column if this is an existing project database.
    cursor.execute("SHOW COLUMNS FROM cars LIKE 'type'")
    if cursor.fetchone():
        cursor.execute("ALTER TABLE cars DROP COLUMN type")
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(100) NOT NULL,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        email VARCHAR(150) NOT NULL DEFAULT '',
        licence VARCHAR(30) NOT NULL DEFAULT ''
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_username VARCHAR(50) NOT NULL,
        car_number VARCHAR(15) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        status VARCHAR(20) NOT NULL DEFAULT 'Booked',
        final_total DECIMAL(10, 2) NULL,
        returned_date DATE NULL
    )""")

    # Add sample cars only the first time the cars table is empty.
    cursor.execute("SELECT COUNT(*) FROM cars")
    if cursor.fetchone()[0] == 0:
        sample_cars = [
            ("MH12AB1234", "Swift", 1200, 5),
            ("MH14CD5678", "City", 2000, 5),
            ("MH12EF9012", "Creta", 3200, 7),
        ]
        cursor.executemany(
            "INSERT INTO cars (number, model, rate, seats) VALUES (%s, %s, %s, %s)",
            sample_cars,
        )

    connection.commit()
    cursor.close()
    connection.close()
