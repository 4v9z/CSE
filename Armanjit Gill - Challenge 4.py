# UK post code


def post_code():
    a = input("Enter the letter(s) that stand for your city/region")
    b = input("Enter the number(s) that stand for an area in that city/region")
    c = input("Enter the number(s) that stand for the street")
    d = input("Enter the letter(s) that stand for the street")
    return a + b + " " + c + d


print(post_code())
