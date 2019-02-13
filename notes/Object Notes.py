import Special_Random


class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, color="Cobalt"):
        # Things that a laptop has.
        # Everything in this lift should be relevant to the program
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = 'Linux'
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            # Computer is already charged
            if self.battery_left >= 100:
                print("The computer is already charged")
                return

            self.battery_left += time   # This adds to the battery life
            # Computer is mostly charged
            if self.battery_left > 100:
                print("The computer quickly charges.")
                self.battery_left = 100

            # Computer is not charged at all
            else:
                print("The computer is now at %d%%" % self.battery_left)
        else:
            print("It's broken. Good Job! (TVT)-^3")

    def smash(self):
        self.functioning = False
        input("How to play Smash Bros: 1. Hit the enemy with a smash attack!")
        print()
        print("....")
        print()
        print("THE ENEMY NOT YOUR COMPUTER!!!!!!!!!")

    def use(self, time):
        if self.functioning:
            self.battery_left -= time
            print("You use the laptop for %s minutes" % time)
            print('You now have %d%%' % self.battery_left)
        else:
            print("Great, it's broken, good job idiot")


my_computer = Laptop("1920x1080", 1000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("90000000000000000000000000000000000000000000000000000000000000000000000000000000"
                        "0000000000000000000000000x90000000000000000000000000000000000000000000000000000000000000"
                        "0000000000000000000000000000000000000000000000",
                        999999999999999999999999999999999999999999999999999999999999999999999999999999999999, "AWESOME")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(20)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)
wiebe_computer.smash()
wiebe_computer.use(40)

print(Special_Random.RandomWiebe.special_random())
