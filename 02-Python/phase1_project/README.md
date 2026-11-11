# Jahan Felez Product Catalog Manager

## Problem

Jahan Felez works with different office furniture products, and product information needs to be organized in a clear and consistent way. A structured catalog makes it easier to view products, search by model, and add new items without creating duplicate model codes. This project is my first step toward building a reusable product data source for Jahan Felez.

## What it does

The application is a simple command-line product catalog manager. It can:

- Display all products in the catalog.
- Search for a product by its model code.
- Add a new product to the catalog.
- Prevent duplicate model codes.
- Validate the price and reject non-numeric, zero, or negative values.
- Normalize model codes by removing extra spaces and converting English letters to uppercase.

Each product has four fields:

- `model`
- `name`
- `category`
- `price`

## How it works

The project is organized into separate files:

- `catalog_app.py` handles the menu, user input, application flow, and displaying product information.
- `catalog_tools.py` contains the reusable catalog operations: loading and saving data, finding a product, and adding a product.
- `catalog.json` stores the product data as JSON.

`catalog.json` is created automatically when the first product is added. It is not included in the repository.

The application loads the catalog from `catalog.json` when it starts. When a new product is added successfully, the updated catalog is saved back to that file.

## Design decisions

### 1. Separating application flow from catalog operations

I kept user interaction in `catalog_app.py` and the catalog operations in `catalog_tools.py`. This makes the catalog logic easier to reuse. For example, a future website or automation could use the same catalog operations without having to reuse the command-line menu.

### 2. Normalizing model codes in `catalog_tools.py`

I used `strip()` and `upper()` inside both `find_product()` and `add_product()`. This means model codes are checked and stored in a consistent format, even if someone enters lowercase letters or extra spaces. I put this rule in the tools layer so every part of the project that uses these functions follows the same rule.

### 3. Treating a missing file and invalid data differently

If `catalog.json` does not exist yet, `load_catalog()` returns an empty list. That is a normal starting point for a new catalog, not an application error.

A price of zero or less is different: it is invalid product data. For that reason, `add_product()` raises a `ValueError` when the price is not greater than zero. Duplicate model codes are also rejected.

## Testing

I manually tested the main features and error cases:

- Displaying all products.
- Finding an existing product.
- Handling a search for a product that does not exist.
- Handling an invalid menu option.
- Adding a new product and checking that it was saved in `catalog.json`.
- Rejecting a duplicate model code.
- Rejecting a non-numeric price.
- Rejecting zero and negative prices.
- Searching with lowercase model codes and extra spaces.
- Adding a lowercase model code and checking that it was saved in uppercase.

During testing, I found that searching for `k2020` did not find the saved model `K2020`. This happened because the comparison was case-sensitive. I fixed this by normalizing the model code with `strip().upper()` in `find_product()` and `add_product()`. After the change, lowercase input and extra spaces were handled correctly, and new model codes were saved in uppercase.

All the tests listed above passed for this version.

## How to run

Requires Python 3 (tested with Python 3.14).

Open a terminal in the `phase1_project` folder and run:

```
python catalog_app.py
```

Choose an option from the menu and follow the instructions.

The program handles one menu choice per run. A continuous menu loop is not included in this version.

## Next steps

The product data stored in `catalog.json` can become the starting data source for the Products page on the Jahan Felez website.

Before using it in a live website, the data structure, storage method, and the way the website accesses the catalog will need to be reviewed and adapted to the website's requirements.