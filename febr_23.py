import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
year = int(year)

username = input("What is your username? ")
print(f"Wow that is a nice name {username}")

user_age = input("What is your username? ")
print(f" {username}, how old are you?")
print(f"Dear {username} , {user_age} is the best age?")

user_age = int(user_age)
years_to_100 = 100 - user_age
year_when_100 = year + years_to_100
print(f" after {years_to_100} you be 100 year old in {year_when_100}")


