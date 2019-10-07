from termcolor import colored
import sys
import random


def pizza_time(a):
    pizzaing = True
    order = []
    while pizzaing:
        aa = input(colored("%s Computer: Good afternoon to you sir/madam, what Pizza would"
                           " you like to order? (Write out the full menu item)"
                           "\n- Cheese Pizza: $6.26"
                           "\n- Peperoni: $7.26"
                           "\n- Veggie Lover's: $6.48"
                           "\n- Meat Lover's: 8.44"
                           "\n- Vegan: $4.36"
                           "\n- Pineapple Pizza: Your reputation and $5.32"
                           "\n- Olive Pizza: $6.44"
                           "\n- Super Mario Pizza (Mushroom Pizza): $7.40"
                           "\n- The ultimate Pizza Time Pizza (Meat Lover's + Veggie Lovers): $10.20"
                           "\n - " % str(a), 'yellow', 'on_grey'))
        peezas = ["cheese", 'peperoni', "veggie lover's", "meat lover's", 'vegan', 'pineapple',
                  'olive', 'super mario', 'pizza time', 'combo']
        if aa.lower() in peezas:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order another pizza?" % str(a), "yellow", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(a), 'yellow', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(a), 'yellow', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you dislike the pizzas.... "
                              "Then why are you here? Either way... Alright then... Enjoy your next"
                              " option" % str(a), "yellow", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(a), 'yellow', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(a)), "red", "on_grey")
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: Alright then... I see you dislike the pizzas.... "
                          "Then why are you here? Either way... Alright then... Enjoy your next"
                          " option" % str(a), "yellow", "on_grey"))
            aa = ""
            return
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(a), 'green', 'on_grey'))


def chips(z):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Computer: Alright and what chips would you like?"
                           "\n - Hot Cheetos: $1.39"
                           "\n - Doritos: $1.45"
                           "\n - Fritos: $1.25"
                           "\n - Lays: $1.59"
                           "\n -" % str(z), 'red', 'on_grey'))
        cheos = ["hot cheetos", 'doritos', 'fritos', 'lays']
        if aa.lower() in cheos:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order more chips?" % str(z), "red", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(z), 'red', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(z), 'red', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you dislike the selection of chips... *sniff sniff* "
                              "it's not like I... put a lot of time and thought into"
                              " the options I gave you..." % str(z), "red", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(z), 'red', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(z), "magenta", "on_grey"))
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: Alright then... I see you dislike the selection of chips... *sniff sniff* "
                          "it's not like I... put a lot of time and thought into"
                          " the options I gave you..." % str(z), "red", "on_grey"))
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(z), 'red', 'on_grey'))


def bread(z):
    getting_this_bread = True
    order = []
    while getting_this_bread:
        aa = input(colored("%s Computer: Alright and what bread would you like?"
                           "\n - Standard Rolls: $2.39"
                           "\n - Pretzels: $2.45"
                           "\n - The Michael Scott Pretzel: Caloric Overload!: $4.20"
                           "\n - Banana Bread: $2.79"
                           "\n -" % str(z), 'yellow', 'on_grey'))
        the_graaaaaaains_true_form = ["rolls", 'pretzels', 'the michael scott pretzel', 'banana bread']
        if aa.lower() in the_graaaaaaains_true_form:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order more bread?" % str(z), "yellow", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(z), 'yellow', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(z), 'yellow', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you are not a gamer as you do "
                              "not want to get this bread..." % str(z), "yellow", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(z), 'yellow', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(z), "red", "on_grey"))
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: Alright then... I see you are not a gamer as you do "
                          "not want to get this bread..." % str(z), "yellow", "on_grey"))
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(z), 'yellow', 'on_grey'))


def sodas(z):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Computer: Alright and what size beverage would you like?"
                           "\n - Small Pepsi: $1.55"
                           "\n - Medium Pepsi: $2.55"
                           "\n - Large Pepsi: $3.25"
                           "\n - Small Sprite: $1.75"
                           "\n - Medium Sprite: $2.65"
                           "\n - Large Sprite: $3.75"
                           "\n- Small Coke: $2.50"
                           "\n- Medium Coke: $3.50"
                           "\n- Large Coke: $ 4.20"
                           "\n- Terrible Beverage: Milk + Soda Mix: $4.40"
                           "\n -" % str(z), 'green', 'on_grey'))
        droonks = ["small pepsi", 'medium pepsi', 'large pepsi', "small sprite", 'medium sprite',
                   'large sprite', "small coke", 'medium coke', 'large coke', 'milk + soda mix']
        if aa.lower() in droonks:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order another drink?" % str(z), "green", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(z), 'green', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(z), 'green', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you dislike the drink selection... *sniff sniff* "
                              "it's not like I... put a lot of time and thought into"
                              " the options I gave you..." % str(z), "green", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(z), 'green', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(z), "red", "on_grey"))
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: Alright then... I see you dislike the drink selection... *sniff sniff* "
                          "it's not like I... put a lot of time and thought into"
                          " the options I gave you..." % str(z), "green", "on_grey"))
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(z), 'green', 'on_grey'))


