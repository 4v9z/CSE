def challenge1(firstname, lastname):
    return "%s %s" % (lastname, firstname)


print(challenge1("John", "Doe"))


def challenge2(number):
    if number % 2 == 0:
        return "even"
    else:
        return"odd"


print(challenge2(10))
print(challenge2(11))


def challenge3(base, height):
    return(height * base) / 2


print(challenge3(2, 2))


def challenge4(number):
    if number == 0:
        return"Your number is 0"
    elif number >= 1:
        return"Your number is positive!"
    else:
        return"Your number is negative"


print(challenge4(3))
print(challenge4(0))
print(challenge4(-3))


def challenge5(radius):
    return radius**2 * 3.14159


print(challenge5(1.1))


def challenge6(radius):
    return 4/3*(radius**3) * 3.14159


print(challenge6(1.1))