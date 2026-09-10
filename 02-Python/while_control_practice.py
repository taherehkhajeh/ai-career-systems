number = 1

while number <= 10:
    if number == 4:
        number = number + 1
        continue
    if number == 8:
        break

    print(number)
    number = number + 1
    