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
        drin = input(colored("%s Waiter: Excellent choice, now would you like a drink?" % str(restaurant_name), 'green', 'on_grey'))
        if drin.lower() == 'yes':
            drink_size = input(colored("%s Waiter: Alright and what size beverage would you like?"
                                       "\n - Small: $1.00"
                                       "\n - Medium: $1.75"
                                       "\n - Large: $2.25"
                                       "\n -" % str(restaurant_name), 'green', 'on_grey'))
            if drink_size.lower() == 'small':
                cost += 1.00
            elif drink_size.lower() == 'medium':
                cost += 1.75
            elif drink_size.lower() == 'large':
                cost += 2.25
        elif drin.lower() == 'no':
            print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
    elif sandwich.lower() == 'beef sandwich':
        cost += 6.25
        drin = input(colored("%s Waiter: Excellent choice, now would you like a drink?" % str(restaurant_name), 'green',
                             'on_grey'))
        if drin.lower() == 'yes':
            drink_size = input(colored("%s Waiter: Alright and what size beverage would you like?"
                                       "\n - Small: $1.00"
                                       "\n - Medium: $1.75"
                                       "\n - Large: $2.25"
                                       "\n -" % str(restaurant_name), 'green', 'on_grey'))
            if drink_size.lower() == 'small':
                cost += 1.00
            elif drink_size.lower() == 'medium':
                cost += 1.75
            elif drink_size.lower() == 'large':
                cost += 2.25
        elif drin.lower() == 'no':
            print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
    elif sandwich.lower() == 'tofu sandwich':
        cost += 5.75
        drin = input(colored("%s Waiter: Excellent choice, now would you like a drink?" % str(restaurant_name), 'green',
                             'on_grey'))
        if drin.lower() == 'yes':
            drink_size = input(colored("%s Waiter: Alright and what size beverage would you like?"
                                       "\n - Small: $1.00"
                                       "\n - Medium: $1.75"
                                       "\n - Large: $2.25"
                                       "\n -" % str(restaurant_name), 'green', 'on_grey'))
            if drink_size.lower() == 'small':
                cost += 1.00
            elif drink_size.lower() == 'medium':
                cost += 1.75
            elif drink_size.lower() == 'large':
                cost += 2.25
        elif drin.lower() == 'no':
            print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
    if len(str(cost)) == 4:
        print(cost)
    else:
        print(str(cost) + '0')


print(order_off_the_menu("Burger Time"))
