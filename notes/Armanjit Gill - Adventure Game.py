import random


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

    def fuse(self):
        if key_1 and key_2 and key_3 and key_4 in self.inventory:
            self.max_space = self.max_space
            JEVIL_KEY.grabbed = True
            Inventory.inventory.append(JEVIL_KEY)
            key_1.grabbed = False
            Inventory.inventory.remove(key_1)
            key_2.grabbed = False
            Inventory.inventory.remove(key_2)
            key_3.grabbed = False
            Inventory.inventory.remove(key_3)
            key_4.grabbed = False
            Inventory.inventory.remove(key_4)
            print("* You put the 4 key pieces together and form the Door Key")


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
            print("%s: I'm not supposed to talk to the customer, sorry" % self.name)
        else:
            if self.like == 0:
                print("%s: %s" % (self.name, self.dialogue))
                self.like += 1
                self.aaaaaaa = len(self.items)
            elif self.like == 1:
                if self.aaaaaaa == 0:
                    if self.name != "Agent 3":
                        print("%s: %s" % (self.name, self.dialogue))
                    elif self.name == "Agent 3":
                        self.oo += 1
                    if self.oo == 1:
                        print("Agent 3: So... on a quest to save the world? Sounds fun.")
                    elif self.oo == 2:
                        print("Agent 3: I've saved the world before... It was pretty exhilarating")
                    elif self.oo == 3:
                        print("Agent 3: Let's fight again! Heh, just kidding. "
                              "\n Based on the look on your face, I'd assume that you wouldn't enjoy that.")
                    elif self.oo == 4:
                        print("Agent 3: ........")
                    elif self.oo == 5:
                        print("Agent 3: (This person is quite the talker....)")
                    elif self.oo == 6:
                        print("Agent 3: (I wonder how all my friends are doing?)")
                    elif self.oo == 7:
                        print("Agent 3: (Maybe if I act like I'm bored, they'll leave)")
                    elif self.oo == 8:
                        print("Agent 3: (Why is this person talking to me so much???)")
                    elif self.oo == 9:
                        print("Agent 3: (I miss Agent 8, wonder what she's up to?)")
                    elif self.oo == 10:
                        print("Agent 3: (While this person is still here I guess I'll just listen to some music)")
                    elif self.oo == 11:
                        print("Agent 3 is humming a tune overly loud to try to annoy you into "
                              "bailing from the conversation")
                else:
                    if len(Inventory.inventory) + len(self.items) <= Inventory.max_space:
                        if self.name == "Dog":
                            print("Bark! Bark! Bark!")
                        else:
                            print("%s: I would like to give you this" % self.name)
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
                            print("Here is/are your %s" % self.items[i].name)
                            print(self.items)
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
            if player.chestplate is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.chestplate = undershirt
                Inventory.inventory.append(self)


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
            if player.boots is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.boots = none4
                Inventory.inventory.append(self)


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
            if player.leggings is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s" % self.name)
                player.leggings = underwear
                Inventory.inventory.append(self)


class Weapon(object):
    def __init__(self, name="", price=0):
        self.price = price
        self.name = name
        self.attack_stat = 0
        self.grabbed = False

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
                player.weapon = None
                Inventory.inventory.append(self)


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
                self.durability -= 1
                if self.durability <= 0:
                    print("Your weapon has become dull from constant use")
                    self.sharp = False
                    self.dull = True
                    self.attack_stat /= 2
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
            print("Remaining durability: %s" % self.durability)
            print("While this weapon can defeat any enemy in one hit, your HP is constantly going to be at 1HP")


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


leather1 = Boots(1, "Leather Boots")

leather2 = Leggings(2, "Leather leggings")

leather3 = Chestplate(3, "Leather Chestplate")

Wooden_Sword = Sword(5, True, False, 8, "Wooden Sword")

Magic_Sword = Sword(20, True, False, 999999999999999999999999, "Magic Sword")

Fire = Sword(30, True, False, 20, "Burning Blade", 0)

leather4 = Helmet(3, "Leather Helmet")

none = Helmet(0, "None")

none2 = Chestplate(0, "None")

none3 = Leggings(0)

none4 = Boots(0)

none5 = Sword(0, True, False, 000, "")


