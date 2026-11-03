def calculate_total(unit_price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    if unit_price < 0:
        raise ValueError("Unit price cannot be negative")
    return unit_price * quantity

def get_shipping_fee(city):
    if city == "Tehran":
        return 0
    return 500_000

def get_discount_rate(quantity):
    if quantity >= 20:
        return 0.15
    elif quantity >= 10:
        return 0.1
    return 0

def calculate_final_price(unit_price, quantity, city):
    subtotal = calculate_total(unit_price, quantity)
    discount = subtotal * get_discount_rate(quantity)
    shipping = get_shipping_fee(city)
    return subtotal - discount + shipping


