print("--- Shipping fee ---")

def get_shipping_fee(city):
    if city == "Tehran":
        return 0
        print("Free shipping!")
    return 500_000

print(get_shipping_fee("Tehran"))
print(get_shipping_fee("Karaj"))

print("\n--- Discount ---")

def get_discount(quantity):
    if quantity >= 10:
        return 0.1
    return 0

print(get_discount(12))
print(get_discount(3))

print("\n--- Final price ---")

def calculate_final_price(unit_price, quantity, city):
    subtotal = unit_price * quantity
    discount = subtotal * get_discount(quantity)
    shipping = get_shipping_fee(city)
    return subtotal - discount + shipping

print(calculate_final_price(1_000_000, 12, "Karaj"))
print(calculate_final_price(1_000_000, 3, "Tehran"))

print("\n--- raise ---")

def calculate_subtotal(unit_price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return unit_price * quantity

print(calculate_subtotal(1_000_000, 2))

try:
    print(calculate_subtotal(1_000_000, -3))
except ValueError as error:
    print("Order rejected:", error)