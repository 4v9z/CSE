import csv


<<<<<<< HEAD
def highest_profit(aa, aaa):
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
=======
def average_money(the_product, the_profit):



with open("Sales Records.csv", 'r') as the_Sales:
=======
def average_money(the_product, the_profit):



with open("Sales Records.csv", 'r') as the_Sales:
>>>>>>> parent of facef8c... ok
    with open("The Best Product.csv", "w", newline='') as the_best_product_of_all:
        reader = csv.reader(the_Sales)
        writer = csv.writer(the_best_product_of_all)
        input("PROCESSING...")
        input("WRITING FILE...")
        for row in reader:
            the_product = row[2]
            priority = row[4]
            num_sold = row[8]
            the_profit = row[13]
    print("DONE")
<<<<<<< HEAD
>>>>>>> parent of facef8c... ok
=======
>>>>>>> parent of facef8c... ok
