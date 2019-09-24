from termcolor import colored


def sandwich(a):
    sandwiching = True
    c = 0
    order = []
    while sandwiching:
        aa = input(colored("%s Computer: Good afternoon to you sir/madam, what Sandwich would"
                           " you like to order? (Write out the full menu item)"
                           "\n- Chicken Sandwich: $5.25"
                           "\n- Beef Sandwich: $6.25"
                           "\n- Tofu Sandwich: $5.75"
                           "\n - " % str(a), 'yellow', 'on_grey'))
        sanswiches = ["chicken sandwich", 'beef sandwich', 'tofu sandwich']
        if aa in sanswiches:
            if aa == "chicken sandwich":
                c += 5.25
            elif aa == "beef sandwich":
                c += 6.25
            elif aa == "tofu sandwich":
                c += 5.75
            order.append(aa)
            order.append(c)
        else:
            print("%s Computer: Sorry... that isn't on the menu you nerd!" % str(a))
        b = input("%s Computer: Would you like to order another sandwich?" % str(a))
        if b.lower() == "yes":
            print("%s Computer: Very well then..." % str(a))
        elif b.lower() == "no":
            print("Okay then... good day")
            return order
        else:
            print("%s Computer: I'll take that as a no... good day to you")
            return order


def drink(z):
    drinking = True
    co = 0
    order = []
    while drinking:
        aa = input(colored("%s Waiter: Alright and what size beverage would you like?"
                           "\n - Small: $1.00"
                           "\n - Medium: $1.75"
                           "\n - Large: $2.25"
                           "\n -" % str(z), 'green', 'on_grey'))
        sanswiches = ["chicken sandwich", 'beef sandwich', 'tofu sandwich']
        if aa in sanswiches:
            if aa == "chicken sandwich":
                co += 5.25
            elif aa == "beef sandwich":
                co += 6.25
            elif aa == "tofu sandwich":
                co += 5.75
            order.append(aa)
            order.append(co)
        else:
            print("%s Computer: Sorry... that isn't on the menu you nerd!" % str(z))
        b = input("%s Computer: Would you like to order another sandwich?" % str(z))
        if b.lower() == "yes":
            print("%s Computer: Very well then..." % str(z))
        elif b.lower() == "no":
            print("Okay then... good day")
            return order
        else:
            print("%s Computer: I'll take that as a no... good day to you")
            return order


def order_off_the_menu(restaurant_name):
        sandwich(restaurant_name)
        drink(restaurant_name)
        fries(restaurant_name)
        ketchup(restaurant_name)
        receipt(restaurant_name)


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