class Player(object):
    def __init__(self, starting_location, health=80, helmet=leather4, chestplate=leather3, boots=leather1,
                 weapon=Wooden_Sword, mp=15, leggings=leather2, inked=False, money=30):
        self.health = health
        self.leggings = leggings
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
        self.inked = inked
        self.money = money
        self.can_attack = False
        self.choice = ""
        self.random = 0

    def attack(self, target):
            if self.weapon.__class__ is Sword:
                self.weapon.attack()
            if self.weapon.__class__ is Axe:
                self.weapon.attack()
            if self.weapon.__class__ is Gun:
                self.weapon.shoot()
            if self.weapon.__class__ is Splattershot:
                self.weapon.shoot()
                target.inked = True
                print("Your enemy has been inked and attacks now do double damage")
            print("You attack %s for %d damage" %
                  (target.name, self.weapon.attack_stat))
            target.take_damage(self.weapon.attack_stat)

    def cast(self, target):
        if target != self:
            self.choice = input("What do you want to attack with?"
                                "\nFire Blast, Thunder, or Blizzard"
                                "\n   5MP       10MP      15MP    ")
            target.take_mp()
        elif target == self:
            self.choice = input("Do you want to cast heal on yourself?")
            if self.choice.lower() == "yes":
                if self.MP >= 25:
                    player.MP -= 25
                    if player.health + 30 <= player.max_health:
                        player.health += 30
                        print("You heal yourself and restore 30 health")
                    else:
                        print("You heal yourself and your HP is maxed out")
                        player.health = player.max_health
                else:
                    print("You do not have enough MP to cast heal on yourself")

    def rob(self, target):
        if target.__class__ is NPC:
            if target.name != "Dog":
                if self.weapon.attack_stat > target.power:
                    self.money += target.money
                    target.money -= target.money
                    print("You rob and overpower %s and take their money" % target.name)
                else:
                    print("You try to rob %s, but they easily overpower you and they take some of "
                          "your money" % target.name)
                    player.money -= player.money/9
                    target.attack(self, target.power)
            else:
                print("The dog bites you and while you are stunned, the dog takes all of your money and eats it"
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
        if new_location == TEMPLE:
            if self.helmet is water_pendant:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to swim down to the structure, but you drown...")
                self.health -= self.health
        elif new_location == NOVA_1:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go through the giant clockwork star but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == TRAP:
            self.current_location = new_location
            self.inked = False
            self.health -= self.health
        elif new_location == CASTLE_3:
            if self.current_location == CASTLE_2:
                self.random = random.randint(1, 10)
                if self.random == 1 or 2 or 6:
                    self.health -= self.health
                    print("You get cut up by the sawblades on your way through!")
                else:
                    self.current_location = new_location
                    self.inked = False
            else:
                    self.health = 0
                    print("Wait.... Why did you think going back into the room that filled to the top with lava was a good idea?!")
        elif new_location == CASTLE_1:
            if self.current_location == CASTLE_2:
                self.random = random.randint(1, 10)
                if self.random == 1 or 2 or 6:
                    self.health -= self.health
                    print("You get cut up by the sawblades on your way through!")
                else:
                    self.current_location = new_location
                    self.inked = False
        elif new_location == MT_SILVER:
            self.random = random.randint(1, 10)
            if self.random == 1 or 6:
                self.health -= self.health
                print("You fell of the mountain while climbing it and died!")
            else:
                self.current_location = new_location
                self.inked = False
        elif new_location == TOWN:
            if self.current_location == OASIS:
                if player.helmet == water_pendant:
                    print("While you're in the water...")
                    key_2.grab()
                    self.current_location = new_location
                    self.inked = False
                else:
                    print("You hop into the water where you drown. "
                          "\n You emerge from the waterway in a town where people are somehow "
                          "scared of a corpse in their drinking water that is now contaminated.")
            else:
                self.current_location = new_location
                self.inked = False
        elif new_location == NOVA2:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go on but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == NOVA3:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go on but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == NOVA4:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go on but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == NOVA5:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go on but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == NOVA7:
            if self.helmet is space:
                self.current_location = new_location
                self.inked = False
            else:
                print("You try to go on but it turns out "
                      "that you kinda need a space helmet to survive in space...")
                self.health -= self.health
        elif new_location == NOVA6:
            print("You do no need a space helmet to breathe in this room")
            self.current_location = new_location
            self.inked = False
        elif new_location == MARX:
            print("You do no need a space helmet to breathe in this room")
            self.current_location = new_location
            self.inked = False
        elif new_location == SPLAT4:
            if self.helmet is scuba:
                self.current_location = new_location
                self.inked = False
            else:
                print("You can't swim through ink, so you're kind of stuck here....")
        elif new_location == SPLAT6:
            if self.helmet is scuba:
                self.current_location = new_location
                self.inked = False
            else:
                print("You can't swim through ink, so you're kind of stuck here....")
        elif new_location == SPLAT7:
            if self.helmet is scuba:
                self.current_location = new_location
                self.inked = False
            else:
                print("You can't swim through ink, so you're kind of stuck here....")
        elif new_location == INTERIOR:
            self.random = random.randint(1, 10)
            if self.current_location == SUBSPACE_ENTER:
                print("You jump down into the volcano and...")
                if self.random == 1 or 2 or 7:
                    print("You survived!")
                    self.current_location = new_location
                    self.inked = False
                else:
                    print("You fall into molten lava and burn to death...")
                    self.health = 0
            else:
                self.current_location = new_location
                self.inked = False
        elif new_location == BAY:
            if player.helmet is water_pendant:
                self.random = random.randint(5, 10)
            else:
                self.random = random.randint(1, 10)
            if self.current_location == CLIMB:
                print("You jump down into the bay and...")
                if self.random == 9 or 6 or 7 or 8 or 10:
                    print("You survived!")
                    self.current_location = new_location
                    self.inked = False
                else:
                    if self.random == 1 or 2 or 3:
                        print("You fall onto the ground and die!")
                        self.health = 0
                    else:
                        print("You fall too far down into the water and drown!")
                        self.health = 0
            else:
                self.current_location = new_location
                self.inked = False
        elif new_location == MT_SILVER:
            self.random = random.randint(1, 10)
            if self.current_location == MTN_BASE:
                print("You try to climb the mountain and...")
                if self.random == 1 or 6 or 3 or 8 or 10:
                    print("You survived!")
                    self.current_location = new_location
                    self.inked = False
                else:
                    print("You fall onto the ground and die!")
                    self.health = 0
        elif new_location == KEY:
            self.random = random.randint(1, 10)
            if self.current_location == TEMPLE_5:
                print("You try to climb the pile and...")
                if self.random == 1 or 6 or 3 or 8 or 10:
                    print("You survived!")
                    self.current_location = new_location
                    self.inked = False
                else:
                    print("You fall onto the ground and die!")
                    self.health = 0
        else:
            self.current_location = new_location
            self.inked = False

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

    def check_stats(self):
        print("You:")
        print("Weapon: %s, does %i attack damage" % (self.weapon.name, self.weapon.attack_stat))
        print("Total Defense: %i" % self.defense)
        print("Health: %i/%d" % (self.health, self.max_health))
        print("MP: %i/%d" % (self.MP, self.max_MP))
        print("Money: %i" % self.money)
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
            print("Restores %s health" % self.restore)


rage_candy = Eat1(20, "Rage Candy Bar", 20)

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

candy2 = Eat2(40, "MP Candy")

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


class Key(object):
    def __init__(self, name="", price=0):
        self.grabbed = False
        self.name = name
        self.price = price

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the key fragment")
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the key")
            self.grabbed = False
            Inventory.inventory.remove(self)


class Key3(object):
    def __init__(self, unlock, r_b4, r, name="", price=0):
        self.grabbed = False
        self.name = name
        self.unlocks = unlock
        self.r_b4 = r_b4
        self. r = r
        self.price = price
        self.zzzzz = 0

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the key")
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the key")
            self.grabbed = False
            Inventory.inventory.remove(self)

    def use(self):
        if self.grabbed:
            if player.current_location == self.r:
                TOT3.north = "GHOMA"
                print("You use the key and unlock a room")
                TOT3.description = "There is a large door in front of you that had a padlock on it" \
                                   "The door is currently unlocked and you can go north to go through it"
            else:
                print("There is no use for this key in this room")


class Key2(object):
    def __init__(self, unlock, r_b4, r, name="", price=0):
        self.grabbed = False
        self.name = name
        self.unlocks = unlock
        self.r_b4 = r_b4
        self. r = r
        self.price = price

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the key")
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the key")
            self.grabbed = False
            Inventory.inventory.remove(self)

    def use(self):
        if self.grabbed:
            if player.current_location == self.r:
                FACTORY.enter = "M_MARIO"
                print("You use the keycard and unlock the factory")
                FACTORY.description = "You are looking at a strange factory, " \
                                      "you can now enter the factory as you unlocked it with the keycard"
            else:
                print("There is no use for this keycard in this room")


class Skelkey(Key2):
    def __init__(self, unlock, r_b4, r_b42, r_b43, name=""):
        super(Skelkey, self).__init__(unlock, r_b4, name)
        self.grabbed = False
        self.name = name
        self.r_b42 = r_b42
        self.r_b43 = r_b43

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the key")
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the key")
            self.grabbed = False
            Inventory.inventory.remove(self)

    def use(self):
        if self.grabbed:
            self.r_b43 = self.r_b42
            TEMPLE_3.north = "CHAOS_FIGHT"
            TEMPLE_1.east = "WATER_MP"
            TEMPLE_2.east = "D_LINK"
            print("The Key flies out of your hand and unlocks the doors of the temple")
            TEMPLE_1.description = "You are in a room with a now unlocked door leading east. " \
                                   "\n You can continue through the temple to the north"
            TEMPLE_2.description = "There is a door to the east and a door leading north. "
            TEMPLE_3.description = "In front of you is a large door that had a fittingly over-sized lock." \
                                   "\n You can now go north through the door"


class SKey(Key):
    def __init__(self, name=""):
        super(SKey, self).__init__()
        self.name = name

    def use(self):
        if self.grabbed:
            if player.current_location == JEVIL_ENTRANCE:
                print("* You use the door key"
                      "\n * The door key created a door")
                JEVIL_ENTRANCE.enter = 'JEVIL_FIGHT'
                JEVIL_ENTRANCE.description = "*There is a cage-like gate in front of you, " \
                                             "* There's a note saying: 'Collect the 4 keys to enter'" \
                                             "\n* You have created an entrance through the gate using the door key"


key_1 = Key("Key Fragment 1")
key_2 = Key("Key Fragment 2")
key_3 = Key("Key Fragment 3")
key_4 = Key("Key Fragment 4", 0)

JEVIL_KEY = SKey("Door Key")


class Ball(Eat1):
    def __init__(self, restore, name="", multiply=1.15):
        super(Ball, self).__init__(restore, name)
        self.multiply = multiply

    def use(self):
        print("You eat the.... %s.... and you restore 1 health...."
              "\n WHAT?! Your weapon has magically increased in strength by %i times" % (self.name, self.multiply))
        player.weapon.attack_stat *= self.multiply
        Inventory.inventory.remove(self)


Inventory.inventory.append(Wooden_Sword)

Wooden_Sword.grabbed = True

leather1.grabbed = True

leather2.grabbed = True

leather3.grabbed = True

ball = Ball(1, "Rubber? Ball")


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
        if self in Inventory:
            Inventory.inventory.remove(self)
            print("You forever parted ways with the %s."
                  "\nYou can never retrieve it, it vanishes as soon as it hits the ground"
                  "\nGoodbye %s" % (self.name, self.name))


CG = Gun("Coconut Gun", 30)

Egg = Filler("EGG")

Briefcase = Filler("Locked Briefcase")

Melee = Filler("Unopened Copy of Smash Bros Melee")

egg2 = Filler("EGG 2: ELECTRIC BOOGALOO")

Book = Filler("Book")


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

dog.items.append(ball)

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
        if target.inked:
            self.weapon.attack_stat *= 2

        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.attack_stat))
        target.take_damage(self.weapon.attack_stat)
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
            NOVA4.east = 'NOVA7'
            NOVA4.description = "You have solved the riddle needed to progress" \
                                "\n You can go east or you can go south"
        else:
            print("Incorrect! The wall that blocks your path is still here")


