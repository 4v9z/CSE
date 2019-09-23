from termcolor import colored


def sandwich(a):
    sandwiching = True
    while sandwiching:
        aa = input(colored("%s Computer: Good afternoon to you sir/madam, what Sandwich would"
                           " you like to order? (Write out the full menu item)"
                           "\n- Chicken Sandwich: $5.25"
                           "\n- Beef Sandwich: $6.25"
                           "\n- Tofu Sandwich: $5.75"
                           "\n - " % str(a), 'yellow', 'on_grey'))
        sanswiches = ["chicken sandwich", 'beef sandwich', 'tofu sandwich']
        if aa in sanswiches:
            if aa == "chicken sandwi"
        else:
            print("%s Computer: Sorry... that isn't on the menu you nerd!")


def order_off_the_menu(restaurant_name):
        sandwich(restaurant_name)
        drink(restaurant_name)
        fries(restaurant_name)
        ketchup(restaurant_name)
        receipt(restaurant_name)


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
