class Character(object):
    def __init__(self, weapon, armor, health=20, name="", current_location=None):
        self.health = health
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.current_location = current_location

    def take_damage(self, damage):
        if damage < self.armor.defense:
            print("You took no damage!")
        else:
            self.health -= damage - self.armor.defense
            if self.health < 0:
                self.health = 0
                print("%s has been defeated!" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.attack_stat))
        target.take_damage(self.weapon.attack_stat)


class NPC(Character):
    def __init__(self, name, hp, power):
        super(NPC, self).__init__(hp, name, None, None, None)
        self.items = []
        self.power = power


class Armor(object):
    def __init__(self, defense, name=""):
        self.defense = defense
        self.grabbed = False
        self.name = name

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
    def __init__(self, defense, name=""):
        super(Helmet, self).__init__(2020, "")
        self.defense = defense
        self.name = name

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
                player.helmet = None


class Chestplate(Armor):
    def __init__(self, defense, name=""):
        super(Chestplate, self).__init__(2020, "")
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
                print("You already have a Chestplate equiped, unequip your current chestplate to equip this chestplate")
        else:
            print()

    def unequip(self):
        if self.grabbed:
            if player.chestplate is None:
                print(".......... you have nothing equipped already.... what do you want to remove")
            else:
                print("You remove the %s")
                player.chestplate = undershirt


class Boots(Armor):
    def __init__(self, defense, name=""):
        super(Boots, self).__init__(2020, "")
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
                player.boots = None


class Leggings(Armor):
    def __init__(self, defense, name=""):
        super(Leggings, self).__init__(2020, "")
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


class Weapon(object):
    def __init__(self, name=""):
        self.name = name
        self.attack_stat = 0


class Blade(Weapon):
    def __init__(self, attack_stat=None, sharp=True, dull=False, durability=None, title=""):
        super(Blade, self).__init__("  ")
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability
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
            print("Your weapon has regained its durability")
            print()
            print("Your weapon is back to %s durability from this" % self.base_durability)

    def check(self):
        if self.grabbed:
            print(self.title)
            print("Attack: %s" % self.attack_stat)
            print("Remaining durability: %s" % self.durability)

    def grab(self):
        if Inventory.inventory.__len__() < Inventory.max_space:
            if self.grabbed:
                print("You already have this")
            else:
                print("You pick up the %s" % self.title)
                self.grabbed = True
                Inventory.inventory.append(self)
                # add stuff to bag
        else:
            print("You can't carry any more items, you need to drop some items to make space")

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.title)
            self.grabbed = False
            Inventory.inventory.remove(self)


class Sword(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, title):
        super(Sword, self).__init__(5, True, False, 20, "")
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability


class Specialsword(Sword):
    def __init__(self, attack_stat, sharp, dull, durability, title, can_get=False):
        super(Specialsword, self).__init__(30, True, False, 20, "")
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability
        self.activated = can_get

    def grab(self):
            if Inventory.inventory.__len__() < Inventory.max_space:
                if self.activated:
                    if self.grabbed:
                        print("You already have this")
                    else:
                        print("You pick up the %s" % self.title)
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
            print("You drop the %s" % self.title)
            self.grabbed = False
            Inventory.inventory.remove(self)


class Axe(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, title):
        super(Axe, self).__init__()
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability


leather1 = Boots(1, "Leather Boots")

leather2 = Leggings(2, "Leather leggings")

leather3 = Chestplate(3, "Leather Chestplate")

Wooden_Sword = Sword(5, True, False, 5, "Wooden Sword")

Magic_Sword = Sword(999999999, True, False, 999999999999999999999999, "Magic Sword")

Wiebe_Armor = Chestplate(99999999999999999999999999999999999999999999999999999999, "Wiebe Armor")


class Player(object):
    def __init__(self, starting_location, health=50, helmet=None, chestplate=leather3, boots=leather1,
                 weapon=Wooden_Sword, mp=15, defense=3, leggings=leather2):
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
        self.defense = defense

    def move(self, new_location):
        """ This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction and finds the variable of the room

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not exist
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


player = Player('AA')


orc = Character(100, "Orc", Wooden_Sword, None)

wiebe = Character(999999999999999999999999,Magic_Sword, Wiebe_Armor, "Wiebe" )


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


Inventory = Bag()

F_Sword = Sword(40, True, False, 200, "Frost Sword")

Money_Sword = Sword(1, True, False, 999999999999999999999999999999999999999999, "Money Sword")

E_Sword = Sword(45, True, False, 100, "Lightning Sword")

Light_Sword = Specialsword(40, True, False, 125, "Light Sword")

One_Shot = Sword(99999999999, True, False, 100000, "One-Shot Sword")

Ancient_axe = Axe(30, True, False, 999999999999999999999999999999999999, "Ancient Axe")


class Gun(Weapon):
    def __init__(self, name="", ammo=10, attack_stat=10):
        super(Gun, self).__init__("")
        self.ammo = ammo
        self.reeeeee = ammo
        self.grabbed = False
        self.name = name
        self.attack_stat = attack_stat

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


Unnamed_gun = Gun("Unnamed Gun")


class Splattershot(Gun):
    def __init__(self, name, ammo=200, attack_stat=0):
        super(Splattershot, self).__init__("", 200)
        self.ammo = ammo
        self.reeeeee = ammo
        self.grabbed = False
        self.name = name
        self.attack_stat = attack_stat

    def shoot(self):
        if self.grabbed:
            print("You shoot your weapon, you lose some ink")
            self.ammo -= 5


Splattershot_Jr = Splattershot('Splattershot Jr')

Hero_Shot = Splattershot("Hero Shot", 400, 20)

Inventory.check()

Hero_Shot.grab()

Inventory.check()

Hero_Shot.drop()

Inventory.check()


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

scuba = Helmet(2, "Strange Scuba Mask")

space = Helmet(4, "Space Helmet")

ancient1 = Leggings(10, "Ancient Leggings")

ancient2 = Boots(5, "Ancient Boots")

ancient3 = Chestplate(13, "Ancient Chestplate")

ancient4 = Helmet(7, "Ancient Helmet")

lava = Leggings(8, "Lava Leggings")

lava2 = Boots(3, "Lava Boots")

light = Boots(4, "Light Boots")

tabuu = Chestplate(200, "")

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


class SKey(Key):
    def __init__(self, name=""):
        super(SKey, self).__init__()
        self.name = name

    def use(self):
        if self.grabbed:
            print("* You use the door key"
                  "\n * The door key created a door")


key_1 = Key("Key Fragment 1")
key_2 = Key("Key Fragment 2")
key_3 = Key("Key Fragment 3")
key_4 = Key("Key Fragment 4")

JEVIL = SKey("Door Key")


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
            self.activated = True


class Shield(object):
    def __init__(self, defense=10):
        self.defense = defense
        self.blocking = False
        self.normal_defense = defense

    def block(self):
        if not self.blocking:
            self.defense = self.defense * 1.25
            self.blocking = True

    def stop_blocking(self):
        if self.blocking:
            self.defense = self.normal_defense
            self.blocking = False


orc.attack(wiebe)

wiebe.attack(orc)
