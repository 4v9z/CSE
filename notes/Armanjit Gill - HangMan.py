import random
Won = False
first_letter = 1
second_letter = 2
third_letter = 3
fourth_letter = 4
fifth_letter = 5
sixth_letter = 6
guesses_left = 8
print("Hangman! []____0-/-<")
Words = ("dragon", "zoinks", "demons","hanger", "jumped")
random_word = random.choice(Words)
if random_word == "dragon":
    first_letter = "d"
    second_letter = "r"
    third_letter = "a"
    fourth_letter = "g"
    fifth_letter = "o"
    sixth_letter = "n"
if random_word == "zoinks":
    first_letter = "z"
    second_letter = "o"
    third_letter = "i"
    fourth_letter = "n"
    fifth_letter = "k"
    sixth_letter = "s"
if random_word == "demons":
    first_letter = "d"
    second_letter = "e"
    third_letter = "m"
    fourth_letter = "o"
    fifth_letter = "n"
    sixth_letter = "s"
if random_word == "hanger":
    first_letter = "h"
    second_letter = "a"
    third_letter = "n"
    fourth_letter = "g"
    fifth_letter = "e"
    sixth_letter = "r"
if random_word == "jumped":
    first_letter = "j"
    second_letter = "u"
    third_letter = "m"
    fourth_letter = "p"
    fifth_letter = "e"
    sixth_letter = "d"
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
while guesses_left > 0:
    guess = input("What is the first letter?")
    guesses_left -= 1
    if guess == first_letter:
            print(first_letter)
    if guess == second_letter:
        print(second_letter)
    if Won:
        input("Executioner: Wow! You did it! Guess I'll let %s free." % Man)
        input("%s: Thank you %s! You saved me!" % (Man, You))
        input("%s: If there is anything I can do to repay your kindness all you need to do is ask!" % Man)
        input("%s It was nothing, I did the good!" % You)
        input("THE END")
        print("You win! Congratulations!")
