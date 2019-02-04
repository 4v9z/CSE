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
            "SOUTH": "ADVENTURE_START"
        }
    },
    'FOREST_2': {
        'NAME': "Lost Woods",
        'DESCRIPTION': "You've made it to the second part of the forest, remember the hint",
        'PATHS': {
            'NORTH': "FOREST_3",
            'SOUTH': "FOREST"
        }
    },
    'FOREST_3': {
        "NAME": "Lost Woods",
        'DESCRIPTION': "Third room, but where to next?"
    }

}

# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['ADVENTURE_START']     # This is your current location
playing = True

# Controller
while playing:
    if current_node['NAME'] == "Lost Woods":
        in_lost_woods = True
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
