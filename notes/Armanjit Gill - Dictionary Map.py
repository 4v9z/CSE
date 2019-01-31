world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the room that you are in",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here",
        'PATHS': {
            'SOUTH': "R19A",
            "DOWN": "MARX_ARENA"
        }
    },
    'MARX_ARENA': {
        'NAME': "Marx's Domain",
        'DESCRIPTION': "You find yourself somewhere that looks like a planet separate from ours, this place is "
                       "barren, devoid of any life. This is not a safe place, the only thing here is "
                       "Marx, ready for battle. "
                       "Marx is staring you down, waiting "
                       "for you to step forwards",
        'PATHS': {
            'UP': "PARKING_LOT"
        }
    }
}

# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['R19A']     # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command == "":
        print(current_node["DESCRIPTION"])
    elif command == "recognized":
        print("Command not reco- Oh... VERY funny! HA! HA! HA! Don't do that again")
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go this way")
    else:
        print("Command not recognized, if you inputted a direction, write it again in all caps")
