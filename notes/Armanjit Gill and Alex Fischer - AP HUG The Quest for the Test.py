import random
from termcolor import colored

instructions = True


class Gold(object):
    def __init__(self, worth=0):
        self.worth = worth
        self.name = "Gold"

    def grab(self):
        player.money += self.worth
        print("You picked up the gold")


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

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if damage < self.armor.defense:
            print("No damage was taken!")
        else:
            self.health -= damage - self.armor.defense
            if self.health < 0:
                self.health = 0
                print("%s has been defeated!" % self.name)
                player.money += self.money
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.attack_stat))
        target.take_damage(self.weapon.attack_stat)
        if self.weapon.__class__ is Splattershot:
            target.inked = True
            print("You have been inked and attacks now do double damage")


class NPC(Character):
    def __init__(self, name, health, power, money, shop=False, dialogue=''):
        super(NPC, self).__init__(none, none5, health, name, False, money)
        self.items = []
        self.power = power
        self.shopkeeper = shop
        self.option = ""
        self.dialogue = dialogue
        self.like = 0
        self.aaaaaaa = 0
        self.oo = 0

    def talk(self):
        if self.shopkeeper:
            input("%s: I'm not supposed to talk to the customer, sorry" % self.name)
        else:
            if self.like == 0:
                input("%s: %s" % (self.name, self.dialogue))
                self.like += 1
                self.aaaaaaa = len(self.items)
            elif self.like == 1:
                if self.aaaaaaa == 0:
                    if self.name != "Agent 3":
                        input("%s: %s" % (self.name, self.dialogue))
                    elif self.name == "Agent 3":
                        self.oo += 1
                    if self.oo == 1:
                        input("Agent 3: So... on a quest to save the world? Sounds fun.")
                    elif self.oo == 2:
                        input("Agent 3: I've saved the world before... It was pretty exhilarating")
                    elif self.oo == 3:
                        input("Agent 3: Let's fight again! Heh, just kidding. "
                              "\n Based on the look on your face, I'd assume that you wouldn't enjoy that.")
                    elif self.oo == 4:
                        input("Agent 3: ........")
                    elif self.oo == 5:
                        input("Agent 3: (This person is quite the talker....)")
                    elif self.oo == 6:
                        input("Agent 3: (I wonder how all my friends are doing?)")
                    elif self.oo == 7:
                        input("Agent 3: (Maybe if I act like I'm bored, they'll leave)")
                    elif self.oo == 8:
                        input("Agent 3: (Why is this person talking to me so much???)")
                    elif self.oo == 9:
                        input("Agent 3: (I miss Agent 8, wonder what she's up to?)")
                    elif self.oo == 10:
                        input("Agent 3: (While this person is still here I guess I'll just listen to some music)")
                    elif self.oo == 11:
                        input("Agent 3 is humming a tune overly loud to try to annoy you into "
                              "bailing from the conversation")
                else:
                    if len(Inventory.inventory) + len(self.items) <= Inventory.max_space:
                        if self.name == "Dog":
                            input("Bark! Bark! Bark!")
                        else:
                            input("%s: I would like to give you this" % self.name)
                        for i in range(len(self.items)):
                            Inventory.inventory.append(self.items[i])
                            self.aaaaaaa = 0
                            if self.name == "Dog":
                                self.dialogue = self.dialogue
                            elif self.name == "Agent 3":
                                self.dialogue = ("%s: Nice to see ya again!" % self.name)
                            else:
                                self.dialogue = ("%s: Hello, nice to see you!" % self.name)
                    else:
                        if self.name == "Dog":
                            print("The dog barks sadly, you can't carry what he wants to give you")
                        else:
                            print("%s: I would like to give you thi-- Oh... I'm not sure you have enough"
                                  " space in your bag to hold my items...." % self.name)

    def buy(self):
        if self.shopkeeper:
            print()
            for num, item in enumerate(self.items):
                print(str(num + 1) + ": " + item.name + " - " + "%i" % item.price)
            print()
            self.option = input("%s: What do you want to buy?" % self.name)
            for i in range(len(self.items)):
                if i < len(self.items):
                    if self.items[i].name.lower() == self.option.lower():
                        if player.money >= self.items[i].price:
                            player.money -= self.items[i].price           # FIX THIS NOW
                            self.items[i].grabbed = True
                            Inventory.inventory.append(self.items[i])
                            if self.name.lower() == "gerudo shopkeeper" \
                                    and self.option.lower() == "battered rubber mat that reads 'welcome to zork'":
                                print("Gerudo Shopkeeper: Thank Hylia that someone FINALLY decided to buy this thing!"
                                      "\n Here, take it!")
                                self.items.remove(self.items[i])
                            elif self.name.lower() == "stone tablet" \
                                    and self.option.lower() == "health upgrade":
                                print("You buy and then proceed to absorb the health upgrade")
                                self.items[i].grab()
                            else:
                                print("%s: Here is/are your %s" % (self.name, self.items[i].name))
                                self.items.remove(self.items[i])
                        else:
                            print("Sorry, you do not have enough money to purchase this")


class Armor(object):
    def __init__(self, defense, name="", price=0):
        self.defense = defense
        self.grabbed = False
        self.name = name
        self.price = price

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Defense: %i" % self.defense)


class Helmet(Armor):
    def __init__(self, defense, name="", price=0):
        super(Helmet, self).__init__(2020, "", price)
        self.defense = defense
        self.name = name
        self.activated = False

    def grab(self):
        if self.activated:
            if Inventory.inventory.__len__() < Inventory.max_space:
                if self.grabbed:
                    print("You already have this")
                else:
                    print("You pick up the %s" % self.name)
                    self.grabbed = True
                    Inventory.inventory.append(self)
                    # add stuff to bag
            else:
                print("You can't carry any more items, you need to drop some items to make space")
        else:
            print("You can't grab this yet")

    def equip(self):
        if self.grabbed:
            if player.helmet is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.helmet = self
                player.defense += self.defense
                Inventory.inventory.remove(self)
            else:
                print("You already have a helmet equiped, unequip your current helmet to equip this helmet")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if player.helmet is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.helmet = none
                Inventory.inventory.append(self)


class Robinson(Helmet):
    def __init__(self, defense, name='', price=0):
        super(Robinson, self).__init__(defense, name, price)
        self.name = name
        self.defense = defense
        self.grabbed = False
        self.price = price
        self.stage = 1
        self.token = 0

    def develop(self):
        self.stage += 1
        self.token = 0
        if self.stage < 5:
            print("You have destroyed one level of distortion in the armor! Your map is now more accurate and closer to"
                  " perfection")
            self.stage += 7
        elif self.stage == 5:
            print("You have achieved GLOBAL STATUS. Your armor is now a perfect globe free of distortion, but cannot be"
                  " upgraded anymore.")
            self.stage += 10
            self.name = "Global Helmet"
        else:
            print("You cannot upgrade this armor.")

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the armor in its current form." % self.token)


robinson = Robinson(10, "Robinson Projection", 30)


class Chestplate(Armor):
    def __init__(self, defense, name="", price=0):
        super(Chestplate, self).__init__(2020, "", price)
        self.defense = defense
        self.name = name

    def equip(self):
        if self.grabbed:
            if player.chestplate is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.chestplate = self
                player.defense += self.defense
                Inventory.inventory.remove(self)
            else:
                print("You already have a Chestplate equipped, unequip your current chestplate to equip "
                      "this chestplate")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if self.name.lower() == 'undershirt':
                print(".....please do not take that off...")
            else:
                print("You remove the %s" % self.name)
                player.chestplate = undershirt
                Inventory.inventory.append(self)


class Homolosine(Chestplate):
    def __init__(self, defense, name="", price=0):
        super(Homolosine, self).__init__(defense, name, price)
        self.name = name
        self.defense = defense
        self.price = price
        self.grabbed = False
        self.token = 0
        self.stage = 1

    def develop(self):
        self.stage += 1
        self.token = 0
        if self.stage < 5:
            print("You have destroyed one level of distortion in the armor! Your map is now more accurate and closer to"
                  " perfection")
            self.stage += 7
        elif self.stage == 5:
            print("You have achieved GLOBAL STATUS. Your armor is now a perfect globe free of distortion, but cannot be"
                  " upgraded anymore.")
            self.stage += 10
            self.name = "Global Chestplate"
        else:
            print("You cannot upgrade this armor.")

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the armor in its current form." % self.token)


homolosine = Homolosine(10, "Homolosine Projection", 30)


class Boots(Armor):
    def __init__(self, defense, name="", price=0):
        super(Boots, self).__init__(2020, "", price)
        self.defense = defense
        self.name = name

    def equip(self):
        if self.grabbed:
            if player.boots is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.boots = self
                player.defense += self.defense
                Inventory.inventory.remove(self)
            else:
                print("You already have boots equiped, unequip your current boots to equip these boots")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if player.boots is none4:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.boots = none4
                Inventory.inventory.append(self)


class Louisiana(Boots):
    def __init__(self, defense, name="", price=0):
        super(Louisiana, self).__init__(defense, name, price)
        self.name = name
        self.defense = defense
        self.price = price
        self.grabbed = False
        self.token = 0
        self.stage = 1

    def develop(self):
        self.stage += 1
        self.token = 0
        if self.stage < 5:
            print("You have destroyed one level of distortion in the armor! Your map is now more accurate and closer to"
                  " perfection")
            self.stage += 7
        elif self.stage == 5:
            print("You have achieved GLOBAL STATUS. Your armor is now a perfect globe free of distortion, but cannot be"
                  " upgraded anymore.")
            self.stage += 10
            self.name = "Global Boots"
        else:
            print("You cannot upgrade this armor.")

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the armor in its current form." % self.token)


louisiana = Louisiana(10, "Louisiana Boots", 20)


class Leggings(Armor):
    def __init__(self, defense, name="", price=0):
        super(Leggings, self).__init__(2020, "", price)
        self.defense = defense
        self.name = name

    def equip(self):
        if self.grabbed:
            if player.leggings is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.leggings = self
                player.defense += self.defense
                Inventory.inventory.remove(self)
            else:
                print("You already have leggings equiped, unequip your current leggings to equip this leggings")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if self.name.lower() == 'underwear':
                print(".......... please.... UNDER NO CIRCUMSTANCES TAKE THAT OFF!!!!!!")
            else:
                print("You remove the %s" % self.name)
                player.leggings = underwear
                Inventory.inventory.append(self)


class Mercator(Leggings):
    def __init__(self, defense, name='', price=0):
        super(Mercator, self).__init__(defense, name, price)
        self.name = name
        self.defense = defense
        self.price = price
        self.stage = 1
        self.token = 0
        self.grabbed = False

    def develop(self):
        self.stage += 1
        self.token = 0
        if self.stage < 5:
            print("You have destroyed one level of distortion in the armor! Your map is now more accurate and closer to"
                  " perfection")
            self.stage += 7
        elif self.stage == 5:
            print("You have achieved GLOBAL STATUS. Your armor is now a perfect globe free of distortion, but cannot be"
                  " upgraded anymore.")
            self.name = "Global Leggings"
            self.stage += 10
        else:
            print("You cannot upgrade this armor.")

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the armor in its current form." % self.token)


mercator = Mercator(10, "Mercator Projection", 30)


class Weapon(object):
    def __init__(self, name="", price=0):
        self.price = price
        self.name = name
        self.attack_stat = 0
        self.grabbed = False
        self.token = 0

    def equip(self):
        if self.grabbed:
            if player.weapon is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.weapon = self
                Inventory.inventory.remove(self)
            else:
                print("You already have a weapon equipped, unequip your current weapon to equip this weapon")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if player.weapon is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.weapon = none5
                Inventory.inventory.append(self)


class Disc(Weapon):
    def __init__(self, name, price):
        super(Disc, self).__init__(name, price)
        self.name = name
        self.attack_stat = 12
        self.price = price
        self.grabbed = False
        self.token = 0
        self.stage = 1

    def develop(self):
        self.stage += 1
        if 1 <= self.stage <= 5:
            print("Your %s has developed to the next ring! You now attack with larger, more expensive rings!" %
                  self.name)
            self.attack_stat += 10
        else:
            print("Your %s can no longer develop." % self.name)

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the weapon in its current stage." % self.token)


class Weber(Weapon):
    def __init__(self, name="", price=0):
        super(Weber, self).__init__(name, price)
        self.name = name
        self.price = price
        self.grabbed = False
        self.attack_stat = 18
        self.token = 0
        self.stage = 1

    def develop(self):
        self.stage += 1
        if self.stage == 2:
            print("Your %s has become a bulk reducing industry. Damage has been increased!" % self.name)
            self.attack_stat = 8
        elif self.stage == 3:
            print("Your %s has become a bulk gaining industry! It receives a big damage increase!")
            self.attack_stat = 13

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the weapon in its current stage." % self.token)


