import string
from termcolor import colored
punctuation = list(string.punctuation)


def check_it():
    palin = input("Input your palindrome here: ")
    pa = 0
    palindrome = ""
    for i in range(len(palin)):
        if palin[i] == ' ':
            pal = palin[pa:i]
            pa = len(pal) + 1
            print(pal)
            palindrome += pal
            print(palindrome)


print(check_it())
