class Bag(object):
    def __init__(self):
        self.inventory = []


class Blade(object):
    def __init__(self, attack_stat=None, sharp=True, dull=False, durability=None, title=""):
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability
        self.grabbed = True

    def attack(self):
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
        print("You sharpen your weapon")
        self.durability = self.base_durability
        print("Your weapon has regained its durability")
        print()
        print("Your weapon is back to %s durability from this" % self.base_durability)

    def check(self):
        print(self.title)
        print("Attack: %s" % self.attack_stat)
        print("Remaining durability: %s" % self.durability)

    def grab(self):
        if self.grabbed:
            print("You already have this")
        else:
            print("You pick up the %s" % self.title)
            self.grabbed = True
            # add stuff to bag

    def drop(self):
        if not self.grabbed:
            print("You don't have this item")
        else:
            print("You drop the %s" % self.title)
            self.grabbed = False


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

E_Sword = Sword(25, True, False, 100, "Lightning Sword")

Light_Sword = Sword(40, True, False, 125, "Light Sword")

One_Shot = Sword(99999999999, True, False, 100000, "One-Shot Sword")

Wooden_Sword = Sword(5, True, False, 2, "Wooden Sword")
Wooden_Sword.attack()

Ancient_axe = Axe(30, True, False, 999999999999999999999999999999999999, "Ancient Axe")

Ancient_axe.attack()
Ancient_axe.sharpen()


Wooden_Sword.check()
Ancient_axe.check()

Wooden_Sword.drop()
Wooden_Sword.drop()
Wooden_Sword.grab()
Wooden_Sword.grab()
