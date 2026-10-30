def add_product(product_list, product_id, name, price):
    product_list.append({"id": product_id, "name": name, "price": price})

def display_products(product_list):
    for product in product_list:
        print(product)