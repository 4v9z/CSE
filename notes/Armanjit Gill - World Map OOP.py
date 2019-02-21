class Room(object):
    def __init__(self, name, description='This is a room', north=None, south=None, east=None, west=None,
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


# Option 2 - Use strings, but more difficult controller
BEGIN = Room("An Adventure's Beginning", "You stand atop a hill looking ahead at the forest to "
                                         "the north and turn around to see the desert to the south. "
                                         "\n You're ready for your quest.", 'FOREST', 'TOWN', 'OASIS',
             'FACTORY', 'CHEATS', 'LOSS')
LOSS = Room('|     |i   ||  |__', '|     |i   ||  |__')
FACTORY = Room('Factory', "You are looking at a strange factory, will you enter it?", None, None, 'BEGIN', None,
               'M_MARIO')
M_MARIO = Room('Inside the Factory', "You are in a fight with Metal Mario, a Robotic "
                                     "copy of the beloved plumber! Let's see if you can win!",
               None, None, None, None)
FOREST = Room("Lost Woods", 'You are in a forest that feels mysterious, if you make a wrong move,'
                            ' you will be sent back to the first room of the forest.', 'FOREST2', 'FOREST',
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
                            "it's dark and seems to have lost all of it's power", "MOUNTAIN_PASS",
                "FOREST", "JEVIL_ENTRANCE", "RIVER_PATH")
