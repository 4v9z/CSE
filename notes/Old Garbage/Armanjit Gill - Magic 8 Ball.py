from colorama import Fore, Back, Style
import random


def _8_ball(lists, name):
    ballin = True
    qs = 0
    _list = lists
    while ballin:
        _8_ = input(Fore.MAGENTA + Style.BRIGHT + "Ask the 8 ball a question... any question: ")
        if _8_.lower() in ["quit", "exit", "leave", "altf4", "q", "im done", 'no']:
            print(Fore.LIGHTCYAN_EX + Style.DIM + "Alright then, until you come back... Hasta la bye bye!")
            print(Fore.GREEN + "You asked the Magic 8 ball %d questions this time %s" % (qs, name))
            return
        if "?" in _8_:
            qs += 1
            if _8_.lower() in ['is the sky blue?', 'is earth round?', 'is water a liquid?']:
                print(Fore.BLUE + Back.YELLOW + "Yes. I'm not an idiot %s..." % name)
            elif _8_.lower() in ["do vaccines cause autism?", 'is earth flat?']:
                print(Fore.RED + Back.BLACK + "You are everything wrong with the world %s if you t"
                      "hink that 'yes' is the right answer" % name)
            elif _8_.lower() == "is water wet?":
                print(Fore.WHITE + Back.BLACK + "I'm not allowed to say anything on that %s" % name)
            else:
                ll = random.choice(_list)
                ll += " "
                ll += name
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + ll)
        else:
            print("I require a question mark")


def instruct(name):
    insting = True
    while insting:
        inst = input(Fore.GREEN + "What would you like to learn about %s?"
                     "\n 1 - How to play 8 Ball"
                     "\n 2 - How to Add Your Own Responses"
                     "\n Enter the number of the instructions you want or type in "
                     "'quit' if you'd like to return to the menu" % name)
        if inst == '1':
            print(Fore.WHITE + Back.BLACK + "Instructions on how to play 8 Ball:"
                  "\n - Ask the 8 ball a question: Just type in whatever you want to ask"
                  "\n - Your question must end in a question mark and be a yes or no question as the 8 ball "
                  "only has positive or negative responses"
                  "\n - Type in 'quit', 'exit', 'leave', 'altf4', 'q', 'im done', or "
                  "'no' in order to quit out of the 8 ball Program when you're done. "
                  "(This can also be done to quit out from the menu)")
        elif inst == '2':
            print(Fore.LIGHTYELLOW_EX + "Instructions on how to add your own responses:")
            print("Every time you want to add a response, type in 'yes' when asked if you'd like to add a response"
                  "\n Then, you are to type in whatever response you would like to add"
                  "\n When you are done, type in 'no' the next time you're asked if you'd like to add a response")
        elif inst.lower() == "quit":
            print(Fore.GREEN + "Alright, hope you learned something %s!" % name)
            return


def respond(name):
    responding = True
    the_list = ["Answer unclear, try again", 'Most Definitely', "Perhaps",
                "Almost certainly a No", "I can't disclose information on that",
                "I don't like that question. Ask me another one", "Definitely Not",
                "Almost Certainly a Yes", "When pigs fly. "
                                          "Not saying if they need wing"
                                          "s or if they can be on an airplane", "Maybe", "Outlook not so Good"]
    while responding:
        ab = input(Fore.MAGENTA + "Would you like to add a response to the 8 Ball %s?" % name)
        if ab.lower() in ["yes", 'ye', 'yee', 'yeah', 'sure']:
            print(Fore.MAGENTA + Style.DIM + "You open the 8 ball and take out the many sided object inside with "
                                             "responses."
                                             "\n Magically, a new side gets added for each new response you add")
            a = input(Fore.WHITE + Back.BLACK + "Type in the response you'd like to add: ")
            the_list.append(a)
        elif ab.lower() in ['no', 'nah', 'heck no', 'not at all']:
            print(Fore.BLUE + "Okay, sending you back to the menu")
            return the_list


def menu():
    print(Fore.LIGHTBLACK_EX + "To navigate the menu, type in whatever you want to do when you are"
                               " asked to or type in its number"
          "\n If you would like to quit the game, type in quit.")
    ur_name = input(Fore.MAGENTA + Style.BRIGHT + "Hello there. Welcome to the Magic 8 Ball's domain! What is "
                                                  "your name?")
    print(Fore.MAGENTA + Style.BRIGHT + "Well then, hello %s! Nice to meet you!" % ur_name)
    menuu = True
    count = 0
    my_list = ["Answer unclear, try again", 'Most Definitely', "Perhaps",
               "Almost certainly a No", "I can't disclose information on that",
               "I don't like that question. Ask me another one", "Definitely Not",
               "Almost Certainly a Yes", "When pigs fly. "
                                         "Not saying if they need wing"
                                         "s or if they can be on an airplane for it "
                                         "to count", "Maybe", "Outlook not so Good"]
    while menuu:
        print(Fore.WHITE + Style.BRIGHT + Back.BLACK + "         Magic 8 Ball"
              "\n___________________________"
              "_____________________________"
              "_____________________________")
        print(Fore.WHITE + Style.BRIGHT + Back.BLACK + "1. Start")
        print(Fore.WHITE + Style.BRIGHT + Back.BLACK + "2. Instructions")
        print(Fore.WHITE + Style.BRIGHT + Back.BLACK + "3. Add your Own Responses")
        a = input(Fore.WHITE + Style.BRIGHT + Back.BLACK + "Type in what you would like to do %s: " % ur_name)
        if a.lower() == "start" or a == "1":
            count += 1
            _8_ball(my_list, ur_name)
        elif a.lower() == "instructions" or a == "2":
            instruct(ur_name)
        elif a.lower() == "add your own responses" or a == "3":
            my_list = respond(ur_name)
        elif a.lower() == "quit":
            print(Fore.MAGENTA + Back.BLACK + Style.DIM + "You consulted the Magic 8 Ball %d "
                                                          "times %s" % (count, ur_name))
            break


menu()
