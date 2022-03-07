user_text = input("please enter some text: ")

position_not = user_text.find("not")
position_bad = user_text.find("bad")

# print("position_not: ", position_not)

if user_text.find("not") > 0 and user_text.find("bad") > 0:
    user_text = f"{user_text[:position_not]}is good{user_text[position_bad+3:]}"

print("user_text: ", user_text)
