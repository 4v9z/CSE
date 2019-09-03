def math(a, b, c, d):
    a += b
    b += a
    a *= b
    b *= a
    c += d
    d += c
    c *= d
    d *= c
    return a + b + c + d


number1 = 20
number2 = 45

print(math(number1, number2, 420, 31))


def ace_the_test():
    hours = int(input("For how many hours would you like to study?"))
    if 1 <= hours <= 3:
        print("You study for %i hours, now you have a better chance of passing!" % hours)
    elif 6 > hours >= 4:
        print("You study for %i hours, that sure is a lot!" % hours)
    elif 24 > hours >= 6:
        print("You studied a lot. %i hours of studying... How do you have that much time?" % hours)
    elif 48 > hours >= 24:
        print("You studied for at least one day, you're fine, you will ace the test")
    elif hours >= 48:
        print("Okay, this is getting out of hand, I'm glad that you enjoy school, "
              "but you've been studying for at least two days and "
              "you haven't slept. Calm down buddy")
    elif hours == 0:
        print("Oh, okay, you're confident that you won't need to study eh? Nice")
    elif hours < 0:
        print("Okay you study for- wait wait excuse me, what? "
              "How do you study for a NEGATIVE amount of time?! What does that even mean?!")


ace_the_test()
