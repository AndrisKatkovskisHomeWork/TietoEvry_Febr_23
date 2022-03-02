while True:
    height_number = input(f"How tall should a Christmas tree be?: ")
    try:
        height_number = int(height_number)
    except ValueError:
        print(f"Wrong number format. {height_number} is not an integer.")
        continue
    else:
        break

half_height = int(height_number / 2)
print(half_height)

for i in range(height_number + 1):
    i += 1
    if i % 2 == 1:
        print(half_height * " ", i * "*", half_height * " ")
        half_height -= 1
