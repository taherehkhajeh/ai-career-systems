print("--- Write to file ---")
with open("orders.txt", "w") as file:
    file.write("B721,2\n")
    file.write("K2020,1\n")

print("Orders saved")

print("\n--- Read from file ---")

with open("orders.txt", "r") as file:
    content = file.read()

print(content)

print("\n--- Append to file ---")

with open("orders.txt", "a") as file:
    file.write("B721,5\n")

print("New order added")

print("\n--- persian text ---")

with open("customers.txt", "w", encoding="utf-8") as file:
    file.write("مشتری : سارا محمدی - میز K2020\n")

with open("customers.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Missing file ---")

try:
    with open("returns.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("Returns file not found")

print("This line comes after reading")

print("\n--- Order Log Challenge ---")

try:
    with open("order_log.txt", "r", encoding="utf-8") as file:
        print("Previous orders:")
        print(file.read())
except FileNotFoundError:
    print("No previous orders")

customer = input("Enter your name:")
product_model = input("Enter product model:")
new_order = customer + "," + product_model

with open("order_log.txt", "a", encoding="utf-8") as file:
    file.write(new_order + "\n")

print("Order saved")
          