marx_board = Keyboard("tombstone")


class Keyboard2(object):
    def __init__(self, solution=""):
        self.solution = solution
        self.solv = ""

    def solve(self):
        self.solv = input("What is the answer?")
        if self.solv.lower() == self.solution:
            print("Correct!")
            SUBSPACE2.east = 'SUBSPACE4'
            SUBSPACE2.description = "Now that you have solved the riddle, the path to the east has opened up and " \
                                    "\nnow you can go east to get an upgrade or go north to continue"
        else:
            print("WRONG!!! PREPARE FOR THE DRAINING OF YOUR LIFE FORCE")
            player.health -= player.health


sub_board = Keyboard2("mewtwo")

temple_bot = NPC("Shopkeeper bot model NX HAC serial no 84493587", 99999999999999, 0, 0, True)
forest_directions = Filler("UP, UP, DOWN, DOWN, LEFT, RIGHT, LEFT, RIGHT"
                           "\nKEY: UP = NORTH, DOWN = SOUTH, LEFT = WEST, RIGHT = EAST", 0)
zork_mat = Filler("Battered Rubber Mat that reads 'WELCOME TO ZORK'")
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
rock.items.append(key_4)


class Boss(Enemy):
    def __init__(self, weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon):
        super(Boss, self).__init__(weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon)
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)


