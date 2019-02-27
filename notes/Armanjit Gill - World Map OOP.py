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


class Player(object):
    def __init__(self, starting_location, helmet=None, chestplate='Leather Shirt', boots='Leather Boots',
                 weapon="Wooden Sword"):
        self.health = 50
        self.inventory = []
        self.current_location = starting_location
        self.helmet = helmet
        self.chestplate = chestplate
        self.boots = boots
        self.defense = 5
        self.MP = 15
        self.weapon = weapon

    def move(self, new_location):
        """ This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


class NPC(object):
    def __init__(self, dialogue="SAMPLE TEXT", name="NAMEHERE", money=300, gives_item=False, robbable=True):
        self.dialogue = dialogue
        self.robbable = robbable
        self.money = money
        self.name = name
        self.gives_item = gives_item


Kirby = NPC('HI!', 'Kirby', 25)
Dog = NPC('Woof', "Dog", 9999999999999999999999999999999, True)
EGG = NPC('EGG', 'EGG', 0, True)


# Option 2 - Use strings, but more difficult controller

TEMPLE_1 = Room('Lock Room', "You are in a room with a locked door leading east. "
                "\n You can continue through the temple to the north", 'TEMPLE_2', 'TEMPLE', 'WATER_MP')
TEMPLE_2 = Room('Empty Chamber', "There is a locked door to the east and a door leading north. "
                                 "\n You feel like something in the water is watching you, "
                                 "when you're suddenly attacked", 'TEMPLE_3', 'TEMPLE_1', 'D_LINK')
TRAP = Room('Trap', "As you walk to the west, the floor beneath you crumbles, "
                    "dropping you into a large pool of piranha-infested waters"
                    "\n You struggle to survive but you realize it's futile, you are not going to survive")
TEMPLE_3 = Room('Boss Room', "In front of you is a large door that has a fittingly over-sized lock."
                             "\n You look to the east and west, either direction can hold the key", 'CHAOS_FIGHT',
                'TEMPLE_2', 'TRAP', 'TEMPLE_4')
CHAOS_FIGHT = Room('Chaos Battle', "You are face to face with Chaos 0! The strange watery creature looks angry. "
                                   "Since normal weapons phase through it, ice or electricity "
                                   "would likely be most effective to "
                                   "attack it", None, 'TEMPLE_3', None, None, 'BAY')
TEMPLE_4 = Room('Gold Room', "You are in a room that is entirely made of gold, a sign says:"
                             "\n DO NOT BE GREEDY, TAKE NO MORE THAN 150 GOLD!"
                             "\n It's up to you whether or not you should heed this warning"
                             " You can head north to continue through the temple", 'TEMPLE_5', None, None, 'TEMPLE_3')
TEMPLE_5 = Room('Skeleton Room', "You are in a room full of bones. "
                                 "\n On top of a particularly large pile of bones is a skeleton key that will unlock"
                                 " any room in the temple"
                                 "\n climbing up the pile might be risky but it's the only way to "
                                 "fight the temple's boss", None, 'TEMPLE_4', None, None, 'KEY')
KEY = Room('Top of Pile', "You've made it to the top of the pile, the key is yours for the taking."
                          "\n Dropping down the pile will not be as risky as climbing the pile", None, None, None,
           None, None, 'TEMPLE_5')
D_LINK = Room('Reflecting Pond', "You find yourself in a room where the floor is covered in a thin layer of of water. "
                                 "In the middle of the room there is a small mound of dirt with a "
                                 "large black tree growing out of it."
                                 "\n As you walk through the room, you look down and see your reflection is gone. "
                                 "You turn around and see Dark Link!"
                                 "\n The evil version of the fabled hero won't be pulling any punches, "
                                 "but you clutch your weapon and ready yourself for a fight.", None, None, None,
              'TEMPLE_2')
WATER_MP = Room('Magic Room', "You look around the room. There are strange characters etched into the walls."
                              "\n You feel your MP get restored as well as increase", None, None, None, 'TEMPLE_1')
DESERT_FIGHT = Room('Empty Expanse', 'You look around the large vast desert. It feels like something is here... '
                                     'watching you...'
                                     '\n '
                                     'As you think this, you get attacked!', "OASIS", 'CASTLE_BACK', 'TOWER', 'TOWN')
CASTLE_BACK = Room('Desert Castle (Back)', "You are behind a large castle, there is a door in front of you "
                                           "that you can enter.", 'DESERT_FIGHT', 'CASTLE', None, None, None,
                   None, "CASTLE_7")
CASTLE = Room('Desert Castle', 'There is a large stone castle in front of you, it towers over you ominously. '
                               'There is a large door in front of you',
              'BACK_CASTLE', 'ROAD', None, 'MARKET', None, None, 'CASTLE_1')
CASTLE_1 = Room("Castle Entrance", "You have just entered the castle, looking ahead, "
                                   "there is a room full of rotating saw blades.", 'CASTLE_2', None, None, None, None,
                None, None, 'CASTLE')
CASTLE_2 = Room('Saw Room', "You are in a room in which saws are rotating on a set path, "
                            "you can sprint North to make it through here."
                            "\n However, this is risky, and it can lead to your demise", 'CASTLE_3', 'CASTLE_1')
CASTLE_3 = Room('Lava Room', "You are walking on a narrow platform, looking down, there's a pit of lava."
                             "\n !!!"
                             "\n The lava is now rising! Climbing up is your only option!", None, 'CASTLE_2', None,
                None, 'CASTLE_4')
CASTLE_4 = Room('Empty Room?', "You feel uneasy, like you're being watched. There is a door leading east, "
                               "but you feel like you're about to be ambushed", None, None, 'CASTLE_5', None,
                None, 'CASTLE_3')
CASTLE_5 = Room('Boss Room', "You are at the end of the castle, you can head north through the "
                             "large doors or east towards the back exit", "BOWSER", None, 'CASTLE_6')
CASTLE_6 = Room('Near Back Exit', "You are near the back exit of a castle, "
                                  "but to get there you'd have to hop across rocks floating in a river of lava"
                                  "\n To the west is the room before the boss in this castle", 'CASTLE_7',
                None, None, 'CASTLE_5')
CASTLE_7 = Room('Back Exit', "You are at the back exit of the castle. To go further through the castle, "
                             "you'd have to hop across rocks floating in a river of lava, or you can leave now",
                None, 'CASTLE_6', None, None, None, None, None, 'CASTLE_BACK')
BOWSER = Room('Bowser Battle', "After walking through the door you find yourself face to face "
                               "with the King of Koopas, Bowser!"
                               "\n Ready? FIGHT!", None, 'CASTLE_5')
ROAD = Room('Rainbow Road', "You are standing in front of a rainbow that appears to continue through "
                            "the atmosphere and into space"
                            "\n"
                            "You can walk up the rainbow", 'CASTLE', None, None, None, 'DARK_STAR')
DARK_STAR = Room('Galaxy Reactor', "There is a dark orb floating in the center of a large "
                                   "platform. You take a step forward."
                                   "\n Suddenly... the orb transforms into: DARK BOWSER!", None, None,
                 None, None, None, 'ROAD')
TEMPLE2 = Room('Temple of Time (Entrance)', "You look in front of you to see an temple with open doors, "
                                            "there is also a "
                                            "staircase leading down, and to the South is another strange temple",
               None, 'LIGHT', 'MARKET', None, None, 'TOT_SHOP', 'TOT1')
TOT1 = Room('Temple of Time', "You have entered the temple, you can continue through a door to the north", 'TOT2',
            None, None, None, None, None, None, 'TEMPLE2')
TOT2 = Room('Watch Room', "In the center of the room there is a magic pocket watch. You sigh as you realize "
                          "some time-travel shenanigans will ensue"
                          "\n You can use the watch to open up paths to the east or west that existed in "
                          "the past or future", 'TOT3', 'TOT1', 'PAST1', 'FUTURE1')
TOT3 = Room('Boss Room', "There is a large door in front of you with a large padlock on it, "
                         "it appears that a keys is needed. "
                         "\n You can use the watch to open up pathways to the east and west in the past and future.",
            'GHOMA', 'TOT2', 'FUTURE2', 'PAST2')
GHOMA = Room('Ghoma Fight', "In this room is the disgusting abomination of a spider: Ghoma"
                            "\n The strategy for this is to hit it with magic, as numerous "
                            "defeats has led to this boss gaining a resistance to swords and other similar weapons",
             'PORTAL', 'TOT3')
PORTAL = Room('Time Portal', "In front of you is a portal that leads into a future ~12,000 years after the "
                             "extinction of humans. "
                             "\n You can go south to reenter the temple or you can enter the portal", None, 'GHOMA',
              None, None, None, None, 'SPLAT1')
SPLAT1 = Room('Octo Valley', "You are on a strange floating platform, you "
                             "can enter the time portal from here or head north to continue", 'SPLAT2', None, None,
              None, None, None, 'PORTAL')
SPLAT2 = Room('Moray Towers', "You are climbing a tower currently, you can go back south, head"
                              " north, or go east or west"
                              "\n Going East requires some way to swim through ink", 'SPLAT3', 'SPLAT1',
              'SPLAT4', 'SPLAT5')
SPLAT3 = Room('Urchin Underpass', 'You are in an are filled with conveyor belts and is surrounded by water.'
                                  '\n You can go north or east, but you will require some way to swim through ink',
              'SPLAT6', 'SPLAT2', 'SPLAT7')
SPLAT6 = Room('Arowana Mall', )
SPLAT4 = Room('Octo Canyon', "After swimming through the ink, you have reached a large canyon. "
                             "\n Looking down in the canyon you can see something that looks like"
                             " a cross between a squid and a kid...", None, None, None, 'SPLAT2', None, '_3')
_3 = Room('Agent 3 Battle', "Upon getting closer, the squid-kid sees you. She turns around and she looks ready to fight"
                            "\n this 'Inkling' is known as Agent 3, and she will be one of your most "
                            "difficult battles yet."
                            "\n You can only defeat her with a weapon that fires ink, and either way... Good Luck!",
          None, None, None, None, 'SPLAT4')
SPLAT5 = Room('Bluefin Depot', "You are on a platform floating in the water, there is a large crate "
                               "here that can be opened", None, None, 'SPLAT2')
PAST2 = Room('Coin Room (Past)', "Upon a pedestal in this room is a single coin from the past."
                                 "\n This coin is worthless today: It's worth nothing in the present",
             None, None, 'TOT3')
FUTURE2 = Room('Key Room (Future)', "While the path leading here has caved "
                                    "in during our present day, and this "
                                    "path had not yet been built in the past you can visit, "
                                    "\n the key in this "
                                    "room appears to be broken. In our present day, "
                                    "this key was most definitely intact",
               None, None, None, 'TOT3')
FUTURE1 = Room('Gold Room (Future)', "In this room, there is a single coin upon a pedestal."
                                     "\n Because this is the future, this single "
                                     "coin is worth about 1,537 coins in the present", None, None, 'TOT2')
PAST1 = Room('Empty Citadel (Past)', "You enter this room in the past."
                                     "\n You feel this room has nothing to see, when suddenly you're attacked!",
             None, None, None, 'TOT2')
LIGHT = Room('Light Temple', "You've (ironically) entered a very dark place. "
                             "There are stairs leading up.", TEMPLE2, None, None, None, 'U_NECROZMA')
U_NECROZMA = Room('Megalo Tower', "You see a golden dragon towering over you. "
                                  "\n Ultra Necrozma: Lie..."
                                  " Lieeee.... LIGHT!!!!!!       "
                                  "\n                 Time to see who will prevail in battle", None, None, None, None,
                  None, 'LIGHT')
TOT_SHOP = Room('Temple Shop', 'ROBOT: BEEP BOOP, What do you want to buy? ZZZZZT! '
                               '\n '
                               'We have a thunder sword, increased health and MP, Directions through the '
                               'Lost Woods, and Armor', None, None, None, None, 'TEMPLE2')
TOWER = Room('Sheikah Tower', "You look up at the tower in front of you. you can climb it,"
                              " and it looks like there'll be a reward at the top for you", None, None, None,
             'DESERT_FIGHT', 'TOP_TOWER')
TOP_TOWER = Room('Shiekah Tower (Top)', 'You look in front of you and see two pedestals, one has an axe'
                                        ' on it, one has a shield.'
                                        '\n '
                                        'There appears to be a sign in between them that says "ONLY TAKE ONE".'
                                        ' Will you listen to it?', None, None, None, None, None, 'TOWER')
VOLCANO = Room('Volcano', "You are in front of a volcano... do you want to jump in?", None, None, None,
               None, None, None, 'INTERIOR')
INTERIOR = Room('Inside Volcano', "HOLY HECK, YOU'RE ALIVE!!"
                                  "\n .... Anyways, there is a fragment of a key here", None, None, None, None, VOLCANO)
MT_SILVER = Room('Mt. Silver', "You are on top of the mountain. Hail is plummeting down and the wind is howling. "
                               "There is someone at the edge of the cliff you're standing on"
                               "\n Red:..............!!!", None, None, None, None, None, 'MTN_BASE')
MTN_BASE = Room('Mt. Silver Base', "You are at the base of a snowy mountain. You can likely climb it, but the rocks "
                                   "are slightly slippery, so you might slip and fall", 'VOLCANO', None, None, None,
                'MT_SILVER', 'MTN_PASS')
CAVE = Room('Frozen Cave', "You are in a cold cave. The ground and walls are frozen and "
                           "there are icicles hanging from the ceiling"
                           "\n In the center of the cave is an icy sword encased in an impenetrable layer of ice. "
                           "It seems like this ice wasn't here before... If only you could rewind time...",
            None, None, 'MTN_PASS')
MTN_PASS = Room('Mountain Pass', "There is a frozen path leading west, a shop to the east, "
                                 "and towering above you, a mountain",
                None, None, 'MTN_SHOP', "CAVE", 'MTN_BASE')
MTN_SHOP = Room('Mountain Shop', "There is engraving on stone: BUY SOMETHING AND LEAVE THE MONEY OR ELSE..."
                                 "\n There is a keycard, armor, health upgrades, and a space helmet",
                None, None, 'CLIMB', 'MTN_PASS')
CLIMB = Room('Dangerous Climb', "You feel like this place isn't safe, when suddenly, you're attacked!", None, None,
             None, 'MTN_SHOP', 'PEAK', 'BAY')
PEAK = Room('Mountain Peak', "You are at the top of a mountain, you can see into space from here."
                             "\n There is floating wreckage here, if only you could see what this "
                             "place looked like in the past"
                             "\n You feel like you can walk west, there is no platform there,"
                             " but your instincts tell you to do it.", None, None, None, 'SUBSPACE_ENTER', None,
            'CLIMB', 'NOVA_1')
SUBSPACE_ENTER = Room('Edge of the Universe', "You stand in front of a dark void... unsure"
                                              " of what will become of you once you enter, there is only one thing you "
                                              "know for sure..."
                                              "\n Your adventure is nearing its end", None, None, 'PEAK', None, None,
                      'INTERIOR', 'SUBSPACE_1')
BAY = Room('Great Bay', 'There is an open ocean around you, you can see a strange structure under the water',
           None, None, None, 'RIVER', None, 'TEMPLE')
TEMPLE = Room('Water Temple', 'You are in the first room of the Water Temple. '
                              '\n You can swim back up or head north to the second room', 'TEMPLE_1', None, None, None,
              "BAY")
BEGIN = Room("An Adventure's Beginning", "You stand atop a hill looking ahead at the forest to "
                                         "the north and turn around to see the desert to the south. "
                                         "\n You're ready for your quest.", 'FOREST', 'TOWN', 'OASIS',
             'FACTORY', 'CHEATS', 'LOSS')
MARKET = Room('Desert Market', "You browse the fine selection of goods, you see potions that increase health and MP,"
                               "\n a strange pendant with a drop of water engraved on it, a scimitar, strange scuba "
                               "gear, and an odd key "
                               "\n You also see a battered rubber door mat saying 'WELCOME TO ZORK', but it "
                               "seems to be worthless. "
                               "\n You can buy or sell something here.", 'TOWN', 'DESERT_FIGHT', 'CASTLE', 'TEMPLE2')
TOWN = Room('Desert Town', "You are in a barren town, there isn't much to see here, save for some bags of gold..."
                           "\n But you wouldn't steal from innocent people... would you?",
            'BEGIN', 'MARKET', 'DESERT_FIGHT')
CHEATS = Room()
OASIS = Room("Desert Oasis", "You're in the middle of a desert next to the only water here. "
                             "\n There is a waterway barely big enough for you in the water.",
             'RIVER', 'DESERT_FIGHT', None, 'BEGIN', None, 'TOWN')
LOSS = Room('|     |i   ||  |__', '|     |i   ||  |__')
FACTORY = Room('Factory', "You are looking at a strange factory, will you enter it?", None, None, 'BEGIN', None,
               'M_MARIO')
M_MARIO = Room('Inside the Factory', "You are in a fight with Metal Mario, a Robotic "
                                     "copy of the beloved plumber! Let's see if you can win!",
               None, None, None, None, None, None, None, 'FACTORY')
FOREST = Room("Lost Woods", 'You are in a forest that feels mysterious, if you make a wrong move,'
                            ' you will be sent back to the first room of the forest.', 'FOREST2', 'BEGIN',
              'FOREST', 'FOREST')
FOREST2 = Room("Lost Woods", 'You are in a forest that feels mysterious, if you make a wrong move, '
                             ' you will be sent back to the first room of the forest.', 'FOREST3', 'FOREST',
               'FOREST', 'FOREST')
FOREST3 = Room("Lost Woods", 'You are in a forest that feels mysterious, if you make a wrong move, '
                             ' you will be sent back to the first room of the forest.', 'FOREST', 'FOREST4', 'FOREST',
               'FOREST')
FOREST4 = Room('Lost Woods', 'You are in a forest that feels mysterious, if you make a wrong move, it will send you '
                             'back to the first room of the forest.', 'FOREST', 'FOREST5', 'FOREST', 'FOREST')
FOREST5 = Room('Lost Woods', 'You are in a forest that feels mysterious, if you make a wrong move, it will send you '
                             'back to the first room of the forest.', 'FOREST', 'FOREST', 'FOREST', 'FOREST6')
FOREST6 = Room('Lost Woods', 'You are in a forest that feels mysterious, if you make a wrong move, it will send you '
                             'back to the first room of the forest.', 'FOREST', 'FOREST', 'FOREST7', 'FOREST')
FOREST7 = Room('Lost Woods', 'You are in a forest that feels mysterious, if you make a wrong move, it will send you '
                             'back to the first room of the forest.', 'FOREST', 'FOREST', 'FOREST', 'FOREST8')
FOREST8 = Room('Lost Woods', 'You are in a forest that feels mysterious, if you make a wrong move, it will send you '
                             'back to the first room of the forest.', 'FOREST', 'FOREST', 'CLEARING', "FOREST")
CLEARING = Room('Clearing', "You've made it to a clearing, you can move East, West, or North."
                            "\n "
                            "There is also a strange sword embedded in the ground, however, "
                            "it's dark and seems to have lost all of it's power", "MTN_PASS",
                "FOREST", "JEVIL_ENTRANCE", "RIVER")
RIVER = Room('River Path', 'There is a small river flowing next to you.'
                           '\n You can follow it to the east or you can go North, South, or West',
             'MTN_SHOP', 'OASIS', 'BAY', 'CLEARING')
JEVIL_ENTRANCE = Room('???????????', "*There is a cage-like gate in front of you, "
                                     "* There's a note saying: 'Collect the 4 keys to enter'",
                      None, None, 'CLEARING', None, None, None, 'JEVIL_FIGHT')
JEVIL_FIGHT = Room("???????", "JEVIL: 'I CAN DO ANYTHING!!' Watch out! Here comes JEVIL! "
                              "There's no strategy to beat this enemy, Good Luck! LET THE GAMES BEGIN!",
                   None, None, None, None, None, None, None, 'JEVIL_ENTRANCE')


player = Player(BEGIN)

directions = ['north', 'south', 'east', 'west', 'up', 'down', 'enter', 'leave', 'NORTH', 'SOUTH', 'EAST', 'WEST', 'UP',
              'DOWN', 'ENTER', 'LEAVE']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'altf4']:
        playing = False
    elif command == "":
        print()
    elif command == "scream":
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    elif command in ['die', 'drop dead', 'drop dead for no apparent reason', 'die for no reason', 'kill self']:
        player.health -= player.health
        print("Welp, you're dead now. Good job, you decided you wouldn't"
              " die from an enemy. You made sure of it by killing yourself...")
        print()
        print()
        print()
        print("Quick Question.... WHY????????????"
              "\n Oh well, I give up on trying to find your reasoning..."
              "\n"
              "\n"
              "\n..."
              "\n"
              "\n"
              "\n GAME OVER")
        playing = False
    elif command == "recognized":
        print("Command not reco- Oh... VERY funny! HA! HA! HA! Don't do that again")
    elif command == 'rob':
        #  This will be used to take money from NPCs
        print(Kirby.dialogue)
    elif command.lower() in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't do this or go this way")
    elif command.upper() in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't do this or go this way")
    else:
        print("Command not recognized, if you inputted a direction, write it again in all lowercase")
