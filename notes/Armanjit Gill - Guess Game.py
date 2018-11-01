import random
number = random.randint(1,10)
Your_Name=input("What is your name? ")
print("Guess Game!")
print()
print("Guess my number to win! You get 5 guesses.")

winner = False
for i in range (5):
    if winner = True:
        print("You guessed correctly! Congratulations %s" % (Your_Name))
    else:
    guess = int(input("What is your guess? "))
    if guess == number:
        print("You win!")
        winner = True
    elif guess > number:
        print("Guess a lower number")
    elif guess < number:
        print("Guess a larger number")
    else:
        print("YOU GET NOTHING! YOU LOSE! GOOD DAY SIR!")
