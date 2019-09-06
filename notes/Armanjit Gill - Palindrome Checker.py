import string
from termcolor import colored
punctuation = list(string.punctuation)


def check_it():
    finding = True
    a = 0
    b = 0
    while finding:
        palin = input(colored("Input your palindrome here: ", 'magenta'))
        pa = 0
        palindrome = ""
        for i in range(len(palin)):
            if palin[i] in punctuation:
                pal = palin[pa:i]
                pa = i + 1
                palindrome += pal.lower()
        palindrome += palin[pa:].lower()
        palindrome2 = palindrome[::-1].lower()
        if palindrome == palindrome2:
            print(colored("Alright, that phrase is a palindrome", 'green'))
            a += 1
        else:
            print(colored("That is not a palindrome...", 'red'))
            b += 1
        try_again = input("Would you like to check another palindrome?")
        if try_again.lower() == 'yes':
            print(colored("Okay, let's do another one", 'blue'))
        else:
            finding = False
            return colored("Alright, hope you had fun"
                           "\n You found {} palindromes and you entered {} phrases, "
                           "meaning you had {} phrases that weren't palindromes".format(a, a + b, b), 'blue')


print(check_it())
