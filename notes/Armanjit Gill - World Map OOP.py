class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None,
                 enter=None, leave=None, up=None, down=None, description='This is a room'):
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


# Option 1 - Use the Variables, fix later
R19A = Room("Mr. Wiebe's Room", None)
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("The Parking Lot", 'None, R19A')
