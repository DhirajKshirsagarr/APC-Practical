from products import catalog
from customers import profile
from orders import order
from payments import payment

product_list = []
customer_list = []
order_list = []

catalog.add_product(product_list, "P1", "Laptop", 50000)
profile.add_customer(customer_list, "C1", "Rehan")
order.place_order(order_list, "O1", "P1", "C1")

catalog.display_products(product_list)
profile.display_customers(customer_list)
order.display_orders(order_list)

payment.process_payment(50000, "UPI")