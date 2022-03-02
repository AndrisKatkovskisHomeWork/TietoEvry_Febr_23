while True:
    smallest_number = input(f"please enter the smallest number in row of numbers: ")
    try:
        smallest_number = int(smallest_number)
    except ValueError:
        print(f"Wrong number format. {smallest_number} is not an integer.")
        continue
    else:
        break

while True:
    biggest_number = input(f"please enter the biggest number in row of numbers: ")
    try:
        biggest_number = int(biggest_number)
    except ValueError:
        print(f"Wrong number format. {biggest_number} is not an integer.")
        continue
    else:
        break

if smallest_number > biggest_number:
    print(f"You entered", smallest_number, "and", biggest_number,
          ". Please first enter smallest number and only then biggest.")

print("Catch the result!")

for i in range(smallest_number, biggest_number + 1):
    if i % 5 == 0:
        if i % 7 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
