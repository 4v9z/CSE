import csv


def validate(num: str):
    if odd(num) and even(num):
        return True
    return False


def divisible_by_4(num: str):
    first_num = int(num[0])
    if first_num % 4 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def even(num: str):
    second_num = int(num[1])
    if second_num % 2 == 0:
        return True
    return False


def odd(num: str):
    first_num = int(num[0])
    if first_num % 2 != 0:
        return True
    return False

# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         print(old_number)
#         new_number = int(old_number)

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         input("PROCESSING...")
#         input("WRITING FILE...")
#
#         for row in reader:
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if len(old_number) != 16:
#                 writer.writerow(row)
#     print("DONE")


def reverse_it(string):
    return string[::-1]


print(reverse_it("dlroW olleH"))

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        input("PROCESSING...")
        input("WRITING FILE...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
    print("DONE")
