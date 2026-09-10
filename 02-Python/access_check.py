age = 17
is_blocked = False
is_owner = True
if age >= 18 and not is_blocked:
    print("Access granted")

elif is_owner or (age >= 18 and not is_blocked):
    print("Access granted")

else:
    print("Access denied")