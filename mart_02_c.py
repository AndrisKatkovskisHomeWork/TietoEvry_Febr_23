while True:
    user_entered_number = input("Please enter a positive number: ")
    try:
        user_entered_number = int(user_entered_number)
    except ValueError:
        print(f"Wrong number format. {user_entered_number} is not an integer.")
        continue
    else:
        break

print("You entered", user_entered_number, "\n")

if user_entered_number < 0:
    print(f"The number you entered {user_entered_number} is negative!")
elif user_entered_number == 0:
    print(f"The number you entered {user_entered_number} is zero!")
else:
    for i in range(2, int(user_entered_number / 2 + 1)):
        print("Trying to divide by", i)
        if user_entered_number % i == 0:
            print(f" The number {user_entered_number} is divided by {i} !")
            break
    else:
        print(f" The entered number {user_entered_number}, and it is prime number !! ")
