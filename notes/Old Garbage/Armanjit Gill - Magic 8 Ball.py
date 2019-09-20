import colorama
import random


def _8_ball():
    ballin = True
    while ballin:
        _8_ = input("Ask the 8 ball a question... any question: ")
        _list = ["Answer unclear, try again", 'Most Definitely', "Perhaps",
                 "Almost certainly a No", "I can't disclose information on that",
                 "I don't like that question. Ask me another one", "Definitely Not",
                 "Almost Certainly a Yes", "When pigs fly. "
                                           "Not saying if they need wing"
                                           "s or if they can be on an airplane", "Maybe"]
        if _8_.lower() in ["quit", "exit", "leave", "altf4", "q", "im done", 'no']:
            print("Alright then, until you come back... Hasta la bye bye!")
            ballin = False
            menu()
        if "?" in _8_:
            if _8_.lower() in ['is the sky blue?', 'is earth round?', 'is water a liquid?']:
                print("Yes I'm not an idiot...")
            elif _8_.lower() in ["do vaccines cause autism?", 'is earth flat?']:
                print("You are everything wrong with the world")
            elif _8_.lower() == "is water wet?":
                print("I'm not allowed to say anything on that")
            else:
                print(random.choice(_list))
        else:
            print("I require a question mark")


def instruct():
    print("Instructions:"
          "\n - 8 Ball:"
          "\n - Ask the 8 ball a question. Just type in whatever you want")


def menu():
    menuu = True
    while menuu:
        print("         Magic 8 Ball"
              "\n___________________________"
              "_____________________________"
              "_____________________________")
        print("Start")
        print("Instructions")
        print("Add your Own Prompts")
        a = input("Type in what you would like to do: ")
        if a.lower() == "start":
            _8_ball()
        elif a.lower() == "instructions":
            instruct()


menu()
