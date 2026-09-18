products = ["Chair", "Desk", "Sofa", "Cabinet"]
print(products[0])
print(products[2])
print(products[-1])
print(products[-3])
products[1] = "Workstation"
print(products)

products.append("Bookshelf")
print(products)
products.remove("Sofa")
print(products)
print(len(products))

chairs = ["B721", "OCEAN", "NILPER 123"]
print(chairs[1])
chairs[2] = "NILPER 124"
print(chairs)
chairs.append("K2020")
print(chairs)
print(len(chairs))
chairs.insert(1, "B202")
print(chairs)
removed_chair = chairs.pop(2)
print(removed_chair)
print(chairs)

last_chair = chairs.pop()
print(last_chair)
print(chairs)

for chair in chairs:
    print("Available:", chair)

if "B202" in chairs:
    print("B202 is available")
else:
    print("B202 is not available")

if "OCEAN" in chairs:
    print("OCEAN is available")
else:
    print("OCEAN is not available")

if "OCEAN" not in chairs:
    print("OCEAN needs to be added")

new_chair = "OCEAN"
if new_chair not in chairs:
    chairs.append(new_chair)
    print("OCEAN added")
print(chairs)