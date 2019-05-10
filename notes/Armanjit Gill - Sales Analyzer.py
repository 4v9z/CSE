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
    ssafrica_profit = 0
    mena_profit = 0
    ausoceania_profit = 0
    euro_profit = 0
    asia_profit = 0
    centamercarrib_profit = 0
    namer_profit = 0
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
        region = row[0]
        the_profit2 = row[13]
        # meat_profit = 0
        # cereal_profit = 0
        # ssafrica_profit = 0
        # mena_profit = 0
        # ausoceania_profit = 0
        # euro_profit = 0
        # asia_profit = 0
        # centamercarrib_profit = 0
        # namer_profit = 0
        if region == "Sub-Saharan Africa":
            ssafrica_profit += float(the_profit2)
        if region == "Middle East and North Africa":
            mena_profit += float(the_profit2)
        if region == "Australia and Oceania":
            ausoceania_profit += float(the_profit2)
        if region == "Europe":
            euro_profit += float(the_profit2)
        if region == "Asia":
            asia_profit += float(the_profit2)
        if region == "Central America and the Carribean":
            centamercarrib_profit += float(the_profit2)
        if region == "North America":
            namer_profit += float(the_profit2)
        the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                       beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit]
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
