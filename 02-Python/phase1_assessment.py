
products = [
    {"model": "B721", "category": "office", "price": 8200000},
    {"model": "K2020", "category": "home", "price": 30000000},
    {"model": "M310", "category": "office", "price": 12500000},
    {"model": "H450", "category": "home", "price": 6500000}
]


def filter_by_category(products, category):
    category = category.strip().upper()

    if not category:
        raise ValueError("Category cannot be empty")

    filtered_products = []

    for product in products:
        product_category = product["category"].strip().upper()

        if product_category == category:
            filtered_products.append(product)

    return filtered_products


def total_value(products):
    total = 0

    for product in products:
        total = total + product["price"]

    return total



category = input("Enter category: ")

try:
    filtered_products = filter_by_category(products, category)

except ValueError as error:
    print(error)

else:
    if not filtered_products:
        print("No products in this category")

    else:
        for product in filtered_products:
            print(product["model"], product["price"])

        print("Total:", total_value(filtered_products))
