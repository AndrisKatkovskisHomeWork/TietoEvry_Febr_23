while True:
    first_number = input(f"Please enter first number: ")
    try:
        number = float(first_number)
    except ValueError:
        print(f"Wrong number {first_number} format. Please enter in format xx.x")
        continue
    else:
        break

while True:
    second_number = input(f"Please enter second number: ")
    try:
        number = float(second_number)
    except ValueError:
        print(f"Wrong number {second_number} format. Please enter in format xx.x")
        continue
    else:
        break

while True:
    third_number = input(f"Please enter third number: ")
    try:
        number = float(third_number)
    except ValueError:
        print(f"Wrong number {third_number} format. Please enter in format xx.x")
        continue
    else:
        break

print(f"You entered: ", {first_number}, {second_number}, {third_number}, "Lets sort it!")

middle_number = second_number

if first_number <= third_number and first_number <= second_number:
    smallest_number = first_number
if second_number <= third_number and second_number <= first_number:
    smallest_number = second_number
if third_number <= first_number and third_number <= second_number:
    smallest_number = third_number

if first_number >= second_number and first_number >= third_number:
    biggest_number = first_number
if second_number >= first_number and second_number >= third_number:
    biggest_number = second_number
if third_number >= first_number and third_number >= second_number:
    biggest_number = third_number

if first_number <= second_number and second_number <= third_number:
    middle_number = second_number
if second_number <= first_number and first_number <= third_number:
    middle_number = first_number
if first_number <= third_number and third_number <= second_number:
    middle_number = third_number

print(smallest_number, middle_number, biggest_number)