class DTM(Weapon):
    def __init__(self, name="", price=0):
        super(DTM, self).__init__(name, price)
        self.name = name
        self.price = price
        self.attack_stat = 15
        self.stage = 1
        self.token = 0
        self.grabbed = False

    def develop(self):
        print("Your %s is developing!" % self.name)
        self.stage += 1
        self.token = 0
        if self.stage == 2:
            print("Your %s is now in stage 2! The NIR is skyrocketing! And so is the damage!" % self.name)
            self.attack_stat = 24
        elif self.stage == 3:
            print("Your %s has reached stage 3! Gender equality is rapidly improving and the NIR has started to fall!"
                  "Your death rate is continuing to drop, but so is the birth rate!" % self.name)
            self.attack_stat = 36
        elif self.stage == 4:
            print("Your %s has now reached stage 4! At this point, it is a fully developed nation! The dependency "
                  "ratio has fallen as well!" % self.name)
            self.attack_stat = 50
        elif self.stage == 5:
            print("Your %s is now stage 5, a rare sight indeed! The NIR, CBR, and CDR have come together to make an"
                  " incredibly sharp weapon!\n However, the aging population means that your bones aches when you swing"
                  " it and you take damage." % self.name)
            self.attack_stat = 60
        else:
            print("Your DTM could not develop.")

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
        else:
            print("You have %d tokens invested in the weapon in its current stage." % self.token)


class Sector(Weapon):
    def __init__(self, name="", price=0):
        super(Sector, self).__init__(name, price)
        self.name = name
        self.price = price
        self.token = 0
        self.grabbed = False
        self.stage = 1
        self.attack_stat = 5

    def develop(self):
        self.stage += 1
        self.attack_stat += 5
        print("You are on sector %d of the model. Your %s's damage has been slightly increased." % (self.stage,
                                                                                                    self.name))

    def token(self):
        self.token += 1
        if self.token >= 3:
            try:
                self.develop()
            except AttributeError:
                print("Error in development.")
            else:
                print("You have %d tokens invested in the weapon in its current stage." % self.token)


class Blade(Weapon):
    def __init__(self, attack_stat=None, sharp=True, dull=False, durability=None, name="", price=0):
        super(Blade, self).__init__("  ", price)
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.name = name
        self.base_durability = durability
        self.base_attack = attack_stat
        self.grabbed = False

    def attack(self):
        if self.grabbed:
            if self.sharp:
                print("You swing your weapon")
            elif self.dull:
                print("You swing your now dull weapon")

    def sharpen(self):
        if self.grabbed:
            print("You sharpen your weapon")
            self.durability = self.base_durability
            self.attack_stat = self.base_attack
            print("Your weapon has regained its durability")
            print()
            print("Your weapon is back to %s durability from this" % self.base_durability)

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Attack: %s" % self.attack_stat)
            print("Remaining durability: %s" % self.durability)

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)


