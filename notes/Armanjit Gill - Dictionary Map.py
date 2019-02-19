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
            'WEST': "CLEARING",
            'EAST': "BAY",
            'SOUTH': 'TEMPLE2'
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
            'EAST': "RIVER_PATH",
            'SOUTH': "FOREST"
        }
    },
    'MOUNTAIN_PASS': {
      'NAME': "Mountain Pass",
      'DESCRIPTION': "There is a frozen path leading west, a shop to the east, and towering above you, a mountain",
      'PATHS': {
          'WEST': "CAVE",
          'UP': "MTN_BASE",
          'EAST': "MTN_SHOP"
      }
    },
    'MTN_SHOP': {
      'NAME': "Mountain Shop",
      'DESCRIPTION': "There is engraving on stone: BUY SOMETHING AND LEAVE THE MONEY OR ELSE..."
                     "\n There is a keycard, armor, health upgrades, and a space helmet",
      'PATHS': {
          'EAST': "CLIMB",
          'WEST': "MOUNTAIN_PASS"
      }
    },
    'CLIMB': {
      'NAME': "Dangerous Climb",
      'DESCRIPTION': "You feel like this place isn't safe, when suddenly, you're attacked!",
      'PATHS': {
          "UP": "PEAK",
          'WEST': "MTN_SHOP",
          'DOWN': "BAY"
      }
    },
    'PEAK': {
        'NAME': "Tallest Peak",
        'DESCRIPTION': "There is floating wreckage here, if only you could see what this place looked like in the past",
        'PATHS': {
            'ENTER': "NOVA_1",
            'WEST': "END",
            'DOWN': "CLIMB"
        }
    },
    'END': {
        'NAME': "Edge of the Universe",
        'DESCRIPTION': "You stand in front of a dark void... unsu"
                       "re of what will become of you once you enter, there is only one thing you know for sure..."
                       "\n Your adventure is at its end",
        'PATHS': {
            'ENTER': "SUBSPACE_1",
            'DOWN': "VOLCANO",
            'EAST': "PEAK"
        }
    },
    'CAVE': {
        'NAME': "Frozen Cave",
        'DESCRIPTION': "You are in a cold cave. The ground and walls are frozen and "
                       "there are icicles hanging from the ceiling"
                       "\n In the center of the cave is an icy sword encased in an impenetrable layer of ice. "
                       "It seems like this ice wasn't here before... If only you could rewind time...",
        'PATHS': {
            'EAST': "MOUNTAIN_PASS"
        }
    },
    'MTN_BASE': {
      'NAME': "Mt. Silver Base",
      'DESCRIPTION': "You are at the base of a snowy mountain. You can likely climb it, but the rocks "
                     "are slightly slippery, so you might slip and fall",
      'PATHS': {
            'UP': "MT.SILVER",
            'DOWN': "MOUNTAIN_PASS",
            'NORTH': "VOLCANO"
        }
    },
    'VOLCANO': {
      'NAME': "Volcano",
      'DESCRIPTION': "You are in front of a volcano... what do you want do?",
      'PATHS': {
           'ENTER': "INTERIOR",
           'SOUTH': 'MTN_BASE'
       }
    },
    'INTERIOR': {
      'NAME': "Inside of Volcano",
      'DESCRIPTION': "HOLY HECK YOU'RE STILL ALIVE!!!!! Ahem.... Anyways... There is a key here",
      'PATHS': {
          'UP': "VOLCANO"
      }
    },
    'MT.SILVER': {
      'NAME': "Mt. Silver",
      'DESCRIPTION': "You are on top of the mountain. Hail is plummeting down and the wind is howling. "
                     "There is someone at the edge of the cliff you're standing on"
                     "\n Red:..............!!!",
      'PATHS': {
          'DOWN': "MTN_BASE"
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
        'NAME': "????????????",
        "DESCRIPTION": "JEVIL: 'I CAN DO ANYTHING!!' Watch out! Here comes JEVIL! "
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
    'TEMPLE': {
        'NAME': "Water Temple",
        'DESCRIPTION': "You are in the first room of the Water Temple."
                       "\n You can swim back up or head north to the second room",
        'PATHS': {
            'UP': "BAY",
            'NORTH': 'TEMPLE_2'
        }
    },
    'TEMPLE_2': {
        'NAME': "Lock Room",
        'DESCRIPTION': "You are in a room with a locked door leading east. "
                       "\n You can continue through the temple to the north",
        'PATHS': {
            'EAST': "MP_ROOM",
            'NORTH': "TEMPLE_3",
            'SOUTH': "TEMPLE"
        }
    },
    'MP_ROOM': {
      'NAME': "Magic Room",
      'DESCRIPTION': "You look around the room. There are strange characters etched into the walls."
                     "\n You feel your MP get restored as well as increase",
      'PATHS': {
          'WEST': 'TEMPLE_2'
      }
    },
    'TEMPLE_3': {
        'NAME': "Empty Chamber",
        'DESCRIPTION': "There is a locked door to the east and a door leading north. "
                       "\n You feel like something in the water is watching you, when you're suddenly attacked",
        'PATHS': {
            'EAST': "DARK_LINK",
            'SOUTH': "TEMPLE_2",
            'NORTH': "TEMPLE_4"
        }
    },
    'TEMPLE_4': {
      'NAME': "Boss Room",
      'DESCRIPTION': "In front of you is a large door that has a fittingly over-sized lock."
                     "\n You look to the east and west, either direction can hold the key",
      'PATHS': {
          'WEST': "TRAP",
          'EAST': "TEMPLE_5",
          'ENTER': "CHAOS"
      }
      },
    'CHAOS': {
      'NAME': "Chaos Battle",
      'DESCRIPTION': "You are face to face with Chaos 0! The strange watery creature looks angry. "
                     "Since normal weapons phase through it, ice or electricity would likely be most effective to "
                     "attack it",
      'PATHS': {
          'LEAVE': "TEMPLE_4"
      }
    },
    'TEMPLE_5': {
      'NAME': "Gold Room",
      'DESCRIPTION': "You are in a room that is entirely made of gold, a sign says:"
                     "\n DO NOT BE GREEDY, TAKE NO MORE THAN 150 GOLD!"
                     "\n It's up to you whether or not you should heed this warning"
                     " You can head north to continue through the temple",
      'PATHS': {
          'NORTH': "TEMPLE_6",
          'WEST': "TEMPLE_4"
      }
    },
    'TEMPLE_6': {
      'NAME': "Skeleton Room",
      'DESCRIPTION': "You are in a room full of bones. "
                     "\n On top of a particularly large pile of bones is a skeleton key that will unlock"
                     " any room in the temple"
                     "\n climbing up the pile might be risky but it's the only way to fight the temple's boss",
      'PATHS': {
          'UP': "KEY",
          'SOUTH': "TEMPLE_5"
      }
    },
    'KEY': {
        'NAME': "Top of pile",
        'DESCRIPTION': "You've made it to the top of the pile, the key is yours for the taking."
                       "\n Dropping down the pile will not be as risky as climbing the pile",
        'PATHS': {
            'DOWN': "TEMPLE_6"
        }
    },
    'TRAP': {
      'NAME': "Trap",
      'DESCRIPTION': "As you walk to the west, the floor beneath you crumbles, "
                     "dropping you into a large pool of piranha-infested waters"
                     "\n You struggle to survive but you realize it's futile, you are not going to survive",
      'PATHS': {

      }
    },
    'DARK_LINK': {
        'NAME': "Reflecting Pond",
        'DESCRIPTION': "You find yourself in a room where the floor is covered in a thin layer of of water. "
                       "In the middle of the room there is a small mound of dirt with a "
                       "large black tree growing out of it."
                       "\n As you walk through the room, you look down and see your reflection is gone. "
                       "You turn around and see Dark Link!"
                       "\n The evil version of the fabled hero won't be pulling any punches, "
                       "but you clutch your weapon and ready yourself for a fight.",
        'PATHS': {
            'WEST': "TEMPLE_3"
        }
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
                       "You also see a battered door mat saying 'WELCOME TO ZORK', but it seems to be worthless."
                       "\n You can buy or sell something here.",
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
    'TOT1': {
        'NAME': "Temple of Time",
        'DESCRIPTION': "You have entered the temple, you can continur=e through a door to the north",
        'PATHS': {
            'NORTH': 'TOT2',
            'LEAVE': "TEMPLE2"
        }
    },
    'TOT2': {
      'NAME': 'Watch Room',
      'DESCRIPTION': "In the center of the room there is a magic pocket watch. You sigh as you realize "
                     "some time-travel shenanigans will ensue"
                     "You can use the watch to open up paths to the east or west that existed in "
                     "the past or future",
      'PATHS': {
          'SOUTH': "TOT1",
          'EAST': "PAST1",
          'WEST': "FUTURE1",
          'NORTH': "TOT3"
      }
    },
    'PAST1': {
      'NAME': "Empty Citadel (Past)",   # The text will change based on if you go here in the present, past, or future
      'DESCRIPTION': "You enter this room in the past."
                     "\n You feel this room has nothing to see, when suddenly you're attacked!",
      'PATHS': {
          'WEST': "TOT2"
      }
    },
    'FUTURE1': {
      'NAME': "Gold Room (Future)",
      'DESCRIPTION': "In this room, there is a single coin upon a pedestal."
                     "\n Because this is the future, this single "
                     "coin is worth about 1,537 coins in the present",
      'PATHS': {
          'EAST': "TOT2"
      }
    },
    'TOT3': {
      'NAME': "Boss Room",
      'DESCRIPTION': "There is a large door in front of you with a large padlock on it, "
                     "it appears that a keys is needed. "
                     "\n You can use the watch to open up pathways to the east and west in the past and future.",
      'PATHS': {
          'SOUTH': "TOT2",
          'EAST': "FUTURE2",
          'WEST': "PAST2",
          'NORTH': "GHOMA"
      }
    },
    'PAST2': {
      'NAME': "Coin Room (Past)",
      'DESCRIPTION': "Upon a pedestal in this room is a single coin from the past."
                     "\n This coin is essentially worthless today: It's only worth 1 coin in the present",
      'PATHS': {
          'EAST': "TOT3"
      }
    },
    'FUTURE2': {
      'NAME': "Key Room (Future)",
      'DESCRIPTION': "While the path leading here has caved "
                     "in during our present day, and this "
                     "path had not yet been built in the past you can visit, the key in this "
                     "room appears to be broken. In our present day, this key was most definitely intact",
      'PATHS': {
          'WEST': "TOT3"
      }
    },
    'GHOMA': {
        'NAME': "Ghoma Fight",
        'DESCRIPTION': "In this room is the disgusting abomination of a spider: Ghoma"
                       "\n The strategy for this is to hit it with magic, as numerous "
                       "reincarnations has led to it being immune to physical attacks",
        'PATHS': {
            'NORTH': "PORTAL",
            'SOUTH': "TOT3"
        }
    },
    'PORTAL': {
      'NAME': "Time Portal",
      'DESCRIPTION': "In front of you is a portal that leads into a future ~12,000 years after the "
                     "extinction of humans. "
                     "\n You can go south to reenter the temple or you can enter the portal",
      'PATHS': {
          'SOUTH': 'GHOMA',
          'ENTER': "SPLAT1"
      }
    },
    'SPLAT1': {
        'NAME': "Octo Valley",
        'DESCRIPTION': "You are on a strange floating platform, you "
                       "can enter the time portal from here or head north to continue",
        'PATHS': {
            'ENTER': "PORTAL",
            'NORTH': "SPLAT2"
        }
    },
    'SPLAT2': {
      'NAME': "Moray Towers",
      'DESCRIPTION': "You are climbing a tower currently, you can go back south, head north, or go east or west"
                     "\n Going East requires some way to swim through ink",
      'PATHS': {
          'SOUTH': "SPLAT1",
          'NORTH': "SPLAT3",
          'WEST': "SPLAT4",
          'EAST': "SPLAT5"
      }
    },
    'SPLAT3': {
        'NAME': "Urchin Underpass",
        'DESCRIPTION': 'You are in an are filled with conveyor belts and is surrounded by water.'
                       '\n You can go north or east, but you will require some way to swim through ink',
        'PATHS': {
            'NORTH': "SPLAT6",
            'EAST': "SPLAT7",
            'SOUTH': "SPLAT2"
        }
    },
    'SPLAT7': {
        'NAME': "Hammerhead Bridge",
        'DESCRIPTION': "You are walking across a large bridge leading to the east."
                       "\n To the east is what looks to be a dark and removed part of "
                       "this world. cast way, in the shadows",
        'PATHS': {
            'WEST': "SPLAT3",
            'EAST': "SPLAT8"
        }
    },
    'SPLAT8': {
      'NAME': "Cephalon HQ",
      'DESCRIPTION': "You are in an area with floating platforms. "
                     "Below you is a toxic sludge with stone tentacles rising out of it",
      'PATHS': {
          'NORTH': "DJOCTAVIO",
          "WEST": "SPLAT7"
      }
    },
    'DJOCTAVIO': {
      'NAME': "DJ Octavio Fight",
      ''
    },
    'SPLAT6': {
      'NAME': "Arowana Mall",
      'DESCRIPTION': "You are in a shopping mall. Here you can buy upgrades to your health or magic, "
                     "as well as buy items to restore your health",
      'PATHS': {
          'SOUTH': "SPLAT3",
      }
    },
    'SPLAT5': {
        'NAME': "Octo Canyon",
        'DESCRIPTION': "After swimming through the ink, you have reached a large canyon. "
                       "\n Looking down in the canyon you can see something that looks like"
                       " a cross between a squid and a kid...",
        'PATHS': {
            'DOWN': "3",
            'WEST': "SPLAT2"
        }
    },
    '3': {
      'NAME': "Agent 3 battle",
      'DESCRIPTION': "Upon getting closer, the squid-kid sees you.She turns around and she looks ready to fight"
                     "\n this 'Inkling' is known as Agent 3, and she will be one of your most difficult battles yet.",
      'PATHS': {
          'UP': "SPLAT5"
      }
    },
    'SPLAT4': {
        'NAME': "Bluefin Depot",
        'DESCRIPTION': "You are on a platform floating in the water, there is a large crate here that can be opened",
        'PATHS': {
            'EAST': "SPLAT2"
        }
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
    },
    'BACK_CASTLE': {
        'NAME': "Back of Castle",
        'DESCRIPTION': "You are behind a large castle, there is a door in front of you.",
        'PATHS': {
            'ENTER': 'CASTLE_7',
            'NORTH': 'DESERT_FIGHT',
            'SOUTH': 'CASTLE'
        }
    },
    'CASTLE': {
        'NAME': 'Desert Castle',
        'DESCRIPTION': "There is a large stone castle in front of you, it towers over you ominously.",
        'PATHS': {
            'NORTH': 'BACK_CASTLE',
            'WEST': "MARKET",
            'ENTER': 'CASTLE_1',
            'SOUTH': "ROAD"
        }
    },
    'CASTLE_1': {  # DUNGEON
        'NAME': "Castle Entrance",
        'DESCRIPTION': "You have just entered the castle, looking ahead, there is a room full of rotating saw blades.",
        'PATHS': {
            'NORTH': "CASTLE_2",
            'LEAVE': "CASTLE"
        }
    },
    'CASTLE_2': {
       'NAME': "Saw Room",
       'DESCRIPTION': "You are in a room in which saws are rotating on a set path, you can sprint North to make it "
                      "through here."
                      "\n However, this is risky, and it can lead to your demise",
       'PATHS': {
            'NORTH': "CASTLE_3",
            'SOUTH': "CASTLE_1"
       }
    },
    'CASTLE_3': {
       'NAME': "Lava Room",
       'DESCRIPTION': "You are walking on a narrow platform, looking down, there's a pit of lava."
                      "\n !!!"
                      "\n The lava is now rising! Climbing up is your only option!",
       'PATHS': {
            'UP': "CASTLE_4",
            'SOUTH': "CASTLE_2"
        }
    },
    'CASTLE_4': {
       'NAME': "Empty Room",
       'DESCRIPTION': "You feel uneasy, like you're being watched. There is a door leading east, "
                      "but you feel like you're about to be ambushed",
       'PATHS': {
           'EAST': "CASTLE_5",
           'DOWN': "CASTLE_3"
       }
    },
    'CASTLE_5': {
       'NAME': "Boss Room",
       'DESCRIPTION': "You are at the end of the castle, you can head north through the "
                      "large gate or east towards the back exit",
       "PATHS": {
           'NORTH': "BOWSER",
           'EAST': "CASTLE_6",
           'WEST': "CASTLE_4"
       }
    },
    'BOWSER': {
        'NAME': "Bowser Battle",
        'DESCRIPTION': "After walking through the door you find yourself face to face with the King of Koopas, Bowser!"
                       "\n Ready? FIGHT!",
        'PATHS': {
            'SOUTH': "CASTLE_5"
        }
    },
    'CASTLE_6': {
      'NAME': "Near Back exit",
      'DESCRIPTION': "You are near the back exit of a castle, "
                     "but to get there you'd have to hop across rocks floating in a river of lava"
                     "\n To the west is the room before the boss in this castle",
      'PATHS': {
          'WEST': "CASTLE_5",
          'NORTH': "CASTLE_7"
      }
    },
    'CASTLE_7': {
        'NAME': "Back Exit of Castle",
        'DESCRIPTION': "You are at the back exit of the castle. To go further through the castle, "
                       "you'd have to hop across rocks floating in a river of lava, or you can leave now",
        'PATHS': {
            'LEAVE': 'BACK_CASTLE',
            'SOUTH': 'CASTLE_6'
        }
    },
    'ROAD': {
        'NAME': "Rainbow Road",
        'DESCRIPTION': "You are standing in front of a rainbow that appears to continue through "
                       "the atmosphere and into space"
                       "\n"
                       "You can walk up the rainbow",
        'PATHS': {
            'UP': "DARK_STAR",
            'NORTH': "CASTLE"
        }
    },
    'DARK_STAR': {
        'NAME': "Galaxy Reactor",
        'Description': "There is a dark orb floating in the center of a large platform. You take a step forward."
                       "\n Suddenly... the orb transforms into: DARK BOWSER!",
        'PATHS': {
            'DOWN': "ROAD"
        }
    },
}

# Other variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", 'ENTER', "LEAVE", 'CLIMB']
current_node = world_map['ADVENTURE_START']     # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'altf4']:
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
