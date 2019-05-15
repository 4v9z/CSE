import csv


def average_it(c1, c2, c3, c4, c5, c6, c7, c8,
               c9, c10, c11, c12, p1, p2, p3, p4,
               p5, p6, p7, p8, p9, p10, p11, p12,
               ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8,
               ll9, ll10, ll11, ll12):
    t1 = p1 - c1
    t2 = p2 - c2
    t3 = p3 - c3
    t4 = p4 - c4
    t5 = p5 - c5
    t6 = p6 - c6
    t7 = p7 - c7
    t8 = p8 - c8
    t9 = p9 - c9
    t10 = p10 - c10
    t11 = p11 - c11
    t12 = p12 - c12
    t1 /= ll1
    t2 /= ll2
    t3 /= ll3
    t4 /= ll4
    t5 /= ll5
    t6 /= ll6
    t7 /= ll7
    t8 /= ll8
    t9 /= ll9
    t10 /= ll10
    t11 /= ll11
    t12 /= ll12
    the_costs = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]
    if max(the_costs) == t1:
        return t1
    elif max(the_costs) == t2:
        return t2
    elif max(the_costs) == t3:
        return t3
    elif max(the_costs) == t4:
        return t4
    elif max(the_costs) == t5:
        return t5
    elif max(the_costs) == t6:
        return t6
    elif max(the_costs) == t7:
        return t7
    elif max(the_costs) == t8:
        return t8
    elif max(the_costs) == t9:
        return t9
    elif max(the_costs) == t10:
        return t10
    elif max(the_costs) == t11:
        return t11
    else:
        return t12


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
    cosmetic_cost = 0
    fruit_cost = 0
    baby_cost = 0
    office_cost = 0
    personal_cost = 0
    beverage_cost = 0
    veggie_cost = 0
    house_cost = 0
    snack_cost = 0
    clothes_cost = 0
    meat_cost = 0
    cereal_cost = 0
    l1 = 0
    l2 = 0
    l3 = 0
    l4 = 0
    l5 = 0
    l6 = 0
    l7 = 0
    l8 = 0
    l9 = 0
    l10 = 0
    l11 = 0
    l12 = 0
    for row in reader:
        the_product = row[2]
        the_profit = row[13]
        the_cost = row[9]
        if the_product == "Fruits":
            fruit_profit += float(the_profit)
            try:
                fruit_cost += float(the_cost)
                l1 += 1
            except ValueError:
                fruit_cost = fruit_cost
        if the_product == "Cosmetics":
            cosmetic_profit += float(the_profit)
            try:
                cosmetic_cost += float(the_cost)
                l2 += 1
            except ValueError:
                cosmetic_cost = cosmetic_cost
        if the_product == "Baby Food":
            baby_profit += float(the_profit)
            try:
                baby_cost += float(the_cost)
                l3 += 1
            except ValueError:
                baby_cost += baby_cost
        if the_product == "Office Supplies":
            office_profit += float(the_profit)
            try:
                office_cost += float(the_cost)
                l4 += 1
            except ValueError:
                office_cost = office_cost
        if the_product == "Personal Care":
            personal_profit += float(the_profit)
            try:
                personal_cost += float(the_cost)
                l5 += 1
            except ValueError:
                personal_cost = personal_cost
        if the_product == "Beverages":
            beverage_profit += float(the_profit)
            try:
                beverage_cost += float(the_cost)
                l6 += 1
            except ValueError:
                beverage_cost = beverage_cost
        if the_product == "Vegetables":
            veggie_profit += float(the_profit)
            try:
                veggie_cost += float(the_cost)
                l7 += 1
            except ValueError:
                veggie_cost = veggie_cost
        if the_product == "Household":
            house_profit += float(the_profit)
            try:
                house_cost += float(the_cost)
                l8 += 1
            except ValueError:
                house_cost = house_cost
        if the_product == "Snacks":
            snack_profit += float(the_profit)
            try:
                snack_cost += float(the_cost)
                l9 += 1
            except ValueError:
                snack_cost = snack_cost
        if the_product == "Clothes":
            clothes_profit += float(the_profit)
            try:
                clothes_cost += float(the_cost)
                l10 += 1
            except ValueError:
                clothes_cost = clothes_cost
        if the_product == "Meat":
            meat_profit += float(the_profit)
            try:
                meat_cost += float(the_cost)
                l11 += 1
            except ValueError:
                meat_cost = meat_cost
        if the_product == "Cereal":
            cereal_profit += float(the_profit)
            try:
                cereal_cost += float(the_cost)
                l12 += 1
            except ValueError:
                cereal_cost = cereal_cost
        the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                       beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit,
                       snack_profit]
        region = row[0]
        the_profit2 = row[13]
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
        the_profits2 = [ssafrica_profit, mena_profit, ausoceania_profit, euro_profit, asia_profit,
                        centamercarrib_profit, namer_profit]
        the_cost_per_unit = average_it(fruit_cost, cosmetic_cost, meat_cost, cereal_cost, house_cost, baby_cost,
                                       clothes_cost, veggie_cost, beverage_cost, office_cost, personal_cost,
                                       snack_cost, fruit_profit, cosmetic_profit, meat_profit, cereal_profit,
                                       house_profit, baby_profit, clothes_profit, veggie_profit, beverage_profit,
                                       office_profit, personal_profit, snack_profit, l1, l2, l3, l4, l5,
                                       l6, l7, l8, l9, l10, l11, l12)
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

print(the_cost_per_unit)
