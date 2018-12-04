#  Easy: Challenge 1


def challenge1(firstname, lastname):
    return "%s %s" % (lastname, firstname)


print(challenge1("John", "Doe"))

# Easy: Challenge 2


def challenge2(number):
    if number % 2 == 0:
        return "even"
    else:
        return"odd"


print(challenge2(10))
print(challenge2(11))

# Easy: Challenge 3


def challenge3(base, height):
    return(height * base) / 2


print(challenge3(2, 2))

# Easy: Challenge 4


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

# Medium: Challenge 5


def challenge5(radius):
    return radius**2 * 3.14159


print(challenge5(1.1))

# Medium: Challenge 6


def challenge6(radius):
    return 4/3*(radius**3) * 3.14159


print(challenge6(1.1))

# Medium: Challenge 7


def challenge7(your_number):
    return your_number + (your_number**2) + (your_number**3)


print(challenge7(2))


# Hard Challenge: Challenge 8


def challenge8(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return "Thanks for the vowel!"
    else:
        return "That's not a vowel! You goof! That's a consonant!"


print(challenge8("a"))
print(challenge8("e"))
print(challenge8("i"))
print(challenge8("o"))
print(challenge8("u"))
print(challenge8("z"))
