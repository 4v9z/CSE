import random
# Random number Generator w/ 3 digits


def random_num():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    return "%i" % a + "%i" % b + "%i" % c


print(random_num())