def sweets(h):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Computer: Alright and what dessert would you like?"
                           "\n - Chocolate Lava Cake: $5.48"
                           "\n - Tart: $4.76"
                           "\n - Ice Cream Sundae with Chocolate Sauce and many sprinkles: $3.25"
                           "\n - Pokeball Surprise! (A cake pop in the shape of a Pokeball with a "
                           "Pokemon toy inside): $ 5.50"
                           "\n -" % str(h), 'magenta', 'on_grey'))
        frees = ["chocolate lava cake", 'tart', 'ice cream sundae', 'pokeball surprise']
        if aa.lower() in frees:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order another "
                              "dessert?" % str(h), "magenta", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(h), 'magenta', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(h), 'magenta', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: You don't want dessert. SWEET less work for the staff! "
                              "Get it? C'mon that was good... I gotta say... Your PUDDING me on the spot if "
                              "you expect better humor! Eh? Eh? Okay... I'll stop" % str(h), "magenta", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(h), 'magenta', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(h), "red", "on_grey"))
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: You don't want dessert. SWEET less work for the staff! "
                          "Get it? C'mon that was good... I gotta say... Your PUDDING me on the spot if "
                          "you expect better humor! Eh? Eh? Okay... I'll stop" % str(h), "magenta", "on_grey"))
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(h), 'magenta', 'on_grey'))


def extra_cheese(h):
    the_cheesey = True
    cheeses = 0
    while the_cheesey:
        aa = input(colored("%s Computer: How many Cheeeeeseyy brand extra Cheese packets would "
                           "you like? They are $0.75 each" % str(h), 'yellow', 'on_grey'))
        try:
            if int(aa) == 0:
                print(colored("%s Computer: You don't want Cheeeeeseyy brand extra Cheese packets packets?"
                              "\n You do know what Cheeeeesey Co. does when someone doesn't want their Cheese, right?"
                              "\n Let's just say... I hope you don't like being dropped into a vat of molten "
                              "cheese" % str(h), "yellow", "on_grey"))
                return aa
            elif int(aa) < 0:
                print(colored("%s Computer: You can't have "
                              "negative cheese! That would destroy our very fabric "
                              "of existence!" % str(h), "red", "on_grey"))
                fate_of_the_world = input(colored("%s Computer: Do you still want negative"
                                                  " cheese? Y or N" % str(h), "red", "on_grey"))
                if fate_of_the_world.lower() == 'y':
                    print(colored("%s Computer: Wait! What?! NO"
                                  "\n The fabric of our existence is tearing apart!"
                                  "\nNOOOOOOOOOOOOOO)SU568768796Jq wgbuyrfgvbwuyr"
                                  "h42069jfgyuwergs7ydvbwtye6987687vftywgeytufgv4TY3GWGFYUGR"
                                  "🕷🕸🔌🔦🔌⋷🐘🩩⋶🕚🩢𝋫𖺋∉🐘☠💀🕱⛹🙎🙋🧔😣" % str(h), "magenta", "on_grey"))
                    sys.exit()
                elif fate_of_the_world.lower() == 'n':
                    print(colored("%s Computer: A wise choice..." % str(h), "magenta", "on_grey"))
            elif aa.lower() == 'q':
                aa = 'q'
                print(colored("%s Computer: Ah... I see... you would like to quit..."
                              " alright... see you later alligator" % str(h), "magenta", "on_grey"))
                break
            else:
                try:
                    cheeses += int(aa)
                except ValueError:
                    print(colored("%s Computer: That isn't a number..." % str(h), "red", 'on_grey'))
                else:
                    b = input(colored("%s Computer: Would you like to order anymore "
                                      "Cheeeeeseyy brand extra Cheese packets?" % str(h), "red", 'on_grey'))
                    if b.lower() == "yes":
                            print(colored("%s Computer: Very well then..." % str(h), 'red', 'on_grey'))
                    elif b.lower() == "no":
                        print(colored("%s Computer: Okay then... good day" % str(h), 'red', 'on_grey'))
                        return cheeses
                    elif b.lower() == 'pass':
                        print(colored("%s Computer: You don't want Cheeeeeseyy brand extra Cheese "
                                      "packets?"
                                      "\n You do know what Cheeeeeseyy Co."
                                      " does when someone doesn't want their cheese, right?"
                                      "\n Let's just say... I hope you don't like being dropped into a vat of molten "
                                      "cheese" % str(h)), "red", "on_grey")
                        the_cheesey = False
                        break
                    else:
                        print(colored("%s Computer: I'll take that as a no... good da"
                                      "y to you" % str(h), 'red', 'on_grey'))
                        return cheeses
        except ValueError:
            print("That wasn't a number")


