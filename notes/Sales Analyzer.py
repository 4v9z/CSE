import csv


def cost_per_unit(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12):
    t1 = (sum(l1) / len(l1))
    t2 = (sum(l2) / len(l2))
    t3 = (sum(l3) / len(l3))
    t4 = (sum(l4) / len(l4))
    t5 = (sum(l5) / len(l5))
    t6 = (sum(l6) / len(l6))
    t7 = (sum(l7) / len(l7))
    t8 = (sum(l8) / len(l8))
    t9 = (sum(l9) / len(l9))
    t10 = (sum(l10) / len(l10))
    t11 = (sum(l11) / len(l11))
    t12 = (sum(l12) / len(l12))
    the_prices = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]
    return max(the_prices)


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
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    for row in reader:
        the_product = row[2]
        the_profit = row[13]
        the_cost = row[12]
        if the_product == "Fruits":
            fruit_profit += float(the_profit)
            list1.append(float(the_profit) - float(the_cost))
        if the_product == "Cosmetics":
            cosmetic_profit += float(the_profit)
            list2.append(float(the_profit) - float(the_cost))
        if the_product == "Baby Food":
            baby_profit += float(the_profit)
            list3.append(float(the_profit) - float(the_cost))
        if the_product == "Office Supplies":
            office_profit += float(the_profit)
            list4.append(float(the_profit) - float(the_cost))
        if the_product == "Personal Care":
            personal_profit += float(the_profit)
            list5.append(float(the_profit) - float(the_cost))
        if the_product == "Beverages":
            beverage_profit += float(the_profit)
            list6.append(float(the_profit) - float(the_cost))
        if the_product == "Vegetables":
            veggie_profit += float(the_profit)
            list7.append(float(the_profit) - float(the_cost))
        if the_product == "Household":
            house_profit += float(the_profit)
            list8.append(float(the_profit) - float(the_cost))
        if the_product == "Snacks":
            snack_profit += float(the_profit)
            list9.append(float(the_profit) - float(the_cost))
        if the_product == "Clothes":
            clothes_profit += float(the_profit)
            list10.append(float(the_profit) - float(the_cost))
        if the_product == "Meat":
            meat_profit += float(the_profit)
            list11.append(float(the_profit) - float(the_cost))
        if the_product == "Cereal":
            cereal_profit += float(the_profit)
            list12.append(float(the_profit) / float(the_cost))
        the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                       beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit]
        region = row[0]
        if region == "Sub-Saharan Africa":
            ssafrica_profit += float(the_profit)
        if region == "Middle East and North Africa":
            mena_profit += float(the_profit)
        if region == "Australia and Oceania":
            ausoceania_profit += float(the_profit)
        if region == "Europe":
            euro_profit += float(the_profit)
        if region == "Asia":
            asia_profit += float(the_profit)
        if region == "Central America and the Carribean":
            centamercarrib_profit += float(the_profit)
        if region == "North America":
            namer_profit += float(the_profit)
        the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                       beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit]
        the_profits2 = [ssafrica_profit, mena_profit, ausoceania_profit, euro_profit, asia_profit,
                        centamercarrib_profit, namer_profit]
the_lowest_cost_per_unit = cost_per_unit(list1, list2, list3, list4, list5, list6, list7, list8, list9,
                                         list10, list11, list12)
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

if max(the_profits2) == ssafrica_profit:
    print("The most profitable region is Sub-Saharan Africa with a total profit of %f" % ssafrica_profit)
elif max(the_profits2) == mena_profit:
    print("The most profitable region is the Middle East and North Africa with a total profit of %f" % mena_profit)
elif max(the_profits2) == ausoceania_profit:
    print("The most profitable region is Australia and Oceania with a total profit of %f" % ausoceania_profit)
elif max(the_profits2) == euro_profit:
    print("The most profitable region is Europe with a total profit of %f" % euro_profit)
elif max(the_profits2) == asia_profit:
    print("The most profitable region is Asia with a total profit of %f" % asia_profit)
elif max(the_profits2) == centamercarrib_profit:
    print("The most profitable region is Central America and the Caribbean with a total"
          " profit of %f" % centamercarrib_profit)
elif max(the_profits2) == namer_profit:
    print("The highest profit came from North America with a total profit of %f" % veggie_profit)
elif max(the_profits) == house_profit:
    print("The highest profit came from Households with a total profit of %f" % house_profit)
elif max(the_profits) == clothes_profit:
    print("The highest profit came from Clothes with a total profit of %f" % clothes_profit)
elif max(the_profits) == meat_profit:
    print("The highest profit came from Meat with a total profit of %f" % meat_profit)
elif max(the_profits) == cereal_profit:
    print("The highest profit came from Cereal with a total profit of %f" % cereal_profit)

print(the_lowest_cost_per_unit)
