import random
rounds_lasted = 0
Your_Money = 15
Highest_Amount_Of_Money = 15
Round_with_most_Money = 0
Casino_Name = input("You want to go gambling with your $15, what's the name of the Casino you're going to? ")
You = input("Casino Worker: Hello sir/madam! Welcome to the %s! What is your name? " % Casino_Name)
print()
print("Press Enter to go through dialogue! (Be careful not to accidentally skip something important!)")
print()
input("%s: My name is %s." % (You, You))
input("Casino Worker: Ok %s, have fun gambling!" % You)
D6 = random.randint(2, 12)
while Your_Money > 0:
    input("Do you want to bet a dollar? (You HAVE to say Yes!)")
    Your_Money -= 1
    if D6 == 7:
        print("You won a round!")
        print("You gained $5!")
        Your_Money += 5
        rounds_lasted += 1
        D6 = random.randint(2, 12)
        if Your_Money > Highest_Amount_Of_Money:
            Highest_Amount_Of_Money = Your_Money
            Round_with_most_Money = rounds_lasted
    elif D6 != 7:
        print("Ah Man! I lost!")
        rounds_lasted += 1
        D6 = random.randint(2, 12)
        if Your_Money > Highest_Amount_Of_Money:
            Highest_Amount_Of_Money = Your_Money
            Round_with_most_Money = rounds_lasted

if Your_Money == 0:
    print("%s: Oh noes! I became bankrupt! Because my entire Life Savings was those $15!" % You)
    print("You lasted %s rounds!" % rounds_lasted)
    print("The most money you had was $%s" % Highest_Amount_Of_Money)
    print("You had the most money in round %s" % Round_with_most_Money)
    print("You did good! :D")