class Sword(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, name, price=0):
        super(Sword, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.grabbed = False

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Attack: %s" % self.attack_stat)


class Swword(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, name, price=0):
        super(Swword, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.grabbed = False

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Attack: %s" % self.attack_stat)
            print("Remaining durability: %s" % self.durability)
            print("While this weapon can defeat any enemy in one hit, your HP is constantly going to be at 1HP")

    def attack(self):
        if self.grabbed:
            if self.sharp:
                print("You swing your weapon")
                player.money += 40
                self.durability -= 1
                if self.durability <= 0:
                    print("Your weapon has become dull from constant use")
                    self.sharp = False
                    self.dull = True
                    self.attack_stat /= 2
            elif self.dull:
                print("You swing your now dull weapon")
                player.money += 20


class Shword(Sword):
    def __init__(self, attack_stat, sharp, dull, durability, name, price=0):
        super(Shword, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.grabbed = False

    def equip(self):
        if self.grabbed:
            if player.weapon is None:  # Fix this later!
                print("You equip the %s" % self.name)
                player.weapon = self
                Inventory.inventory.remove(self)
                player.health = 1
            else:
                print("You already have a weapon equipped, unequip your current weapon to equip this weapon")
        else:
            print()


class Specialsword(Sword):
    def __init__(self, attack_stat, sharp, dull, durability, name, can_get=False, price=0):
        super(Specialsword, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.activated = can_get
        self.grabbed = False

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.activated:
                if self.grabbed:
                    print("You already have this")
                else:
                    print("You pick up the %s" % self.name)
                    self.grabbed = True
                    Inventory.inventory.append(self)
                    # add stuff to bag
            elif not self.activated:
                print("You try to grab the sword, but it can't be picked up currently")
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)


class Axe(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, name="", price=0):
        super(Axe, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.name = name
        self.base_durability = durability


paper1 = Boots(1, "Paper Boots")

paper2 = Leggings(2, "Paper leggings")

paper3 = Chestplate(3, "Paper Chestplate")

Wooden_Sword = Sword(13, True, False, 8, colored("Blue Pen", 'blue'))

Book = Sword(18, True, False, 90, colored("A smaller textbook", 'orange'))

Magic_Sword = Sword(20, True, False, 999999999999999999999999, "Magic Sword")

Fire = Sword(30, True, False, 20, "Burning Blade", 0)

paper4 = Helmet(3, "Paper Helmet")

none = Helmet(0, "None")

none2 = Chestplate(0, "None")

none3 = Leggings(0)

none4 = Boots(0)

none5 = Sword(0, True, False, 000, "")


class Player(object):
    def __init__(self, starting_location, health=80, helmet=paper4, chestplate=paper3, boots=paper1,
                 weapon=Wooden_Sword, mp=15, leggings=paper2, inked=False, money=30):
        self.health = health
        self.just_moved = True
        self.leggings = leggings
        self.normal_defense = 0
        self.normal_attack = 0
        self.rooms = 0
        self.roomz = 0
        self.stored_weapon = weapon
        self.inventory = []
        self.current_location = starting_location
        self.helmet = helmet
        self.chestplate = chestplate
        self.boots = boots
        self.MP = mp
        self.weapon = weapon
        self.max_health = health
        self.max_MP = mp
        self.defense = self.helmet.defense + self.chestplate.defense + self.leggings.defense + self.boots.defense
        self.name = "you"
        self.development_tokens = 0
        self.inked = inked
        self.money = money
        self.can_attack = False
        self.choice = ""
        self.random = 0
        self.du = False
        self.moves = 0
        self.hunger = 30

    def attack(self, target):
        if self.weapon.__class__ is Sword:
            self.weapon.attack()
        if self.weapon.__class__ is Axe:
            self.weapon.attack()
        if self.weapon.__class__ is Gun:
            self.weapon.shoot()
        if self.weapon.__class__ is Splattershot:
            self.weapon.shoot()
            if not target.inked:
                print("Your enemy has been inked and attacks now do double damage")
            target.inked = True
        if not target.inked:
            print("You attack %s for %d damage" %
                  (target.name, self.weapon.attack_stat))
        else:
            print("You attack %s for %d damage" %
                  (target.name, self.weapon.attack_stat * 2))
        if target.inked:
            target.take_damage(self.weapon.attack_stat * 2)
        else:
            target.take_damage(self.weapon.attack_stat)

    def cast(self, target):
        if target != self:
            print("What do you want to attack with?")
            print(colored("Fire Blast 🔥大🔥 - 5 MP", 'red'))
            print(colored("Thunder 🗲 - 10 MP", 'yellow'))
            print(colored("Blizzard ❄ - 15 MP", 'cyan'))
            print(colored('Your MP: %i/%i' % (self.MP, self.max_MP), 'magenta'))
            self.choice = input("")
            target.take_mp()
        elif target == self:
            print("What do you want to cast on yourself?")
            print(colored("Study (health restore) 💛 - 25 MP", 'yellow'))
            print(colored("Attack Up ⚔ - 35 MP", 'red'))
            print(colored("Defense Up 🛡 - 40 MP", 'blue'))
            print(colored('Your MP: %i/%i' % (self.MP, self.max_MP), 'magenta'))
            self.choice = input("")
            if self.choice.lower() == 'study':
                if self.MP >= 25:
                    print("You flip through a magic notebook you materialized")
                    if self.health + 30 > self.max_health:
                        print("Your HP is maxed out")
                        self.health = self.max_health
                    else:
                        print("You heal 30 HP")
                        self.health += 30
                else:
                    print("You don't have enough MP to cast heal")
            if self.choice.lower() == 'attack up':
                if self.MP >= 25:
                    print("You cast attack up, your weapon's attack is doubled for the next 3 rooms!")
                    self.normal_attack = self.weapon.attack_stat
                    self.weapon.attack_stat *= 2
                    self.rooms = 3
                else:
                    print("You don't have enough MP to cast attack up")
            if self.choice.lower() == 'defense up':
                if self.MP >= 25:
                    print("You cast attack up, your weapon's attack is doubled for the next 3 rooms!")
                    self.normal_defense = self.defense
                    self.defense *= 2
                    self.roomz = 3
                    self.du = True
                else:
                    print("You don't have enough MP to cast defense up")

    def rob(self, target):
        if target.__class__ is NPC:
            if target.name != "Dog":
                if self.weapon.attack_stat > target.power:
                    self.money += target.money
                    target.money -= target.money
                    input("You rob and overpower %s and take their money" % target.name)
                else:
                    input("You try to rob %s, but they easily overpower you and they take some of "
                          "your money" % target.name)
                    player.money -= player.money/9
                    target.attack(self, target.power)
            else:
                input("The dog bites you and while you are stunned, the dog takes all of your money and eats it"
                      " in front of your eyes")
                self.take_damage(10)
                self.money = 0
        else:
            print("You can't rob this being")

    def take_damage(self, damage):
        if not self.inked:
            if damage < self.defense:
                print("No damage was taken!")
            else:
                self.health -= damage*1.2 - self.defense
                if self.health < 0:
                    self.health = 0
                    print("You have been defeated!")
            print("You have %d health left" % self.health)
        elif self.inked:
            if damage * 2.5 < self.defense:
                print("No damage was taken!")
            else:
                self.health -= damage*2.5 - self.defense
                if self.health < 0:
                    self.health = 0
                    print("You have been defeated!")
            print("You have %d health left" % self.health)

    def move(self, new_location):
        """ This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.just_moved = True
        self.current_location = new_location
        self.inked = False
        self.rooms -= 1
        self.roomz -= 1
        if self.rooms == 0:
            print(colored("Your Attack Up Spell has run out", 'red'))
            self.weapon.attack_stat = self.normal_attack
        if self.roomz == 0:
            print(colored("Your Defense Up Spell has run out", 'blue'))
            self.defense = self.normal_defense
        if new_location == CH1K3:
            if self.current_location == RELOCATION:
                print("You try to go north, but you are assimilated and become part of the blob of globalization")
                player.health = 0
            else:
                self.just_moved = True
                self.current_location = new_location
                self.inked = False
                self.rooms -= 1
                self.roomz -= 1
                if self.rooms == 0:
                    print(colored("Your Attack Up Spell has run out", 'red'))
                    self.weapon.attack_stat = self.normal_attack
                if self.roomz == 0:
                    print(colored("Your Defense Up Spell has run out", 'blue'))
                    self.defense = self.normal_defense

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

    def check_stats(self):
        self.defense = self.helmet.defense + self.chestplate.defense
        self.defense += self.leggings.defense
        self.defense += self.boots.defense
        print("You:")
        print("Weapon: %s, does %i attack damage" % (self.weapon.name, self.weapon.attack_stat))
        print("Helmet: %s - %i defense" % (self.helmet.name, self.helmet.defense))
        print("Chestplate: %s - %i defense" % (self.chestplate.name, self.chestplate.defense))
        print("Leggings: %s - %i defense" % (self.leggings.name, self.leggings.defense))
        print("Boots: %s - %i defense" % (self.boots.name, self.boots.defense))
        print("Total Defense: %i" % self.defense)
        print("Health: %i/%d" % (self.health, self.max_health))
        print("MP: %i/%d" % (self.MP, self.max_MP))
        print("Money: %i" % self.money)
        print("Development Tokens: %i" % self.development_tokens)
        Inventory.check()


Inventory = Bag()

F_Sword = Sword(40, True, False, 200, "Frost Sword")

Money_Sword = Swword(1, True, False, 999999999999999999999999999999999999999999, "Money Sword")

E_Sword = Sword(45, True, False, 100, "Lightning Sword", 200)

Light_Sword = Specialsword(40, True, False, 125, "Light Sword")

One_Shot = Shword(99999999999, True, False, 100000, "One-Shot Sword", 9999999999)

Ancient_axe = Axe(30, True, False, 999999999999999999999999999999999999, "Ancient Axe")


class Gun(Weapon):
    def __init__(self, name="", ammo=10, attack_stat=10, price=0):
        super(Gun, self).__init__(name)
        self.ammo = ammo
        self.reeeeee = ammo
        self.grabbed = False
        self.attack_stat = attack_stat
        self.grabbed = False
        self.price = price

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Attack: %s" % self.attack_stat)

    def shoot(self):
        if self.grabbed:
            print("You shoot your weapon, you lose a bullet")
            self.ammo -= 1

    def reload(self):
        if self.grabbed:
            print("You reload your weapon")
            self.ammo = self.reeeeee

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)


Unnamed_gun = Gun("Unnamed Gun", 10, 10, 20)


class Splattershot(Gun):
    def __init__(self, name, ammo=200, attack_stat=0, price=0):
        super(Splattershot, self).__init__("", 200)
        self.ammo = ammo
        self.reeeeee = ammo
        self.grabbed = False
        self.name = name
        self.attack_stat = attack_stat
        self.price = price

    def shoot(self):
        if self.grabbed:
            print("You shoot your weapon, you lose some ink")
            self.ammo -= 5


Splattershot_Jr = Splattershot('Splattershot Jr', 200, 15, 400)

Splattershot_Pro = Splattershot("Splattershot Pro", 250, 20, 600)

Hero_Shot = Splattershot("Hero Shot", 400, 40)


class Consumables(object):
    def __init__(self, name=""):
        self.name = name
        self.grabbed = False

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)


class Health(Consumables):
    def __init__(self, name="", restore1=20):
        super(Health, self).__init__("")
        self.name = name
        self.restore = restore1

    def use(self):
        if self.grabbed:

            if player.health + self.restore <= player.max_health:
                player.health += self.restore
                print("You eat the %s, and restore %i health" % (self.name, self.restore))
            elif player.health + self.restore > player.max_health:
                print("You eat the %s and your health is maxed out" % self.name)
                player.health = player.max_health

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s health" % self.restore)


class Saturday(Health):
    def __init__(self, name="", restore=0):
        super(Saturday, self).__init__(name, restore)
        self.name = name
        self.restore = restore

    def use(self):
        print("You attend the Saturday Practice exam and take a full practice test complete with FRQs. Not to mention"
              "\n you also had some very tasty donuts. Your health is fully restored.")
        player.health = player.max_health
        player.inventory.remove(self)


class Practice(Health):
    def __init__(self, name=""):
        super(Practice, self).__init__(name)
        self.name = name
        self.factor = 0.5 * player.max_health
    
    def use(self):
        print("You take a full multiple choice test by yourself. This makes you feel more alive than ever and you are"
              "excited to continue on with your quest. Your health is healed by half.")
        player.health += self.factor
        player.inventory.remove(self)


class Quiz(Health):
    def __init__(self, name="", restore=0):
        super(Quiz, self).__init__(name, restore)
        self.name = name
        self.restore = restore

    def use(self):
        print("You spend 20 minutes playing a game on you phone to study for the test. You are healed by %d" %
              self.restore)
        player.inventory.remove(self)
        player.health += self.restore


class Vocab(Health):
    def __init__(self, name="", restore=0, amount=0):
        super(Vocab, self).__init__(name, restore)
        self.name = name
        self.restore = restore
        self.amount = amount
        self.heal = self.restore * self.amount
        self.lose = random.randint(0, self.amount)

    def use(self):
        print("You study with your vocab cards, learning the intense vocabulary of human geography. Each flip of the"
              " card brings you new knowledge\n that healths your damaged soul by %d each." % self.restore)
        player.health += self.heal
        if self.lose > 0:
            print("However, you dropped and lost %d cards" % self.lose)
            self.amount -= self.lose
        else:
            print("You managed to not be a clumsy idiot and you kept all of your vocab cards. Good job.")


class Potion1(Health):
    def __init__(self, restore2=20, name="", price=0):
        super(Potion1, self).__init__("", 20)
        self.restore = restore2
        self.name = name
        self.price = price

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s health" % self.restore)

    def use(self):
        if self.grabbed:
            if player.health + self.restore <= player.max_health:
                player.health += self.restore
                print("You drink the %s, and restore %i health" % (self.name, self.restore))
            else:
                print("You drink the %s and your health is maxed out" % self.name)
                player.health = player.max_health


class Eat1(Health):
    def __init__(self, restore=30, name="", price=0):
        super(Eat1, self).__init__()
        self.restore = restore
        self.name = name
        self.price = price
        self.grabbed = False

    def check(self):
        if self.grabbed:

            print(self.name)
            print("Restores %s hunger" % self.restore)

    def use(self):
        if self.grabbed:
            if player.hunger + self.restore <= 50:
                player.hunger += self.restore
                print("You eat the %s, and restore %i hunger" % (self.name, self.restore))
            else:
                print("You eat the %s and you are full" % self.name)
                player.hunger = 50


class Foood(Health):
    def __init__(self, restore=30, name="", price=0):
        super(Foood, self).__init__()
        self.restore = restore
        self.name = name
        self.price = price
        self.grabbed = False

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s hunger" % self.restore)

    def use(self):
        if self.grabbed:
            if player.hunger + self.restore <= 50:
                player.hunger += self.restore
                print("You eat the %s, and restore %i hunger" % (self.name, self.restore))
            else:
                print("You eat the %s and you are full" % self.name)
                player.hunger = 50


rage_candy = Eat1(20, "Rage Candy Bar", 20)

Maize = Foood(15, "Maize", 20)

Borger = Foood(25, "Beef", 40)

Carrot = Foood(10, "Carrot", 10)

C_candy = Foood(18, "Chocolate", 20)

Pork = Foood(25, "Pork", 20)

fruit = Eat1(9999999999999999999999999999999999999, "Hearty Simmered Fruit", 70)

sandwich = Eat1(45, "Crusty Seanwich", 50)

tomato = Eat1(9999999999999999999999999999999999999999999999999999999, "Maximum Tomato", 70)


class MP(Consumables):
    def __init__(self, name="", restore1=20):
        super(MP, self).__init__("")
        self.name = name
        self.restore = restore1

    def use(self):
        if self.grabbed:

            if player.MP + self.restore <= player.MP:
                player.MP += self.restore
                print("You eat the %s, and restore %i MP" % (self.name, self.restore))
            elif player.MP + self.restore > player.MP:
                print("You eat the %s and your MP is maxed out" % self.name)
                player.MP = player.max_MP

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.name)
            self.grabbed = False
            Inventory.inventory.remove(self)

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s MP" % self.restore)


class Potion2(MP):
    def __init__(self, restore2=20, name="", price=0):
        super(Potion2, self).__init__("", 20)
        self.restore = restore2
        self.name = name
        self.grabbed = False
        self.price = price

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s MP" % self.restore)

    def use(self):
        if self.grabbed:
            if player.MP + self.restore <= player.max_MP:
                player.MP += self.restore
                print("You drink the %s, and restore %i MP" % (self.name, self.restore))
            else:
                print("You drink the %s and your MP is maxed out" % self.name)
                player.MP = player.max_MP


class Eat2(MP):
    def __init__(self, restore=30, name="", price=0):
        super(Eat2, self).__init__()
        self.restore = restore
        self.name = name
        self.price = price
        self.grabbed = False

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s MP" % self.restore)


class ALL(Consumables):
    def __init__(self, health, mp, name):
        super(ALL, self).__init__("")
        self.restore1 = health
        self.restore2 = mp
        self.name = name

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s MP and %s HP" % (self.restore2, self.restore1))

    def use(self):
        if self.grabbed:
            if player.MP + self.restore2 <= player.max_MP:
                player.MP += self.restore2
                print("You eat the %s, and restore %i MP" % (self.name, self.restore2))
            elif player.MP + self.restore2 > player.max_MP:
                print("You eat the %s and your MP is maxed out" % self.name)
                player.MP = player.max_MP
            if player.health + self.restore1 <= player.max_health:
                player.health += self.restore1
                print("You eat the %s, and restore %i HP" % (self.name, self.restore1))
            elif player.health + self.restore1 > player.max_health:
                print("You eat the %s and your HP is maxed out" % self.name)
                player.health = player.max_health


candy = Eat2(100000000000, "Rare Candy", 100)

Green_Potion = Potion2(25, "Green Potion", 20)

super_mushroom = Eat2(10, "Super Mushroom", 30)

red_potion = Potion1(50, "Red Potion", 40)

candy2 = Eat2(40, "MP Candy", 15)

void = ALL(999999999999999999999, 99999999999999999999999999, "Void Candy")

cake = ALL(64, 64, "Princess Peach's Cake")

undershirt = Chestplate(0, "Undershirt")

underwear = Leggings(0, "Underwear")

frost_helmet = Helmet(5, "Frost Helmet")

Cape = Chestplate(15, "Hero Cape replica + Hero Jacket replica")

scuba = Helmet(2, "Strange Scuba Mask", 35)

space = Helmet(4, "Space Helmet", 30)

ancient1 = Leggings(10, "Ancient Leggings", 67)

ancient2 = Boots(5, "Ancient Boots", 40)

desert_helmet = Helmet(6, "Golden Helmet", 50)

ancient3 = Chestplate(13, "Ancient Chestplate", 85)

ancient4 = Helmet(7, "Ancient Helmet", 20)

lava = Leggings(8, "Lava Leggings", 41)

lava2 = Boots(3, "Lava Boots", 26)

light = Boots(4, "Light Boots")

light2 = Leggings(9, "Light Leggings")

light3 = Helmet(6, "Light Helmet")

light4 = Chestplate(11, "Light Chestplate")


class Inroomrestore(object):
    def __init__(self, restore=20):
        self.restore = restore
        self.name = "An enormous pile of many meats, vegetables, fruit, deserts, and other foods"

    def use(self):
        if player.health + self.restore <= player.max_health:
            player.health += self.restore
            print("You eat some of the food in the room and restore 20 HP")
        else:
            player.health = player.max_health
            print("You eat some of the food in the room and your HP is maxed out")


foods = Inroomrestore()


class Healthupgrade(object):
    def __init__(self, upgrade=10, price=0, name=""):
        self.activated = False
        self.upgrade = upgrade
        self.price = price
        self.name = name

    def grab(self):
        self.activated = True
        if self.activated:
            print("You use the health upgrade and your HP gets maxed out."
                  "\n Your HP is also increased by %i" % self.upgrade)
            player.max_health += self.upgrade
            player.health = player.max_health


upgrade3 = Healthupgrade(15, 50, "Health Upgrade")


Wooden_Sword.grabbed = True

paper1.grabbed = True

paper2.grabbed = True

paper3.grabbed = True


class Filler(object):
    def __init__(self, name="", price=0):
        self.name = name
        self.grabbed = False
        self.price = price

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)

    def drop(self):
        if self in Inventory.inventory:
            Inventory.inventory.remove(self)
            print("You forever parted ways with the %s."
                  "\nYou can never retrieve it, it vanishes as soon as it hits the ground"
                  "\nGoodbye %s" % (self.name, self.name))


class Filler2(object):
    def __init__(self, name="", price=0):
        self.name = name
        self.grabbed = False
        self.price = price

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.name)
                self.grabbed = True
                Inventory.inventory.append(self)

    def drop(self):
        if self in Inventory.inventory:
            Inventory.inventory.remove(self)
            print("You dropped the %s" % self.name)


CG = Gun("Coconut Gun", 30)

Egg = Filler("EGG")

Briefcase = Filler("Locked Briefcase")

Melee = Filler("Unopened Copy of Smash Bros Melee")

egg2 = Filler("EGG 2: ELECTRIC BOOGALOO")

A_3 = NPC("Agent 3", 99999999999999999, 99999999999999999999999999999999999999999999999, 99999999999999, False,
          "You're pretty powerful. I've never been beaten before, the only other time I was beaten was "
          "\nonly when someone thought of a hole in my attack pattern.")

A_3.items.append(Hero_Shot)

A_3.items.append(Cape)

NPC1 = NPC("Greg", 10, 1, 20, False, "Hello there sir. How are you?")

NPC1.items.append(Egg)

NPC2 = NPC("Egg Vendor", 900, 20, 9999999999, False, "May I offer you an egg in these trying times?")

NPC2.items.append(egg2)

NPC3 = NPC("Johnny", 1, 0, 1, False, "Hello, my name is Johnny.")

NPC4 = NPC("Bob", 35, 15, 99999,  False, "Hi, I'm Bob")

NPC5 = NPC("Jim", 20, 8, 100, False, "Hello, my name is Jim")

NPC7 = NPC("Jack Handey", 99, 20, 1000, False, "Would you like to here some deep thoughts?")

NPC7.items.append(Book)

dog = NPC("Dog", 20, 5, 0, False, "Bark Bark!")


NPC8 = NPC("Sarah", 99, 20, 800, False, "Hello")

NPC9 = NPC('Cheyanne', 10, 10, 10, False, "Hello there, I'm from Wyoming")

NPC10 = NPC("Zo R. Kuh", 70,  20, 1980, False, "Hey there, I was named after some text based game, those things are "
                                               "boring. "
                                               "\nWhy would anyone play one??? (please don't quit playing now)")


class Enemy(Character):
    def __init__(self, weapon=None, health=0, can_ink=False, elecfrost=False, can_weapon=True, name="", defense=0,
                 mon=0):
        super(Enemy, self).__init__(weapon, None, health, name, False, mon)
        self.only_ink = can_ink
        self.elecfrost = elecfrost
        self.no_weapon = can_weapon
        self.defense = defense

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.attack_stat))
        if not target.inked:
            target.take_damage(self.weapon.attack_stat)
        else:
            target.take_damage(self.weapon.attack_stat * 2)
        if self.weapon.__class__ is Splattershot:
            target.inked = True
            print("You have been inked and attacks now do double damage")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if not self.elecfrost:
                if player.MP >= 5:
                    print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                    self.health -= 20
                    player.MP -= 5
                    if self.health < 0:
                        self.health = 0
                        print("%s has been defeated!" % self.name)
                        player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("You do not have enough MP to cast this")
            else:
                print("You cannot damage this enemy with fire")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by Physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")

        elif self.only_ink:
            if player.weapon.__class__ is Splattershot:
                if damage < self.defense:
                    print("No damage was taken!")
                else:
                    self.health -= damage - self.defense
                    if self.health < 0:
                        self.health = 0
                        print("%s has been defeated!" % self.name)
                        player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


foot = Sword(2, True, False, 9999999999999999999999999999, "")

shell = Sword(5, True, False, 9999999999999999999999999999, "")

parasol = Sword(18, True, False, 9999999999999999999999999999, "")

Iron_Blade = Sword(15, True, False, 9999999999999999999999999, "")

Claw = Sword(20, True, False, 999999999999, "")

Claw2 = Sword(15, True, False, 99999999999999, "")

goomba = Enemy(foot, 5, False, False, True, "Goomba", 2, 15)
Koopa = Enemy(shell, 10, False, False, True, "Koopa Troopa", 6, 25)
Spiny = Enemy(shell, 14, False, False, True, "Spiny", 8, 40)

Bokkoblin = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9, 60)
Bokkoblin2 = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9, 65)
Bokkoblin3 = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9, 70)

Frosty = Enemy(F_Sword, 30, False, False, True, "Mr. Frosty", 12, 89)

Dee = Enemy(parasol, 20, False, False, True, "Big Waddle Dee", 10, 99)

G_Knights = Enemy(E_Sword, 25, False, False, True, "Galactic Knights", 12, 100)

Lizalfos = Enemy(Iron_Blade, 20, False, False, True, "Lizalfos", 10, 116)
Lizalfos2 = Enemy(Iron_Blade, 20, False, False, True, "Lizalfos", 10, 106)

Dynablade = Enemy(Claw2, 45, False, False, True, "Dynablade", 15, 130)

caterkiller = Enemy(Iron_Blade, 25, False, False, True, "Giant Caterkiller", 12, 60)


class Keyboard(object):
    def __init__(self, solution=""):
        self.solution = solution
        self.solv = ""

    def solve(self):
        self.solv = input("What is the answer?")
        if self.solv.lower() == self.solution:
            print("Correct!")
            # NOVA4.east = 'NOVA7'
            # NOVA4.description = "You have solved the riddle needed to progress" \
            #                     "\n You can go east or you can go south"
        else:
            print("Incorrect! The wall that blocks your path is still here")


marx_board = Keyboard("socialism")


class Keyboard2(object):
    def __init__(self, solution=""):
        self.solution = solution
        self.solv = ""

    def solve(self):
        self.solv = input("What is the answer?")
        if self.solv.lower() == self.solution:
            print()
        else:
            print("WRONG!!! PREPARE FOR THE DRAINING OF YOUR LIFE FORCE")
            player.health -= player.health


sub_board = Keyboard2("mewtwo")

temple_bot = NPC("Shopkeeper bot model NX HAC serial no 84493587", 99999999999999, 0, 0, True)
forest_directions = Filler("UP, UP, DOWN, DOWN, LEFT, RIGHT, LEFT, RIGHT"
                           "\nKEY: UP = NORTH, DOWN = SOUTH, LEFT = WEST, RIGHT = EAST", 0)
zork_mat = Filler("Battered Rubber Mat that reads 'WELCOME TO ZORK'", 1)
rock = NPC("Stone Tablet", 0, 0, 0, True)

temple_bot.items.append(E_Sword)
temple_bot.items.append(Unnamed_gun)
temple_bot.items.append(ancient1)
temple_bot.items.append(ancient2)
temple_bot.items.append(ancient3)
temple_bot.items.append(ancient4)
temple_bot.items.append(forest_directions)

rock.items.append(lava)
rock.items.append(lava2)
rock.items.append(space)
rock.items.append(upgrade3)
rock.items.append(Fire)


class Boss(Enemy):
    def __init__(self, weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon):
        super(Boss, self).__init__(weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon)
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)


class Vonthanos(Boss):
    def __init__(self):
        super(Vonthanos, self).__init__(Claw, 75, False, False, True, "Von Thanos", 5, 1500)
        self.name = "Von Thanos"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Von Thanos attacks you with his weird Infinity Gauntlet, but he misses")
            else:
                print("Von Thanos attacks you for %i with his weird Infinity Gauntlet!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Von Thanos uses the forestry ring in his Infinity Gauntlet to "
                      "launch you into the air by making a tree appear beneath you")
                target.take_damage(30)
            else:
                print("Von Thanos tries to use aring in his gauntlet... but fails!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Von Thanos uses the dairy ring in his Gauntlet and he throws a giant cow at you")
                target.take_damage(28)
            else:
                print("Von Thanos uses the dairy ring in his Gauntlet and he throws a giant cow at you but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Bowser grows in size for one quick attack!")
                target.take_damage(25)
            else:
                print("Bowser attacks but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Bowser breathes a large amount of fire to attack you")
                target.take_damage(27)
            else:
                print("Bowser breathes fire in your direction but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Bowser charges at you")
                target.take_damage(22)
            else:
                print("Bowser charges at you but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Bowser winds up a large punch and hits you")
                target.take_damage(30)
            else:
                print("Bowser tries to punch you but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 30
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 30
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


class Test1(Boss):
    def __init__(self):
        super(Test1, self).__init__(Claw, 60, False, False, True, "Test1", 7, 1500)
        self.name = "Test1"
        self.answers = ''

    def attack(self, target):
        self.attack_choice = random.randint(1, 5)
        if self.attack_choice == 1:
            print("Geography is about ____ and why and History is about when and why")
            self.answers = input('')
            if self.answers.lower() == "where":
                print(colored('Correct! You take no damage!', 'green'))
            else:
                print(colored("Wrong! You take 25 damage!", 'red'))
                player.take_damage(25)
        elif self.attack_choice == 2:
            print("What projection minimizes distortion?")
            self.answers = input('')
            if self.answers.lower() in ["goode homosline", 'goode homosline projection']:
                print(colored('Correct! You take no damage!', 'green'))
            else:
                print(colored("Wrong! You take 28 damage!", 'red'))
                player.take_damage(28)
        elif self.attack_choice == 3:
            print("What type of region is the area of influence of a TV station?")
            self.answers = input('')
            if self.answers.lower() in ["functional region", 'functional', 'nodal region', 'nodal']:
                print(colored('Correct! You take no damage!', 'green'))
            else:
                print(colored("Wrong! You take 25 damage!", 'red'))
                player.take_damage(25)
        elif self.attack_choice == 4:
            print("What type of region is the area of influence of a TV station?")
            self.answers = input('')
            if self.answers.lower() in ["functional region", 'functional', 'nodal region', 'nodal']:
                print(colored('Correct! You take no damage!', 'green'))
            else:
                print(colored("Wrong! You take 25 damage!", 'red'))
                player.take_damage(25)
        elif self.attack_choice == 5:
            print("What makes an ecosystem unsustainable?")
            self.answers = input('')
            if self.answers.lower() in ["inefficient resource use", 'using more resources than can be replenished']:
                print(colored('Correct! You take no damage!', 'green'))
            else:
                print(colored("Wrong! You take 25 damage!", 'red'))
                player.take_damage(25)

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 30
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 30
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 30
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


class Wiebe(Boss):
    def __init__(self):
        super(Wiebe, self).__init__(None, 100, False, False, True, "Mr. Wiebe", 12, 99999999)
        self.name = "Mr. Wiebe"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Wiebe tries to run code that would damage you, but it fails!")
            else:
                print("Wiebe runs target.take_damage(40)")
                target.take_damage(40)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Wiebe runs self.health += 22")
                self.health += 22
            else:
                print("Wiebe runs self.Health += 22, but it glitches and failes!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Wiebe runs target.take_damage(50)!")
                target.take_damage(50)
            else:
                print("Wiebe runs target.take_damage(50, but forgetting to close the parentheses causes the code to"
                      " break")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6 or 7 or 8 or 1 or 2 or 3 or 9 or 10 or 11:
                print("Wiebe shuts off the computer, deleting all of your progress")
                target.take_damage(99999999999999999999999999999999999999999999999999999999999999999999999)
            else:
                print("Wiebe tries to shut off the computer, but it just went into sleep mode")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Wiebe attacks you with a firewall")
                target.take_damage(47)
            else:
                print("Wiebe tries to attack you with a firewall, but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Wiebe launches out a barrage of code at you!")
                target.take_damage(52)
            else:
                print("Wiebe launches out a barrage of code at you, but misses!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 4 or 5 or 6 or 7 or 8 or 1 or 2 or 3 or 9 or 10 or 11:
                print("Wiebe ran code that healed all of his health")
                self.health = 100
            else:
                print("Wiebe tries to run code that heals all of his health... but it failed!")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("Wiebe has retreated!")
                    player.money += self.money
                    player.health = player.max_health
                print("%s has %d 'health' left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("Wiebe has retreated!")
                    print("%s has %d 'health' left" % (self.name, self.health))
                    player.money += self.money
                    player.health = player.max_health
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("Wiebe has retreated!")
                    player.money += self.money
                    player.health = player.max_health
                print("%s has %d 'health' left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("Wiebe has retreated!")
                            player.money += self.money
                            player.health = player.max_health
                    print("%s has %d 'health' left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("Wiebe has retreated!")
                            player.money += self.money
                            player.health = player.max_health
                    print("%s has %d 'health' left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("Wiebe has retreated!")
                            player.money += self.money
                    print("%s has %d 'health' left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


wiebe = Wiebe()

bowser = Bowser()

spider_leg = Sword(9, True, False, 9999999999999999999, "")


class Donkeykong(Boss):
    def __init__(self):
        super(Donkeykong, self).__init__(None, 100, False, False, True, "Donkey Kong", 9, 1500)
        self.name = "Donkey Kong"
        self.anger = 0

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Donkey Kong tries to hit you with a giant punch!!")
            else:
                print("Donkey Kong hits you with a giant punch!")
                if self.anger == 0:
                    target.take_damage(43)
                else:
                    target.take_damage(50)
                    self.anger -= 1
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("DK shoots at you with his coconut gun! It fired in spurts, he shot you! That's gonna hurt!")
                if self.anger == 0:
                    target.take_damage(39)
                else:
                    target.take_damage(46)
                    self.anger -= 1
            else:
                print("DK shoots at you with his coconut gun! It fired in spurts, he misses you! That would've hurt!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("DK kicked you in the face with a giant kick that sent you flying!")
                if self.anger == 0:
                    target.take_damage(41)
                else:
                    target.take_damage(48)
                    self.anger -= 1
            else:
                print("DK tried to hit you with a very powerful kick!")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("DK launches a barrage of punches with one final uppercut that sends you flying into the air!")
                if self.anger == 0:
                    target.take_damage(49)
                else:
                    target.take_damage(56)
            else:
                print("DK tries to hit you with a powerful barrage of punches, but they miss!")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9 or 1 or 3:
                if self.anger == 0:
                    print("DK plays a strange melody on the bongos! DK's next attack will be more powerful!")
                    self.anger = 1
                else:
                    print("DK plays a strange melody on the bongos! DK's next 2 attacks will be more powerful!")
                    self.anger = 2
            else:
                print("DK plays a strange melody on the bongos, based on DK's angry yet sad expression tells you that "
                      "\nwhatever he tried to do with that failed")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("DK grabs a big banana and then eats it with a happy expression on his face")
                if self.anger == 0:
                    if self.health + 40 <= 100:
                        self.health += 30
                        print("DK restores 30 HP")
                        print("DK now has %i HP" % self.health)
                    elif self.health + 30 > 100:
                        self.health = 100
                        print("DK maxes out his health")
                        print("DK has 100 HP again")
                else:
                    if self.health + 40 <= 100:
                        self.health += 40
                        print("DK restores 40 HP")
                        print("DK now has %i HP" % self.health)
                        self.anger -= 1
                    elif self.health + 40 > 100:
                        self.health = 100
                        print("DK maxes out his health")
                        print("DK has 100 HP again")
                        self.anger -= 1
            else:
                if self.anger == 0:
                    print("DK starts to eat a banana, but you quickly knock the banana out of his hands."
                          "\n This makes DK angry, powering up his next attack")
                    self.anger = 1
                else:
                    print("DK starts to eat a banana, but you quickly knock the banana out of his hands."
                          "\n This makes DK angry, powering up his next 2 attacks")
                    self.anger = 2
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("DK slams his hands against the ground creating a shockwave on the ground that damages you")
                if self.anger == 0:
                    target.take_damage(40)
                else:
                    target.take_damage(47)
                    self.anger -= 1
            else:
                print("DK slams his hands against the ground creating a shockwave on the ground that you jump over")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


DK = Donkeykong()


class Gohma(Boss):
    def __init__(self, name="Gohma"):
        super(Gohma, self).__init__(spider_leg, 45, False, False, False, name, 8, 1000)
        self.name = "Gohma"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Gohma attacks with its legs! But it misses!")
            else:
                print("Gohma attacks for %d damage with its legs!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Gohma attacks with a laser from its eye")
                target.take_damage(14)
            else:
                print("Gohma tries to hit you with a laser from its eye but misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Gohma bites you!")
                target.take_damage(17)
            else:
                print("Gohma tries to bite you but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Gohma launches a harmful web at you")
                target.take_damage(24)
            else:
                print("Gohma launches a powerful web at you but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Gohma tries to stomp on you")
                target.take_damage(14)
            else:
                print("Gohma tries to stomp on you but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Gohma charges at you")
                target.take_damage(13)
            else:
                print("Gohma charges at you but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Gohma launches a sweeping attack with its legs and hits you")
                target.take_damage(12)
            else:
                print("Gohma launches a sweeping attack with its legs but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_MP += 35
                    player.MP = player.max_MP
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_MP += 35
                    player.MP = player.max_MP
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_MP += 35
                    player.MP = player.max_MP
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if player.weapon.__class__ is Splattershot:
            self.inked = True
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 35
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 35
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 35
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


gohma = Gohma()


class Chaos(Boss):
    def __init__(self, name="Chaos 0"):
        super(Chaos, self).__init__(Claw, 75, False, True, False, name, 9, 2000)
        self.name = "Chaos 0"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Chaos extends out its claws to attack! But it misses!")
            else:
                print("Chaos attacks for %d with its watery claws!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Chaos turns into a shark and attacks you!")
                target.take_damage(50)
            else:
                print("Choas turns into a shark, tries to attack you, but misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Chaos launches some sort of energy blast")
                target.take_damage(46)
            else:
                print("Chaos launches some sort of energy blast, but misses!")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Choas turns into a giant monster and launches a massive laser at you")
                target.take_damage(67)
            else:
                print("Choas turns into a giant monster and launches a massive laser at you, but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Chaos grows in size and punches you")
                target.take_damage(40)
            else:
                print("Chaos attacks, but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Chaos glides into you")
                target.take_damage(25)
            else:
                print("Chaos tries to glide into you but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Chaos stretches his arms out to punch you")
                target.take_damage(39)
            else:
                print("Chaos stretches his arms out to punch you but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.weapon.attack_stat += 7
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.weapon.attack_stat += 7
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.weapon.attack_stat += 7
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 7
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by Physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 7
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 7
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


chaos0 = Chaos()

metal = Sword(29, True, False, 9999999999999999, "")


class Metalmario(Boss):
    def __init__(self, name="Metal Mario"):
        super(Metalmario, self).__init__(metal, 85, False, False, True, name, 13, 6464)
        self.name = "Metal Mario"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Metal Mario punches you but misses")
            else:
                print("Metal Mario attacks for %d with his fists!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Metal Mario hits you with a forward ariel!")
                target.take_damage(30)
            else:
                print("Metal Mario tries to hit you with a forward ariel, but misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Metal Mario spins into you")
                target.take_damage(26)
            else:
                print("Metal Mario tries to spin into you but misses!")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Metal Mario uses his Super Jump Punch!")
                target.take_damage(37)
            else:
                print("Metal Mario uses his Super Jump Punch, but misses!")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Metal Mario launches a fireball at you!")
                target.take_damage(40)
            else:
                print("Metal Mario launches a fireball at you, but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Metal Mario slides into you!")
                target.take_damage(25)
            else:
                print("Metal Mario tries to slide into you, but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Metal Mario charges and launches a Smash attack")
                target.take_damage(33)
            else:
                print("Metal Mario charges and launches a Smash attack but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.chestplate.defense += 10
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.chestplate.defense += 10
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.chestplate.defense += 10
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.chestplate.defense += 10
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by Physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.chestplate.defense += 10
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.chestplate.defense += 10
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


m_mario = Metalmario()

Claw3 = Blade(47)


class Dbowser(Boss):
    def __init__(self):
        super(Dbowser, self).__init__(Claw, 100, False, False, True, "Dark Bowser", 9, 2008)
        self.name = "Dark Bowser"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Dark Bowser attacks with his claws! But he misses!")
            else:
                print("Dark Bowser attacks for %d with his claws!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Dark Bowser attacks with a fireball!")
                target.take_damage(38)
            else:
                print("Dark Bowser attacks with a fireball but misses!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Dark Bowser attacks with his shell!")
                target.take_damage(32)
            else:
                print("Dark Bowser attacks with his shell but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Dark Bowser grows in size for one quick attack!")
                target.take_damage(51)
            else:
                print("Bowser attacks but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Bowser breathes a large amount of fire to attack you")
                target.take_damage(41)
            else:
                print("Bowser breathes fire in your direction but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Bowser charges at you")
                target.take_damage(32)
            else:
                print("Bowser charges at you but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Bowser winds up a large punch and hits you")
                target.take_damage(39)
            else:
                print("Bowser tries to punch you but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 40
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_health += 40
                    player.health = player.max_health
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 40
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 40
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 40
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 40
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


d_bowser = Dbowser()

d_m_sword = Blade(37)


class Darklink(Boss):
    def __init__(self):
        super(Darklink, self).__init__(d_m_sword, 90, False, False, True, "Dark Link", 11, 3059)
        self.name = "Dark Link"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Dark Link attacks with his sword! But he misses!")
            else:
                print("Dark Link attacks for %d with his sword!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Dark Link attacks with a sword beam!")
                target.take_damage(15)
            else:
                print("Dark Link attacks with a sword beam but misses!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Dark Link attacks with a Fire Arrow from his bow!")
                target.take_damage(F_Sword.attack_stat)
            else:
                print("Dark Link attacks with a Fire Arrow from his bow but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Dark Link unleashes a series of quick slashes and then hits you with one final powerful slash")
                target.take_damage(64)
            else:
                print("Dark Link unleashes a series of quick slashes and then misses with one final slash, "
                      "\nhowever he still grazed you with some other slashes")
                target.take_damage(12)
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Dark Link uses a spin attack!")
                target.take_damage(27)
            else:
                print("Dark Link uses a spin attack but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Dark Link charges at you with his sword")
                target.take_damage(22)
            else:
                print("Dark Link charges at you with his sword but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Dark Link hits you with an Ice Arrow")
                target.take_damage(F_Sword.attack_stat)
            else:
                print("Dark Link tries to hit you with an Ice Arrow but misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


dark_link = Darklink()


class Marx(Boss):
    def __init__(self):
        super(Marx, self).__init__(None, 100, False, False, True, "Karl Marx", 12, 9298)
        self.name = "Karl Marx"
        self.Q1 = ""
        self.Q2 = ''
        self. Q3 = ''
        self. Q4 = ''
        self.Q5 = ''

    def attack(self, target):
        self.attack_choice = random.randint(1, 5)
        if self.attack_choice == 1:
            self.Q1 = input("")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_MP += 40
                    player.MP = player.max_MP
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_MP += 40
                    player.MP = player.max_MP
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_MP += 40
                    player.MP = player.max_MP
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 40
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 40
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_MP += 40
                            player.MP = player.max_MP
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


marx = Marx()


class Dj(Boss):
    def __init__(self):
        super(Dj, self).__init__(None, 88, True, False, False, "DJ Octavio", 10, 2015)
        self.name = "DJ Octavio"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("DJ Octavio launches out a punch from his mech, but he misses")
            else:
                print("DJ Octavio launches out a punch from his mech and hits you"
                      "\n This attack has now covered you in purple ink")
                target.inked = True
                target.take_damage(20)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3 or 5:
                print("DJ Octavio launches a spinning punch at you!"
                      "\n This attack has now covered you in purple ink")
                target.inked = True
                target.take_damage(25)
            else:
                print("DJ Octavio launches a spinning punch at you but misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1 or 2:
                print("DJ Octavio drops a shower of ink down from his mech and dashes towards you")
                target.inked = True
                target.take_damage(22)
            else:
                print("DJ Octavio drops a shower of ink down from his mech and dashes towards you but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6 or 7:
                print("DJ Octavio uses a Killer Wail special!")
                target.inked = True
                target.take_damage(38)
            else:
                print("DJ Octavio uses a Killer Wail special but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("DJ Octavio launches a missile barage at you")
                target.inked = True
                target.take_damage(20)
            else:
                print("DJ Octavio barages you with missiles, but you somehow dodge all of them")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10 or 3:
                print("DJ Octavio launches a giant strange mechanical eye at you")
                target.inked = True
                target.take_damage(23)
            else:
                print("DJ Octavio launches a giant strange mechanical eye at you, but he misses!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11:
                print("DJ Octavio launches out a bomb rush!")
                target.inked = True
                target.take_damage(17)
            else:
                print("DJ Octavio launches out a bomb rush, but he misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 45
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.max_health += 45
                    player.health = player.max_health
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.max_health += 45
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 45
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")
            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.max_health += 45
                            player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
        elif self.only_ink:
            if player.weapon.__class__ is Splattershot:
                if damage < self.defense:
                    print("No damage was taken!")
                else:
                    self.health -= damage - self.defense
                    if self.health < 0:
                        self.health = 0
                        print("%s has been defeated!" % self.name)
                        player.money += self.money
                        player.max_health += 45
                        player.health = player.max_health
                    print("%s has %d health left" % (self.name, self.health))
            else:
                print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


octavio = Dj()

Lance = Sword(60, False, True, 999999999999, "Galacta Knight's Lance")


class Galactaknight(Boss):
    def __init__(self):
        super(Galactaknight, self).__init__(Lance, 66, False, False, True, "Galacta Knight", 11, 2008)
        self.name = "Galacta Knight"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Galacta Knight tries to hit you with his shield, but he misses")
            else:
                print("Galacta Knight bashes you with his shield")
                target.take_damage(25)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Galacta Knight slashes at you with his lance")
                target.take_damage(39)
            else:
                print("Galacta Knight slashes at you with his lance but you nearly dodge it"
                      "\n(You are still grazed by the attack)")
                target.take_damage(10)
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Galacta Knight stabs his lance into the ground a fire rises from the ground")
                target.take_damage(37)
            else:
                print("Galacta Knight stabs his lance into the ground a fire rises from the ground but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6 or 7:
                print("Galacta Knight uses his lance to cut a hole in the space time continuum and uses that to shoot "
                      "a massive laser at you")
                target.take_damage(57)
            else:
                print("Galacta Knight uses his lance to cut a hole in the space time continum and uses that to shout a "
                      "massive laser at you but he misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Galacta Knight raises his lance into the air and strikes you with lightning")
                target.take_damage(30)
            else:
                print("Galacta Knight raises his lance into the air and and nearly strikes you with lightning")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10 or 3:
                print("Galacta Knight raises his lance into the air and sword beams rain down upon you")
                target.take_damage(43)
            else:
                print("Galacta Knight raises his lance into the air and sword beams rain down, but you dodge them.")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11:
                print("Galacta Knight spins into a tornado and rams into you")
                target.take_damage(17)
            else:
                print("Galacta Knight spins into a tornado and tries to ram into you but he misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


galacta_knight = Galactaknight()


class Red(Boss):
    def __init__(self):
        super(Red, self).__init__(None, 60, False, False, True, "Pokemon Trainer Red", 12, 9451)
        self.name = "Pokemon Trainer Red"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Red sends out his Charizard who uses flamethrower on you, but it misses!")
            else:
                print("Red sends out his Charizard who uses flamethrower on you")
                target.take_damage(36)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Red's Venusaur uses Solar Beam on you")
                target.take_damage(34)
            else:
                print("Red's Venusaur uses Solar Beam on you but it misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Red's Blastoise used Hydro Pump on you")
                target.take_damage(35)
            else:
                print("Red's Blastoise tried to use Hydro Pump on you but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6 or 7:
                print("Red sends out his Charizard, Venusaur, and Blastoise out and uses Triple Finish!")
                target.take_damage(47)
            else:
                print("Red sends out his Charizard, Venusaur, and Blastoise out and uses Triple Finish but they miss")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Red's Pikachu used Volt Tackle on you! It does big damage but also hurts itself a little")
                target.take_damage(46)
                self.health -= 5
                if self.health <= 0:
                    print("Red was defeated!")
                    player.money += self.money
            else:
                print("Red's Pikachu used Volt Tackle on you, but it misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10 or 3 or 12:
                print("Red's Mewtwo used Psystrike on you!")
                target.take_damage(47)
            else:
                print("Red's Mewtwo used Psystrike on you, but it misses!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11:
                print("Red's Snorlax uses Giga Impact on you!")
                target.take_damage(36)
            else:
                print("Red's Snorlax uses Giga Impact on you but it misses")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("You defeated all of Red's Pokemon!")
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("You defeated all of Red's Pokemon!")
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("You defeated all of Red's Pokemon!")
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("You defeated all of Red's Pokemon!")
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("You defeated all of Red's Pokemon!")
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("You defeated all of Red's Pokemon!")
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


red = Red()


class Duon(Boss):
    def __init__(self):
        super(Duon, self).__init__(None, 75, False, False, True, "Duon", 10, 2451)
        self.name = "Duon"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Duon slashes at you with its sword-like claws, but it misses!")
            else:
                print("Duon slashes at you with its sword-like claws!")
                target.take_damage(39)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Duon launches out lasers at you!")
                target.take_damage(39)
            else:
                print("Duon launches out lasers at you but it misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Duon charges at you and rams into you")
                target.take_damage(36)
            else:
                print("Duon charges at you but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5:
                print("Duon slashes at you with a giant axe on its head")
                target.take_damage(45)
            else:
                print("Duon slashes at you with a giant axe on its head but it misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Duon launches a large bomb at you from cannons on it arms")
                target.take_damage(39)
            else:
                print("Duon launches a large bomb at you from cannons on it arms, but it misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Duon jumps into the air and lands on you!")
                target.take_damage(44)
            else:
                print("Duon jumps into the air and tries to land on you, but it misses!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11:
                print("Duon hits you with spikes on its wheels!")
                target.take_damage(42)
            else:
                print("Duon tries to hit you with the spikes on its wheels but misses!")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


duon = Duon()


class Galleom(Boss):
    def __init__(self):
        super(Galleom, self).__init__(None, 80, False, False, True, "Galleom", 11, 27823)
        self.name = "Galleom"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Galleom charges up a powerful punch but misses with it!!")
            else:
                print("Galleom charges up a powerful punch and hits you with it!")
                target.take_damage(45)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Galleom grabs you and then throws you!!")
                target.take_damage(40)
            else:
                print("Galleom tries to grab you but it misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Galleom stomps on you!")
                target.take_damage(41)
            else:
                print("Galleom tries to stomp on you but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Galleom turns into a tank and shoots missiles at you!")
                target.take_damage(46)
            else:
                print("Galleom turns into a tank and shoots missiles at you but it misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Galleom turns into a tank and runs you over")
                target.take_damage(42)
            else:
                print("Galleom turns into a tank and tries to run you over, but it misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10 or 12 or 7 or 2 or 1:
                print("Galleom begins to overheat a bit and launches a flaming uppercut at you!")
                target.take_damage(56)
            else:
                print("Galleom begins to overheat a bit and launches a flaming uppercut at you, but it misses!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                print("Galleom grabs you and immediately the orb in the center of it's body splits in half "
                      "and Galleom self-destructs!")
                target.take_damage(9999999999999999999999999999999999999)
                self.take_damage(999999999999999999999999999999999999999)
            else:
                print("Galleom grabs you and immediately the orb in the center of it's body splits in half "
                      "and Galleom self-destructs!"
                      "\nHowever, you manage to break free from Galleom but Galleom still self-destructs")
                self.take_damage(99999999999999999999999999999999999999)

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


galleom = Galleom()


class Hand1(Boss):
    def __init__(self):
        super(Hand1, self).__init__(None, 90, False, False, True, "Master Hand", 11, 2063)
        self.name = "Master Hand"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Master Hand tries to attack you but misses")
            else:
                print("Master Hand launches out explosive bullets from his fingers")
                target.take_damage(48)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Master Hand slaps you")
                target.take_damage(43)
            else:
                print("Master Hand tries to slap you but he misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Master Hand launches out giant blobs of ink at you")
                target.take_damage(26)
                target.inked = True
            else:
                print("Master Hand launches out giant blobs of ink at you but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Master hand shoots lasers at you from his fingers!")
                target.take_damage(45)
            else:
                print("Master hand shoots lasers at you from his fingers but he misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Master Hand hand spins his hand like a drill and he hits you")
                target.take_damage(46)
            else:
                print("Master Hand hand spins his hand like a drill but you dodge his attack")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Master Hand launches out 5 fireballs at you")
                self.attack_choice = random.randint(1, 5)
                target.take_damage(22*self.attack_choice)
            else:
                print("Master Hand launches out 5 fireballs at you but you dodge all of them!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 2 or 3 or 4:
                print("Master Hand charges up a massive laser and hits you with it")
                target.take_damage(73)
            else:
                print("Master Hand tries to hit you with a massive laser, but you dodge it")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


master_hand = Hand1()


class Hand2(Boss):
    def __init__(self):
        super(Hand2, self).__init__(None, 90, False, False, True, "Crazy Hand", 12, 2061)
        self.name = "Crazy Hand"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Crazy Hand tries to attack you but misses")
            else:
                print("Crazy Hand launches out several bombs at you!")
                target.take_damage(53)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Crazy Hand flails around wildly and rams into you")
                target.take_damage(47)
            else:
                print("Crazy Hand flails around wildly and tries to ram into you but he misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Crazy Hand launches out a paralyzing ray of light at you!")
                target.take_damage(49)
            else:
                print("Crazy Hand launches out a paralyzing ray of light at you but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Crazy Hand stretches out one of his fingers at you and freezes you for a second!")
                target.take_damage(49)
            else:
                print("Crazy Hand stretches out one of his fingers at you but he misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Crazy Hand launches out lasers at you")
                target.take_damage(50)
            else:
                print("Crazy Hand launches out lasers at you but you dodge his attack")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Crazy Hand gains a shield of blue fireballs and then proceeds to launch them at you")
                target.take_damage(52)
            else:
                print("Crazy Hand gains a shield of blue fireballs and then proceeds to launch them at you but you "
                      "dodge all of them!")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 2 or 3 or 4 or 5:
                print("Crazy Hand charges up a massive laser and hits you with it")
                target.take_damage(79)
            else:
                print("Crazy Hand tries to hit you with a massive laser, but you dodge it")

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


crazy_hand = Hand2()


class Necrozma(Boss):
    def __init__(self):
        super(Necrozma, self).__init__(None, 90, False, False, True, "Ultra Necrozma", 9, 4052)
        self.name = "Ultra Necrozma"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Necrozma tries to use Power Gem on you but it misses")
            else:
                print("Necrozma uses Power Gem!")
                target.take_damage(31)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Necrozma uses Psychic!")
                target.take_damage(37)
            else:
                print("Necrozma uses Psychic! Necrozma's Attack missed!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Necrozma used Photon Geyser!")
                target.take_damage(40)
            else:
                print("Necrozma used Photon Geyser! Necrozma's Attack missed!")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Necrozma used Night Slash!")
                target.take_damage(39)
            else:
                print("Necrozma used Night Slash! Necrozma's Attack missed!")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Necrozma used Moonlight! Necrozma's HP was restored")
                self.health += 30
            else:
                print("Necrozma used Moonlight! Necrozma's move failed!")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Necrozma used Smart Strike!")
                target.take_damage(42)
            else:
                print("Necrozma used Smart Strike! This move cannot miss!")
                target.take_damage(42)
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 2 or 3 or 4 or 5 or 6:
                print("Necrozma uses his Z-Move: Light That Burns the Sky")
                target.take_damage(68)
            else:
                print("Necrozma uses his Z-Move: Light That Burns the Sky, you nearly get out of the blast radius "
                      "but you still take a lot of damage")
                target.take_damage(35)

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    Light_Sword.activated = True
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money

            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            Light_Sword.activated = True
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


ultra_necrozma = Necrozma()


class Jevil(Boss):
    def __init__(self):
        super(Jevil, self).__init__(None, 100, False, False, True, "JEVIL", 9, 5252)
        self.name = "JEVIL"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            print("* JEVIL makes and strange noise, and....")
            if self.dodge_chance == 3:
                print("* JEVIL launches out a volley of diamonds at you but you dodge all of them")
            else:
                print("* JEVIL launches out and hits you with a volley of diamonds at you")
                target.take_damage(36)
        elif self.attack_choice == 2:
            print("* JEVIL: I can do Anything!!")
            if self.dodge_chance != 3:
                print("* A strange carousel of shapes barrage you")
                target.take_damage(40)
            else:
                print("* A strange carousel of shapes barrage you but you keep focused and dodge everything")
        elif self.attack_choice == 3:
            print("JEVIL: I can do anything!")
            if self.dodge_chance != 1:
                print("* JEVIL launches out a barrage of clubs and hearts at you!")
                target.take_damage(42)
            else:
                print("* JEVIL launches out a barrage of clubs and hearts at you but you dodge them")
        elif self.attack_choice == 4:
            print("JEVIL: Let's make the DEVIL'SKNIFE!")
            if self.dodge_chance != 4:
                print("* JEVIL transforms into 4 scythes and slashes at you!")
                target.take_damage(39)
            else:
                print("* JEVIL transforms into 4 scythes and slashes at you but you dodge the attack")
        elif self.attack_choice == 5:
            print("* JEVIL makes a strange noise and...")
            if self.dodge_chance != 8:
                print("* JEVIL launches out several diamonds at you that fly at breakneck speed")
                target.take_damage(43)
            else:
                print("* JEVIL launches out several diamonds at you that fly at breakneck speed but you dodge all of "
                      "them")
        elif self.attack_choice == 6:
            print("JEVIL: CHAOS! CHAOS!")
            if self.dodge_chance != 10:
                print("* JEVIL launches out diamonds, spades, clubs, and hearts at you in a massive barrage of CHAOS!")
                target.take_damage(48)
            else:
                print("* JEVIL launches out diamonds, spades, clubs, and hearts at you in a massive barrage of CHAOS"
                      "\n * But you SOMEHOW keep your cool and dodge all of the attacks")
                target.take_damage(42)
        elif self.attack_choice == 7:
            input("* Something terrible is about to come!")
            print("* Ultimate CHAOS bomb was prepared for you!")
            print("JEVIL: BYE-BYE!")
            if self.dodge_chance != 11 or 2 or 3 or 4 or 5 or 6:
                print("* Several Hundred scythes fall from the sky and hit you, the ones you dodge then "
                      "explode in a big blast")
                target.take_damage(70)
            else:
                print("* Several Hundred scythes fall from the sky, even the ones you dodge then explode in a "
                      "big blast"
                      "\n * Because of this, you still take some damage")
                target.take_damage(41)

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.weapon.attack_stat += 15
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
                    player.weapon.attack_stat += 15
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                    player.weapon.attack_stat += 15
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.inked:
            damage *= 2
        if not self.only_ink:
            if not self.elecfrost:
                if self.no_weapon:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 15
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("This enemy can not be damaged by physical attacks")

            elif self.elecfrost:
                if player.weapon is E_Sword or F_Sword:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 15
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("Enemy takes 0 damage as they can only be hit by ice or electricity")
            elif self.only_ink:
                if player.weapon.__class__ is Splattershot:
                    if damage < self.defense:
                        print("No damage was taken!")
                    else:
                        self.health -= damage - self.defense
                        if self.health < 0:
                            self.health = 0
                            print("%s has been defeated!" % self.name)
                            player.money += self.money
                            player.weapon.attack_stat += 15
                    print("%s has %d health left" % (self.name, self.health))
                else:
                    print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)


jevil = Jevil()


class Tabuu(Boss):
    def __init__(self):
        super(Tabuu, self).__init__(None, 150, False, False, True, "Tabuu", 15, 2008)
        self.name = "Tabuu"
        self.dodges = random.randint(1, 12)

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        self.dodges = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Tabuu pulls out a shimmering golden whip and tries to skewer you with it, but he misses")
            else:
                print("Tabuu skewers you with a shimmering golden whip")
                target.take_damage(87)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Tabuu launches out a stream of bullets from his hand and then one final big blast")
                target.take_damage(80)
            else:
                print("Tabuu launches out a stream of bullets from his hand and then one final big blast"
                      "\n You dodge the individual bullets, but the final blast hits you, catching you off-guard")
                target.take_damage(75)
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Tabuu grows in size and shoots powerful beams out from his eyes!")
                target.take_damage(82)
            else:
                print("Tabuu grows in size and shoots powerful beams out from his eyes but you dodge them")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Tabuu summons some sort of dragon head that shoots out a powerful laser out at you")
                target.take_damage(84)
            else:
                print("Tabuu summons some sort of dragon head that shoots out a powerful laser out at you"
                      " but you dodge the attack")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Tabuu, enraged, karate chops you a couple hundred times")
                target.take_damage(83)
            else:
                print("Tabuu tries to barrage you with karate chops, but you dodge them")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Tabuu duplicates himself and said duplicates then proceed to blow up!")
                target.take_damage(85)
            else:
                print("Tabuu duplicates himself and said duplicates then proceed to blow up, you try to dodge the "
                      "attack, but you get caught off guard by a few clones")
                target.take_damage(82)
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 2 or 3 or 4 or 5 or 6 or 7:
                print("Tabuu grows strange butterfly wings made out of some strange energy"
                      "\nTabuu then proceeds to shoot out a shockwave so deadly, that this attack instantly kills "
                      "you with a direct hit")
                target.take_damage(9999999999999999999999999999999999999999999999999999999999999999999999)
            else:
                print("Tabuu grows strange butterfly wings made out of some strange energy"
                      "\n Tabuu then shoots out a deadly shockwave that you nearly dodge the attack, but the attack "
                      "still, just by barely grazing you, you take massive damage!")
                target.take_damage(81)

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.dodges == 6 or 7 or 8 or 9 or 10:
            if self.inked:
                damage *= 2
            if not self.only_ink:
                if not self.elecfrost:
                    if self.no_weapon:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("This enemy can not be damaged by physical attacks")

                elif self.elecfrost:
                    if player.weapon is E_Sword or F_Sword:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("Enemy takes 0 damage as they can only be hit by ice or electricity")
                elif self.only_ink:
                    if player.weapon.__class__ is Splattershot:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)
        else:
            print("Tabuu quickly teleports away from your attack")


tabuu = Tabuu()


class Agent3(Boss):
    def __init__(self):
        super(Agent3, self).__init__(Hero_Shot, 100, True, False, False, "Agent 3", 13, 5252)
        self.name = "Agent 3"
        self.dodges = random.randint(1, 12)

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        self.dodges = random.randint(1, 12)
        if self.attack_choice == 1:
            print("Agent 3 shoots at you with her Hero Shot")
            target.take_damage(self.weapon.attack_stat)
            target.inked = True
            print("You are now covered in ink")
        elif self.attack_choice == 2:
            if self.dodge_chance != 3 or 4:
                print("Agent 3 uses an autobomb rush and shoots out several bombs that home in on you")
                target.take_damage(38)
                target.inked = True
            else:
                print("Agent 3 uses an autobomb rush and shoots out several bombs that home in on you")
                target.take_damage(38)
                target.inked = True
        elif self.attack_choice == 3:
            if self.dodge_chance != 1 or 2:
                print("Agent 3 equips an inkjet (ink-powered jetpack) and shoots down deadly blasts from above!")
                target.take_damage(34)
                target.inked = True
            else:
                print("Agent 3 equips an inkjet (ink-powered jetpack) and shoots down deadly blasts from above, "
                      "but you somehow dodge them")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4:
                print("Agent 3 gains a giant missile launcher on her back and she shoots down ink missiles at you "
                      "from above")
                target.inked = True
                target.take_damage(35)
            else:
                print("Agent 3 gains a giant missile launcher on her back and she shoots down ink missiles at you "
                      "from above. "
                      "\nYou dodge most of the missiles but get hit by a stray one")
                target.inked = True
                target.take_damage(20)
        elif self.attack_choice == 5:
            if self.dodge_chance != 8:
                print("Agent 3 uses a barrage of splashdowns against you!")
                target.take_damage(39)
                target.inked = True
            else:
                print("Agent 3 uses a barrage of splashdowns against you, but you dodge them")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Agent 3 launches out a barrage of bubbles...."
                      "\nThinking this is far from lethal you are taken aback"
                      "\n But then Agent 3 shoots a single bubble causing a more battle-appropriate chain "
                      "reaction of explosions")
                target.take_damage(37)
                target.inked = True
            else:
                print("Agent 3 launches out a barrage of bubbles...."
                      "\nThinking this is far from lethal you are taken aback"
                      "\n But then Agent 3 shoots a single bubble causing a more battle-appropriate chain "
                      "reaction of explosions, you somehow still dodge some of the explosions, but not "
                      "all of them")
                target.take_damage(31)
                target.inked = True
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 2 or 3:
                print("Agent 3 is fed up with your being here and has decided to barrage you with "
                      "every one of her special weapons, this (of course) does a large amount of damage")
                target.take_damage(59)
                target.inked = True
            else:
                print("Agent 3 is fed up with your being here and has decided to barrage you with "
                      "every one of her special weapons, this (of course) does a large amount of damage"
                      "\n You dodge most of the attacks, but you still get hurt pretty bad")
                target.take_damage(29)
                target.inked = True

    def take_mp(self):
        if player.choice.lower() == "fire blast":
            if player.MP >= 5:
                print("Fire Blast is casted on %s and 20 damage is taken" % self.name)
                self.health -= 20
                player.MP -= 5
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "thunder":
            if player.MP >= 10:
                print("Thunder is casted on %s and 25 damage is taken" % self.name)
                self.health -= 25
                player.MP -= 10
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    print("%s has %d health left" % (self.name, self.health))
                    player.money += self.money
            else:
                print("You do not have enough MP to cast this")
        elif player.choice.lower() == "blizzard":
            if player.MP >= 15:
                print("Blizzard is casted on %s and 35 damage is taken" % self.name)
                player.MP -= 15
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    print("%s has been defeated!" % self.name)
                    player.money += self.money
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
        if self.dodges == 3 or 4 or 8 or 1 or 2:
            if self.inked:
                damage *= 2
            if player.weapon.__class__ is Splattershot:
                self.inked = True
            if not self.only_ink:
                if not self.elecfrost:
                    if self.no_weapon:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("This enemy can not be damaged by physical attacks")

                elif self.elecfrost:
                    if player.weapon is E_Sword or F_Sword:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("Enemy takes 0 damage as they can only be hit by ice or electricity")
                elif self.only_ink:
                    if player.weapon.__class__ is Splattershot:
                        if damage < self.defense:
                            print("No damage was taken!")
                        else:
                            self.health -= damage - self.defense
                            if self.health < 0:
                                self.health = 0
                                print("%s has been defeated!" % self.name)
                                player.money += self.money
                        print("%s has %d health left" % (self.name, self.health))
                    else:
                        print("%s isn't damaged as they can only be attacked by a weapon that fires ink" % self.name)
        else:
            print("Agent 3 quickly dodge-rolls away from you and your attack does not hit her")


Agent_3 = Agent3()

Sheldon = NPC("Sheldon", 50, 10, 2000, True)

Sheldon.items.append(fruit)
Sheldon.items.append(Splattershot_Jr)
Sheldon.items.append(rage_candy)
Sheldon.items.append(tomato)
Sheldon.items.append(sandwich)
Sheldon.items.append(Splattershot_Pro)
Sheldon.items.append(red_potion)

water_pendant = Helmet(15, "Water Pendant", 40)

Gerudo = NPC("Gerudo Shopkeeper", 100, 20, 5000, True)

scimitar = Sword(37, True, False, 60, "Scimitar", 50)

Gerudo.items.append(scimitar)

Gerudo.items.append(water_pendant)
Gerudo.items.append(zork_mat)

Gerudo.items.append(candy)
Gerudo.items.append(candy2)
Gerudo.items.append(super_mushroom)
Gerudo.items.append(Green_Potion)
Gerudo.items.append(desert_helmet)

COVER = Room("The Cultural Landscape", "You are on the cover for the AP HUG textbook, 'entering' "
                                       "the book will allow you to begin your quest into Chapter 1", None, None, None,
             None, None, None, "CHAPTER1K1")
CHAPTER1K1 = Room("Chapter 1 - Key Issue 1 - Area 1", "You are at the beginning of the book, in the most "
                                                      "basic area where you are learning about the basics of geography"
                                                      "\n To the east you can see an open area", None,
                  None, "CH1K1S2", None, None, None, None, "COVER")
CH1K1S2 = Room("Chapter 1 - Key Issue 1 - Area 2", "You feel like you are being watched, and you are, by "
                                                   "satellites! \nThis is done to make maps with GIS and to find "
                                                   "absolute location. Speaking of satellites..."
                                                   "\n What is the acquisition of data "
                                                   "about Earth from satellites?", "CH1KI1S3", None, None, "CHAPTER1K1")

CH1KI1S3 = Room("Map Room", "You are in a room surrounded by many maps. 3 maps slowly glide towards you and attack!",
                None, 'CH1K1S2', None, None,  'CH1K2S1')

CH1K2S1 = Room("Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu",
               "You have entered Key Issue 2 of Chapter 1, and you are currently in the location with the "
               "longest toponym in all of the world", None, None, "REGIONS", None, None, 'CH1KI1S3')

REGIONS = Room("Region Room", 'You are in a room in which there is a question engraved in the wall:'
                              '\nName the three types of regions in alphabetical order?', None, None, None,
               'CH1K2S1', None, 'CH1K3')
CH1K3 = Room("Chapter 1 Key Issue 3", 'You are in a room in which something is spreading towards you.....'
                                      '\n!!!!!'
                                      '\n Quick! Run before you are assimilated! Globalization and '
                                      'Expansion diffusion are chasing you!', None, 'RELOCATION', None, None, 'REGIONS')

RELOCATION = Room("Blank Page", 'You are on a blank page, when suddenly, '
                                'Relocation Diffusion appears! It chased you!', "CH1K3")
CH1K4 = Room("Sustainability Room", "You are on a page where the letters move to say:"
                                    "\n YOUR CHALLENGE IS TO SURVIVE FOR 7 MOVES WITH LIMITED FOOD")
BOSS1 = Room("Chapter 1 Test Room", "You have left the book and are in a white room with a single desk in it", None, "CH1K4")
VONTHANOS = Room("Von Thanos", "You are in a circular room with many rings, some have artificial cows in them"
                           "\n and some have artificial forests in them", None, "CH1K4")
player = Player(COVER)

directions = ['north', 'south', 'east', 'west', 'up', 'down', 'enter', 'leave']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'in', 'out']


gold_room = Gold(150)

past_coin = Gold(1)
Future_coin = Gold(1537)
sub_gold = Gold(812)

dualies = Splattershot("Splat Dualies", 150, 22)

shimmering_whip = Sword(85, True, False, 9999999999999999999999999999999, "Shimmering Golden Whip")
tabuu1 = Helmet(11, "")
tabuu2 = Leggings(13, "")
tabuu3 = Boots(10, "")
tabuu4 = Chestplate(17, "Tabuu's Wings")


# Controller

playing = False

Magic_Compass = Filler2("Magic Compass")

Inventory.inventory.append(Magic_Compass)

while instructions:
    print(colored("AP HUG: THE QUEST FOR THE TEST", 'green'))
    print("TYPE IN 'START' TO START")
    print("TYPE I FOR INSTRUCTIONS")
    command3 = input("")
    if command3.upper() == "I":
        print("            HOW TO PLAY")
        print("_________________________________________")
        input("- You move by typing in north, south, east, west, up, down, enter, or exit."
              "\n- Alternatively, you can use shorthand: n, s, e, w, u, d, in, out")
        input("- Use the command talk to, rob, attack, pick up, grab, drop, take, sharpen, reload, "
              "\nsolve, buy from, or change time to interact with objects/characters")
        input("- If you are carrying the Magic Compass item, type in 'M' in order to see what directions "
              "you can move in")
        input("- At any point, press I to view your inventory, enter 'check stats' to view your stats,"
              " or type in 'speak' to say something, go on!"
              "\n No one is listening!")
    elif command3.upper() == "START":
        instructions = False
        playing = True
        print("--> OKAY"
              "\n --> 3"
              "\n --> 2"
              "\n --> 1")
    else:
        print("That is not a valid command")

aa = False
bbbb = False
aaa = False
c = False
Moves_sus = 0
aaaa = False

while playing:
    if not player.du:
        player.defense = player.helmet.defense + player.chestplate.defense
        player.defense += player.leggings.defense
        player.defense += player.boots.defense
    else:
        player.defense = player.helmet.defense + player.chestplate.defense
        player.defense += player.leggings.defense
        player.defense += player.boots.defense
        player.normal_defense = player.defense
    if player.current_location == CH1K4:
        if not c:
            print("You are given some food")
            Maize.grab()
            Borger.grab()
            C_candy.grab()
            Pork.grab()
            Carrot.grab()
            Moves_sus = player.moves + 7
            c = True
        if not bbbb:
            if player.moves == Moves_sus:
                print("You have survived the challenge, you can now move North or go back south")
                CH1K4.north = BOSS1
                CH1K4.south = RELOCATION
                bbbb = True
            print("You have %i hunger left")
        else:
            print()
    if player.health <= 0:
        playing = False
        print('GAME OVER')
        break
    if tabuu.health <= 0:
        playing = False
        print("YOU WIN! CONGRATULATIONS")
        break
    print(player.current_location.name)
    print(player.current_location.description)
    if len(player.current_location.items) > 0:
        print()
        print("The followisng items are in this room: ")
        for nums, items in enumerate(player.current_location.items):
            print(str(nums + 1) + ": " + items.name)
        print()
    if len(player.current_location.characters) > 0:
        print()
        print("The following characters are in this room: ")
        for nums, persons in enumerate(player.current_location.characters):
            print(str(nums + 1) + ": " + persons.name)
        print()
    if len(player.current_location.enemies) > 0:
        print()
        print("The following enemies are in this room: ")
        for nums, persons in enumerate(player.current_location.enemies):
            print(str(nums + 1) + ": " + persons.name)
        print()
    if player.current_location == CH1K1S2:
        if not aa:
            command2 = input("Well?")
            if command2.lower() == 'remote sensing':
                print("Correct, Here is a development token! These can be used to upgrade your weapons or armor!")
                CH1K1S2.description = "You feel like you are being watched, and you are, by " \
                                      "satellites! \nThis is done to make maps with GIS and to find " \
                                      "absolute location."
                player.development_tokens += 1
            else:
                print("Incorrect! The correct answer was remote sensing!"
                      "\n You look up and see a flaming satellite fall onto you!")
                player.take_damage(25)
                CH1K1S2.description = "You feel like you are being watched, and you are, by " \
                                      "satellites! \nThis is done to make maps with GIS and to find " \
                                      "absolute location."
            aa = True
    if player.current_location == CH1K2S1:
        if not aaa:
            answer = input("What is the location of a place relative to other places?")
            if answer.lower() == "situation":
                player.development_tokens += 1
                print(colored('Correct! You get a development token!', 'green'))
            else:
                print("Incorrect! You have been sent back to the beginning of the book!")
            aaa = True
    if player.current_location == REGIONS:
        if not aaaa:
            answer = input('')
            if answer.lower() == 'formal, functional, vernacular':
                print(colored('Correct! You get a new a weapon', 'green'))
                Inventory.inventory.append(Book)
            else:
                print("Wrong! You get hit in the head with a book!")
            aaaa = True
    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit', 'altf4']:
        playing = False
    elif command.lower() == "give me the hero set":
        player.chestplate = Cape
        player.weapon = Hero_Shot
        print("Given.")
    elif command.lower() in ["use a spell", 'spell', 'cast', 'cast a spell']:
        if len(player.current_location.enemies) > 0:
            for nums, persons in enumerate(player.current_location.enemies):
                print(str(nums + 1) + ": " + colored(persons.name, 'red'))
            print()
        if len(player.current_location.bosses) > 0:
            for nums, persons in enumerate(player.current_location.bosses):
                print(str(nums + 1) + ": " + colored(persons.name, 'red', 'on_grey'))
            print()
        print("Me")
        command4 = input('What do you want to cast a spell on?')
        if command4.lower() == 'me':
            player.cast(player)
        targett = None
        for targets in player.current_location.enemies:
            if targets.name.lower() == command4.lower():
                targett = targets

                player.cast(targett)
        for ttargets in player.current_location.bosses:
            if ttargets.name.lower() == command4.lower():
                targett = ttargets

                player.cast(targett)
    elif 'take ' in command.lower():
        item_name = command[5:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                item_obj = the_item

                item_obj.grab()
                player.current_location.items.remove(item_obj)

    elif 'grab ' in command.lower():
        item_name = command[5:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                item_obj = the_item

                item_obj.grab()
                player.current_location.items.remove(item_obj)

    elif 'pick up ' in command.lower():
        item_name = command[5:]

        item_obj = None
        for the_item in player.current_location.items:
            if the_item.name.lower() == item_name.lower():
                item_obj = the_item

                item_obj.grab()
                player.current_location.items.remove(item_obj)

    elif 'attack ' in command.lower():
        targets_name = command[7:]

        targett = None
        for targets in player.current_location.enemies:
            if targets.name.lower() == targets_name.lower():
                targett = targets

                player.attack(targett)
        for ttargets in player.current_location.bosses:
            if ttargets.name.lower() == targets_name.lower():
                targett = ttargets

                player.attack(targett)
    elif 'talk to ' in command.lower():
        NPCs_name = command[8:]

        the_person = None
        for people in player.current_location.characters:
            if people.name.lower() == NPCs_name.lower():
                the_person = people

                the_person.talk()
    elif command.lower() == "m":
        if Magic_Compass in Inventory.inventory:
            if player.current_location.name.lower() != "lost woods":
                if player.current_location.north is not None:
                    print("You can go north")
                if player.current_location.south is not None:
                    print("You can go south")
                if player.current_location.east is not None:
                    print("You can go east")
                if player.current_location.west is not None:
                    print("You can go west")
                if player.current_location.up is not None:
                    print("You can go up")
                if player.current_location.down is not None:
                    print("You can go down")
                if player.current_location.enter is not None:
                    print("You can go inside something")
                if player.current_location.leave is not None:
                    print("You can exit your current area")
            else:
                print("A strange fog in the forest prevents the compass from working")
        else:
            print("You do not have your magic compass")
    elif 'rob ' in command.lower():
        NPCs_name = command[4:]

        the_person = None
        for people in player.current_location.characters:
            if people.name.lower() == NPCs_name.lower():
                the_person = people

                player.rob(the_person)
    elif 'speak with ' in command.lower():
        NPCs_name = command[11:]

        the_person = None
        for people in player.current_location.characters:
            if people.name.lower() == NPCs_name.lower():
                the_person = people

                the_person.talk()
    elif 'buy from ' in command.lower():
        NPCs_name = command[9:]

        the_person = None
        for people in player.current_location.characters:
            if people.name.lower() == NPCs_name.lower():
                the_person = people

                the_person.buy()
    elif 'equip ' in command.lower():
        items_name = command[6:]

        the_item = None
        for stuff in Inventory.inventory:
            if stuff.name.lower() == items_name.lower():
                the_item = stuff

                try:
                    the_item.equip()
                except AttributeError:
                    print("You can't equip this")
    elif "remove " in command.lower():
        items_name = command[7:]
        if player.weapon.name.lower() == items_name.lower():
            the_item = player.weapon
            try:
                the_item.unequip()
            except AttributeError:
                print("You can't unequip this")
        elif player.helmet.name.lower() == items_name.lower():
            the_item = player.helmet
            try:
                the_item.unequip()
            except AttributeError:
                print("You can't unequip this")
        elif player.boots.name.lower() == items_name.lower():
            the_item = player.boots
            try:
                the_item.unequip()
            except AttributeError:
                print("You can't unequip this")
        elif player.leggings.name.lower() == items_name.lower():
            the_item = player.leggings
            try:
                the_item.unequip()
            except AttributeError:
                print("You can't unequip this")
        elif player.chestplate.name.lower() == items_name.lower():
            the_item = player.chestplate
            try:
                the_item.unequip()
            except AttributeError:
                print("You can't unequip this")
    elif 'use ' in command.lower():
        items_name = command[4:]

        the_item = None
        for stuff in Inventory.inventory:
            if stuff.name.lower() == items_name.lower():
                the_item = stuff
                try:
                    the_item.use()
                except AttributeError:
                    print("You can't use this")
    elif 'drop ' in command.lower():
        items_name = command[5:]

        the_item = None
        for stuff in Inventory.inventory:
            if stuff.name.lower() == items_name.lower():
                the_item = stuff

                try:
                    the_item.drop()
                except AttributeError:
                    print("You can't drop this")
                    if the_item.__class__ is not Filler:
                        player.current_location.items.append(the_item)
    elif 'sharpen ' in command.lower():
        items_name = command[7:]

        the_item = None
        if player.weapon.name.lower() == items_name.lower():
            the_item = player.weapon

            try:
                the_item.sharpen()
            except AttributeError:
                print("You can't use this")
    elif 'reload ' in command.lower():
        items_name = command[6:]

        the_item = None
        if player.weapon.name.lower() == items_name.lower():
            the_item = player.weapon

            try:
                the_item.reload()
            except AttributeError:
                print("You can't use this")
        else:
            print("You do not have the means to do that yet")
    elif command.lower() in ["check inventory", "open inventory", 'i']:
        Inventory.check()
    elif command.lower() in ["check stats", 'c', 'stats', 'check']:
        player.check_stats()
    elif command.lower() in ["solve puzzle", "solve riddle", "solve", "answer"]:
        print("THIS FEATURE HAS NOT BEEN ADDED YET")
    elif command.lower() == "":
        print()
    elif command.lower() in ["speak", "talk"]:
        command2 = input("What would you like to say?")
        print("You: " + command2)
    elif command.lower() == "scream":
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRGGGGGGGGGGGHHHHHHHHH'
              'HHHHHHHHHHHHHHHHHHHHHHHHH')
    elif command.lower() in ['die', 'drop dead', 'drop dead for no apparent reason', 'die for no reason',
                             'kill self']:
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
    elif command.lower() == "recognized":
        print("Command not reco- Oh... VERY funny! HA! HA! HA! Don't do that again")
    elif command.lower() in directions:
        command = command.lower()
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't do this or go this way")
    elif command.upper() == "UPUPDOWNDOWNLEFTRIGHTLEFTRIGHTBASTART":
        input(".")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        input("..")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        input("...")
        print()
        print("cheat code accepted")
        command2 = input("WHAT CHEAT WOULD YOU LIKE?"
                         "\n1. ALL BOSSES (EXCEPT FINAL BOSS) DEFEATED"
                         "\n2. BEAT THE GAME"
                         "\n3. + 75 HEALTH UPGRADE"
                         "\n4. + 75 MP"
                         "\n5. TABUU ARMOR"
                         "\n Pick a number: ")
        if command2 == "1":
            input(".")
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("cheat code accepted")
            bowser.take_damage(999999999999999)
            d_bowser.take_damage(999999999999999999)
            dark_link.take_damage(9999999999999999)
            red.take_damage(9999999999999999)
            player.current_weapon = player.weapon
            player.weapon = Hero_Shot
            Agent_3.take_damage(9999999999999999999)
            octavio.take_damage(99999999999999999)
            chaos0.take_damage(9999999999999999999999)
            player.choice = "blizzard"
            gohma.take_mp()
            player.mp = player.max_MP
            jevil.take_damage(99999999999999999999)
            galleom.take_damage(99999999999999)
            duon.take_damage(999999999999999)
            crazy_hand.take_damage(999999999999999)
            master_hand.take_damage(999999999999999999)
            ultra_necrozma.take_damage(999999999999999999999)
            m_mario.take_damage(9999999999999999999999)
            marx.take_damage(99999999999999999999)
            galacta_knight.take_damage(9999999999999999999999999)
            player.weapon = player.current_weapon
        elif command2 == "2":
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("cheat code accepted")
            tabuu.health = 0
        elif command2 == "3":
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("cheat code accepted")
            player.max_health += 75
            player.health = player.max_health
        elif command2 == "4":
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("cheat code accepted")
            player.max_MP += 75
            player.health = player.mp
        elif command2 == "5":
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("cheat code accepted")
            player.helmet = tabuu1
            player.leggings = tabuu2
            player.boots = tabuu3
            player.chestplate = tabuu4
            player.weapon = shimmering_whip
        else:
            input(".")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("..")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            input("...")
            print()
            print("error - not a valid cheat code")
    elif command.upper() == "ROSEBUD":
        input(".")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        input("..")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        input("...")
        print()
        print("cheat code accepted")
        player.max_health = 9999999999999999999999999999999999999999999999
        player.health = player.max_health
        player.chestplate.defense += 9999999999999999999
        player.weapon.attack_stat += 99999999999999999999999
        player.max_MP += 999999999999999999999999999999999
        player.MP = player.max_MP
    else:
        print("Command not recognized, if you inputted a direction, write it again in all lowercase")
    if not player.just_moved:
        if len(player.current_location.enemies) > 0:
            for nme in range(len(player.current_location.enemies)):
                if player.current_location.enemies[nme].health > 0:
                    player.current_location.enemies[nme].attack(player)
        if len(player.current_location.bosses) > 0:
            for nme in range(len(player.current_location.bosses)):
                if player.current_location.bosses[nme].health > 0:
                    player.current_location.bosses[nme].attack(player)
    if player.current_location == CH1KI1S3:
        if not player.just_moved:
            print("The distortion in the room causes you to take 10 damage!")
            player.take_damage(10)
    if len(player.current_location.enemies) > 0:
        for nmez in player.current_location.enemies:
            if nmez.health <= 0:
                player.current_location.enemies.remove(nmez)
                if nmez == NPC1:
                    RELOCATION.south = CH1K4
                    RELOCATION.description = "You are on a blank page in the textbook... " \
                                             "\n Strange that there is a blank page but who cares?"
    if len(player.current_location.bosses) > 0:
        for nmes in player.current_location.bosses:
            if nmes.health == 0:
                player.current_location.bosses.remove(nmes)
    player.just_moved = False
    if player.current_location == CH1K4:
        if not bbbb:
            player.hunger -= 10
    player.moves += 1
