def add_customer(customer_list, customer_id, name):
    customer_list.append({"id": customer_id, "name": name})

def display_customers(customer_list):
    for customer in customer_list:
        print(customer)