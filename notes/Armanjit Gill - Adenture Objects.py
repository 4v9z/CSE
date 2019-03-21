import random


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
        if Egg and egg2 and egg3 and egg4 and egg5 and egg6 and eggg in self.inventory:
            Inventory.inventory.append(U_Egg)
            Inventory.inventory.append(U_Egg2)
            U_Egg.grabbed = True
            U_Egg2.grabbed = True
            Egg.grabbed = False
            Inventory.inventory.remove(Egg)
            egg2.grabbed = False
            Inventory.inventory.remove(egg2)
            egg3.grabbed = False
            Inventory.inventory.remove(egg3)
            egg4.grabbed = False
            Inventory.inventory.remove(egg4)
            egg5.grabbed = False
            Inventory.inventory.remove(egg5)
            egg6.grabbed = False
            Inventory.inventory.remove(egg6)
            eggg.grabbed = False
            Inventory.inventory.remove(eggg)
            print("The eggs are fused together in a blinding light. When the light clears, two eggs fly into your "
                  "inventory")


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

    def talk(self):

        if self.like == 0:
            print("%s: %s" % (self.name, self.dialogue))
            self.like += 1
            self.aaaaaaa = len(self.items)
        elif self.like == 1:
            if self.aaaaaaa == 0:
                print("%s: %s" % (self.name, self.dialogue))
            else:
                if len(Inventory.inventory) + len(self.items) <= Inventory.max_space:
                    if self.name == "Dog":
                        print("Bark! Bark! Bark!")
                    elif self.name == "Gnorman":
                        print("*Interpretive dances and gives you something*")
                    else:
                        print("%s: I would like to give you this" % self.name)
                    for i in range(len(self.items)):
                        Inventory.inventory.append(self.items[i])
                        self.aaaaaaa = 0
                        if self.name == "Gnorman":
                            print()
                        elif self.name == "Dog":
                            print()
                        else:
                            self.dialogue = "Hello, nice to see you today"
                else:
                    print("%s: I would like to give you thi-- Oh... I'm not sure you have enough"
                          " space in your bag to hold my items...." % self.name)

    def buy(self):
        if self.shopkeeper:
            print()
            for num, item in enumerate(self.items):
                print(str(num + 1) + ": " + item.name)
            print()
            self.option = input("%s: What do you want to buy?" % self.name)
            for i in range(len(self.items)):
                if self.items[i].name.lower() == self.option.lower():
                    if player.money >= self.items[i].price:
                        player.money -= self.items[i].price           # FIX THIS NOW
                        self.items[i].grabbed = True
                        self.items.remove(self.items[i])
                        Inventory.inventory.append(self.items[i])
                        print("Here is your %s" % self.items[i].name)
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
                print("You remove the %s")
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
                print("You remove the %s")
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
                print("You remove the %s")
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
                print("You remove the %s")
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
                print("You remove the %s")
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


class Shword(Sword):
    def __init__(self, attack_stat, sharp, dull, durability, name, price=0):
        super(Shword, self).__init__(attack_stat, sharp, dull, durability, name, price)
        self.grabbed = False


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

Wooden_Sword = Sword(5, True, False, 5, "Wooden Sword")

Magic_Sword = Sword(999999999, True, False, 999999999999999999999999, "Magic Sword")

Wiebe_Armor = Chestplate(99999999999999999999999999999999999999999999999999999999, "Wiebe Armor")

leather4 = Helmet(3, "Leather Helmet")

none = Helmet(0, "None")

none2 = Chestplate(0, "None")

none3 = Leggings(0)

none4 = Boots(0)

none5 = Blade(0)


class Player(object):
    def __init__(self, starting_location, health=50, helmet=leather4, chestplate=leather3, boots=leather1,
                 weapon=Wooden_Sword, mp=15, leggings=leather2, inked=False):
        self.health = health
        self.leggings = leggings
        self.inventory = []
        self.current_location = starting_location
        self.helmet = helmet
        self.chestplate = chestplate
        self.boots = boots
        self.defense = 5
        self.MP = mp
        self.weapon = weapon
        self.max_health = health
        self.max_MP = mp
        self.defense = self.helmet.defense + self.chestplate.defense + self.leggings.defense + self.boots.defense
        self.name = "you"
        self.inked = inked
        self.money = 30
        self.can_attack = False
        self.choice = ""

    def attack(self, target):
        if self.current_location is player.current_location:
            self.can_attack = True
        if self.can_attack:
            print("You attack %s for %d damage" %
                  (target.name, self.weapon.attack_stat))
            target.take_damage(self.weapon.attack_stat)
            if self.weapon.__class__ is Blade:
                self.weapon.attack()
            if self.weapon.__class__ is Gun:
                self.weapon.shoot()
            if self.weapon.__class__ is Splattershot:
                self.weapon.shoot()
                target.inked = True
                print("Your enemy has been inked and attacks now do double damage")

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
            if self.weapon.attack_stat > target.power:
                self.money += target.money
                target.money -= target.money
                print("You rob and overpower %s and take their money" % target.name)
            else:
                print("You try to rob %s, but they easily overpower you and they take some of your money" % target.name)
                player.money -= player.money/9
        else:
            print("You can't rob this being")

    def take_damage(self, damage):
        if not self.inked:
            if damage * 1.2 < self.defense:
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
        self.current_location = new_location
        self.inked = False

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


