from termcolor import colored


def order_off_the_menu(restaurant_name):
        sandwich = ""
        drink_size = ''
        fries = ''
        the_ketchup_is_coming = 0
        the_food = "YOU HAVE ORDERED "
        cost = 0
        #   The Following has been done to fix problems my code had as I added this later:
        drink_size += ''
        fries += ''
        sandwich += ''
        the_ketchup_is_coming += 0
        input(colored("%s Waiter: Ah, hello sir/madam, how are you? Today we are "
                      "running multiple specials. If you spend $15 or above,we will take "
                      "$5 off your price, If you only buy a sandwich, as part of our "
                      "'Let's get this bread' deal, you will have $1.25 "
                      "taken off your price, our last special is that "
                      "if you buy each of our least expensive items, ketchup not included,"
                      " then you'll get $2.50 taken off the price as part o"
                      "f our 'Budget Brunch' deal." % str(restaurant_name), 'magenta', 'on_grey'))
        sandwich = input(colored("%s Waiter: Good afternoon to you sir/madam, what Sandwich would"
                                 " you like to order? (Write out the full menu item)"
                                 "\n- Chicken Sandwich: $5.25"
                                 "\n- Beef Sandwich: $6.25"
                                 "\n- Tofu Sandwich: $5.75"
                                 "\n - " % str(restaurant_name), 'yellow', 'on_grey'))
        if sandwich.lower() == "chicken sandwich":
            the_food += "\n - A "
            the_food += sandwich.upper()
            the_food += ', '
            cost += 5.25
            drin = input(colored("%s Waiter: Excellent choice, now would you like a drink?" % str(restaurant_name),
                                 'green', 'on_grey'))
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
                the_food += '\n - A ' + drink_size.upper() + ' BEVERAGE, '
            elif drin.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
            frye = input(colored("%s Waiter: Would you like some fries with that?" % str(restaurant_name),
                                 'yellow', 'on_grey'))
            if frye.lower() == 'yes':
                fries = input(colored("%s Waiter: Alright then, what size fries would you like?"
                                      "\n- Small: $1.00"
                                      "\n- Medium: $1.50"
                                      "\n- Large: $2.00" % str(restaurant_name), 'yellow', 'on_grey'))
                if fries.lower() == 'small':
                    frys = input(colored("%s Waiter: Would you like to mega-size your "
                                         "fries?" % str(restaurant_name), 'yellow', 'on_grey'))
                    if frys.lower() == 'yes':
                        fries = 'large fries'
                        cost += 2.00
                    else:
                        input(colored("%s Waiter: Fine, have it your way..."
                                      " *under his breath* ₚₑₐₛₐₙₜ" % str(restaurant_name),
                                      'yellow', 'on_grey'))
                        cost += 1.00
                elif fries.lower() == 'medium':
                    cost += 1.50
                elif fries.lower() == 'large':
                    cost += 2.00
                the_food += "\n - " + fries.upper() + ' FRIES, '
            elif frye.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'yellow', 'on_grey'))
            kepchup = input(colored("%s Waiter: Would you like some Ketchup?" % str(restaurant_name), 'red', 'on_grey'))
            if kepchup.lower() == 'yes':
                the_ketchup_is_coming = int(input(colored("%s Waiter: How many Kepchup brand Ketchup packets "
                                                          "would you like? Each packet costs "
                                                          "25 cents" % str(restaurant_name), 'red', 'on_grey')))
                cost += the_ketchup_is_coming * 0.25
                the_food += "\n - " + str(the_ketchup_is_coming) + " KEPCHUP BRAND KETCHUP PACKETS"
            else:
                input(colored("%s Waiter: Okay then, that is all" % str(restaurant_name), 'magenta', 'on_grey'))
        elif sandwich.lower() == 'beef sandwich':
            the_food += '\n - A ' + sandwich.upper() + ', '
            cost += 6.25
            drin = input(colored("%s Waiter: Excellent choice, now would you like a "
                                 "drink?" % str(restaurant_name), 'green',
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
                the_food += '\n - A ' + drink_size.upper() + ' BEVERAGE, '
            elif drin.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
            frye = input(colored("%s Waiter: Would you like some fries with that?" % str(restaurant_name),
                                 'yellow', 'on_grey'))
            if frye.lower() == 'yes':
                fries = input(colored("%s Waiter: Alright then, what size fries would you like?"
                                      "\n- Small: $1.00"
                                      "\n- Medium: $1.50"
                                      "\n- Large: $2.00" % str(restaurant_name), 'yellow', 'on_grey'))
                if fries.lower() == 'small':
                    frys = input(colored("%s Waiter: Would you like to mega-size your "
                                         "fries?" % str(restaurant_name), 'yellow', 'on_grey'))
                    if frys.lower() == 'yes':

                        cost += 2.00
                    else:
                        input(colored("%s Waiter: Fine, have it your way..."
                                      " *under his breath* ₚₑₐₛₐₙₜ" % str(restaurant_name),
                                      'yellow', 'on_grey'))
                        cost += 1.00
                elif fries.lower() == 'medium':
                    cost += 1.50
                elif fries.lower() == 'large':
                    cost += 2.00
                the_food += "\n - " + fries.upper() + ' FRIES, '
            elif frye.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'yellow', 'on_grey'))
            kepchup = input(colored("%s Waiter: Would you like some Ketchup?" % str(restaurant_name), 'red', 'on_grey'))
            if kepchup.lower() == 'yes':
                the_ketchup_is_coming = int(input(colored("%s Waiter: How many Kepchup brand Ketchup packets "
                                                          "would you like? Each packet costs "
                                                          "25 cents" % str(restaurant_name), 'red', 'on_grey')))
                cost += the_ketchup_is_coming * 0.25
                the_food += "\n - " + str(the_ketchup_is_coming) + " KEPCHUP BRAND KETCHUP PACKETS"
            else:
                input(colored("%s Waiter: Okay then, that is all" % str(restaurant_name), 'magenta', 'on_grey'))
        elif sandwich.lower() == 'tofu sandwich':
            cost += 5.75
            the_food += '\n - A ' + sandwich.upper() + ', '
            drin = input(colored("%s Waiter: Excellent choice, now would you like a "
                                 "drink?" % str(restaurant_name), 'green',
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
                the_food += '\n - A ' + drink_size.upper() + ' BEVERAGE, '
            elif drin.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'green', 'on_grey'))
            frye = input(colored("%s Waiter: Would you like some fries with that?" % str(restaurant_name),
                                 'yellow', 'on_grey'))
            if frye.lower() == 'yes':
                fries = input(colored("%s Waiter: Alright then, what size fries would you like?"
                                      "\n- Small: $1.00"
                                      "\n- Medium: $1.50"
                                      "\n- Large: $2.00" % str(restaurant_name), 'yellow', 'on_grey'))
                if fries.lower() == 'small':
                    frys = input(colored("%s Waiter: Would you like to mega-size your "
                                         "fries?" % str(restaurant_name), 'yellow', 'on_grey'))
                    if frys.lower() == 'yes':

                        cost += 2.00
                    else:
                        input(colored("%s Waiter: Fine, have it your way..."
                                      " *under his breath* ₚₑₐₛₐₙₜ" % str(restaurant_name),
                                      'yellow', 'on_grey'))
                        cost += 1.00
                elif fries.lower() == 'medium':
                    cost += 1.50
                elif fries.lower() == 'large':
                    cost += 2.00
            elif frye.lower() == 'no':
                print(colored("%s Waiter: Ah, okay then" % str(restaurant_name), 'yellow', 'on_grey'))
            kepchup = input(colored("%s Waiter: Would you like some Ketchup?" % str(restaurant_name), 'red', 'on_grey'))
            if kepchup.lower() == 'yes':
                the_ketchup_is_coming = int(input(colored("%s Waiter: How many Kepchup brand Ketchup packets "
                                                          "would you like? Each packet costs "
                                                          "25 cents" % str(restaurant_name), 'red', 'on_grey')))
                cost += the_ketchup_is_coming * 0.25
                the_food += "\n -" + str(the_ketchup_is_coming) + " KEPCHUP BRAND KETCHUP PACKETS"
            else:
                input(colored("%s Waiter: Okay then, that is all" % str(restaurant_name), 'magenta', 'on_grey'))
        print(colored(the_food, 'white', 'on_grey'))
        cost += cost * 0.07
        if cost >= 15.00:
            cost -= 5.00
        if sandwich.lower() == "chicken sandwich" and drink_size.lower() == "small" and fries.lower() == "small":
            cost -= 2.50
        if sandwich != "" and drink_size == "" and fries == "" and the_ketchup_is_coming == 0:
            cost -= 1.25
        if fries != '' and sandwich != '' and drink_size != "":
            cost -= 1.00
        for i in range(len(str(cost)) - 1):
            if str(cost)[i-1] is '.':
                a = i
                if len(str(cost)[i:]) >= 3:
                    cost = round(cost, 2)
                else:
                    cost = str(cost) + "0"
        if str(cost) == "0.0":
            cost = "0.00"
        print("Your total comes out to $" + str(cost))


order_off_the_menu("Mr. Aziz's Spider-Man 2 Pizza Time Kitchen")
