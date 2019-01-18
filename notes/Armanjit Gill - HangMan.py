import random
import string
uppercases = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
correct_guess = False
words = ["pingo", "mouse", "dragon", "pizza", "triangle", "python",
         "octopus", "squid", "dog", "horse", "PyCharm", "hello person!"]
letters_guessed = [" ", "!", "?", ".", ",", "/", "[", "]"]
Word = random.choice(words)
letters_in_word = len(Word)
word = list(Word)
w0rd = list(Word)
guesses = 6
playing_Hangman = False
if Word == "PyCharm":
    w0rd[0] = "p"
    w0rd[2] = "c"
if Word == "hello person!":
    letters_in_word -= 5
if Word == "octopus":
    letters_in_word -= 1
if Word == "pizza":
    letters_in_word -= 1
guess = "never gonna give you up, never gonna get you down never gonna..."
print(Word)
print("Hangman []---O-<-<")
print()
input("PRESS ENTER TO CONTINUE")
print()
input("Hello! Welcome to Hangman! You get 6 guesses, one for each part of the body: Head, Torso, "
      "Arm 1, Arm 2, Leg 1, and Leg 2")
begin = input("Ready to start?")
if begin == "yes":
    playing_Hangman = True
elif begin == "no":
    print("Oh, okay goodbye! Prepare to be ejected into the void!")
while playing_Hangman:
    for i in range(len(word)):
        if word[i] not in letters_guessed:
            word.pop(i)
            word.insert(i, "?")
    input("".join(word))
    correct_guess = False
    word = list(Word)
    guess = input("Guess a letter in the word, or, you can try to guess the entire word")
    if guess == "":
        print("You didn't guess anything....")
    else:
        if guess in w0rd:
            print("You guessed a letter!")
            correct_guess = True
            letters_in_word -= 1
        if guess == Word:
            print("You guessed it! Wow! The word was %s, and you guessed it!" % Word)
            correct_guess = True
            letters_in_word -= letters_in_word
        letters_guessed.append(guess)
        if letters_in_word == 0:
            playing_Hangman = False
            print("Correct! The word was %s!" % Word)
        print("You guessed the following letters (or words):")
        print(", ".join(letters_guessed))
        if guess not in word and not correct_guess:
            guesses -= 1
            input("There are no %s's" % guess)
        if guesses == 0:
            print("You lose! You need to get better at HangMan!")
            print("Oh well.... Oh! By the way, the word was %s" % Word)
            playing_Hangman = False