player = Player('AA')

Inventory = Bag()

F_Sword = Specialsword(40, True, False, 200, "Frost Sword")

Money_Sword = Sword(1, True, False, 999999999999999999999999999999999999999999, "Money Sword")

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
    def __init__(self, restore2=20, name=""):
        super(Potion1, self).__init__("", 20)
        self.restore = restore2
        self.name = name

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
    def __init__(self, restore=30, name=""):
        super(Eat1, self).__init__()
        self.restore = restore
        self.name = name
        self.grabbed = False

    def check(self):
        if self.grabbed:
            print(self.name)
            print("Restores %s health" % self.restore)


rage_candy = Eat1(20, "Rage Candy Bar")

fruit = Eat1(9999999999999999999999999999999999999, "Hearty Simmered Fruit")

sandwich = Eat1(45, "Crusty Seanwich")

tomato = Eat1(9999999999999999999999999999999999999999999999999999999, "Maximum Tomato")


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
    def __init__(self, restore2=20, name=""):
        super(Potion2, self).__init__("", 20)
        self.restore = restore2
        self.name = name

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
    def __init__(self, restore=30, name=""):
        super(Eat2, self).__init__()
        self.restore = restore
        self.name = name
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


candy = Eat2(100000000000, "Rare Candy")

Green_Potion = Potion2(25, "Green Potion")

super_mushroom = Eat2(10, "Super Mushroom")

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

ancient3 = Chestplate(13, "Ancient Chestplate", 85)

ancient4 = Helmet(7, "Ancient Helmet", 20)

lava = Leggings(8, "Lava Leggings", 41)

lava2 = Boots(3, "Lava Boots", 26)

light = Boots(4, "Light Boots")

light2 = Leggings(9, "Light Leggings")

light3 = Helmet(6, "Light Helmet")

light4 = Chestplate(11, "Light Chestplate")


class Upgrades(Consumables):
    def __init__(self, upgrade=10):
        super(Upgrades, self).__init__()
        self.upgrade = upgrade


class Inroomrestore(object):
    def __init__(self, restore=20):
        self.restore = restore


class Health2(Inroomrestore):
    def __init__(self, filler=1):
        super(Health2, self).__init__()
        self.filler = filler

    def use(self):
        print("You eat some of the provided food and your HP is maxed out")
        player.health = player.max_health
        self.filler = self.filler


class Healthupgrade(Upgrades):
    def __init__(self, upgrade=10):
        super(Healthupgrade, self).__init__()
        self.activated = False
        self.upgrade = upgrade

    def grab(self):
        self.activated = True
        if self.activated:
            print("You use the health upgrade and your HP gets maxed out."
                  "\n Your HP is also increased by %i" % self.upgrade)
            player.max_health += self.upgrade
            player.health = player.max_health


upgrade1 = Healthupgrade()


class MPupgrade(Upgrades):
    def __init__(self, upgrade=25):
        super(MPupgrade, self).__init__()
        self.upgrade = upgrade
        self.activated = False

    def grab(self):
        self.activated = True
        if self.activated:
            print("You use the MP upgrade and your MP gets maxed out."
                  "\n Your MP is also increased by %i" % self.upgrade)
            player.max_MP += self.upgrade
            player.MP = player.max_MP


upgrade2 = MPupgrade()


class Key(object):
    def __init__(self, name=""):
        self.grabbed = False
        self.name = name

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


class Key2(object):
    def __init__(self, unlock, r_b4, name=""):
        self.grabbed = False
        self.name = name
        self.unlocks = unlock
        self.r_b4 = r_b4

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
            if player.current_location == self.r_b4:
                self.r_b4 = self.unlocks


class SKey(Key):
    def __init__(self, name=""):
        super(SKey, self).__init__()
        self.name = name

    def use(self):
        if self.grabbed:
            if player.current_location == JEVIL_ENTRANCE:
                print("* You use the door key"
                      "\n * The door key created a door")


key_1 = Key("Key Fragment 1")
key_2 = Key("Key Fragment 2")
key_3 = Key("Key Fragment 3")
key_4 = Key("Key Fragment 4")

JEVIL_KEY = SKey("Door Key")


