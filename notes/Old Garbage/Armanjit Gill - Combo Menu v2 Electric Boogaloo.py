from termcolor import colored


def sandwich(a):
    sandwiching = True
    order = []
    while sandwiching:
        aa = input(colored("%s Computer: Good afternoon to you sir/madam, what Sandwich would"
                           " you like to order? (Write out the full menu item)"
                           "\n- Chicken Sandwich: $5.25"
                           "\n- Beef Sandwich: $6.25"
                           "\n- Tofu Sandwich: $5.75"
                           "\n - " % str(a), 'yellow', 'on_grey'))
        sanswiches = ["chicken sandwich", 'beef sandwich', 'tofu sandwich']
        if aa.lower() in sanswiches:
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order another sandwich?" % str(a), "yellow", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(a), 'yellow', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(a), 'yellow', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you dislike the snadw- "
                              "I mean sanswic- I mean sandwiches. Alright then... Enjoy your next"
                              " option" % str(a)), "yellow", "on_grey")
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
            print(colored("%s Computer: Alright then... I see you dislike the snadw- "
                          "I mean sanswic- I mean sandwiches. Alright then... Enjoy your next"
                          " option" % str(a)), "yellow", "on_grey")
            aa = ""
            return
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(a), 'green', 'on_grey'))


def drink(z):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Computer: Alright and what size beverage would you like?"
                           "\n - Small: $1.00"
                           "\n - Medium: $1.75"
                           "\n - Large: $2.25"
                           "\n -" % str(z), 'green', 'on_grey'))
        droonks = ["small", 'medium', 'large']
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


def fries(h):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Computer: Alright and what size beverage would you like?"
                           "\n - Small: $1.00"
                           "\n - Medium: $1.75"
                           "\n - Large: $2.25"
                           "\n -" % str(h), 'yellow', 'on_grey'))
        frees = ["small", 'medium', 'large']
        if aa.lower() in frees:
            if aa.lower() == "small":
                fryes = input(colored("%s Computer: Would you like to mega-size your "
                                      "fries instead?" % str(h), "yellow", 'on_grey'))
                if fryes.lower() in ["sure", 'yeah', 'yes', 'yee']:
                    print(colored("%s Computer: hehehehehe sucker... - I mean alrigh"
                                  "t... nice!" % str(h), "yellow", 'on_grey'))
                    aa = "large"
                elif fryes.lower() in ['no', 'nah', 'nope', 'not at all', 'no god please no. no. no. nooooooooooo']:
                    if fryes.lower == 'no god please no. no. no. nooooooooooo':
                        print(colored("%s Computer: Calm Down Michael Scott!" % str(h), "yellow", 'on_grey'))
                    else:
                        print(colored("%s Computer: Fine... have it your way..."
                                      "ₚₑₐₛₐₙₜ" % str(h), "yellow", 'on_grey'))
            order.append(aa.lower())
            b = input(colored("%s Computer: Would you like to order another set of"
                              " fries?" % str(h), "yellow", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(h), 'yellow', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(h), 'yellow', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: You don't like fries? Are you SALTY"
                              " about something that happened? eh? eh?"
                              "\n Not funny? Oh well... If you actually don't "
                              "want fries.... why not?" % str(h), "yellow", "on_grey"))
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(h), 'yellow', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            aa = 'q'
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(h), "red", "on_grey"))
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: You don't like fries? Are you SALTY"
                          " about something that happened? eh? eh?"
                          "\n Not funny? Oh well... If you actually don't "
                          "want fries.... why not?" % str(h), "yellow", "on_grey"))
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(h), 'yellow', 'on_grey'))


