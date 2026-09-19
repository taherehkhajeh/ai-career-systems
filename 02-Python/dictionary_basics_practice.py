chair = {
    "model": "B721",
    "price": 7500000,
    "available": True
}
print(chair["model"])
print(chair["price"])
#print(chair["color"])

print(chair.get("color", "color not specified"))
print(chair.get("model", "Model not specified"))

chair["price"] = 8200000
print(chair["price"])
print(chair)

chair["color"] = "Black"
print(chair)

removed_color = chair.pop("color")
print(removed_color)
print(chair)

if "color" in chair:
    print("Color exists")
else:
    print("Color does not exist")

for key in chair:
    print(key, ":", chair[key])

for key, value in chair.items():
    print(key, ":", value)

for value in chair.values():
    print(value)

print(len(chair))


desk = {
    "model": "K2020",
    "price": 12500000,
    "available": False
}
print(desk.get("color", "Color not specified"))

desk["color"] = "White"

desk["available"] = True

if "discount" not in desk:
    desk["discount"] = 10

for key, value in desk.items():
    print(key, ":", value)

print(len(desk))