class Watch(object):
    def __init__(self):
        self.past = False
        self.future = False

    def use(self, time):
        if time.lower() == "past":
            self.past = True
            self.future = False
            print("You travel backwards in time to the past")
        elif time.lower() == "present":
            self.past = False
            self.future = False
            print("You go back to the present")
        elif time.lower() == "future":
            self.past = False
            self.future = True
            print("You go to the future")


watch = Watch()


class Wreckage(object):
    def __init__(self):
        self.activated = False
        if watch.past:
            PEAK.enter = NOVA_1


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

egg3 = Filler("EGG 3: THE VOID BECKONS")

egg4 = Filler("EGG 4: SOME MORE LORE")

egg5 = Filler("EGG 5: THE VOID IS COMING")

egg6 = Filler("3GG 6: The2435i43WORLD1323059450CAN'T483280HANDLE4982355fdzjjANYMORE93053484032EGGS")

eggg = Filler("EGG # 90239040320053937865531994736486164623559875"
              "535321324899464656444446446465496       there are too many eggs")

Book = Filler("Book")


A_3 = NPC("Agent 3", 99999999999999999, 99999999999999999999999999999999999999999999999, 99999999999999, False,
          "You're pretty powerful. I've never been beaten before, the only other time I was beaten was "
          "\nonly when someone thought of a hole in my attack pattern.")

A_3.items.append(Hero_Shot)

A_3.items.append(Cape)

NPC1 = NPC("Gregg", 10, 1, 20, False, "Here. Egg. My name no longer Gregg, my name now Gr, because I now no have egg.")

NPC1.items.append(Egg)

NPC2 = NPC("Danny DeVito", 900, 20, 9999999999, False, "May I offer you an egg in these trying times?")

NPC2.items.append(egg2)

NPC2.items.append(egg3)

NPC2.items.append(egg4)

NPC3 = NPC("Johnny", 1, 0, 1, False, "Hello, my name is Johnny.")

NPC4 = NPC("Bob", 35, 15, 99999,  False, "Hi, I'm Bob")

NPC5 = NPC("Jim", 20, 8, 100, False, "Hello, my name is Jim")

NPC6 = NPC("Gnorman", 99999999, 99999999999999999999, 1000000000000, False, "*Interpretive dances*")

U_Egg = ALL(9999999, 9999999, "Ultimate Egg #1")

U_Egg2 = Ball(99999999, "Ultimate Egg #2", 2)

NPC7 = NPC("Jack Handey", 99, 20, 1000, False, "Here, have a book of my greatest deep thoughts")

NPC7.items.append(Book)

dog = NPC("Dog", 20, 5, 0, False, "Bark Bark!")

dog.items.append(ball)

NPC8 = NPC("Sarah", 99, 20, 800, False, "Hello")

NPC9 = NPC('Cheyanne', 10, 10, 10, False, "Hello there, I'm from Wyoming")

NPC10 = NPC("Zo R. Kuh", 70,  20, 1980, False, "Hey there, I was named after some text based game, those things are "
                                               "boring. "
                                               "\nWhy would anyone play one??? (please don't quit playing now)")
NPC2.items.append(egg5)
NPC3.items.append(egg6)
NPC6.items.append(eggg)
# weapon, armor, health=20, name="", current_location=None, inked=False, mon=0


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


foot = Blade(2, True, False, 9999999999999999999999999999)

shell = Blade(5, True, False, 9999999999999999999999999999)

foot2 = Blade(10, True, False, 9999999999999999999999999999)

Iron_Blade = Blade(15, True, False, 9999999999999999999999999)

Claw = Blade(20, True, False, 999999999999)

Claw2 = Blade(15, True, False, 99999999999999)

octoling1 = Enemy(Splattershot_Jr, 30, True, False, False, "Octoling", 5)
octoling2 = Enemy(Splattershot_Jr, 30, True, False, False, "Octoling", 5)
octoling3 = Enemy(Splattershot_Jr, 30, True, False, False, "Octoling", 8)

goomba = Enemy(foot, 5, False, False, True, "Goomba", 2)
Koopa = Enemy(shell, 10, False, False, True, "Koopa Troopa", 6)
Spiny = Enemy(shell, 14, False, False, True, "Spiny", 8)

Bokkoblin = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9)
Bokkoblin2 = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9)
Bokkoblin3 = Enemy(Wooden_Sword, 20, False, False, True, "Bokkoblin", 9)

Frosty = Enemy(F_Sword, 30, False, False, True, "Mr. Frosty", 12)

Dee = Enemy(foot2, 20, False, False, True, "Big Waddle Dee", 10)

G_Knights = Enemy(E_Sword, 25, False, False, True, "Galactic Knights", 12)

Lizalfos = Enemy(Iron_Blade, 20, False, False, True, "Lizalfos", 10)
Lizalfos2 = Enemy(Iron_Blade, 20, False, False, True, "Lizalfos", 10)

