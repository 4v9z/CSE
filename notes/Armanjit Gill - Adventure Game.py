import random
Flee_Chance = random.randint(1,10)
in_battle = False
print("Choose your own adventure!")
print()
got_banana = False
open_inventory = " "
inventory = ["Magic Sword"]
weapons = ["Magic Sword"]
Plantopia_Saved = False
Hydro_World_Saved = False
Magma_Dome_Saved = False
Frost_Paradise_Saved = False
Secret = False
Your_Health = 30
World = input("Name the fantasy world in the story ")
if World == "win":
    input("Good Day. I am pig")
Guide = input("Name the person who will guide you on your adventure ")
Villain = input("Name the Villain: ")
You = input("Hello, my name is %s. I will be your guide on your adventure. What is your name? " % Guide)
print()
print("Press enter to cycle through dialogue! Be careful not to skip anything important though!")
print()
secret = input("Input any cheat codes here:")
if secret == "Wiebe Weakness":
    inventory.append("Wiebe_Weakness")
    Secret = True
    print("You found the secret weapon...")
elif secret == "Wiebe Sword":
    weapons.append("Wiebe Sword")
    print("You can now use the ultimate weapon in combat!")
elif secret == "all weapons get":
    weapons.append("Leaf Blade" "Wiebe Sword" "Ice Blade" "FrostBite Beam" "Magma Blade")
    weapons.append("")
input("%s: %s, the world of %s is on the verge of destruction" % (Guide, You, World))

input("This is being caused by the evil wizard %s" % Villain)
input("%s: The world of %s is split into 4 distinct regions, each is going through a problem" % (Guide, World))
input("%s: These problems are all being caused by %s" % (Guide, Villain))
Region_to_Explore = input("Which region would you like to go to first? Plantopia or Hydro Kingdom? ")
if Region_to_Explore == "Flex World":
    input("%s: Where am I???" % You)
    input("You've been stabbed!")
    input("Phil Swift: THAT'S ALOTTA DAMAGE!")
    input("Phil Swift: HOW ABOUT SOME MORE?!")
    input("You've been attacked with a chainsaw!")
    print("You've been turned into Flex Glue!!")
    input("GAME OVER")
if Region_to_Explore == "Swamp":
    input("Shrek: WHAT ARE YOU DOIN IN MY SWAMP?!?!")
    Your_Health -= 30
    print("%s has died. You have lost and %s will take over %s" % (You, Villain, World))
if Region_to_Explore == "19A":
    print("... You shouldn't be here....")
    input("Wiebe appeared!")
    Choice = input("Fight or Flee?")
    if Choice == "Fight":
        if not Secret:
            input("You missed! You did absolutely nothing! 0 Damage done to Wiebe!")
            input("Wiebe used Pep8 Pow!")
            input("30 damage done to you!")
            Your_Health -= Your_Health
        if Your_Health == 0:
            input("You lost to Wiebe. GAME OVER")
            print("Pep8: Dead")
        if Secret:
            Fight_option = input("Magic Sword  Wiebe Weakness")
            if Fight_option == "Win":
                input("%s used" % You)
                print("bsdhfsbjvmdlkfjssf!")
                input("1234567890987654323456765456766548476584835642456765 damage to Wiebe!")
                input("You win!!")
                input("You got 99999 gold! You get Wiebe Sword")
                weapons.append("Wiebe Sword")
                input("Now to the final boss!")
                print()
                print()
                input("%s appeared!" % Villain)
                Fight_option = input("Attack: Wiebe Sword")
                if Fight_option == "Wiebe Sword":
                    input("%s attacked with Wiebe Sword!" % You)
                    input("∞ damage to %s!" % Villain)
                    input("%s: NOOO NOO! I can't lose!!! You.... you.... you...." % Villain)
                    input("%s; You did it... you saved us all...." % Guide)
                    input("%s: Yeah! I did it! I'm unstoppable!" % You)
                    input("%s:I saved Plantopia, the Hydro Kingdom, Magma Dome, and Frost Paradise!" % You)
                    input("I won!!")
                    print("YOU WIN")
                    print("But you kinda cheated a bit...")
            if Fight_option == "Magic Sword":
                input("You missed! You did absolutely nothing! 0 Damage done to Wiebe!")
                input("Wiebe used Pep8 Pow!")
                input("30 damage done to you!")
                Your_Health -= Your_Health
                if Your_Health == 0:
                    input("You lost to Wiebe. GAME OVER")
                    print("Pep8: Dead")
            if Fight_option == "Wiebe Weakness":
                input("You did 999999999 damage to Wiebe")
                input("You win! You beat Wie12y784237493uyr838594387485")
                input("Wiebe: You can't win")
                input("Wiebe uses break code!")
                input("3278r3723897864ewoidjshwd damge to kfherdsbgfyerg891389489rthfudcfj00")
                print("GaMe OVEr")
                print(" wjqadeksfhajKWDLAFUEIWG I29043EQWU  iqufbdwijoq785e2d")
    if Choice == "Flee":
        input("You couldn't escape!")
        input("Wiebe used Bad Joke Friday!")
        input("You are now laughing uncntrollably... You can't get a chance to breathe...")
        input("You die of suffocation")
        Your_Health -= Your_Health
        if Your_Health == 0:
            input("You lost to Wiebe. GAME OVER")
            print("You died to bad jokes... What a horrible PUNishment")
