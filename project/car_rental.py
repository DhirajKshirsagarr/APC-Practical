from mysql.connector import Error as MySQLError

from car_rental.admin.admin import admin_menu
from car_rental.customer.customer import customer_login, register_customer
from car_rental.database.database import prepare_database

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def main():
    try:
        prepare_database()
    except MySQLError as error:
        print("\nCould not connect to MySQL")
        print(f"MySQL says: {error}")
        print("Check the MySQL username/password in car_rental/database/database.py.")
        print("Also make sure car_rental_db exists.")
        return

    while True:
        print("\n========== CAR RENTAL SYSTEM ==========")
        print("1. Admin login  2. Customer register  3. Customer login  0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            username = input("Admin username: ").strip()
            password = input("Admin password: ").strip()
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                admin_menu()
            else:
                print("Incorrect admin login.")
        elif choice == "2":
            register_customer()
        elif choice == "3":
            customer_login()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose a listed option.")


if __name__ == "__main__":
    main()
