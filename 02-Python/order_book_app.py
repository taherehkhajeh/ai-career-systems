import json
import products_data
from order_tools import calculate_total

print("\n--- Order Book ---")

try:
    with open("orders.json", "r", encoding="utf-8") as file:
        orders = json.load(file)

except FileNotFoundError:
    orders = []

print("Previous orders:", len(orders))

product_model = input("Enter product model: ")
quantity_text = input("Enter quantity: ")
name = input("Enter your name: ")
try:
    quantity = int(quantity_text)
    unit_price = products_data.products[product_model]
    total_price = calculate_total(unit_price, quantity)
except KeyError:
    print("Product model not found")
except ValueError as error:
    print("Invalid order:", error)
else:
    new_order = {
        "customer": name,
        "model": product_model,
        "quantity": quantity,
        "total": total_price
    }
    orders.append(new_order)

    with open("orders.json", "w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False, indent=2)
    print("Order saved")
    total_sales = 0

    for order in orders:
        total_sales = total_sales + order["total"]

    print("Total sales:", total_sales)