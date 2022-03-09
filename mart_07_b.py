lives = 10
hidden_letter_shadow = "*"

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

asterisks = ""
for i in hangman_string:
    if i.isspace():
        asterisks += " "
    else:
        asterisks += hidden_letter_shadow

asterisks_compare = asterisks

while lives > 0 or asterisks == asterisks_compare:
    while True:
        print("\nYou have ", lives, "lives left.")
        print("You have to find letters hidden under asterisks: ", asterisks_compare)
        letter_mentioned_by_second_player = input("Please enter letter you want to check: ")
        if len(letter_mentioned_by_second_player) == 1:
            letter_mentioned_by_second_player = letter_mentioned_by_second_player.upper()
            break
        else:
            print("something WRONG.... Why you enter ", letter_mentioned_by_second_player)

    for index, item in enumerate(hangman_string):
        #        print("lets search letter", letter_mentioned_by_second_player)
        if asterisks_compare[index] == hidden_letter_shadow and item == letter_mentioned_by_second_player:
            asterisks_compare = asterisks_compare[:index] + letter_mentioned_by_second_player + asterisks_compare[
                                                                                                index + 1:]

    if asterisks_compare == asterisks:
        print("Sorry, there is no such '", letter_mentioned_by_second_player, "' in the name.")
        lives -= 1
    else:
        print("Wow! You did some progress!, There is ", item)
