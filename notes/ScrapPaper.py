print("Choose your own adventure!")
print()
Plantopia_Saved = False
Hydro_World_Saved = False
Magma_Dome_Saved = False
Frost_Paradise_Saved = False
Your_Health = 30
World = input("Name the fantasy world in the story ")
Guide = input("Name the person who will guide you on your adventure ")
Villain = input("Name the Villain: ")
You = input("Hello, my name is %s. I will be your guide on your adventure. What is your name? " % Guide)
print()
print("Press enter to cycle through dialogue! Be careful not to skip anything important though!")
print()
input("%s: %s, the world of %s is in danger. It is being attacked by the evil Wizard %s" % (Guide, You, World, Villain))
input("%s: The world of %s is split into 4 distinct regions, each is going through a problem" % (Guide, World))
input("%s: These problems are all being caused by %s" % (Guide, Villain))
Region_to_Explore = input("Which region would you like to go to first? Plantopia or Hydro Kingdom? ")
if Region_to_Explore == "Swamp":
    input("Shrek: WHAT ARE YOU DOIN IN MY SWAMP?!?!")
    Your_Health -= 30
    print("%s has died. You have lost and %s will take over %s" % (You, Villain, World))
if Region_to_Explore == "Plantopia":
    input("%s: Okay... Plantopia is a rainforest normally full of friendly animals" % Guide)
    input("%s: However %s has turned the animals into fierce beasts! Even the plants can kill you!" % (Guide, Villain))
    input("%s: There are also myths of some kind of plant people living there, but they're just myths" % Guide)
    input("%s: Alright, Plantopia. Let's get through here" % You)
    Path = input("There are two directions, one with nothing in sight and one with some monkeys. Which do you choose? ")
    if Path == "monkeys":
        input("You go through the monkey path, they start attacking you fiercely.")
        Your_Health -= 5
        input("You lose 5 health. You have %i health" % Your_Health)
        Monkey_Attack = input("How do you retaliate? Do you try to throw them off? Or do you hit them with your sword?")
        if Monkey_Attack == "throw":
            input("You throw off the monkeys, they jump back on you")
            input("Now they are biting and scratching harder. It's not looking good")
            Your_Health -= 25
            input("You lost 25 health! Now you have %i health left" % Your_Health)

            if Your_Health == 0:
                input("%s: Ack!!" % You)
                input("Your vision starts to get blurry... You have lost all of your Health!")
                input("Now %s rules %s. All hope is lost" % (Villain, World))
                input("GAME OVER")
                print("You got killed by monkeys... How... sad")
