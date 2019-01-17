import random
import string
uppercases = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
correct_guess = False
words = ["pingo", "mouse", "dragon", "pizza", "triangle", "python",
         "octopus", "squid", "dog", "horse", "PyCharm", "hello person!"]
length_of_guess = 1
word_guess = []
letters_guessed = []
secret_guesses = [" ", "!", "?", ".", ",", "/", "[", "]"]
caps_guess = "1"
Word = random.choice(words)
letters_in_word = len(Word)
word = list(Word)
w0rd = list(Word.lower())
guesses = 6
playing_Hangman = False
if Word == "hello person!":
    letters_in_word -= 5
if Word == "octopus":
    letters_in_word -= 1
if Word == "pizza":
    letters_in_word -= 1
guess = "never gonna give you up, never gonna get you down never gonna..."
print("Hangman []---O-<-<")
print()
input("PRESS ENTER TO CONTINUE")
print()
input("Hello! Welcome to Hangman! You get 6 guesses, one for each part of the body: Head, Torso, "
      "Arm 1, Arm 2, Leg 1, and Leg 2")
begin = input("Ready to start?")
if begin == "yes":
    playing_Hangman = True
elif begin == "":
    print("....... Fine, say nothing... Guess I'll just... eject you into the void, because I can do that.")
    print("You've been sent to an empty void!! You can't escape")
elif begin == "no":
    print("Oh, okay goodbye! Prepare to be ejected into the void!")
while playing_Hangman:
    for i in range(len(word)):
        if word[i] not in letters_guessed:
            word.pop(i)
            word.insert(i, "?")
    word = list(Word)
    for i in range(len(word)):
        if word[i] not in secret_guesses:
            word.pop(i)
            word.insert(i, "?")
    print("".join(word))
    correct_guess = False
    word = list(Word)
    guess = input("Guess a letter in the word, or, you can try to guess the entire word"
                  " Note: Guessing the word requires any punctuation in a phrase")
    length_of_guess = len(guess)
    caps_guess = guess.upper()
    word_guess = list(guess.upper())
    word_guess.append(list(guess.lower()))
    secret_guesses.append(word_guess)
    if guess in secret_guesses:
        print("Ummmm.... you already... guessed that...")
    elif guess in letters_guessed:
        print("Ummmm.... you already... guessed that...")
    elif guess == "":
        print("You didn't guess anything....")
    else:
        if length_of_guess > 1:
            print()
            if guess == Word:
                print("You guessed it! Wow! The word/phrase was %s, and you guessed it! You "
                      "guessed the EXACT Word!" % Word)
                playing_Hangman = False
                correct_guess = True
        else:
            if caps_guess in word:
                secret_guesses.append(caps_guess)
            if guess.lower() in w0rd:
                print("You guessed a letter!")
                correct_guess = True
                letters_in_word -= 1
                letters_in_word -= letters_in_word
            letters_guessed.append(guess.lower())
            secret_guesses.append(guess)
            secret_guesses.append(guess.lower())
            print("You guessed the following letters (or words):")
            print(", ".join(letters_guessed))
            if letters_in_word == 0:
                playing_Hangman = False
                print("Correct! The word/phrase was %s!" % Word)
                print("You had %s guess(es) left when you won" % guesses)
            if guess not in word and not correct_guess:
                guesses -= 1
                input("There are no %s's" % guess)
                print("You have %s guess(es) left" % guesses)
            if guesses == 0:
                print("You lose! You need to get better at HangMan!")
                print("Oh well.... Oh! By the way, the word was %s" % Word)
                playing_Hangman = False
