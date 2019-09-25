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
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(a), 'green', 'on_grey'))


def drink(z):
    drinking = True
    order = []
    while drinking:
        aa = input(colored("%s Waiter: Alright and what size beverage would you like?"
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
            print(colored("%s Computer: Alright then... I see you dislike the snadw- "
                          "I mean sanswic- I mean sandwiches. Alright then... Enjoy your next"
                          " option" % str(z)), "green", "on_grey")
            break
        else:
            print(colored("%s Computer: Sorry... that isn't on the menu you nerd!" % str(a), 'green', 'on_grey'))


def order_off_the_menu(restaurant_name):
        if sandwich(restaurant_name) == "q":
            return
        drink(restaurant_name)
        fries(restaurant_name)
        ketchup(restaurant_name)
        receipt(restaurant_name)


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
