from datetime import date

from ..database.database import connect


def admin_menu():
    while True:
        print("\n--- Admin ---")
        print("1. Add car")
        print("2. View cars")
        print("3. View rental car")
        print("4. View total revenue")
        print("0. Log out")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_car()
        elif choice == "2":
            show_cars()
        elif choice == "3":
            show_rentals()
        elif choice == "4":
            show_revenue()
        elif choice == "0":
            break
        else:
            print("Please choose one of the listed options.")


def add_car():
    number = input("Vehicle number (MH12AB1234): ").strip().upper()
    model = input("Model: ").strip()

    try:
        rate = int(input("Price per day: "))
        seats = int(input("Number of seats: "))
    except ValueError:
        print("Please enter whole numbers.")
        return

    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO cars (number, model, rate, seats) VALUES (%s, %s, %s, %s)",
            (number, model, rate, seats),
        )
        connection.commit()
        print("Car added.")
    except Exception as error:
        print("Could not add car:", error)
    finally:
        cursor.close()
        connection.close()


def show_cars():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT number, model, rate, seats FROM cars")

    print("\nNumber       Model       Rate/day  Seats")
    print("-" * 45)
    for car in cursor.fetchall():
        print(f"{car[0]:<13}{car[1]:<12}Rs.{car[2]:<8}{car[3]}")

    cursor.close()
    connection.close()


def show_rentals():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT cars.number, cars.model, customers.name, customers.phone,
                  bookings.start_date, bookings.end_date
           FROM bookings
           JOIN cars ON bookings.car_number = cars.number
           JOIN customers ON bookings.customer_username = customers.username
           WHERE bookings.status = 'Booked'
           ORDER BY bookings.start_date"""
    )
    rentals = cursor.fetchall()
    cursor.close()
    connection.close()

    if not rentals:
        print("There are no any rental")
        return

    today = date.today()
    print("\nCar | Customer | Phone | Rental dates | Status")
    print("-" * 75)
    for rental in rentals:
        start_date = rental[4]
        end_date = rental[5]

        if start_date > today:
            days_until = (start_date - today).days
            status = f"Upcoming (starts in {days_until} day(s))"
        elif end_date < today:
            days_late = (today - end_date).days
            status = f"Overdue by {days_late} day(s)"
        else:
            days_left = (end_date - today).days
            status = "Due today" if days_left == 0 else f"Rented, {days_left} day left"

        print(
            f"{rental[0]} ({rental[1]}) | {rental[2]} | {rental[3]} | "
            f"{start_date} to {end_date} | {status}"
        )


def show_revenue():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COALESCE(SUM(final_total), 0) FROM bookings WHERE status = 'Returned'"
    )
    revenue = cursor.fetchone()[0]
    cursor.close()
    connection.close()

    print(f"\nTotal collected revenue: Rs.{revenue:.2f}")
