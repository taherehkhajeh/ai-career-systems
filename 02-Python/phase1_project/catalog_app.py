
from catalog_tools import load_catalog, save_catalog, find_product, add_product


def show_product(product):
    print(
        product["model"],
        product["name"],
        product["category"],
        product["price"]
    )


print("--- Jahan Felez Catalog ---")

catalog = load_catalog()

print("1. Show all products")
print("2. Search product")
print("3. Add product")

choice = input("Choose an option: ")

if choice == "1":
    if not catalog:
        print("Catalog is empty")
    else:
        for product in catalog:
            show_product(product)

elif choice == "2":
    model = input("Please enter the model: ")
    product = find_product(catalog, model)

    if product is None:
        print("Product not found")
    else:
        show_product(product)

elif choice == "3":
    model = input("Enter model: ")
    name = input("Enter product name: ")
    category = input("Enter category: ")
    price_text = input("Enter price: ")

    try:
        price = int(price_text)
        add_product(catalog, model, name, category, price)

    except ValueError as error:
        print("Could not add product:", error)

    else:
        save_catalog(catalog)
        print("Product added")

else:
    print("Invalid option")
