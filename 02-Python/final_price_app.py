import products_data
from order_tools import calculate_final_price

print("\n--- Final Price Calculator ---")

product_model = input("Enter product model:")
quantity_text = input("Enter quantity:")
city = input("Enter your city:")

try:
    quantity = int(quantity_text)
    unit_price = products_data.products[product_model]
    final_price = calculate_final_price(
        unit_price, quantity, city
    )
except KeyError:
    print("Product model not found")
except ValueError as error:
    print("Invalid order:", error)
else:
    print("Final price:", final_price)



