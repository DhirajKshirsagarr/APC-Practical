from datetime import date

from ..database.database import connect


def register_customer():
    print("\n--- REGISTER ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    username = input("Choose username: ").strip()
    password = input("Choose password: ").strip()

    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """INSERT INTO customers (username, password, name, phone, email, licence)
               VALUES (%s, %s, %s, %s, '', '')""",
            (username, password, name, phone),
        )
        connection.commit()
        print("Account created. Choose customer login from the main menu.")
    except Exception as error:
        print("Could not register. Maybe that username is already used.", error)
    finally:
        cursor.close()
        connection.close()


def customer_login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT username FROM customers WHERE username = %s AND password = %s",
        (username, password),
    )
    customer = cursor.fetchone()
    cursor.close()
    connection.close()

    if customer:
        customer_menu(username)
    else:
        print("Username or password is incorrect.")


def customer_menu(username):
    while True:
        print("\n--- CUSTOMER ---")
        print("1. View cars")
        print("2. Book car")
        print("3. My bookings")
        print("4. Cancel booking")
        print("5. Return car")
        print("0. Log out")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_available_cars()
        elif choice == "2":
            book_car(username)
        elif choice == "3":
            show_bookings(username)
        elif choice == "4":
            cancel_booking(username)
        elif choice == "5":
            return_car(username)
        elif choice == "0":
            break
        else:
            print("Please choose a listed option.")


def get_available_cars(cursor, start_date, end_date):
    cursor.execute(
        """SELECT cars.number, cars.model, cars.rate, cars.seats
           FROM cars
           WHERE NOT EXISTS (
               SELECT 1 FROM bookings
               WHERE bookings.car_number = cars.number
               AND bookings.status = 'Booked'
               AND bookings.start_date <= %s
               AND bookings.end_date >= %s
           )
           ORDER BY cars.rate""",
        (end_date, start_date),
    )
    return cursor.fetchall()


def show_available_cars():
    start_text = input("Start date (YYYY-MM-DD): ").strip()
    end_text = input("End date (YYYY-MM-DD): ").strip()

    try:
        start_date = date.fromisoformat(start_text)
        end_date = date.fromisoformat(end_text)
        if end_date < start_date:
            print("End date must be on or after the start date.")
            return
    except ValueError:
        print("Please enter dates as YYYY-MM-DD.")
        return

    connection = connect()
    cursor = connection.cursor()
    cars = get_available_cars(cursor, start_text, end_text)
    print(f"\nCars available from {start_text} to {end_text}:")
    if not cars:
        print("No cars are available for these dates.")
    for car in cars:
        print(f"{car[0]} | {car[1]} | Rs.{car[2]} per day | {car[3]} seats")
    cursor.close()
    connection.close()


def car_is_free(cursor, car_number, start_date, end_date):
    """A car is free if no active booking overlaps the requested dates."""
    cursor.execute(
        """SELECT COUNT(*) FROM bookings
           WHERE car_number = %s AND status = 'Booked'
           AND start_date <= %s AND end_date >= %s""",
        (car_number, end_date, start_date),
    )
    return cursor.fetchone()[0] == 0


def book_car(username):
    start_text = input("Start date (YYYY-MM-DD): ").strip()
    end_text = input("End date (YYYY-MM-DD): ").strip()

    try:
        start_date = date.fromisoformat(start_text)
        end_date = date.fromisoformat(end_text)
        if end_date < start_date:
            print("End date must be on or after the start date.")
            return
    except ValueError:
        print("Please enter dates as YYYY-MM-DD.")
        return

    connection = connect()
    cursor = connection.cursor()
    free_cars = get_available_cars(cursor, start_text, end_text)
    if not free_cars:
        print("No cars are available for those dates.")
        cursor.close()
        connection.close()
        return

    print("\nAvailable cars:")
    for car in free_cars:
        print(f"{car[0]} | {car[1]} | Rs.{car[2]} per day | {car[3]} seats")

    car_number = input("Choose a vehicle number: ").strip().upper()
    if not car_is_free(cursor, car_number, start_text, end_text):
        print("That car is already booked for those dates.")
    elif not any(car[0] == car_number for car in free_cars):
        print("Choose a car from the available list.")
    else:
        cursor.execute(
            """INSERT INTO bookings (customer_username, car_number, start_date, end_date)
               VALUES (%s, %s, %s, %s)""",
            (username, car_number, start_text, end_text),
        )
        connection.commit()
        print("Booking confirmed.")

    cursor.close()
    connection.close()


def show_bookings(username):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT id, car_number, start_date, end_date, status
           FROM bookings WHERE customer_username = %s ORDER BY id""",
        (username,),
    )
    bookings = cursor.fetchall()
    if not bookings:
        print("No bookings yet.")
    for booking in bookings:
        print(f"ID {booking[0]} | {booking[1]} | {booking[2]} to {booking[3]} | {booking[4]}")
    cursor.close()
    connection.close()


def cancel_booking(username):
    show_bookings(username)
    try:
        booking_id = int(input("Booking ID to cancel: "))
    except ValueError:
        print("Enter a number for the booking ID.")
        return

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """UPDATE bookings SET status = 'Cancelled'
           WHERE id = %s AND customer_username = %s AND status = 'Booked'""",
        (booking_id, username),
    )
    connection.commit()
    print("Booking cancelled." if cursor.rowcount else "Could not find an upcoming booking with that ID.")
    cursor.close()
    connection.close()


def return_car(username):
    show_bookings(username)
    try:
        booking_id = int(input("Booking ID to return: "))
    except ValueError:
        print("Enter a number for the booking ID.")
        return

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT bookings.start_date, bookings.end_date, cars.rate
           FROM bookings JOIN cars ON bookings.car_number = cars.number
           WHERE bookings.id = %s AND bookings.customer_username = %s
           AND bookings.status = 'Booked'""",
        (booking_id, username),
    )
    booking = cursor.fetchone()
    if not booking:
        print("Active booking not found.")
    else:
        days = (booking[1] - booking[0]).days + 1
        total = days * booking[2]
        today = date.today()
        cursor.execute(
            """UPDATE bookings
               SET status = 'Returned', final_total = %s, returned_date = %s
               WHERE id = %s""",
            (total, today, booking_id),
        )
        connection.commit()
        print(f"Returned. {days} day(s) x Rs.{booking[2]} = Rs.{total}")

    cursor.close()
    connection.close()
