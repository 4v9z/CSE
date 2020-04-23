import random
from termcolor import colored
import winsound
import sys

# FIX THE KEYS AND THE EQUIPPING SYSTEM!!
done_this = False
instructions = True


class Room(object):
    def __init__(self, name='ROOM', description='This is a room', north=None, south=None, east=None, west=None,
                 up=None, down=None, enter=None, leave=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enter = enter
        self.leave = leave
        self.up = up
        self.down = down
        self.items = []
        self.characters = []
        self.bosses = []
        self.enemies = []


class Item(object):
    def __init__(self, name):
        self.name = name


class Bag(object):
    def __init__(self):
        self.inventory = []
        self.max_space = 15

    def check(self):
        print()
        print("You have the following items: ")
        for num, item in enumerate(self.inventory):
            print(str(num + 1) + ": " + item.name)
        print()

class Character(object):
    def __init__(self, weapon, armor, health=20, name="", inked=False, mon=0):
        self.health = health
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.inked = inked
        self.money = mon
        self.can_attack = False



class Player(object):
    def __init__(self, starting_location, health=80):
        self.health = health
        self.inventory = []
        self.current_location = starting_location
        self.name = "you"
        self.choice = ""
        self.random = 0
        self.moves = 0
        self.rooms = 0
        self.roomz = 0
        self.du = False

    def move(self, new_location):
        """ This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.just_moved = True
        self.current_location = new_location
        self.rooms -= 1
        self.roomz -= 1

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


Inventory = Bag()


class Filler(object):
    def __init__(self, name="", price=0, text=''):
        self.name = name
        self.grabbed = False
        self.price = price
        self.flavor_text = text

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)

    def investigate(self):
        print(self.flavor_text)


class Filler2(object):
    def __init__(self, name="", text=''):
        self.name = name
        self.grabbed = False
        self.done_this = False
        self.flavor_text = text

    def investigate(self):
        print(self.flavor_text)

    def cheat(self):
        z = input("What will you write?")
        print("You scribble something that probably reads '%s' on the paper, "
              "put it back under the pillow, and give it a pat" % z)
        if z.upper() in ["SKIP", "GET ON WITH IT", 'I DONT CARE', 'REVEAL', 'END']:
            input("...")
            input(colored("The pillow flashes red", 'red'))
            input(colored("The pillow flashes green", 'green'))
            print(colored("C H E A T    C O D E     A C C E P T E D", 'magenta', 'on_grey'))
            if self.done_this:
                print("Hey.... you asked me this before! AND you decided that you didn't want the answer outright!"
                      "\nwelp... I'm NOT gonna run that code again >:(")
            else:
                input("...")
                input("A-are you sure?")
                command2 = input("")
                if command2.lower() == "yes":
                    input("But... I was excited to show everyone this... =(")
                    input("Are you REALLY sure?")
                    command3 = input("")
                    if command3.lower() == "yes":
                        input("...Alright")
                        print(
                            "The person I have has a tan and white dog, helps as a substitute teacher, and has recently gone to am Ariana Grande Concert")
                        input("In other words...")
                        print(colored("I have Marrkie", 'magenta'))
                        sys.exit()
                    elif command3.lower == "no":
                        print("Alright... back to the game! :)")
                    else:
                        print("... I don't know what ya wrote... but either way.... let's just keep playing? Okay")
                elif command2.lower == "no":
                    print("Alright... back to the game! :)")
                else:
                    print("... I don't know what ya wrote... but either way.... let's just keep playing? Okay")
                self.done_this = True



Table = Filler("A Table", 25, "You look under a table and there is a small tan and white dog underneath"
                              "\n Rudolph: 'Hello friend! How are you? What's your name'"
                              "\n zzzzzzzzzz"
                              "\nRudolph: ... Oh.... he's asleep... Best not to wake him up...")
Tickets = Filler("Pieces of Paper", 200, "Rudolph: 'Oh, these look like concert tickets. It says something, probably 'Ariana Grande'. Who's that though?'")
Pillow = Filler2("A Pillow with some Paper sticking out", "Rudolph: hmmmmmm.... this paper looks like it has something written on it. "
                                                          "I can't read, but it probably says something like 'enter in a cheat code here' on it")
Books = Filler("Pile of books", 0, "Rudolph: Hmmmm.... lots of books. Whoever this Arman guy has for Secret Santa must be smart! Like a teacher! Or at least a substitute teacher")

BEGIN = Room("Living Room", "You are standing in the living room. You were asked by Santa to help this loser named Arman with getting some clues together for a Secret Santa thing"
                            "\n Rudolph: What's so secret about Santa anyways?"
                            "\n Oh well, looks like I can go up, east, west, and north", 'KITCHEN', None, 'FRONTDOOR',
             'DININROOM', 'CHEATS')
CHEATS = Room("Cheats Room", "This room exists for the sole reason of if people don't want to play the game <(0u0<)", None, None, None, None, None, "BEGIN")
DININROOM = Room("Dining Room", "You're in the dining room. I got nothin for descriptions... It's in the name, it's in the game", None, None, "BEGIN")
KITCHEN = Room("The Kitchen", "It's the Kitchen! Smells like a dog."
                              "\n Rudolph: Why would a Kitchen smell like a dog? "
                              "None of that kid's family members even HAVE a kitchen that smells like a dog!", None, "BEGIN")
FRONTDOOR = Room("Front Door", "Rudolph: Can I leave??"
                               "\n Santa's calm voice fills the room"
                               "\n Santa: No. Stop"
                               "\n Rudolph: Ok", None, None, None, "BEGIN")
CHEATS.items.append(Pillow)
DININROOM.items.append(Books)
FRONTDOOR.items.append(Tickets)
KITCHEN.items.append(Table)


player = Player(BEGIN)

directions = ['north', 'south', 'east', 'west', 'up', 'down', 'enter', 'leave']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'in', 'out']


# Adding NPCs + Shopkeepers
playing = False
while instructions:
    print(colored("~~ Secret ", 'red') + colored("Santa ~~", 'green'))
    print('_________________________')
    print("TYPE IN 'START' TO START")
    print("TYPE I FOR INSTRUCTIONS")
    command3 = input("")
    if command3.upper() == "I":
        print("            HOW TO PLAY")
        print("_________________________________________")
        input("- You move by typing in north, south, east, west, up, down, enter, or exit."
              "\n- Alternatively, you can use shorthand: n, s, e, w, u, d, in, out")
        input("- Use the command investigate, pick up, grab, drop, take, and cheat to interact with objects")
        input("- At any point, press I to view your inventory"
              " or type in 'speak' to say something, go on!"
              "\n No one is listening!")
    elif command3.upper() == "START":
        instructions = False
        playing = True
        print("--> OKAY"
              "\n --> 3"
              "\n --> 2"
              "\n --> 1")
        print("OhYeahByTheWayYouPlayAsRudolphInThisForNoGoodReasonIJustThoughtIt'dBeCoolAndStuff")
    else:
        print("That is not a valid command")

# player.helmet = water_pendant
# Inventory.inventory.append(Skel_key)
# Skel_key.grabbed = True
# player.current_location = TEMPLE_1

marxs_death = False

while playing:
    print(colored(player.current_location.name, 'blue'))
    print(colored(player.current_location.description, 'green'))
    if len(player.current_location.items) > 0:
        print()
        print("The following items are in this room: ")
        for nums, items in enumerate(player.current_location.items):
            try:
                print(str(nums + 1) + ": " + colored(items.name, 'grey'))
            except AttributeError:
                print('                               ')
        print()
    if len(player.current_location.characters) > 0:
        print()
        input("The following characters are in this room: ")
        for nums, persons in enumerate(player.current_location.characters):
            print(str(nums + 1) + ": " + colored(persons.name, 'magenta'))
        print()
    if len(player.current_location.enemies) > 0:
        print()
        print("The following enemies are in this room: ")
        for nums, persons in enumerate(player.current_location.enemies):
            print(str(nums + 1) + ": " + colored(persons.name, 'red'))
        print()
    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit', 'altf4']:
        playing = False
    elif 'cheat' in command.lower():
        if player.current_location == CHEATS:
            Pillow.cheat()
    elif 'take ' in command.lower():
        item_name = command[5:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                if the_item.name == "A Table":
                    input("Rudolph:.....")
                    print("Rudolph:" + colored("You... uh... want me to take a WHOLE TABLE?!", "red"))
                    input("Rudolph: I'm just gonna take these doghairs underneath")
                    Inventory.inventory.append("Dog Hair")
                else:
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(item_obj)
    elif 'grab ' in command.lower():
        item_name = command[5:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                if the_item.name == "A Table":
                    input("Rudolph:.....")
                    print("Rudolph:" + colored("You... uh... want me to take a WHOLE TABLE?!", "red"))
                    input("Rudolph: I'm just gonna take these doghairs underneath")
                    Inventory.inventory.append("Dog Hair")
                else:
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(item_obj)
    elif 'pick up ' in command.lower():
        item_name = command[8:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                if the_item.name == "A Table":
                    input("Rudolph:.....")
                    print("Rudolph:" + colored("You... uh... want me to take a WHOLE TABLE?!", "red"))
                    input("Rudolph: I'm just gonna take these doghairs underneath")
                    Inventory.inventory.append("Dog Hair")
                else:
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(item_obj)
    elif 'investigate ' in command.lower():
        item_name = command[12:]
        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                item_obj = the_item
                item_obj.investigate()
    elif 'drop ' in command.lower():
        items_name = command[5:]

        the_item = None
        for stuff in Inventory.inventory:
            if stuff.name.lower() == items_name.lower():
                the_item = stuff

                try:
                    the_item.drop()
                    if the_item.__class__ is not Filler:
                        player.current_location.items.append(the_item)
                except AttributeError:
                    print("You can't drop this")

    elif command.lower() in ["check inventory", "open inventory", 'i']:
        Inventory.check()
    elif command.lower() == "":
        print()
    elif command.lower() in ["speak", "talk"]:
        command2 = input("What would you like to say?")
        print("Rudolph: " + command2)
    elif command.lower() == "scream":
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRGGGGGGGGGGGHHHHHHHHH'
              'HHHHHHHHHHHHHHHHHHHHHHHHH')
    elif command.lower() == "recognized":
        print("Command not reco- Oh... VERY funny! HA! HA! HA! What a comedian!"
              "\nIt's so funny I forgot to laugh!")
    elif command.lower() in directions:
        command = command.lower()
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't do this or go this way")

    else:
        print("Command not recognized, if you inputted a direction, write it again in all lowercase")
    if "Dog Hair" in Inventory.inventory and Tickets in Inventory.inventory and Books in Inventory.inventory:
        input("Rudolph: Hmmmm... based on this list from Santa, I can figure out who this kid has...")
        print("Rudolph: And Arman has Marrkie for Secret Santa!")
        input()
        print("Rudolph: Alright cool. I'm gonna go take my Union Break and drink some Reinbeer with Comet"
              "\n Santa: You're underage. Stop that or you're on the naughty list"
              "\nRudolph: Oh Come On! How could you know that I drink but NOT know that I was bullied for months?!"
              "\nSanta:...you win this time. You get 2 sips, then you don't drink til you're 21"
              "\nRudolph:..."
              "\n Rudolph: Deal, it tastes weird anyways")
        playing = False
    player.just_moved = False
    player.moves += 1
