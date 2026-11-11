import json

CATALOG_FILE = "catalog.json"

def load_catalog():
    try:
        with open(CATALOG_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
                
    except FileNotFoundError:
            return []

def save_catalog(catalog):
    with open(CATALOG_FILE, "w", encoding="utf-8") as file:
        json.dump(catalog, file, ensure_ascii=False, indent=2)

def find_product(catalog, model):
    model = model.strip().upper()

    for product in catalog:
        if product["model"] == model:
            return product

    return None

def add_product(catalog, model, name, category, price):
    model = model.strip().upper()
    
    if price <= 0:
        raise ValueError("Price must be greater than zero")

    existing = find_product(catalog, model)

    if existing is not None:
        raise ValueError("Model already exists")

    new_product = {
        "model": model,
        "name": name,
        "category": category,
        "price": price
    }

    catalog.append(new_product)
               