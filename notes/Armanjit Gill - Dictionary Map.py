world_map = {
    'ADVENTURE_START': {
        'NAME': "An Adventure's Beginning",
        'DESCRIPTION': "You stand atop a hill looking ahead at the forest "
                       "to the north and turn around to see the desert to the south. You're ready for your quest.",
        'PATHS': {
            'NORTH': "FOREST",
            'SOUTH': "DESERT_TOWN"
        }
    },
    'FOREST': {
        'NAME': "Lost Woods",
        'DESCRIPTION': "This is a strange place. You hear a faint wind that whistles: 'konami....",
        'PATHS': {
            'NORTH': "FOREST_2",
            "SOUTH": "ADVENTURE_START",
            'EAST': "FOREST",
            'WEST': "FOREST"
        }
    },
    'FOREST_2': {
        'NAME': "Lost Woods",
        'DESCRIPTION': "You've made it to the second part of the forest, remember the hint",
        'PATHS': {
            'NORTH': "FOREST_3",
            'SOUTH': "FOREST",
            'WEST': 'FOREST',
            'EAST': 'FOREST'
        }
    },
    'FOREST_3': {
        "NAME": "Lost Woods",
        'DESCRIPTION': "Third room, but where to next?",
        'PATHS': {
            'SOUTH': "FOREST_4",
            'NORTH': "FOREST",
            'WEST': 'FOREST',
            'EAST': 'FOREST'
        }
    },
    'FOREST_4': {
        "NAME": "Lost Woods",
        'DESCRIPTION': "Where to next?",
        'PATHS': {
            'SOUTH': "FOREST_5",
            'NORTH': "FOREST",
            'EAST': "FOREST",
            'WEST': 'FOREST'

        }
    },
    'FOREST_5': {
        'NAME': "Lost Woods",
        'DESCRIPTION': "You don't have to go south anymore...",
        'PATHS': {
            "WEST": "FOREST_6",
            'EAST': "FOREST",
            'NORTH': "FOREST",
            'SOUTH': "FOREST"
            }
    },
    "FOREST_6": {
        'NAME': "Lost Woods",
        'DESCRIPTION': "Do I need to tell you anything anymore???",
        'PATHS': {
            "EAST": "FOREST_7",
            'WEST': "FOREST",
            'NORTH': "FOREST",
            'SOUTH': "FOREST"
        }
    },
    'FOREST_7': {
        'NAME': "Lost Woods",
        "DESCRIPTION": "If you got this far you should know where to go next. "
                       "Unless you are using process of elimination",
        'PATHS': {
            "WEST": "FOREST_8",
            'EAST': "FOREST",
            'NORTH': "FOREST",
            'SOUTH': "FOREST"
        }
    },
    'FOREST_8': {
        'NAME': "Lost Woods",
        "DESCRIPTION": "Last room",
        "PATHS": {
            "EAST": "CLEARING",
                    'WEST': "FOREST",
                    'NORTH': "FOREST",
                    'SOUTH': "FOREST"
        }
    },
    'CLEARING': {
        'NAME': "Clearing",
        'DESCRIPTION': "You've made it to a clearing, you can move East, West, or North.",
        'PATHS': {
            'EAST': "??????",
            'NORTH': "MOUNTAIN_PASS",
            'WEST': "RIVER_PATH"
        }
    }
}

# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['ADVENTURE_START']     # This is your current location
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
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
                print("I can't go this way")
    else:
        print("Command not recognized, if you inputted a direction, write it again in all caps")
