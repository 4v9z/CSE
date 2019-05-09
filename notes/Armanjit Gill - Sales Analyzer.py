import csv


def highest_profit(aa, aaa):
<<<<<<< HEAD
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
    if aa == "Fruits":
        fruit_profit += float(aaa)
    elif aa == "Cosmetics":
        cosmetic_profit += float(aaa)
    elif aa == "Baby Food":
        baby_profit += float(aaa)
    elif aa == "Office Supplies":
        office_profit += float(aaa)
    elif aa == "Personal Care":
        personal_profit += float(aaa)
    elif aa == "Beverages":
        beverage_profit += float(aaa)
    elif aa == "Vegetables":
        veggie_profit += float(aaa)
    elif aa == "Household":
        house_profit += float(aaa)
    elif aa == "Snacks":
        snack_profit += float(aaa)
    elif aa == "Clothes":
        clothes_profit += float(aaa)
    elif aa == "Meat":
        meat_profit += float(aaa)
    elif aa == "Cereal":
        cereal_profit += float(aaa)
    the_profits = [fruit_profit, cosmetic_profit, baby_profit, office_profit, personal_profit,
                   beverage_profit, veggie_profit, house_profit, clothes_profit, meat_profit, cereal_profit]
    return max(the_profits)
=======
    product = aa
    profit = aaa
    item_catalog = {}
    if product not in item_catalog:
        item_catalog[product] = 0
    else:
        item_catalog[product] += float(profit)
    return item_catalog


def max_it_out():
    my_items = highest_profit(the_product, the_profit)
    the_best = max(my_items)
    return(the_best)
>>>>>>> parent of 9a7f041... z


with open("Sales Records.csv", 'r') as the_Sales:
    reader = csv.reader(the_Sales)
    print("PROCESSING THE DATA...")
    print("FINDING HIGHEST TOTAL PROFIT...")
    for row in reader:
        the_product = row[2]
        the_profit = row[13]
        the_best_of_all = highest_profit(the_product, the_profit)
print("DONE")
print(the_best_of_all)

