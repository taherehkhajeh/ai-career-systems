import json
print("--- List of dictionaries ---")

products = [
    {"model": "B721", "name": "Office chair", "price": 8_200_000},
    {"model": "K2020", "name": "Manager desk", "price": 30_000_000}
    ]

print(len(products))
print(products[0])
print(products[1]["name"])

first_product = products[0]
print(first_product["price"])


print("\n--- Loop over products ---")
for product in products:
    print(product["model"], "-", product["name"], ":", product["price"])

print("\n--- Products under 10 million ---")
for product in products:
    if product["price"] < 10_000_000:
        print(product["name"])

print("\n--- Total value ---")
total = 0
for product in products:
    total = total + product["price"]
print("Total:", total)

print("\n--- Save to JSON ---")

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

print("Products saved")

print("\n--- Load from JSON ---")

with open("products.json", "r", encoding="utf-8") as file:
    loaded_products = json.load(file)

print(type(loaded_products))
print(loaded_products[1]["name"])