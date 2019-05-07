import csv


def average_money(the_product, the_profit):



with open("Sales Records.csv", 'r') as the_Sales:
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
