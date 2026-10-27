print("Program started")

total_price = 30_000_000
quantity = 5

try:
    average_price = total_price / quantity
    print(average_price)

except ZeroDivisionError:
    print("Quantity cannot be zero")

print("Program finished")

print("\n--- User Input Example ---")

try:
    quantity = int(input("Enter quantity: "))
    average_price = total_price / quantity

except ValueError as error:
    print("Please enter a valid whole number")
    print("Technical details:", error)

except ZeroDivisionError:
    print("Quantity cannot be zero")

else:
    print("Average price:", average_price)

finally:
    print("User input example finished")

print("\n--- Product Order Example ---")

products = {
    "B721": 8_200_000,
    "K2020": 30_000_000
}
model = input("Enter product model: ")
quantity_text = input("Enter quantity: ")

try:
    quantity = int(quantity_text)
    unit_price = products[model]
    total_price = unit_price * quantity

except ValueError:
    print("Please enter a valid quantity")
except KeyError:
    print("Product model not found")
else:
    print("Total price:", total_price)
finally:
    print("Order check finished")

