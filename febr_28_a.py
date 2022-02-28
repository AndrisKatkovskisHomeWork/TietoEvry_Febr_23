while True:
    user_temperature = input("Please enter the temperature in °C: ")
    try:
        user_temperature = float(user_temperature)
    except ValueError:
        print(f"Wrong temperature {user_temperature} format. Please enter in format xx.x")
        continue
    else:
        break

if user_temperature < 0:
    print(f"{user_temperature}°C - Temperature you entered is negative.")
elif user_temperature < 35:
    print(f"{user_temperature}°C -  not too cold")
elif user_temperature > 44:
    print(f"{user_temperature} - Was the temperature really entered in °C?")
elif user_temperature > 37:
    print(f"{user_temperature}°C - possible fever")
elif user_temperature <= 37:
    print(f"{user_temperature}°C - all right")
else:
    print(f"{user_temperature} temperature could not be analyzed.")
