dead = False
world_map = {
    'ADVENTURE_START': {
        'NAME': "An Adventure's Beginning",
        'DESCRIPTION': "You stand atop a hill looking ahead at the forest"
                       "to the north and turn around to see the desert to the south. You're ready for your quest.",
        'PATHS': {
            'NORTH': "FOREST",
            'SOUTH': "TOWN",
            'UP': "CHEATS",
            'WEST': 'FACTORY',
            'EAST': 'OASIS'
        }
    },
    'FACTORY': {
        'NAME': "Strange Factory",
        'DESCRIPTION': "You are looking at a strange factory,"
                       "it's removed from the rest of the world, it feels like it shouldn't be here...",
        'PATHS': {
            "ENTER": "M_MARIO",
            'EAST': "ADVENTURE_START"
        }
    },
    'M_MARIO': {
      "NAME": "Metal Mario: 'HERE WE GOOO!'",
      'DESCRIPTION': "You are in a fight with Metal Mario, a Robotic coby of the beloved plumber! Let's "
                     "see if you can win!",
      'PATHS': {
          'LEAVE': "FACTORY"
      }
    },
    'CHEATS': {
      'NAME': "Traceback (most recent call last): File 'C:/Users/4v9z/Documents/GitHub/"
              "CSE/notes/Armanjit Gill - Dictionary Map.py",
      'DESCRIPTION': "@#%$*@(#^@*!*#&$^hdqoY&*#",
      'PATHS': {
            'WEST': "CLEARING"
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
        'DESCRIPTION': "You've made it to a clearing, you can move East, West, or North."
                       "\n "
                       "There is also a strange sword embedded in the ground, however, "
                       "it's dark and seems to have lost all of it's power",
        'PATHS': {
            'WEST': "JEVIL_ENTRANCE",
            'NORTH': "MOUNTAIN_PASS",
            'EAST': "RIVER_PATH"
        }
    },
    'JEVIL_ENTRANCE': {
        'NAME': '???????',
        'DESCRIPTION': "*There is a cage-like gate in front of you, "
                       "* There's a note saying: 'Collect the 4 keys to enter'",
        'PATHS': {
            "ENTER": "JEVIL_ARENA",
            'EAST': "CLEARING"
        }
    },
    'JEVIL_ARENA': {
        'NAME': "JEVIL: I CAN DO ANYTHING",
        "DESCRIPTION": "Watch out! Here comes JEVIL! "
                       "There's no strategy to beat this enemy, Good Luck! LET THE GAMES BEGIN!",
        'PATHS': {
            'LEAVE': 'JEVIL_ENTRANCE'
        }
    },
    'RIVER_PATH': {
        'NAME': 'River Path',
        'DESCRIPTION': "There is a small river flowing next to you",
        'PATHS': {
            "EAST": "BAY",
            'WEST': 'CLEARING',
            'NORTH': 'MTN_SHOP',
            'SOUTH': 'OASIS'
        }
    },
    'BAY': {
        'NAME': "Great Bay",
        'DESCRIPTION': "There is an open ocean around you, you can see a strange structure under the water",
        'PATHS': {
            'DOWN': 'TEMPLE',
            'WEST': "RIVER_PATH"
        }
    },
    'TEMPLE': {      # DUNGEON

    },
    'OASIS': {
        'NAME': 'Oasis',
        'DESCRIPTION': "You're in the middle of a desert next to the only water here."
                       "\n "
                       "There is a waterway barely big enough for you in the water.",
        'PATHS': {
            'DOWN': 'TOWN',
            'NORTH': 'RIVER_PATH',
            'SOUTH': 'DESERT_FIGHT',
            'WEST': 'ADVENTURE_START'
        }
    },
    'DESERT_FIGHT': {
        'NAME': 'Empty Expanse',
        'DESCRIPTION': 'You look around the large vast desert. It feels like something is here... watching you...'
                       '\n '
                       'As you think this, you get attacked!',
        'PATHS': {
            'NORTH': 'OASIS',
            'SOUTH': 'BACK_CASTLE',
            'WEST': 'TOWN',
            'EAST': 'TOWER'
        }
    },
    'TOWN': {
        'NAME': 'Desert Village',
        'DESCRIPTION': "You find yourself in a large town, looking around there isn't anything to do here",
        'PATHS': {
            'EAST': "DESERT_FIGHT",
            'NORTH': 'ADVENTURE_START',
            'SOUTH': 'MARKET'
        }
    },
    'MARKET': {
        'NAME': 'Desert Market',
        'DESCRIPTION': "You browse the fine selection of goods, you see potions that increase health and MP,"
                       "\n "
                       "a strange pendant with a drop of water engraved on it, a scimitar, strange scuba gear, and "
                       "an odd key"
                       "\n"
                       "You also see a bettered door mat saying 'WELCOME TO ZORK', but it seems to be worthless."
                       " You can buy or sell something here.",
        'PATHS': {
            'NORTH': 'TOWN',
            'EAST': 'CASTLE',
            'WEST': 'TEMPLE2'
        }
    },
    'TOWER': {
        'NAME': 'Shiekah Tower',
        'DESCRIPTION': "You look up at the tower in front of you. you can climb it,"
                       " and it looks like there'll be a reward at the top for you",
        'PATHS': {
            'CLIMB': "TOP_TOWER",
            'WEST': 'DESERT_FIGHT'
        }
    },
    'TOP_TOWER': {
        'NAME': 'Shiekah Tower',
        'DESCRIPTION': 'You look in front of you and see two pedastals, one has an axe in it, one has a shield.'
                       '\n'
                       'There appears to be a sign in between them that says "ONLY TAKE ONE". Will you listen to it?',
        'PATHS': {
            'DOWN': 'TOWER'
        }
    },
    'TEMPLE2': {
        'NAME': 'Temple of Time',
        'DESCRIPTION': "You look in front of you to see an temple with open doors, there is also a "
                       "staircase leading down, and to the South, another strange temple",
        'PATHS': {
            'ENTER': "TOT1",
            'DOWN': "TOT_SHOP",
            'SOUTH': 'LIGHT'
        }
    },
    'TOT1': {   # DUNGEON

    },
    'TOT_SHOP': {
        'NAME': 'Temple Shop',
        'DESCRIPTION': 'ROBOT: BEEP BOOP, What do you want to buy? ZZZZZT! '
                       '\n '
                       'We have a thunder sword, increased health and MP, Directions through the Lost Woods, and Armor',
        'PATHS': {
            'UP': "TEMPLE2"
        }
    },
    'LIGHT': {
        'NAME': 'Light Temple',
        'DESCRIPTION': "You've (ironically) entered a very dark place. "
                       "There are stairs leading up.",
        'PATHS': {
            'UP': "U.NECROZMA",
            'NORTH': 'TEMPLE2'
        }
    },
    'U.NECROZMA': {
        'NAME': "Megalo Tower",
        'DESCRIPTION': "You see a golden dragon towering over you. Ultra Necrozma: Lie..."
                       " Lieeee.... LIGHT!!!!!! Time to see who will prevail in battle",
        'PATHS': {
            'DOWN': 'LIGHT',
            'UP': 'CHEATS'
        }
    }
}

# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", 'ENTER', "LEAVE", 'CLIMB']
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
            print("I can't do this or go this way")
    else:
        print("Command not recognized, if you inputted a direction, write it again in all caps")
