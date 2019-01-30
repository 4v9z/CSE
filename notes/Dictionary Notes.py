AAAAAAAAAAAAAAAAAAAAAAAAA = {"help": {
    "Endless": {
        "why": {
            "ddd": {
                "still going?": {
                    "this is a thing": {
                        "AAAAAAAAAAAAAAA": "AAAAAAAAAAA"
                    }
                }
            }
        }
    }
}}
input(AAAAAAAAAAAAAAAAAAAAAAAAA["help"]["Endless"]["why"]["ddd"]["still going?"]["this is a thing"]["AAAAAAAAAAAAAAA"])
states = {
        "CA": "California",
        "NJ": "New Jersey",
        "WI": "Wisconsin",
        "NY": "New York"

}
print(states["CA"])
print(states["NJ"])
print(states["WI"])
print(states["NY"])
nested_dictionary = {
        "CA": {
            "NAME": "California",
            "POPULATION": 39500000
        },
        "NJ": {
            "NAME": "New Jersey",
            "POPULATION": 9000000
        },
        "WI": {
            "NAME": "Wisconsin",
            "POPULATION": 5800000
        },
        "NY": {
            "NAME": "New York",
            "POPULATION": 19500000
        }

}
print(nested_dictionary["CA"])      # <(|.|<) <(Poyo~!)
print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"]["NAME"])
complex_dictionary = {
        "CA": {
            "NAME": "California",
            "POPULATION": 39500000,
            "CITIES": [
                "Fresno",
                "San Francisco",
                "Los Angeles"
            ]
        },
        "NJ": {
            "NAME": "New Jersey",
            "POPULATION": 9000000,
            "CITIES": [
                "Newark",
                "Trenton",
                "Princeton"
            ]
        },
        "WI": {
            "NAME": "Wisconsin",
            "POPULATION": 5800000,
            "CITIES": [
                "Madison",
                "Milwaukee",
                "Green Bay"
            ]
        },
        "NY": {
            "NAME": "New York",
            "POPULATION": 19500000,
            "CITIES": [
                "New York City",
                "Rockester",
                "Buffalo"
            ]
        }

}
print(complex_dictionary["NY"]["CITIES"][0])
print(complex_dictionary["NJ"]["CITIES"][2])
# <(|.|<) <(HAI~! POYO~!)

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())
# for key, value in complex_dictionary.items():
#    print(key)
#    print(value)
# print("-" * 20)
print()
for state, info in complex_dictionary.items():
    for titles, descriptions in info.items():
        print(titles)
        print(descriptions)
        print("_" * 20)
    print("=" * 20)