def pepe(h):
    rare_pepe_i_mean_pepper = True
    potts = 0
    while rare_pepe_i_mean_pepper:
        aa = input(colored("%s Computer: How many Peeper brand red pepper flake packets would "
                           "you like? They cost $0.90 each" % str(h), 'red', 'on_grey'))
        try:
            if int(aa) == 0:
                print(colored("%s Computer: You don't want Peeper brand red pepper flake packets packets?"
                              "\n You do know what Peeper Industries does when someone doesn't want their pepper,"
                              " right?"
                              "\n Let's just say... I hope you don't like eating 10 tons of "
                              "ghost peppers" % str(h), "red", "on_grey"))
                return aa
            elif int(aa) < 0:
                print(colored("%s Computer: You can't have "
                              "negative pepper! That would destroy our very fabric "
                              "of existence!" % str(h), "red", "on_grey"))
                fate_of_the_world = input(colored("%s Computer: Do you still want negative"
                                                  " pepper? Y or N" % str(h), "red", "on_grey"))
                if fate_of_the_world.lower() == 'y':
                    print(colored("%s Computer: Wait! What?! NO"
                                  "\n The fabric of our existence is tearing apart!"
                                  "\nNOOOOOOOOOOOOOO)SU568768796Jq wgbuyrfgvbwuyr"
                                  "h42069jfgyuwergs7ydvbwtye6987687vftywgeytufgv4TY3GWGFYUGR"
                                  "🕷🕸🔌🔦🔌⋷🐘🩩⋶🕚🩢𝋫𖺋∉🐘☠💀🕱⛹🙎🙋🧔😣" % str(h), "magenta", "on_grey"))
                    sys.exit()
                elif fate_of_the_world.lower() == 'n':
                    print(colored("%s Computer: A wise choice..." % str(h), "magenta", "on_grey"))
            elif aa.lower() == 'q':
                aa = 'q'
                print(colored("%s Computer: Ah... I see... you would like to quit..."
                              " alright... see you later alligator" % str(h), "magenta", "on_grey"))
                break
            else:
                try:
                    potts += int(aa)
                except ValueError:
                    print(colored("%s Computer: That isn't a number..." % str(h), "red", 'on_grey'))
                else:
                    b = input(colored("%s Computer: Would you like to order anymore "
                                      "Peeper brand red pepper flake packets?" % str(h), "red", 'on_grey'))
                    if b.lower() == "yes":
                            print(colored("%s Computer: Very well then..." % str(h), 'red', 'on_grey'))
                    elif b.lower() == "no":
                        print(colored("%s Computer: Okay then... good day" % str(h), 'red', 'on_grey'))
                        return potts
                    elif b.lower() == 'pass':
                        print(colored("%s Computer: You don't want Peeper brand pepper flake "
                                      "packets?"
                                      "\n You do know what Peeper Industries"
                                      " does when someone doesn't want their pepper, right?"
                                      "\n Let's just say... I hope you don't like eating 10 tons of "
                                      "ghost peppers" % str(h)), "red", "on_grey")
                        rare_pepe_i_mean_pepper = False
                        break
                    else:
                        print(colored("%s Computer: I'll take that as a no... good da"
                                      "y to you" % str(h), 'red', 'on_grey'))
                        return potts
        except ValueError:
            print("That wasn't a number")


