# Car Rental System (Simple MySQL version)

Yeh beginner-friendly Python console project MySQL mein cars, customers aur bookings save karta hai.

## Pehli baar setup

1. MySQL Server install/start karein.
2. Project folder mein terminal kholkar connector install karein:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. `car_rental/database/simple_database.py` kholkar `DB_CONFIG` mein apna MySQL username aur password likhein.
4. Program chalayen:

   ```powershell
   py car_rental.py
   ```

`setup.sql` ko MySQL Workbench mein run karke database banayein. Program tables khud banata hai aur pehli baar teen sample cars add karta hai. Is version mein code ko chhota rakhne ke liye sirf basic admin aur customer options hain.

## Login

- Admin username: `admin`
- Admin password: `admin123`
- Customer: registration mein naam, phone, username aur password dein; phir login karein.

Customer date range enter karke dekh sakta hai ki kaunsi cars available hain. Booking ke waqt bhi isi date range ke liye cars check hoti hain. Car return karte waqt program basic rent calculate karta hai. MySQL login details `car_rental/database/simple_database.py` mein set hote hain.

## Project files

```text
project/
├── car_rental.py                 # Program start point
├── car_rental/
│   ├── admin/simple_admin.py     # Add/view cars, rentals, and revenue
│   ├── customer/simple_customer.py # Register, book, cancel, return
│   └── database/simple_database.py # Connect and prepare tables
├── setup.sql                     # Optional manual database setup
└── requirements.txt              # Python packages
```

`python car_rental.py` se app start karein.

## Tables ka kaam

- `cars`: gaadi ki details aur current fleet status
- `customers`: customer account aur contact details
- `bookings`: date range aur booking status

Date overlap check inclusive hai: agar ek booking 10 tareekh tak hai, doosri booking 10 tareekh se start nahi ho sakti.
