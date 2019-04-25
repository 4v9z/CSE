import csv

# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         print(old_number)
#         new_number = int(old_number)

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("PROCESSING...")

        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num == 4:
                writer.writerow(row)
    print("DONE")
