import random
number = random.randint(1, 10)
Your_Name = input("What is your name? ")
print("Guess Game!")
print()
print("Guess my number to win! You get 5 guesses.")
guess = 0
guesses_left = 5
winner = False
playing_Guess_Game = True
while guesses_left > 0 and playing_Guess_Game:
    if winner:
        playing_Guess_Game = False
    else:
        guess = int(input("What is your guess? "))
        guesses_left -= 1
    if guess == number:
        print("You guessed correctly! Congratulations %s" % Your_Name)
        winner = True
    elif guesses_left == 0:
        print("YOU GET NOTHING! YOU LOSE! GOOD DAY TO YOU SIR!")
        print("You need to do better than THAT %s! Ya dun goofed!" % Your_Name)
        playing_Guess_Game = False
    elif guess > number:
        print("Guess a lower number")
    elif guess < number:
        print("Guess a larger number")
