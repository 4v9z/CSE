import random
rounds_lasted = 0
Your_Money = 15
Highest_Amount_Of_Money = 15
Round_with_most_Money = 1
Casino_Name = input("You want to go gambling with your $15, what's the name of the Casino you're going to? ")
You = input("%s Worker: Hello sir/madam! Welcome to the %s! What is your name? " % (Casino_Name, Casino_Name))
print("Press Enter to go through dialogue!")
input("%s: My name is %s." % (You, You))
input("%s Worker: Ok %s, have fun gambling!" % (Casino_Name, You))
Dice1 = random.randint(1, 6)
Dice2 = random.randint(1, 6)
while Your_Money > 0:
    Your_Money -= 1
    if Dice1 + Dice2 == 7:
        print("You won a round!")
        print("You gained $5!")
        Your_Money += 5
        rounds_lasted += 1
        Dice1 = random.randint(1, 6)
        Dice2 = random.randint(1, 6)
        if Your_Money > Highest_Amount_Of_Money:
            Highest_Amount_Of_Money = Your_Money
            Round_with_most_Money = rounds_lasted
    elif Dice1 + Dice2 != 7:
        print("Ah Man! I lost!")
        rounds_lasted += 1
        Dice1 = random.randint(1, 6)
        Dice2 = random.randint(1, 6)
        if Your_Money > Highest_Amount_Of_Money:
            Highest_Amount_Of_Money = Your_Money
            Round_with_most_Money = rounds_lasted

if Your_Money == 0:
    input("%s: Oh noes! I became bankrupt! This game must be rigged!!!" % You)
    input("%s Worker: Actually they are" % Casino_Name)
    print()
    input("%s: WHAAAAAAAAAAAAAAT????!!!!!!!!" % You)
    print()
    input("%s Worker: Sir/Madam? Please put away the sword" % Casino_Name)
    print("You lasted %s rounds!" % rounds_lasted)
    print("The most money you had was $%s" % Highest_Amount_Of_Money)
    print("You had the most money in round %s" % Round_with_most_Money)
    print("You did good! :D")
