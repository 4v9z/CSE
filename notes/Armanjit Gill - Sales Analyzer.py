import csv


def highest_profit(aa, aaa):
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
    return the_best


with open("Sales Records.csv", 'r') as the_Sales:
    reader = csv.reader(the_Sales)
    print("PROCESSING THE DATA...")
    print("FINDING HIGHEST TOTAL PROFIT...")
    for row in reader:
        the_product = row[2]
        the_profit = row[13]
        highest_profit(the_product, the_profit)
print("DONE")
max_it_out()
