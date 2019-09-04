import string
from termcolor import colored
punctuation = list(string.punctuation)


def check_it():
    palindrome1 = input("Input your palindrome here: ")
    list1 = []
    list3 = []
    letters_in_word = 0
    for i in range(len(palindrome1)):
        if palindrome1[i] in punctuation:
            list3.append(palindrome1[i])
        else:
            list1.append(palindrome1[i].lower())
    for ddd in range(len(list3)):
        if list3[ddd] in list1:
            pal = list1[:list3[ddd]]
    list2 = list(list1[::-1])
    list4 = []
    for e in range(len(list2)):
        if list2[e] in punctuation:
            list4.append(list2[e])
    for l in range(len(list4)):
        if list4[l] in list2:
            list2.remove(list3[l])
    print(list1)
    print(list2)
    for o in range(len(list1)):
        if list1[o] == list2[o]:
            letters_in_word += 1
    if len(list1) == letters_in_word:
        return "Your word is a palindrome"
    else:
        return "That is not a palindrome..." \
               "\n I asked for a palindrome..."


print(check_it())