if Region_to_Explore == "Plantopia":
    input("%s: Okay... Plantopia is a rainforest normally full of friendly animals" % Guide)
    input("%s: However %s has turned the animals into fierce beasts! Even the plants can kill you!" % (Guide, Villain))
    input("%s: This is being done via some sort of magical beast" % Guide)
    input("%s: Alright, Plantopia. Let's get through here" % You)
    Path = input("There are two directions, one with nothing in sight and one with some monkeys. Which do you choose? ")
    if Path == "nothing":
        input("You fell into quick sand!")
        Quick_Sand = input("Do you reach for the vines or do you struggle to get out?")
        if Quick_Sand == "vines":
            input("You reach out for the vines... It's a snake you goof!!")
            Your_Health -= 20
            input("The snake bites you... You now have %s health" % Your_Health)
            input(" You start to sink further into the quicksand... You've been engulfed bu it")
            input("GAME OVER")
            print("Wow... that's not how you use Python!")
    if Path == "monkeys":
        input("You go through the monkey path, they start attacking you fiercely.")
        Your_Health -= 5
        input("You lose 5 health. You have %i health" % Your_Health)
        Monkey_Attack = input("How do you retaliate? Do you try to throw them off? Or do you hit them with your sword?")
        if Monkey_Attack == "sword":
            input("You attack the monkeys with your sword. They run away")
            input("%s: Those monkeys left something behind..." % You)
            print("You got a banana! Eating this will restore 20 HP")
            input("%s: Ah, you got an item! Open your inventory with 'i' during certain lines of dialogue" % Guide)
            open_inventory = input("Try it now!")
            if open_inventory == "i":
                print(inventory)
                input("%s: Try using that banana you just got! Just type in banana in the next text box" % Guide)
                item_used = input("What item do you want to use? ")
                if item_used == "banana":
                    Your_Health += 20
                    print("You used the banana! You recovered 20 HP! You now have %i HP" % Your_Health)
            input("%s: THIS IS A GOOD BANANA!" % You)
            input("%s: Alright time to keep going" % You)
            Path = input("You look at the path, do you continue to follow it? Or do you try to go through the trees")
            if Path == "path":
                input("%s: AAAAAAAAAAAHHHH!!!! A BEAR!" % You)
                input("Bear appeared!")
                in_battle = True
                while in_battle:
                    Choice = input("Fight or Flee?")
                    if Choice == "Flee" and Flee_Chance == 8:
                        print("YOU GOT AWAY!")
                        in_battle = False
                    elif Choice == "Flee" and Flee_Chance != 8:
                        print("You couldn't escape!")
                        input("Bear used Slash!")
                        Your_Health -= 15
                        print("You: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
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
                print("You got killed by monkeys... That's bananas!")