class Bowser(Boss):
    def __init__(self):
        super(Bowser, self).__init__(Claw, 60, False, False, True, "Bowser", 7, 1500)
        self.name = "Bowser"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Bowser attacks with his claws! But he misses!")
            else:
                print("Bowser attacks for %d with his claws!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Bowser attacks with a fireball!")
                target.take_damage(30)
            else:
                print("Bowser attacks with a fireball but misses!")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Bowser attacks with his shell!")
                target.take_damage(28)
            else:
                print("Bowser attacks with his shell but misses")
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


bowser = Bowser()

spider_leg = Sword(9, True, False, 9999999999999999999, "")


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
    def __init__(self, name="Chaos"):
        super(Chaos, self).__init__(Claw, 75, False, True, False, name, 9, 2000)
        self.name = "Chaos"

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
        super(Marx, self).__init__(None, 100, False, False, True, "Marx", 12, 9298)
        self.name = "Marx"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Marx launches out 4 crescent blades! But he misses!")
            else:
                print("Marx launches out 4 crescent blades!!")
                target.take_damage(30)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Marx split himself in half and turns into fire, flying into you many times and reverting back")
                target.take_damage(40)
            else:
                print("Marx split himself in half and turns into fire, trying to fly into you many times and reverting "
                      "back after missing")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1 or 2 or 3:
                print("Marx's face stretches into a deformed shape and he shoots a massive laser from his mouth")
                target.take_damage(47)
            else:
                print("Marx's face stretches into a deformed shape and he shoots a massive laser from his "
                      "mouth but he misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6 or 7:
                print("Marx splits his body in half in order to create a black hole")
                target.take_damage(65)
            else:
                print("Marx splits his body in half in order to create a black hole but you somehow avoid being "
                      "sucked in")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Marx launches down strange black seeds, these seeds quickly grow into sharp vines which then "
                      "hit you")
                target.take_damage(37)
            else:
                print("Marx launches down strange black seeds, these seeds quickly grow into sharp vines "
                      "which then barely graze you")
                target.take_damage(5)
        elif self.attack_choice == 6:
            if self.dodge_chance != 10 or 3:
                print("Marx flies quickly down into the ground, then, when you least expect it, he rises out quickly, "
                      "ramming you while laughing eerily")
                target.take_damage(32)
            else:
                print("Marx flies quickly down into the ground and flies out to try to ram into you, but he misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11:
                print("Marx's eyes go blacks a black orbs start coming from his eyes."
                      "\n The orbs then quickly fly into you to do damage")
                target.take_damage(27)
            else:
                print("Marx's eyes go blacks a black orbs start coming from his eyes."
                      "\n The orbs then try to fly into you, but they miss")

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
                    NOVA6.items.append(Lance)
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
                    NOVA6.items.append(Lance)
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
                    NOVA6.items.append(Lance)
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
                            NOVA6.items.append(Lance)
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
                            NOVA6.items.append(Lance)
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
                            NOVA6.items.append(Lance)
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
                    U_NECROZMA.items.append(light)
                    U_NECROZMA.items.append(light2)
                    U_NECROZMA.items.append(light3)
                    U_NECROZMA.items.append(light4)
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
                    Light_Sword.activated = True
                    U_NECROZMA.items.append(light)
                    U_NECROZMA.items.append(light2)
                    U_NECROZMA.items.append(light3)
                    U_NECROZMA.items.append(light4)
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
                    Light_Sword.activated = True
                    U_NECROZMA.items.append(light)
                    U_NECROZMA.items.append(light2)
                    U_NECROZMA.items.append(light3)
                    U_NECROZMA.items.append(light4)
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
                            Light_Sword.activated = True
                            U_NECROZMA.items.append(light)
                            U_NECROZMA.items.append(light2)
                            U_NECROZMA.items.append(light3)
                            U_NECROZMA.items.append(light4)
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
                            U_NECROZMA.items.append(light)
                            U_NECROZMA.items.append(light2)
                            U_NECROZMA.items.append(light3)
                            U_NECROZMA.items.append(light4)
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
                            Light_Sword.activated = True
                            U_NECROZMA.items.append(light)
                            U_NECROZMA.items.append(light2)
                            U_NECROZMA.items.append(light3)
                            U_NECROZMA.items.append(light4)
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
                    _3.characters.append(A_3)
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
                    _3.characters.append(A_3)
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
                    _3.characters.append(A_3)
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
                                _3.characters.append(A_3)
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
                                _3.characters.append(A_3)
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
                                _3.characters.append(A_3)
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

water_pendant = Helmet(15, "Water Pendant")

Gerudo = NPC("Gerudo Shopkeeper", 100, 20, 5000, True)

scimitar = Sword(37, True, False, 60, "Scimitar")

Gerudo.items.append(scimitar)

Gerudo.items.append(water_pendant)

Gerudo.items.append(candy)
Gerudo.items.append(candy2)
Gerudo.items.append(super_mushroom)
Gerudo.items.append(Green_Potion)
Gerudo.items.append(desert_helmet)

TEMPLE_1 = Room('Lock Room', "You are in a room with a locked door leading east. "
                "\n You can continue through the temple to the north", 'TEMPLE_2', 'TEMPLE')
TEMPLE_2 = Room('Empty Chamber', "There is a locked door to the east and a door leading north. ",
                'TEMPLE_3', 'TEMPLE_1')
TRAP = Room('Trap', "As you walk to the west, the floor beneath you crumbles, "
                    "dropping you into a large pool of piranha-infested waters"
                    "\n You struggle to survive but you realize it's futile, you are not going to survive")
TEMPLE_3 = Room('Boss Room', "In front of you is a large door that has a fittingly over-sized lock."
                             "\n You look to the east and west, either direction can hold the key", None,
                'TEMPLE_2', 'TRAP', 'TEMPLE_4')
CHAOS_FIGHT = Room('Chaos Battle', "You are face to face with Chaos 0! The strange watery creature looks angry. "
                                   "Since normal weapons phase through it, ice or electricity "
                                   "would likely be most effective to "
                                   "attack it", None, 'TEMPLE_3', None, None, 'BAY')
TEMPLE_4 = Room('Gold Room', "You are in a room filled with a large pile of gold, about 150 coins"
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
TOT2 = Room('Watch Room', "In the center of the room there is a pedastal labeled 'MAGIC STOPWATCH'. "
                          "You sigh as you realize "
                          "some time-travel shenanigans will ensue"
                          "\n You can use the watch to open up paths to the east or west that existed in "
                          "the past or future", 'TOT3', 'TOT1', 'PAST1', 'FUTURE1')
TOT3 = Room('Boss Room', "There is a large door in front of you with a large padlock on it, "
                         "it appears that a key is needed. "
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
SPLAT7 = Room('Hammerhead Bridge', "You are walking across a large bridge leading to the east."
                                   "\n To the east is what looks to be a dark and removed part of "
                                   "this world. cast way, in the shadows", None, None, 'SPLAT8', 'SPLAT3')
SPLAT8 = Room('Cephalon HQ', "You are in an area with floating platforms. "
                             "Below you is a toxic sludge with stone tentacles rising out of it", 'DJOCTAVIO', None,
              None, 'SPLAT7')
DJOCTAVIO = Room("DJ Octavio Fight", "You find that you have entered a stadium of some sort. "
                                     "In front of you is a giant floating mech with an octopus inside"
                                     "\n You'll need some sort of ink firing weapon to win,"
                                     " otherwise, you will easily perish", None, 'SPLAT8')
SPLAT6 = Room('Arowana Mall', "You are in a shopping mall. Here you can buy upgrades to your health or magic, "
                              "as well as buy items to restore your health."
                              "\n You also can buy a weapon that can fire ink here")
SPLAT4 = Room('Octo Canyon', "After swimming through the ink, you have reached a large canyon. "
                             "\n Looking down in the canyon you can see something that looks like"
                             " a cross between a squid and a kid...", None, None, None, 'SPLAT2', None, '_3')
_3 = Room('Agent 3 Battle', "Upon getting closer, the squid-kid sees you. She turns around and she looks ready to fight"
                            "\n this 'Inkling' is known as Agent 3, and she will be one of your most "
                            "difficult battles yet."
                            "\n You can only defeat her with a weapon that fires ink, and either way... Good Luck!",
          None, None, None, None, 'SPLAT4')
SPLAT5 = Room('Bluefin Depot', "You are on a platform floating in the water",
              None, None, 'SPLAT2')
PAST2 = Room('Coin Room (Past)', "Upon a pedestal in this room is a an old ancient coin on the floor worth 1 coin today",
             None, None, 'TOT3')
FUTURE2 = Room('Key Room (Future)', "While the path leading here has caved "
                                    "in during our present day, and this "
                                    "path had not yet been built in the past you can visit this room in the future. "
                                    "\n The key in this "
                                    "room appears to be broken. In  a time between our present day and the past"
                                    " and before the future, "
                                    "this key was most definitely intact",
               None, None, None, 'TOT3')
FUTURE1 = Room('Gold Room (Future)', "In this room, there is a pedastal labeled 'A COIN FROM THE FUTURE'", None, None,
               'TOT2')
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
TOP_TOWER = Room('Shiekah Tower (Top)', 'You look in front of you and see an axe on a pedestal.', None, None, None,
                 None, None, 'TOWER')
VOLCANO = Room('Volcano', "You are in front of a volcano... do you want to jump in?", None, None, None,
               None, None, None, 'INTERIOR')
INTERIOR = Room('Inside Volcano', "HOLY HECK, YOU'RE ALIVE!!"
                                  "\n .... Anyways, there is a fragment of a key here", None, None, None, None,
                'VOLCANO')
MT_SILVER = Room('Mt. Silver', "You are on top of the mountain. Hail is plummeting down and the wind is howling. "
                               "There is someone at the edge of the cliff you're standing on"
                               "\n Red:..............!!!", None, None, None, None, None, 'MTN_BASE')
MTN_BASE = Room('Mt. Silver Base', "You are at the base of a snowy mountain. You can likely climb it, but the rocks "
                                   "are slightly slippery, so you might slip and fall", 'VOLCANO', None, None, None,
                'MT_SILVER', 'MTN_PASS')
CAVE = Room('Frozen Cave', "You are in a cold cave. The ground and walls are frozen and "
                           "there are icicles hanging from the ceiling"
                           "\n In the center of the cave is an icy sword and a helmet encased in "
                           "an impenetrable layer of ice. "
                           "It seems like this ice wasn't here before... If only you could rewind time...",
            None, None, 'MTN_PASS')
MTN_PASS = Room('Mountain Pass', "There is a frozen path leading west, a shop to the east, "
                                 "and towering above you, a mountain",
                None, None, 'MTN_SHOP', "CAVE", 'MTN_BASE')
MTN_SHOP = Room('Mountain Shop', "There is engraving on stone: BUY SOMETHING AND LEAVE THE MONEY OR ELSE..."
                                 "\n There is a keycard, armor, health upgrades, a key fragment, a blue potion,"
                                 " and a space helmet",
                None, None, 'CLIMB', 'MTN_PASS')
CLIMB = Room('Dangerous Climb', "You feel like this place isn't safe, when suddenly, you're attacked!", None, None,
             None, 'MTN_SHOP', 'PEAK', 'BAY')
PEAK = Room('Mountain Peak', "You are at the top of a mountain, you can see into space from here."
                             "\n There is floating wreckage here, if only you could see what this "
                             "place looked like in the past"
                             "\n You feel like you can walk west, there is no platform there,"
                             " but your instincts tell you to do it.", None, None, None, 'SUBSPACE_ENTER', None,
            'CLIMB', 'NOVA_1')
NOVA_1 = Room("Milkyway Pathway", "You are on some sort of star littered path. You have gained "
                                  "the ability to fly, but only in set paths."
                                  " You can leave this area or fly north or west through space", 'NOVA3', None,
              None, 'NOVA2', None, None, None, 'PEAK')
NOVA2 = Room('Gourmet Room', "You find yourself in a room in which there is a large quantity of food, "
                             "you can eat the food to restore all of your health.", None, None, 'NOVA_1')
NOVA3 = Room('Barren Planet', "You are on an empty planet and then you get attacked", 'NOVA4', 'NOVA_1', 'NOVA5')
NOVA5 = Room("Long Stone Bridge", 'You are on a long, stone bridge suddenly you are attacked', None, 'NOVA6', None,
             'NOVA3')
NOVA6 = Room('Galacta Knight Fight', "You see a floating pink crystal, suddenly, it cracks and shatters!"
                                     "\n You are face to face with the strongest warrior in the galaxy:"
                                     "\n GALACTA KNIGHT")
NOVA4 = Room("Riddle Room", "Engraved into a wall is a riddle:"
                            "\n Marking mortal privation, when firmly in place. An enduring summation, "
                            "engraved in my face."
                            "\n What am I?"
                            "\n It appears there is a stone keyboard you can use to type in your response",
             None, 'NOVA3')
NOVA7 = Room('Mysterious Dimension', 'You have made it past the riddle, and you now see that in front of you is a '
                                     'strange portal, you can go north to enter it, or you can go back west', 'MARX',
             None, None, 'NOVA4')
MARX = Room('Marx Fight', "There... seems to be absolutely nothing here... Or at least, that's what you thought"
            "\n You turn around and see the cosmic jester Marx! He rises into the air, and changes into his "
            "True Form!!", None, 'NOVA7')
SUBSPACE_ENTER = Room('Edge of the Universe', "You stand in front of a dark void... unsure"
                                              " of what will become of you once you enter, there is only one thing you "
                                              "know for sure..."
                                              "\n Your adventure is nearing its end", None, None, 'PEAK', None, None,
                      'INTERIOR', 'SUBSPACE1')
SUBSPACE1 = Room('Entrance to Subspace', 'You enter through the dark portal and find yourself on a strange '
                                         'blue floating platform'
                                         '\n All of a sudden, strange purple orbs fly onto the platform and they '
                                         'get absorbed into one giant monster!', 'SUBSPACE2', None, None, None,
                 None, None, None, 'SUBSPACE_ENTER')
SUBSPACE2 = Room('Riddle Room', 'On a stone tablet there is a riddle written on it:'
                                '\n Designed solely for combat, this fighter was deemed too dangerous to brawl. '
                                '\n He yearns to return for revenge'
                                '\n There seems to be a stone keyboard you can use to type in your response'
                                'You can go north to continue or enter the riddle correctly to open the door '
                                'to the east to a health and MP upgrade'
                                '\n However, be careful, for you only get one opportunity to answer the riddle '
                                'correctly, otherwise, you will perish', 'SUBSPACE3', 'SUBSPACE1')
SUBSPACE3 = Room("Gold Room", 'You find yourself in a room in which you find some gold on the floor'
                              '\n You csn go north or back south', 'SUBSPACE5', 'SUBSPACE2')
SUBSPACE5 = Room('Abandoned Platform', 'You find yourself on an empty platform, when more orbs appear!'
                                       '\n They group together and form a giant robot!', 'SUBSPACE6', 'SUBSPACE3')
SUBSPACE6 = Room('End of a Journey', "You find yourself in the last room of your journey. "
                                     "\n You can go East or West to fight one of two strange disembodied floating "
                                     "hands.", 'TABUU', 'SUBSPACE5', 'C_HAND', 'M_HAND')
# You can go North after beating the bosses to the east and west

TABUU = Room("            ", "You are on a glowing floating platform."
                             "\n In front of you is the puppet-master who has been controlling everything:"
                             "\n TABUU!"
                             "\n You clutch your weapon knowing this is the end of your journey"
                             "\n You will either succeed here, or you'll have had come this far just to fail", None,
             'SUBSPACE6')
# This room is meant to have no name

C_HAND = Room("Crazy Hand Fight", "After going east you find yourself in a fight against Crazy Hand!"
              "\n This more erratic hand is hard to beat, Good Luck! You'll need it", None, None, None, 'SUBSPACE6')
M_HAND = Room('Master Hand Fight', "After going west you find yourself face to fa- er... face to hand... with Master "
                                   "Hand!"
                                   "\n This fight is going to be difficult, so try your best", None, None, 'SUBSPACE6')
SUBSPACE4 = Room('Upgrade Room', 'You enter this room and find that your HP and MP have been increased.', None, None,
                 None, 'SUBSPACE2')

BAY = Room('Great Bay', 'There is an open ocean around you, you can see a strange structure under the water',
           None, None, None, 'RIVER', None, 'TEMPLE')
TEMPLE = Room('Water Temple', 'You are in the first room of the Water Temple. '
                              '\n You can swim back up or head north to the second room', 'TEMPLE_1', None, None, None,
              "BAY")
BEGIN = Room("An Adventure's Beginning", "You stand atop a hill looking ahead at the forest to "
                                         "the north and turn around to see the desert to the south. "
                                         "\n You're ready for your quest.", 'FOREST', 'TOWN', 'OASIS',
             'FACTORY', 'CHEATS')
MARKET = Room('Desert Market', "You browse the fine selection of goods, you see potions that increase health and MP,"
                               "\n a strange pendant with a drop of water engraved on it, armor, a scimitar, "
                               "\n strange scuba gear, items that restore MP"
                               "\n You also see a battered rubber door mat saying 'WELCOME TO ZORK', but it "
                               "seems to be worthless. ", 'TOWN', 'DESERT_FIGHT', 'CASTLE', 'TEMPLE2')
TOWN = Room('Desert Town', "You are in a barren town, there isn't much to see here",
            'BEGIN', 'MARKET', 'DESERT_FIGHT')
CHEATS = Room("Traceback (most recent call last): File 'C:/Users/4v9z/Documents/GitHub/"
              "CSE/notes/Armanjit Gill - Dictionary Map.py", "@#%$*@(#^@*!*#&$^hdqoY&*#",
              'SUBSPACE_ENTER', 'PEAK', "NOVA4", "CLEARING")
OASIS = Room("Desert Oasis", "You're in the middle of a desert next to the only water here. "
                             "\n There is a waterway barely big enough for you in the water. It appears that there is"
                             " something in the water",
             'RIVER', 'DESERT_FIGHT', None, 'BEGIN', None, 'TOWN')
FACTORY = Room('Factory', "You are looking at a strange factory, it "
                          "appears some sort of keycard is required to enter it", None, None, 'BEGIN', None,
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
                "FOREST", "RIVER", "JEVIL_ENTRANCE")
RIVER = Room('River Path', 'There is a small river flowing next to you.'
                           '\n You can follow it to the east or you can go North, South, or West',
             'MTN_SHOP', 'OASIS', 'BAY', 'CLEARING')
JEVIL_ENTRANCE = Room('???????????', "*There is a cage-like gate in front of you, "
                                     "* There's a note saying: 'Collect the 4 keys to enter'"
                                     "\n* There is one fragment of a key here",
                      None, None, 'CLEARING')
JEVIL_FIGHT = Room("???????", "JEVIL: 'I CAN DO ANYTHING!!' Watch out! Here comes JEVIL! "
                              "There's no strategy to beat this enemy, Good Luck! LET THE GAMES BEGIN!",
                   None, None, None, None, None, None, None, 'JEVIL_ENTRANCE')


player = Player(BEGIN)

directions = ['north', 'south', 'east', 'west', 'up', 'down', 'enter', 'leave']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'in', 'out']


# Adding NPCs + Shopkeepers

MARKET.characters.append(NPC1)
MARKET.characters.append(NPC2)
MARKET.characters.append(NPC3)
MARKET.characters.append(NPC4)
MARKET.characters.append(NPC5)
MARKET.characters.append(NPC7)
MARKET.characters.append(dog)
MARKET.characters.append(NPC8)
MARKET.characters.append(NPC9)
MARKET.characters.append(NPC10)
MARKET.characters.append(Gerudo)
MTN_SHOP.characters.append(rock)
SPLAT6.characters.append(Sheldon)
TOT_SHOP.characters.append(temple_bot)

# Adding Enemies

NOVA5.enemies.append(G_Knights)
NOVA3.enemies.append(Frosty)
NOVA3.enemies.append(Dee)
DESERT_FIGHT.enemies.append(caterkiller)
TEMPLE_2.enemies.append(Lizalfos)
TEMPLE_2.enemies.append(Lizalfos2)
PAST1.enemies.append(Bokkoblin)
PAST1.enemies.append(Bokkoblin2)
PAST1.enemies.append(Bokkoblin3)
CLIMB.enemies.append(Dynablade)
CASTLE_4.enemies.append(goomba)
CASTLE_4.enemies.append(Koopa)
CASTLE_4.enemies.append(Spiny)

# Adding Bosses

BOWSER.bosses.append(bowser)
DARK_STAR.bosses.append(d_bowser)
D_LINK.bosses.append(dark_link)
MT_SILVER.bosses.append(red)
_3.bosses.append(Agent_3)
DJOCTAVIO.bosses.append(octavio)
CHAOS_FIGHT.bosses.append(chaos0)
GHOMA.bosses.append(gohma)
JEVIL_FIGHT.bosses.append(jevil)
SUBSPACE1.bosses.append(galleom)
SUBSPACE5.bosses.append(duon)
TABUU.bosses.append(tabuu)
C_HAND.bosses.append(crazy_hand)
M_HAND.bosses.append(master_hand)
U_NECROZMA.bosses.append(ultra_necrozma)
M_MARIO.bosses.append(m_mario)
MARX.bosses.append(marx)
NOVA6.bosses.append(galacta_knight)


playing = True

tot_key = Key3("aaa", "aaaa", TOT3, "Boss Key")
factory = Key2("M_MARIO", "aaaaa", FACTORY, "Strange Keycard", 64)
Skel_key = Skelkey("aaa", "aaaa", "aaa", "aaaa", "Skeleton Key")

rock.items.append(factory)

gold_room = Gold(150)

past_coin = Gold(1)
Future_coin = Gold(1537)
sub_gold = Gold(812)

dualies = Splattershot("Splat Dualies", 150, 22)


class Ice(object):
    def __init__(self):
        self.activated = False

    def un_ice(self):
        self.activated = True
        if the_watch.past:
            CAVE.items.append(F_Sword)
            CAVE.items.append(frost_helmet)
            CAVE.description = "You are in a cold cave. The ground and walls are frozen and " \
                               "there are icicles hanging from the ceiling" \
                               "\n In the center of the cave is an icy sword and a helmet " \
                               "The icy shell encasing them didn't exist in the past"
        else:
            if F_Sword and frost_helmet in CAVE.items:
                CAVE.items.remove(F_Sword)
                CAVE.items.remove(frost_helmet)
                CAVE.description = "You are in a cold cave. The ground and walls are frozen and " \
                                   "there are icicles hanging from the ceiling" \
                                   "\n In the center of the cave is an icy sword and a helmet encased in " \
                                   "an impenetrable layer of ice. " \
                                   "It seems like this ice wasn't here before... If only you could rewind time..."


ice = Ice()


class Watch(object):
    def __init__(self):
        self.past = False
        self.future = False
        self.name = "Magic Stopwatch"
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

    def use(self, time):
        if time.lower() == "past":
            self.past = True
            self.future = False
            print("You travel backwards in time to the past")
            TOT2.east = PAST1
            TOT3.west = PAST2
            TOT2.west = None
            TOT2.east = None
            ice.un_ice()
            if tot_key in FUTURE2.items:
                FUTURE2.items.remove(tot_key)
            FUTURE2.description = "While the path leading here has caved "
            "in during our present day, and this "
            "path had not yet been built in the past you can visit this room in the future. "
            "\n The key in this "
            "room appears to be broken. In  a time between our present day and the past"
            " and before the future, "
            "this key was most definitely intact"
        elif time.lower() == "present":
            self.past = False
            self.future = False
            print("You go back to the present")
            TOT2.east = None
            TOT3.west = None
            TOT2.west = None
            TOT2.east = None
            ice.un_ice()
            if tot_key in FUTURE2.items:
                FUTURE2.items.append(tot_key)
            FUTURE2.description = "Now that you have figured out how to obtain the key you can go back " \
                                  "through the barricade. " \
                                  "\nYou can somehow get out from this end as there is a small " \
                                  "tunnel only accessible from here leading back to the previous room"

        elif time.lower() == "future":
            self.past = False
            self.future = True
            print("You go to the future")
            TOT2.east = None
            TOT3.west = None
            ice.un_ice()
            TOT2.west = FUTURE1
            TOT2.east = FUTURE2
            if tot_key in FUTURE2.items:
                FUTURE2.items.remove(tot_key)
            FUTURE2.description = "While the path leading here has caved "
            "in during our present day, and this "
            "path had not yet been built in the past you can visit this room in the future. "
            "\n The key in this "
            "room appears to be broken. In  a time between our present day and the past"
            " and before the future, "
            "this key was most definitely intact"


the_watch = Watch()

# Adding Items
CLEARING.items.append(Light_Sword)
KEY.items.append(Skel_key)
TOP_TOWER.items.append(Ancient_axe)
JEVIL_ENTRANCE.items.append(key_1)
INTERIOR.items.append(key_3)
TEMPLE_4.items.append(gold_room)
SUBSPACE3.items.append(sub_gold)
FUTURE1.items.append(Future_coin)
PAST2.items.append(past_coin)
SPLAT5.items.append(dualies)
CAVE.items.append(ice)
TOT2.items.append(the_watch)


class Wreckage(object):
        def __init__(self):
            self.activated = False

        def be_unlocked(self):
            if the_watch.past:
                PEAK.enter = NOVA_1
                self.activated = True


nova = Wreckage()

shimmering_whip = Sword(85, True, False, 9999999999999999999999999999999, "Shimmering Golden Whip")
tabuu1 = Helmet(11, "")
tabuu2 = Leggings(13, "")
tabuu3 = Boots(10, "")
tabuu4 = Chestplate(17, "Tabuu's Wings")
# Controller

while playing:
        if player.current_location == MT_SILVER:
            player.health -= 12
        player.defense = player.helmet.defense + player.chestplate.defense
        player.defense += player.leggings.defense
        player.defense += player.boots.defense
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
            print("The following items are in this room: ")
            for nums, items in enumerate(player.current_location.items):
                print(str(nums + 1) + ": " + items.name)
            print()
        if len(player.current_location.characters) > 0:
            print()
            print("The following characters are in this room: ")
            for nums, persons in enumerate(player.current_location.characters):
                print(str(nums + 1) + ": " + persons.name)
            print()
        command = input(">_")
        if command.lower() in short_directions:
            pos = short_directions.index(command.lower())
            command = directions[pos]
        if command.lower() in ['q', 'quit', 'exit', 'altf4']:
            playing = False
        elif 'take ' in command.lower():
            item_name = command[5:]

            item_obj = None
            for the_item in player.current_location.items:
                if the_item.name.lower() == item_name.lower():
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(the_item)
        elif 'grab ' in command.lower():
            item_name = command[5:]

            item_obj = None
            for the_item in player.current_location.items:
                if the_item.name.lower() == item_name.lower():
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(the_item)
        elif 'pick up ' in command.lower():
            item_name = command[8:]

            item_obj = None
            for the_item in player.current_location.items:
                if the_item.name.lower() == item_name.lower():
                    item_obj = the_item

                    item_obj.grab()
                    player.current_location.items.remove(the_item)
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

                    the_item.equip()
        elif 'unequip ' in command.lower():
            items_name = command[8:]

            the_item = None
            for stuff in Inventory.inventory:
                if stuff.name.lower() == items_name.lower():
                    the_item = stuff

                    the_item.unequip()
        elif 'use ' in command.lower():
            items_name = command[4:]

            the_item = None
            for stuff in Inventory.inventory:
                if stuff.name.lower() == items_name.lower():
                    the_item = stuff

                    the_item.use()
        elif 'drop ' in command.lower():
            items_name = command[5:]

            the_item = None
            for stuff in Inventory.inventory:
                if stuff.name.lower() == items_name.lower():
                    the_item = stuff

                    the_item.drop()
                    player.current_location.items.append(the_item)
        elif 'sharpen ' in command.lower():
            items_name = command[7:]

            the_item = None
            if player.weapon.name.lower() == items_name.lower():
                the_item = player.weapon

                the_item.sharpen()
        elif 'refill ' in command.lower():
            items_name = command[6:]

            the_item = None
            if player.weapon.name.lower() == items_name.lower():
                    the_item = player.weapon

                    the_item.reload()
        elif command.lower() in ["change time", "travel through time", 'time travel']:
            command2 = input("Would you like to go to the past, present, or future?")
            the_watch.use(command2.lower())
        elif command.lower() in ["check inventory", "open inventory", 'i']:
            Inventory.check()
        elif command.lower() in ["check stats", 's', 'stats']:
            player.check_stats()
        elif command.lower() in ["solve puzzle", "solve riddle", "solve", "answer"]:
            if player.current_location == NOVA4:
                marx_board.solve()
            elif player.current_location == SUBSPACE2:
                sub_board.solve()
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
            player.money += 9999999999999999999999999999999999
        elif command.upper() == "GODMODE":
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

        if len(player.current_location.enemies) > 0:
            for nme in range(len(player.current_location.enemies)):
                player.current_location.enemies[nme].attack(player)
        if len(player.current_location.bosses) > 0:
            for nme in range(len(player.current_location.bosses)):
                player.current_location.bosses[nme].attack(player)
