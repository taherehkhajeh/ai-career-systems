def calculate_order_total(unit_price, quantity):
    return unit_price * quantity

total_price = calculate_order_total(1800000, 4)
print(total_price)

def calculate_remaining_budget(total_budget, spent_amount):
    return total_budget - spent_amount

remaining_budget = calculate_remaining_budget(
    spent_amount=2500000,
    total_budget=10000000
)
print(remaining_budget)

def show_return_behavior():
    print("Function started")
    return("Function result")
    print("Function finished")
result = show_return_behavior()
print(result)

def calculate_valid_order(unit_price, quantity):
    if unit_price <= 0 or quantity <= 0:
        return "Invalid order"

    return unit_price * quantity
valid_order = calculate_valid_order(2500000, 3)
invalid_order = calculate_valid_order(2500000, 0)

print(valid_order)
print(invalid_order)

def calculate_discounted_price(price, discount_percent):
    if price <= 0:
        return "Invalid data"

    if discount_percent < 0 or discount_percent > 100:
        return "Invalid data"

    discount_amount = price * discount_percent / 100
    return price - discount_amount

final_price = calculate_discounted_price(1000000, 15)
invalid_price = calculate_discounted_price(1000000, 120)

print(final_price)
print(invalid_price)