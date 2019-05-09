# # What does this do????
# # how do i dictionary?????
# Splatoon_Characters = {"Agent 8": "Fly Octo Fly. Also, you used a dictionary, Test Failed! "
#                                   "8 is romantically compatible with 3",
#           "Agent 3": "Calamari Inkantation, autobombs, specials, and lots of splattage, "
#                      "3 is romantically compatible with 8"}
#
# print(Splatoon_Characters["Agent 8"])
# print(Splatoon_Characters["Agent 3"])
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# mydictionary = {"Mario": "Let's a go!", "Luigi": "Okie Dokie!", "Sonic": "You're too slow!", "Kirby": "Poyo!~",
#                 "Link": "Hyaaaaaah!!!!", "Pikachu": "Pika!", "Mimikyu": "Kiki! Kiki!", "Inkling": "Woomy!"}
# input(mydictionary["Mario"])
# input(mydictionary["Luigi"])
# input(mydictionary["Sonic"])
# input(mydictionary["Kirby"])
# input(mydictionary["Link"])
# input(mydictionary["Pikachu"])
# input(mydictionary["Mimikyu"])
# input(mydictionary["Inkling"])
# print("SUPER! SMASH! BROTHERS!! ULTIMATE!")
import csv


with open("Sales Records.csv", 'r') as the_Sales:
    reader = csv.reader(the_Sales)
    print("PROCESSING THE DATA...")
    print("FINDING HIGHEST TOTAL PROFIT...")
    fruit_profit = 0
    cosmetic_profit = 0
    baby_profit = 0
    office_profit = 0
    personal_profit = 0
    beverage_profit = 0
    veggie_profit = 0
    house_profit = 0
    snack_profit = 0
    clothes_profit = 0
    meat_profit = 0
    cereal_profit = 0
    for row in reader:
        the_product = row[2]
        the_profit = row[13]
        if the_product == "Fruits":
            fruit_profit += float(the_profit)
        if the_product == "Cosmetics":
            cosmetic_profit += float(the_profit)
        if the_product == "Baby Food":
            baby_profit += float(the_profit)
        if the_product == "Office Supplies":
            office_profit += float(the_profit)
        if the_product == "Personal Care":
            personal_profit += float(the_profit)
        if the_product == "Beverages":
            beverage_profit += float(the_profit)
        if the_product == "Vegetables":
            veggie_profit += float(the_profit)
        if the_product == "Household":
            house_profit += float(the_profit)
        if the_product == "Snacks":
            snack_profit += float(the_profit)
        if the_product == "Clothes":
            clothes_profit += float(the_profit)
        if the_product == "Meat":
            meat_profit += float(the_profit)
        if the_product == "Cereal":
            cereal_profit += float(the_profit)
        the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                       beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit]
print("DONE")
if max(the_profits) == fruit_profit:
    print("The highest profit came from Fruits with a total profit of %f" % fruit_profit)
elif max(the_profits) == cosmetic_profit:
    print("The highest profit came from Cosmetics with a total profit of %f" % cosmetic_profit)
elif max(the_profits) == baby_profit:
    print("The highest profit came from Baby Food with a total profit of %f" % baby_profit)
elif max(the_profits) == office_profit:
    print("The highest profit came from Office Supplies with a total profit of %f" % office_profit)
elif max(the_profits) == personal_profit:
    print("The highest profit came from Personal Care with a total profit of %f" % personal_profit)
elif max(the_profits) == beverage_profit:
    print("The highest profit came from Beverages with a total profit of %f" % beverage_profit)
elif max(the_profits) == veggie_profit:
    print("The highest profit came from Vegetables with a total profit of %f" % veggie_profit)
elif max(the_profits) == house_profit:
    print("The highest profit came from Households with a total profit of %f" % house_profit)
elif max(the_profits) == clothes_profit:
    print("The highest profit came from Clothes with a total profit of %f" % clothes_profit)
elif max(the_profits) == meat_profit:
    print("The highest profit came from Meat with a total profit of %f" % meat_profit)
elif max(the_profits) == cereal_profit:
    print("The highest profit came from Cereal with a total profit of %f" % cereal_profit)
