user_text = input("please enter some text: ")

position_not = user_text.find("not")

print("position_not: ", position_not)

if user_text.find("not") > 0 and user_text.find("bad") > 0:
    user_text = f"{user_text[:position_not]}is good"

print("user_text: ", user_text)
