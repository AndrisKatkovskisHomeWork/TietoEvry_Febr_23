while True:
    user_name = input("Please enter your name that begins with a capital letter: ")
    ch_first = user_name[0]
    if user_name[0].isupper():
        print("Name", user_name, "you entered corresponds to validation.")
        break
    else:
        print("The first symbol is NOT capital letter: ", ch_first)
        user_name = input("Please enter your name that begins with a capital letter: ")

user_name_changed = user_name[::-1].capitalize()  # slicing + capitalize
print(f"{user_name_changed}, a thorough mess is it not {ch_first}?")