def receipt(name, a, b, c, d, e, f, g):
    cost = 0
    toys = ['Meowth', 'Pikachu', 'Eevee', "Charizard", "Shiny Charizard", "Shiny Meowth", "Shiny Eevee",
            'Shiny Pikachu', 'Blastoise', 'Shiny Blastoise', 'Venusaur', "Shiny Venusaur", 'Mew', "Shiny Mew",
            "Mewtwo", "Shiny Mewtwo"]
    toys2 = 0
    if e is None:
        print()
    else:
        for i in range(len(e)):
            if e[i] == 'pokeball surprise':
                toys2 += 1
    consequences_of_the_pizza_time = {'cheese': 6.26,
                                      'peperoni': 7.26, "veggie lover's": 6.48, "meat lover's": 8.44,
                                      'vegan': 4.36, 'pineapple': 5.32, 'olive': 6.44, 'super mario': 7.40,
                                      'pizza time': 10.20}
    costs_dronk = {'small pepsi': 1.55,
                   'medium pepsi': 2.55, 'large': 3.25, 'small sprite': 1.75,
                   'medium sprite': 2.65, 'large sprite': 3.75, 'small coke': 2.50, 'medium coke': 3.50,
                   'large coke': 4.20, 'milk + soda mix': 4.40}
    costs_chip = {'hot cheetos': 1.39, 'doritos': 1.45, 'fritos': 1.25, 'lays': 1.59}
    costs_bread = {'rolls': 2.39, 'pretzels': 2.45,
                   'the michael scott pretzel': 4.20, 'banana bread': 2.79}
    costs_sweets = {'chocolate lava cake': 5.48, 'tart': 4.76, 'ice cream sundae': 3.25,
                    'pokeball surprise': 5.50}
    if a is None:
        print(colored("You didn't order any pizza", 'white', 'on_grey'))
    else:
        print(colored("You ordered the following pizzas:", 'white', 'on_grey'))
        for i in range(len(a)):
            if a[i] in consequences_of_the_pizza_time:
                cost += consequences_of_the_pizza_time[a[i]]
                print(str(i + 1) + ": " + colored(a[i], 'white', 'on_grey') + colored(' pizza - ', 'white', 'on_grey') +
                      colored(consequences_of_the_pizza_time[a[i]], 'white', 'on_grey'))
    if b is None:
        print(colored("You didn't order any chips", 'white', 'on_grey'))
    else:
        print(colored("You ordered the following chips:", 'white', 'on_grey'))
        for i in range(len(b)):
            if b[i] in costs_chip:
                cost += costs_chip[b[i]]
                print(str(i + 1) + ": some" + colored(b[i], 'white', 'on_grey') + colored('s - ', 'white',
                                                                                          'on_grey') + colored(
                    costs_chip[b[i]], 'white', 'on_grey'))
    if c is None:
        print(colored("You didn't order any drinks", 'white', 'on_grey'))
    else:
        print(colored("You ordered the following drinks:", 'white', 'on_grey'))
        for i in range(len(c)):
            if c[i] in costs_dronk:
                cost += costs_dronk[c[i]]
                print(str(i + 1) + ": a " + colored(c[i], 'white', 'on_grey') + colored(' - ', 'white',
                                                                                        'on_grey') + colored(
                    costs_dronk[c[i]], 'white', 'on_grey'))
    if d is None:
        print(colored("You didn't order any bread", 'white', 'on_grey'))
    else:
        print(colored("You ordered the following bread:", 'white', 'on_grey'))
        for i in range(len(d)):
            if d[i] in costs_bread:
                cost += costs_bread[d[i]]
                print(str(i + 1) + ": " + colored(d[i], 'white', 'on_grey') + colored(' - ', 'white',
                                                                                      'on_grey') + colored(
                    costs_bread[d[i]], 'white', 'on_grey'))
    if e is None:
        print(colored("You didn't order any dessert", 'white', 'on_grey'))
    else:
        print(colored("You ordered the following desserts:", 'white', 'on_grey'))
        for i in range(len(e)):
            if e[i] in costs_sweets:
                cost += costs_sweets[e[i]]
                print(str(i + 1) + ": " + colored(e[i], 'white', 'on_grey') + colored(' - ', 'white',
                                                                                      'on_grey') + colored(
                    costs_sweets[e[i]], 'white', 'on_grey'))
        while toys2 > 0:
            zz = random.choice(toys)
            print(colored("You opened up the container in your cake pop and you found a " + zz + ' Figurine'
                                                                                                 ' inside!', 'white',
                          'on_red'))
            if 'Shiny' in zz:
                print(colored("Wow! A Figurine of a Shiny Pokemon! A Rare Find!", 'red', 'on_blue'))
            toys2 -= 1
    print(colored("You also ordered %d Peeper brand red pepper flake packets which "
                  "costed $%f" % (f, .90 * f), 'white', 'on_grey'))
    print(colored("You also ordered %d Cheeeeeseyy brand extra Cheese packets which "
                  "costed $%f" % (f, .75 * f), 'white', 'on_grey'))
    cost += .75 * f
    cost += .90 * g
    cost += cost * 0.07
    if cost >= 15.00:
        cost -= 5.00
    if a is not None and b is not None and c is not None and d is not None and e is not None:
        cost -= 1.00
    for i in range(len(str(cost)) - 1):
        if str(cost)[i - 1] is '.':
            if len(str(cost)[i:]) >= 3:
                cost = round(cost, 2)
            else:
                cost = str(cost) + "0"
    if str(cost) == "0.0":
        cost = "0.00"
    print("Your total comes out to $" + str(cost))
    again = input(colored("%s Computer: Would you like to order another "
                          "meal? Y or N" % str(name), "magenta", "on_grey"))
    if again.lower() == 'y':
        order_off_the_menu(name)
    else:
        print(colored("%s Computer: I'll take that as a no" % str(name), "magenta", "on_grey"))
        sys.exit()