Dynablade = Enemy(Claw2, 45, False, False, True, "Dynablade", 15)

caterkiller = Enemy(Iron_Blade, 25, False, False, True, "Giant Caterkiller", 12)


class Keyboard(object):
    def __init__(self, solution=""):
        self.solution = solution
        self.solv = ""

    def solve(self):
        self.solv = input("What is the answer?")
        if self.solv.lower() == self.solution:
            print("Correct!")
            NOVA4.east = NOVA7


marx_board = Keyboard("tombstone")


class Keyboard2(object):
    def __init__(self, solution=""):
        self.solution = solution
        self.solv = ""

    def solve(self):
        self.solv = input("What is the answer?")
        if self.solv.lower() == self.solution:
            print("Correct!")
            SUBSPACE3.east = SUBSPACE4
        else:
            print("WRONG!!! PREPARE FOR THE DRAINING OF YOUR LIFE FORCE")
            player.health -= player.health


sub_board = Keyboard2("mewtwo")

temple_bot = NPC("Shopkeeper bot model NX HAC serial no 84493587", 99999999999999, 0, 0, True)
forest_directions = Filler("UP, UP, DOWN, DOWN, LEFT, RIGHT, LEFT, RIGHT"
                           "\nKEY: UP = NORTH, DOWN = SOUTH, LEFT = WEST, RIGHT = EAST", 0)
zork_mat = Filler("Battered Rubber Mat that reads 'WELCOME TO ZORK'")
rock = NPC("", 0, 0, 0, True)

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
rock.items.append(upgrade1)
rock.items.append(key_4)


class Ice(object):
    def __init__(self):
        self.activated = False
        if watch.past:
            F_Sword.activated = True
            frost_helmet.activated = True


class Boss(Enemy):
    def __init__(self, weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon):
        super(Boss, self).__init__(weapon, health, can_ink, elecfrost, can_weapon, name, defense, mon)
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)


class Bowser(Boss):
    def __init__(self):
        super(Bowser, self).__init__(Claw, 60, False, False, True, "Bowser", 10, 1500)
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
                    player.max_health += 20
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
                    player.max_health += 20
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
                    player.max_health += 20
                    player.health = player.max_health
                print("%s has %d health left" % (self.name, self.health))
            else:
                print("You don't have enough MP to cast this")

    def take_damage(self, damage):
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
                            player.max_health += 20
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
                            player.max_health += 20
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

spider_leg = Blade(9, True, False, 9999999999999999999)


class Ghoma(Boss):
    def __init__(self, name="Ghoma"):
        super(Ghoma, self).__init__(spider_leg, 45, False, False, False, name, 8, 1000)
        self.name = "Ghoma"

    def attack(self, target):
        self.attack_choice = random.randint(1, 7)
        self.dodge_chance = random.randint(1, 12)
        if self.attack_choice == 1:
            if self.dodge_chance == 3:
                print("Ghoma attacks with its legs! But it misses!")
            else:
                print("Ghoma attacks for %d damage with its legs!" % self.weapon.attack_stat)
                target.take_damage(self.weapon.attack_stat)
        elif self.attack_choice == 2:
            if self.dodge_chance != 3:
                print("Ghoma attacks with a laser from its eye")
                target.take_damage(14)
            else:
                print("Ghoma tries to hit you with a laser from its eye but misses")
        elif self.attack_choice == 3:
            if self.dodge_chance != 1:
                print("Ghoma bites you!")
                target.take_damage(17)
            else:
                print("Ghoma tries to bite you but misses")
        elif self.attack_choice == 4:
            if self.dodge_chance != 4 or 5 or 6:
                print("Ghoma launches a harmful web at you")
                target.take_damage(24)
            else:
                print("Ghoma launches a powerful web at you but misses")
        elif self.attack_choice == 5:
            if self.dodge_chance != 8 or 9:
                print("Ghoma tries to stomp on you")
                target.take_damage(14)
            else:
                print("Ghoma tries to stomp on you but misses")
        elif self.attack_choice == 6:
            if self.dodge_chance != 10:
                print("Ghoma charges at you")
                target.take_damage(13)
            else:
                print("Ghoma charges at you but misses")
        elif self.attack_choice == 7:
            if self.dodge_chance != 11 or 12:
                print("Ghoma launches a sweeping attack with its legs and hits you")
                target.take_damage(12)
            else:
                print("Ghoma launches a sweeping attack with its legs but misses")

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


gohma = Ghoma()


class Chaos(Boss):
    def __init__(self, name="Chaos"):
        super(Chaos, self).__init__(Claw, 75, False, True, True, name, 13, 2000)
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

metal = Blade()


class Metalmario(Boss):
    def __init__(self, name="Metal Mario"):
        super(Metalmario, self).__init__(metal, 75, False, True, True, name, 13, 2000)
        self.name = "Metal Mario"

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
