no_bonus_years = 2
bonus_size = 15 / 100

while True:
    user_monthly_salary = input("Please enter amount of the monthly salary: ")
    try:
        user_monthly_salary = float(user_monthly_salary)
    except ValueError:
        print(f"Wrong salary {user_monthly_salary} format. Please enter in format xx.x")
        continue
    else:
        break

while True:
    user_years_of_service = input("Please enter number of years worked: ")
    try:
        user_years_of_service = float(user_years_of_service)
    except ValueError:
        print(f"Wrong years {user_years_of_service} format. Please enter in format xx.x")
        continue
    else:
        break

user_years_of_service = int(user_years_of_service)

if user_years_of_service <= no_bonus_years:
    print("Bonus will be for another year.")
else:
    christmas_bonus = (user_years_of_service - no_bonus_years) * bonus_size * user_monthly_salary
    print(f"You have worked for {user_years_of_service} full years,"
          f"and with {user_monthly_salary} Euro salary,"
          f"Bonus will be", '{0:.2f}'.format(christmas_bonus), "Euro.")