def order_off_the_menu(restaurant_name):
    input(colored("%s Computer: Ah, hello sir/madam, how are you? Today we are "
                  "running multiple specials. If you spend $15 or above,we will take "
                  "$5 off your price, and should you buy one of each menu item, you'll get 1.00 taken off your "
                  "price" % str(restaurant_name), 'magenta', 'on_grey'))
    aaaa = input(colored("Would you like a terrible intro? Y or N", 'red', 'on_grey'))
    if aaaa.upper() == "N":
        print(colored("%s Computer: Hello, and welcome to %s! If at any point you would like to quit, simply "
                      "type in 'q', \n should you want to pass on a menu item, type in 'pass'. However, "
                      "if you don't want condiments, don't type in 'pass', instead, type in '0' when asked "
                      "how much you'd like" % (restaurant_name, restaurant_name), 'magenta', 'on_grey'))
    elif aaaa.upper() == "Y":
        print(colored("%s Computer: Hewwo UwU, and welcome to %s owo! If at any point you would like to quit, simply "
                      "type in 'q', but don't think that means you'll escape the owo "
                      "army! \n Should you want to pass on a menu item, type in 'pass'."
                      " However, we'll also make sure you pass too!. However, "
                      "if you don't want a condiment, don't type in 'pass', instead, type in '0', not 0w0, when asked "
                      "how much you'd like owo uwu "
                      "IuI" % (restaurant_name, restaurant_name), 'magenta', 'on_grey'))
    else:
        print(colored("I did not get a proper response, so I'll take that as a yes!", 'red', 'on_grey'))
        print(colored("%s Computer: Hewwo UwU, and welcome to %s owo! If at any point you would like to quit, simply "
                      "type in 'q', but don't think that means you'll escape the owo "
                      "army! \n Should you want to pass on a menu item, type in 'pass'."
                      " However, we'll also make sure you pass too!. However, "
                      "if you don't want a condiment, don't type in 'pass', instead, type in '0', not 0w0, when asked "
                      "how much you'd like owo uwu "
                      "IuI" % (restaurant_name, restaurant_name), 'magenta', 'on_grey'))
    poiza = pizza_time(restaurant_name)
    if poiza == "q":
        return
    chipppppppps = chips(restaurant_name)
    if chipppppppps == 'q':
        return
    how_am_i_supposed_to_eat_this_pizza_without_my_drink = sodas(restaurant_name)
    if how_am_i_supposed_to_eat_this_pizza_without_my_drink == "q":
        return
    grains = bread(restaurant_name)
    if grains == 'q':
        return
    the_sweet_sweet_song_of_death = sweets(restaurant_name)  # This is a video game reference
    if the_sweet_sweet_song_of_death == 'q':
        return
    cheeeeeeeeeeeeeeseeyys_labrynth_of_lies_and_deception = extra_cheese(restaurant_name)
    if cheeeeeeeeeeeeeeseeyys_labrynth_of_lies_and_deception == 'q':
        return
    pepper_potts = pepe(restaurant_name)
    if pepper_potts == 'q':
        return
    receipt(restaurant_name, poiza, chipppppppps,
            how_am_i_supposed_to_eat_this_pizza_without_my_drink,
            grains, the_sweet_sweet_song_of_death,
            cheeeeeeeeeeeeeeseeyys_labrynth_of_lies_and_deception,
            pepper_potts)


order_off_the_menu("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                   "AAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH")
