import random
import products_data
from products_data import show_price

print("--- Random order number ---")

order_number = random.randint(1000, 9999)
print("Order number:", order_number)

print("\n--- My own module ---")

print(products_data.products)
products_data.show_price("K2020")

print("\n--- from import ---")

show_price("B721")

print("\n--- return review ---")

def show_total(price):
    print(price * 2)

def get_total(price):
    return price * 2

a = show_total(100)
b = get_total(100)

print("a:", a)
print("b:", b)