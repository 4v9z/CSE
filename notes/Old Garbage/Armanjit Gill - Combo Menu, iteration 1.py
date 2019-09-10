from termcolor import colored


def order_off_the_menu(restaurant_name):
    cost = 0
    sandwich = input(colored("%s Waiter: Good afternoon to you sir/madam, what Sandwich would"
                             " you like to order? (Write out the full menu item)"
                             "\n- Chicken Sandwich: $5.25"
                             "\n- Beef Sandwich: $6.25"
                             "\n- Tofu Sandwich: $5.75"
                             "\n - " % str(restaurant_name), 'yellow', 'on_grey'))
    print(sandwich)
    if sandwich.lower() == "chicken sandwich":
        cost += 5.25
    elif sandwich.lower() == 'beef sandwich':
        cost += 6.25
    elif sandwich.lower() == 'tofu sandwich':
        cost += 5.75


print(order_off_the_menu("Burger Time"))
