import random
Won = False
Hint = 3
Loop_Left = False
You_Lost = False
letter_guessed = 12345654321
All_Letters_Guessed = False
Letters_Guessed = 0
first_letter_guessed = False
second_letter_guessed = False
third_letter_guessed = False
fourth_letter_guessed = False
fifth_letter_guessed = False
sixth_letter_guessed = False
hint_subtext = " "
first_letter = 1
second_letter = 2
third_letter = 3
fourth_letter = 4
fifth_letter = 5
sixth_letter = 6
guesses_left = 6
print("Hangman! []____0-/-<")
Words = ("dragon", "zoinks", "demons", "hanger", "jumped", "joklhlaup")
random_word = random.choice(Words)
if random_word == "dragon":
    first_letter = "d"
    second_letter = "r"
    third_letter = "a"
    fourth_letter = "g"
    fifth_letter = "o"
    sixth_letter = "n"
    Hint = "Hint: This is a fire breathing beast"
if random_word == "zoinks":
    first_letter = "z"
    second_letter = "o"
    third_letter = "i"
    fourth_letter = "n"
    fifth_letter = "k"
    sixth_letter = "s"
    Hint = "Hint: This is the catchphrase of Shaggy from Scooby Doo"
if random_word == "demons":
    first_letter = "d"
    second_letter = "e"
    third_letter = "m"
    fourth_letter = "o"
    fifth_letter = "n"
    sixth_letter = "s"
    Hint = "Hint: These are evil spirits"
if random_word == "hanger":
    first_letter = "h"
    second_letter = "a"
    third_letter = "n"
    fourth_letter = "g"
    fifth_letter = "e"
    sixth_letter = "r"
    Hint = "Hint: You use this to hang up clothes (This is a huge giveaway of a hint)"
if random_word == "jumped":
    first_letter = "j"
    second_letter = "u"
    third_letter = "m"
    fourth_letter = "p"
    fifth_letter = "e"
    sixth_letter = "d"
    Hint = "Hint: It's time to ____ up in the air! ____ up don't be scared! _____ up and your cares will soar away!"
    hint_subtext = "(Add ed to the end) Also, second hint, he ______ off the trampoline"
if random_word == "joklhlaup":
    Hint = "This is an Icelandic term meaning 'Glacial Run'"
Man = input("What is the name of the person who will be hung? ")
You = input("You are %s's last chance. What is your name? " % Man)
print()
print()
print("%s: Help!" % Man)
print()
print("Press Enter to cycle through dialogue")
print()
input("Executioner: Hello sir/madam, what is your business here?")
input("%s: Don't hang %s!" % (You, Man))

input("Executioner: Hmmmm... Do my son's English homework, you gotta guess a word or something boring like that.")
input("Executioner: If you guess correctly, I'll let %s go " % Man)
input("Executioner: But for each letter you get wrong, I'll tighten this rope by a little bit")
input("%s: I'll do it! Why you'd have English Homework decide someone's life is beyond me, but I'll do it!" % You)
print(Hint)
print(hint_subtext)
guess = " "
while not You_Lost and not Loop_Left:
    if Letters_Guessed == 6 and guesses_left >= 0:
        Won = True
    if Won:
        input("Executioner: Wow! You did it! Guess I'll let %s free." % Man)
        input("%s: Thank you %s! You saved me!" % (Man, You))
        input("%s: If there is anything I can do to repay your kindness all you need to do is ask!" % Man)
        input("%s: We can visit the Lucky 7s Casino, I heard it's a good place" % You)
        input("THE END")
        print("You win! Congratulations! :D")
        Loop_Left = True
    else:
        guess = input("What is your guess?")
        if guess == first_letter:
            if not first_letter_guessed:
                Letters_Guessed += 1
                first_letter_guessed = True
                print(first_letter)
        if guess == second_letter:
            if not second_letter_guessed:
                Letters_Guessed += 1
                second_letter_guessed = True
                print(second_letter)
        if guess == third_letter:
            if not third_letter_guessed:
                Letters_Guessed += 1
                third_letter_guessed = True
                print(third_letter)
        if guess == fourth_letter:
            if not fourth_letter_guessed:
                Letters_Guessed += 1
                fourth_letter_guessed = True
                print(fourth_letter)
        if guess == fifth_letter:
            if not fifth_letter_guessed:
                Letters_Guessed += 1
                fifth_letter_guessed = True
                print(fifth_letter)
        if guess == sixth_letter:
            if not sixth_letter_guessed:
                Letters_Guessed += 1
                sixth_letter_guessed = True
                print(sixth_letter)
        if guesses_left == 0:
            input("Executioner: You're out of guesses!")
            input("%s: NO WAIT DON'T HANG %s!" % (You, Man))
            input("%s is dead now. Press F to pay respects" % Man)
            input("You got the bad ending...")
            print("Ya dun goofed!")
            You_Lost = True
        else:
            guesses_left -= 1
