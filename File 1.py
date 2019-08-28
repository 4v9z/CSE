print("Hello Again World!")

o = 10

type(o)


def function_title():
    local_a = 7
    local_b = 2
    c = local_a + local_b
    print(c)


function_title()


def function_two(a, b):
    c = a*b
    print(c)


function_two(7, 6)


def function_three(a, b):
    c = a/b
    print(c)



Thing1 = 3
Thing2 = 2
function_three(3, 2)


def function_four(a, b):
    c = a - b
    return c
    # Anything underneath return will not be displayed/done


function_four(3, 2)


def in_Swamp(people):  # This creates a function that will check how many  people are in the swamp
    if people > 1:
        return "Shrek: What are you doing my swamp?!"
    else:
        return "Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed She was looking kind of dumb with her finger and her thumb In the shape of an ‘L’ on her forehead"


print(in_Swamp(55))
