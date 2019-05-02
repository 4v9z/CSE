import csv


def validate(num: str):
    if check_if_valid(num):
        return True
    return False


def check_if_valid(num: str):
    if len(num) == 16:
        last_number = int(num[15])
        the_num_to_use = num[0:15]
        the_reversed_num = the_num_to_use[::-1]
        first_num = int(the_reversed_num[0])
        third_num = int(the_reversed_num[2])
        fifth_num = int(the_reversed_num[4])
        seventh_num = int(the_reversed_num[6])
        ninth_num = int(the_reversed_num[8])
        eleventh_num = int(the_reversed_num[10])
        thirteenth_num = int(the_reversed_num[12])
        fifteenth_num = int(the_reversed_num[14])
        nums_to_validate = [first_num, third_num, fifth_num, seventh_num, ninth_num,
                            eleventh_num, thirteenth_num, fifteenth_num]
        for i in range(len(nums_to_validate)):
            nums_to_validate[i] *= 2
        for i in range(len(nums_to_validate)):
            if nums_to_validate[i] >= 10:
                nums_to_validate[i] -= 9
        nums_to_validate.append(int(the_reversed_num[1]))
        nums_to_validate.append(int(the_reversed_num[3]))
        nums_to_validate.append(int(the_reversed_num[5]))
        nums_to_validate.append(int(the_reversed_num[7]))
        nums_to_validate.append(int(the_reversed_num[9]))
        nums_to_validate.append(int(the_reversed_num[11]))
        nums_to_validate.append(int(the_reversed_num[13]))
        the_sum = sum(nums_to_validate)
        if the_sum % 10 == last_number:
            return True
        return False
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("The Valid Credit Cards.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        input("PROCESSING...")
        input("WRITING FILE...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
    print("DONE")
