lives = 10

while True:
    hangman_string = str(input("Please enter text. It is forbidden to write numbers: "))
    for i in hangman_string:
        if i.isdigit():
            is_clear_from_digits = False
            break
        else:
            is_clear_from_digits = True
    if is_clear_from_digits:
        print("\n\n\n\n\n\n\n Game can begin!")
        hangman_string = hangman_string.upper()
        break
    else:
        hangman_string = input("You enter number. Please enter text without numbers: ")

asterisks_string = ""
hidden_letter_shadow = "*"
for i in hangman_string:
    if i.isspace():
        asterisks_string += " "
    else:
        asterisks_string += hidden_letter_shadow

print("So... You have to find letters hidden under asterisks: ", asterisks_string)
asterisks_string_after_change = ""

while lives > 0:
    while True:
        print("\nYou have ", lives, "lives left.")
        letter_mentioned_by_second_player = input("Please enter letter you want to check: ")
        if len(letter_mentioned_by_second_player) == 1:
            letter_mentioned_by_second_player = letter_mentioned_by_second_player.upper()
            print("Let's check if name has letter: ", letter_mentioned_by_second_player)
            break
        else:
            print("something WRONG.... Why you enter ", letter_mentioned_by_second_player)

    for s in hangman_string:
        print("lets search letter", letter_mentioned_by_second_player)
        if s == letter_mentioned_by_second_player:
            print("TRUEEEEEEEEEEEEEEEEEE !!! There is ", s)
            asterisks_string_after_change += s
        elif s.isspace():
            asterisks_string_after_change += " "
        else:
            asterisks_string_after_change += hidden_letter_shadow

    if asterisks_string_after_change == asterisks_string:
        lives -= 1
        print("Sorry, there is no such, ", letter_mentioned_by_second_player, "in the name.")
    else:
        print("You have some progress. There are now fewer closed words: ", asterisks_string_after_change)
