import csv


<<<<<<< HEAD
def average_it(c1, c2, c3, c4, c5, c6, c7, c8,
               c9, c10, c11, c12, p1, p2, p3, p4,
<<<<<<< HEAD
               p5, p6, p7, p8, p9, p10, p11, p12,
               l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12):
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
    t1 /= len(l1)
    t2 /= len(l2)
    t3 /= len(l3)
    t4 /= len(l4)
    t5 /= len(l5)
    t6 /= len(l6)
    t7 /= len(l7)
    t8 /= len(l8)
    t9 /= len(l9)
    t10 /= len(l10)
    t11 /= len(l11)
    t12 /= len(l12)
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
=======
               p5, p6, p7, p8, p9, p10, p11, p12):
    t1 = p1 - c1
>>>>>>> parent of 765d17b... SSSSSSSSSSSSSSSSSSSSS


=======
>>>>>>> parent of f8374cc... TG73 TG578U1HYG 876YH8
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
        if the_product == "Fruits":
            fruit_profit += float(the_profit)
            try:
                fruit_cost += float(the_cost)
                list1.append(the_cost)
            except ValueError:
                fruit_cost = fruit_cost
        if the_product == "Cosmetics":
            cosmetic_profit += float(the_profit)
            try:
                cosmetic_cost += float(the_cost)
                list2.append(the_cost)
            except ValueError:
                cosmetic_cost = cosmetic_cost
        if the_product == "Baby Food":
            baby_profit += float(the_profit)
            try:
                baby_cost += float(the_cost)
                list3.append(the_cost)
            except ValueError:
                baby_cost += baby_cost
        if the_product == "Office Supplies":
            office_profit += float(the_profit)
            try:
                office_cost += float(the_cost)
                list4.append(the_cost)
            except ValueError:
                office_cost = office_cost
        if the_product == "Personal Care":
            personal_profit += float(the_profit)
            try:
                personal_cost += float(the_cost)
                list5.append(the_cost)
            except ValueError:
                personal_cost = personal_cost
        if the_product == "Beverages":
            beverage_profit += float(the_profit)
            try:
                beverage_cost += float(the_cost)
                list6.append(the_cost)
            except ValueError:
                beverage_cost = beverage_cost
        if the_product == "Vegetables":
            veggie_profit += float(the_profit)
            try:
                veggie_cost += float(the_cost)
                list7.append(the_cost)
            except ValueError:
                veggie_cost = veggie_cost
        if the_product == "Household":
            house_profit += float(the_profit)
            try:
                house_cost += float(the_cost)
                list8.append(the_cost)
            except ValueError:
                house_cost = house_cost
        if the_product == "Snacks":
            snack_profit += float(the_profit)
            try:
                snack_cost += float(the_cost)
                list9.append(the_cost)
            except ValueError:
                snack_cost = snack_cost
        if the_product == "Clothes":
            clothes_profit += float(the_profit)
            try:
                clothes_cost += float(the_cost)
                list10.append(the_cost)
            except ValueError:
                clothes_cost = clothes_cost
        if the_product == "Meat":
            meat_profit += float(the_profit)
            try:
                meat_cost += float(the_cost)
                list11.append(the_cost)
            except ValueError:
                meat_cost = meat_cost
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
<<<<<<< HEAD
=======
            try:
                cereal_cost += float(the_cost)
                list12.append(the_cost)
            except ValueError:
                cereal_cost = cereal_cost
>>>>>>> parent of 765d17b... SSSSSSSSSSSSSSSSSSSSS
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
<<<<<<< HEAD
        the_profits2 = [ssafrica_profit, mena_profit, ausoceania_profit, euro_profit, asia_profit,
                        centamercarrib_profit, namer_profit]
<<<<<<< HEAD
        the_cost_per_unit = average_it(fruit_cost, cosmetic_cost, meat_cost, cereal_cost, house_cost, baby_cost,
                                       clothes_cost, veggie_cost, beverage_cost, office_cost, personal_cost,
                                       snack_cost, fruit_profit, cosmetic_profit, meat_profit, cereal_profit,
                                       house_profit, baby_profit, clothes_profit, veggie_profit, beverage_profit,
                                       office_profit, personal_profit, snack_profit, list1, list2, list3, list4, list5,
                                       list6, list7, list8, list9, list10, list11, list12)
=======
>>>>>>> parent of f8374cc... TG73 TG578U1HYG 876YH8
=======
>>>>>>> parent of 765d17b... SSSSSSSSSSSSSSSSSSSSS
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
<<<<<<< HEAD

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
<<<<<<< HEAD

print(the_cost_per_unit)
=======
>>>>>>> parent of f8374cc... TG73 TG578U1HYG 876YH8
=======
>>>>>>> parent of 765d17b... SSSSSSSSSSSSSSSSSSSSS
