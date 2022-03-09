while True:
    first_number = input("Please enter number: ")
    if first_number.isdigit():
        print("You entered correct first number: ", first_number)
        first_number = int(first_number)
        break
    else:
        print("You was NOT enter correct number")

while True:
    second_number = input("Please enter another number: ")
    if first_number == second_number:
        print("Both numbers are same(", first_number, ")! Please enter a different number.")
    elif second_number.isdigit():
        print("You entered correct ended number: ", second_number)
        second_number = int(second_number)
        break
    else:
        print("You was NOT enter correct number")

if first_number > second_number:
    temp = second_number
    second_number = first_number
    first_number = temp

quantity_of_cubes_to_be_calculated = second_number - first_number + 1

print(f"\nTwo numbers were entered: {first_number} and {second_number} ")
print(f"Let's immediately calculate the size of {quantity_of_cubes_to_be_calculated} cubes")

i = 0
while i < quantity_of_cubes_to_be_calculated:
    result = first_number ** 3
    print("Number", first_number, "cube is:", result)
    i += 1
    first_number += 1