def ketchup(h):
    ketchuping = True
    ketches = 0
    while ketchuping:
        aa = input(colored("%s Computer: How many Kepchup brand ketchup packets would "
                           "you like?" % str(h), 'red', 'on_grey'))
        try:
            if int(aa) == 0:
                print(colored("%s Computer: You don't want Kepchup brand ketchup packets?"
                              "\n You do know what Kepchup Co. does when someone doesn't want their ketchup, right?"
                              "\n Let's just say... something red will be on their ha"
                              "nds... and it ain't ketchup..." % str(h), "red", "on_grey"))
                break
            elif aa.lower() == 'q':
                aa = 'q'
                print(colored("%s Computer: Ah... I see... you would like to quit..."
                              " alright... see you later alligator" % str(h), "magenta", "on_grey"))
                break
            else:
                try:
                    ketches += aa
                except ValueError:
                    print(colored("%s Computer: That isn't a number..." % str(h), "red", 'on_grey'))
                else:
                    b = input(colored("%s Computer: Would you like to order anymore Kepchup brand Ketchup "
                                      "packets?" % str(h), "red", 'on_grey'))
                    if b.lower() == "yes":
                            print(colored("%s Computer: Very well then..." % str(h), 'red', 'on_grey'))
                    elif b.lower() == "no":
                        print(colored("%s Computer: Okay then... good day" % str(h), 'red', 'on_grey'))
                        return ketches
                    elif b.lower() == 'pass':
                        print(colored("%s Computer: You don't want Kepchup brand ketchup packets?"
                                      "\n You do know what Kepchup Co."
                                      " does when someone doesn't want their ketchup, right?"
                                      "\n Let's just say... something red will be on the"
                                      "ir hands... and it ain't ketchup..." % str(h)), "red", "on_grey")
                        ketchuping = False
                        break
                    else:
                        print(colored("%s Computer: I'll take that as a no... good day to you" % str(h), 'red', 'on_grey'))
                        return ketches
        except ValueError:
            print("That wasn't a number")


def receipt(name, a, b, c, d):
    e = 0
    costs_snad = {'beef sandwich': 6.25,
                  'chicken sandwich': 5.25, 'tofu sandwich': 5.75}
    for i in range(len(a)):
        if a[i] in costs_snad:
            e += costs_snad[a[i]]

    e += e * 0.07
    if e >= 15.00:
        e -= 5.00
    if "chicken sandwich" in a and "small" in b and "small" in c:
        e -= 2.50
    if len(a) > 0 and b is None and c is None and d is None:
        e -= 1.25
    try:
        if len(c) > 0 and len(b) > 0 and len(a) > 0:
            e -= 1.00
    except TypeError:
        print()
    for i in range(len(str(e)) - 1):
        if str(e)[i - 1] is '.':
            if len(str(e)[i:]) >= 3:
                e = round(e, 2)
            else:
                e = str(e) + "0"
    if str(e) == "0.0":
        e = "0.00"
    print("Your total comes out to $" + str(e))


def order_off_the_menu(restaurant_name):
    aaaa = input(colored("Would you like a terrible intro? Y or N", 'red', 'on_grey'))
    if aaaa.upper() == "N":
        print(colored("%s Computer: Hello, and welcome to %s! If at any point you would like to quit, simply "
                      "type in 'q', \n should you want to pass on a menu item, type in 'pass'. However, "
                      "if you don't want ketchup, don't type in 'pass', instead, type in '0' when asked "
                      "how many packets you'd like" % (restaurant_name, restaurant_name), 'magenta', 'on_grey'))
    else:
        print(colored("I did not get a proper response, so I'll take that as a yes!", 'red', 'on_grey'))
        print(colored("%s Computer: Hewwo UwU, and welcome to %s owo! If at any point you would like to quit, simply "
                      "type in 'q', but don't think that means you'll escape the owo army! \n Should you want to pass on a menu item, type in 'pass'."
                      " However, we'll also make sure you pass too!. However, "
                      "if you don't want ketchup, don't type in 'pass', instead, type in '0', not 0w0, when asked "
                      "how many packets you'd like owo uwu IuI" % (restaurant_name, restaurant_name), 'magenta', 'on_grey'))
    snadwich = sandwich(restaurant_name)
    if snadwich == "q":
        return
    how_am_i_supposed_to_eat_this_pizza_without_my_drink = drink(restaurant_name)
    if how_am_i_supposed_to_eat_this_pizza_without_my_drink == "q":
        return
    evie_and_jacob_frye = fries(restaurant_name)
    if evie_and_jacob_frye == 'q':
        return
    kepchups_labrynth_of_lies_and_deception = ketchup(restaurant_name)
    if kepchups_labrynth_of_lies_and_deception == 'q':
        return
    receipt(restaurant_name, snadwich,
            how_am_i_supposed_to_eat_this_pizza_without_my_drink,
            evie_and_jacob_frye, kepchups_labrynth_of_lies_and_deception)


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
