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
            order.append(aa)
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
            order.append(aa)
            b = input(colored("%s Computer: Would you like to order another drink?" % str(z), "green", 'on_grey'))
            if b.lower() == "yes":
                print(colored("%s Computer: Very well then..." % str(z), 'green', 'on_grey'))
            elif b.lower() == "no":
                print(colored("%s Computer: Okay then... good day" % str(z), 'green', 'on_grey'))
                return order
            elif b.lower() == 'pass':
                print(colored("%s Computer: Alright then... I see you dislike the drink selection... *sniff sniff* "
                              "it's not like I... put a lot of time and thought into"
                              " the options I gave you..." % str(z)), "green", "on_grey")
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(z), 'green', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(z)), "red", "on_grey")
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: Alright then... I see you dislike the drink selection... *sniff sniff* "
                          "it's not like I... put a lot of time and thought into"
                          " the options I gave you..." % str(z)), "green", "on_grey")
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
            order.append(aa)
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
                              "want fries.... why not?" % str(h)), "yellow", "on_grey")
                break
            else:
                print(colored("%s Computer: I'll take that as a no... good day to you" % str(h), 'yellow', 'on_grey'))
                return order
        elif aa.lower() == 'q':
            print(colored("%s Computer: Ah... I see... you would like to quit..."
                          " alright... see you later alligator" % str(h)), "red", "on_grey")
            return aa
        elif aa.lower() == 'pass':
            print(colored("%s Computer: You don't like fries? Are you SALTY"
                          " about something that happened? eh? eh?"
                          "\n Not funny? Oh well... If you actually don't "
                          "want fries.... why not?" % str(h)), "yellow", "on_grey")
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
                              "nds... and it ain't ketchup..." % str(h)), "red", "on_grey")
                break
            elif aa.lower() == 'q':
                print(colored("%s Computer: Ah... I see... you would like to quit..."
                              " alright... see you later alligator" % str(h)), "magenta", "on_grey")
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

def order_off_the_menu(restaurant_name):
    snadwich = sandwich(restaurant_name)
    if snadwich == "q":
        return
    how_am_i_supposed_to_eat_this_pizza_without_my_drink = drink(restaurant_name)
    if how_am_i_supposed_to_eat_this_pizza_without_my_drink == "q":
        return
    fries(restaurant_name)
    ketchup(restaurant_name)
    receipt(restaurant_name)


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
