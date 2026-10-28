import random
import products_data
from order_tools import calculate_total

print("\n--- Order App ---")

order_number = random.randint(1000, 9999)
print("Order number:", order_number)

product_model = input("Enter product model:")
quantity_text = input("Enter quantity:")

try:
    quantity = int(quantity_text)
    unit_price = products_data.products[product_model]
    total_price = calculate_total(unit_price, quantity)
except KeyError:
    print("Product model not found")
except ValueError:
    print("Please enter a valid quantity")
else:
    print("total price:", total_price)
