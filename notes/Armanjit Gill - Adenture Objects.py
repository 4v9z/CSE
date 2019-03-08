class Player(object):
    def __init__(self, starting_location, health=50, helmet=None, chestplate='Leather Shirt', boots='Leather Boots',
                 weapon="Wooden Sword"):
        self.health = health
        self.inventory = []
        self.current_location = starting_location
        self.helmet = helmet
        self.chestplate = chestplate
        self.boots = boots
        self.defense = 5
        self.MP = 15
        self.weapon = weapon
        self.max_health = health

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


class Bag(object):
    def __init__(self):
        self.inventory = []

    def check(self):
        print()
        print("You have the following items: ")
        for num, item in enumerate(self.inventory):
            print(str(num + 1) + ": " + item.name)
        print()


Inventory = Bag()


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
        if self.grabbed:
            print("You already have this")
        else:
            print("You pick up the %s" % self.title)
            self.grabbed = True
            Inventory.inventory.append(self)
            # add stuff to bag

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


class Axe(Blade):
    def __init__(self, attack_stat, sharp, dull, durability, title):
        super(Axe, self).__init__()
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability


Money_Sword = Sword(1, True, False, 999999999999999999999999999999999999999999, "Money Sword")

E_Sword = Sword(45, True, False, 100, "Lightning Sword")

Light_Sword = Sword(40, True, False, 125, "Light Sword")

One_Shot = Sword(99999999999, True, False, 100000, "One-Shot Sword")

Wooden_Sword = Sword(5, True, False, 5, "Wooden Sword")

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
        if self.grabbed:
            print("You already have this")
        else:
            print("You pick up the %s" % self.name)
            self.grabbed = True
            Inventory.inventory.append(self)
            # add stuff to bag

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


class Health(Consumables):
    def __init__(self, name="", restore1=20):
        super(Health, self).__init__("")
        self.name = name
        self.restore = restore1

    def use(self):
        if self.grabbed:

            if player.health + self.restore <= player.health:
                player.health += self.restore
                print("You eat the %s, and restore %i health" % (self.name, self.restore))
            elif player.health + self.restore > player.health:
                print("You eat the %s and your health is maxed out" % self.name)
                player.health = player.max_health

    def grab(self):
        if self.grabbed:
            print("You already have this")
        else:
            print("You pick up the %s" % self.name)
            self.grabbed = True
            Inventory.inventory.append(self)
            # add stuff to bag

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
            if player.health + self.restore <= player.health:
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
