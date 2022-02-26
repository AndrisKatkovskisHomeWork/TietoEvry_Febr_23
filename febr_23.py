import datetime

current_Date_Time = datetime.datetime.now()
date = current_Date_Time.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
year = int(year)

username = input("What is your username? ")
print(f"Wow that is a nice name {username}")

user_age = input("What is your age? ")
print(f"Dear {username} , {user_age} is the best age?")

user_age = int(user_age)
years_to_100 = 100 - user_age
year_when_100 = year + years_to_100
print(f" after {years_to_100} you be 100 year old in {year_when_100}")
print(sep="\n")

########################################################################

room_width = input("please input Room width ")
print(f"Room width is {room_width}")
room_length = input("please input Room length ")
print(f"Room length is{room_length}")
room_height = input("please input Room height ")
print(f"Room height is{room_height}")
room_width = float(room_width)
room_length = float(room_length)
room_height = float(room_height)

room_square_meters = room_width * room_length
room_volume = room_width * room_length * room_height

print(f"room square meters {room_square_meters} and room volume is {room_volume}")

########################################################################

user_temperature_C = float(input("What is your temperature in Celsius? "))
user_temperature_F = round((32+user_temperature_C*(9/5)), 2)
print(f"{user_temperature_C} in Celsius is  {user_temperature_F} in Farenheit")
