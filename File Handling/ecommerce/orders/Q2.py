def place_order(order_list, order_id, product_id, customer_id):
    order_list.append({"order_id": order_id, "product_id": product_id, "customer_id": customer_id})
    print("Order placed successfully")

def display_orders(order_list):
    for order in order_list:
        print(order)