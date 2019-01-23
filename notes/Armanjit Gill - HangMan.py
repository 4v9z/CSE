import random
import string
uppercases = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
Won = False
Loss = False
word_guess_lower = []
word_guess_upper = []
correct_guess = False
words = ["pingo", "mouse", "dragon", "pizza", "triangle", "python",
         "octopus", "squid", "dog", "horse", "PyCharm", "hello person!"]
letters_guessed = []
secret_guesses = [" ", "!", "?", ".", ",", "/", "[", "]", "'", "=", "*"]
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
elif begin == "no":
    print("Oh, okay goodbye! Prepare to be ejected into the void!")
while playing_Hangman:
    for i in range(len(word)):
        if word[i] not in secret_guesses:
            word.pop(i)
            word.insert(i, "?")
    print("".join(word))
    correct_guess = False
    word = list(Word)
    guess = input("Guess a letter in the word, or, you can try to guess the entire word")
    caps_guess = guess.upper()
    if guess in secret_guesses:
        print("Ummmm.... you already... guessed that...")
    elif guess in letters_guessed:
        print("Ummmm.... you already... guessed that...")
    elif guess == "":
        print("You didn't guess anything....")
    else:
        if len(guess) > 1:
            word_guess_lower = list(guess.lower())
            print("Please wait a moment while we verify if your guess is correct....")
            for i in range(len(word_guess_lower)):
                if word_guess_lower[i] == w0rd[i].lower():
                    letters_in_word -= 1
            if letters_in_word <= 0:
                playing_Hangman = False
                Won = True
            if guess == Word:
                print("You guessed it! Wow! The word/phrase was %s, and you guessed it!" % Word)
                correct_guess = True
                letters_in_word -= letters_in_word
        else:
            if caps_guess in word:
                secret_guesses.append(caps_guess)
            if guess.lower() in w0rd:
                print("You guessed a letter!")
                correct_guess = True
                letters_in_word -= 1
            letters_guessed.append(guess.lower())
            secret_guesses.append(guess.upper())
            secret_guesses.append(guess.lower())
            if letters_in_word <= 0:
                playing_Hangman = False
                Won = True
            print("You guessed the following letters (or words):")
            print(", ".join(letters_guessed))

            if guess not in word and not correct_guess:
                guesses -= 1
                input("There are no %s's" % guess)
            if guesses == 0:
                Loss = True
                playing_Hangman = False
            print("You have %s guess(es) left" % guesses)
if Loss:
    print("You lose! You need to get better at HangMan!")
    print("Oh well.... Oh! By the way, the word was %s" % Word)
if Won:
    print("Correct! The word/phrase was %s!" % Word)
    print("You had %s guess(es) left when you won" % guesses)
