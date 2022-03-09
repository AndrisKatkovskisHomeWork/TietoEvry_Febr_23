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
letters_used = ""

while lives > 0 and hangman_string != asterisks_compare:
    while True:
        print("\nYou have ", lives, "lives left.")
        print("You have to find letters hidden under asterisks: ", asterisks_compare)
        entered_letter = input("Please enter letter you want to check: ")
        if len(entered_letter) == 1 and not entered_letter.isdigit():
            entered_letter = entered_letter.upper()
            break
        else:
            print("something WRONG.... Why you enter ", entered_letter)

    for index, item in enumerate(hangman_string):
        #        print("lets search letter", letter_mentioned_by_second_player)
        if asterisks_compare[index] == hidden_letter_shadow and item == entered_letter:
            asterisks_compare = asterisks_compare[:index] + entered_letter + asterisks_compare[index + 1:]

    if asterisks_compare == asterisks:
        for ch in letters_used:
            if ch == entered_letter:
                lives += 1
                break
        letters_used += entered_letter
        lives -= 1
        print("Sorry, there is no such '", entered_letter, "' in the name. You already try: ",
              ''.join(sorted(set(letters_used))))

    else:
        print("Wow! You did some progress!, There is ", entered_letter)
        asterisks = asterisks_compare

print("\n\nGame is over!")

if hangman_string != asterisks_compare:
    print("You didn't guess the hidden: ", hangman_string)
else:
    print("Congratulations! You are the winner with", lives, "lives left!")
