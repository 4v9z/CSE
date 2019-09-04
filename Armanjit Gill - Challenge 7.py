import random
# Random number Generator w/ 2 digits


def random_num():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    return "%i" % a + "%i" % b


print(random_num())
