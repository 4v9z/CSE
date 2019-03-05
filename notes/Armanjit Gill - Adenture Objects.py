aaa = 0


class Blade(object):
    def __init__(self, attack_stat=None, sharp=True, dull=False, durability=None, title=""):
        self.attack_stat = attack_stat
        self.sharp = sharp
        self.dull = dull
        self.durability = durability
        self.title = title
        self.base_durability = durability

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


class Sword(Blade):
    def __init__(self):
        super(Sword, self).__init__(5, True, False, 20, "")


class Axe(Blade):
    def __init__(self):
        super(Axe, self).__init__(28, True, False, 9999999999999999999999999999999999999999999999, "Ancient Axe")


Ancient_axe = Axe()

Ancient_axe.attack()
Ancient_axe.sharpen()
