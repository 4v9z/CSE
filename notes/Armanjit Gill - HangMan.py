import random
words = ["pingo", "mouse", "dragon", "pizza", "triangle", "python",
         "octopus", "squid", "dog", "horse", "PyCharm", "hello human!"]
letters_guessed = []
Word = random.choice(words)
word = list(Word)
guesses = 6
playing_Hangman = False
guess = "AAAAAAAAAAAAAAAAAAAAA"
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
            word.insert(i, "*")
    input("".join(word))
    guess = input("Guess a letter in the word")
    letters_guessed.append(guess)
    print("You guessed the following letters:")
    print(", ".join(letters_guessed))
    if guess not in word:
        guesses -=1
    if guesses == 0:
        print("You fail! HAHA!")
        playing_Hangman = False