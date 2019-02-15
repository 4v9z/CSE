a = 0


class NintendoSwitch(object):
    def __init__(self, brightness=50, design="Red and Blue"):
        self.battery = 100
        self.brightness = brightness
        self.screenshots_taken = 0
        self.design = design
        self.working = True
        self.volume = 10
        self.game = "Home"

    def charge(self, time):
        if self.working:
            if self.battery >= 100:
                print("It can't be charged any further, but you charge it anyways")
                self.battery = 100
                return
            if self.battery > 100:
                print('You charge your Switch')
                self.battery = 100
            elif self.battery <= 0:
                print("Alright, after %s minutes, the Switch now has %d%%" % (time, self.battery))
                self.battery += time
        else:
            print("Your Switch is broken... it can't be charged")

    def open(self, game):
        if self.battery > 0:
            if self.working:
                if game.lower() in ["super smash bros", "splatoon", "kirby star allies", "mario odyssey",
                                    "pokemon let's go", "mario party"]:
                    self.game = game.lower()
                    print("You opened up %s on your Switch" % self.game)
                elif game.lower() == "home":
                    print("You go to the home menu")
                    self.game = game
                elif game.lower not in ["super smash bros", "splatoon", "kirby star allies", "mario odyssey",
                                        "pokemon let's go", "mario party"]:
                    print("You haven't bought this game")
            else:
                print("You have broken the Switch... "
                      "\n HOW DO YOU EXPECT TO PLAY GAMES ON A BROKEN CONSOLE???????")
        else:
            print("You can't open something on a dead console")

    def volume_change(self, volume):
        if self.battery > 0:
            if self.working:
                if volume >= 10:
                    self.volume = 10
                    print("You set the volume to 10")
                elif volume <= 0:
                    self.volume = 0
                    print("You set the volume to 0")
                else:
                    self.volume = volume
                    print("The volume is now %s" % self.volume)
            else:
                print("Your Switch is broken. "
                      "\n You press the buttons but you have no way of knowing what volume the Switch is at")
        else:
            print("You can't change the volume on a dead console")

    def change_bright(self, change):
        if self.battery > 0:
            if self.working:
                if change >= 100:
                    self.brightness = 100
                    print("You set the brightness to its maximum setting")
                elif change <= 0:
                    self.brightness = 0
                    print("You set the brightness to its lowest setting")
                else:
                    self.brightness = change
                    print("You set the brightness to %s" % self.brightness)
            else:
                print("It's broken... You can't do anything")
        else:
            print("Your Switch is dead, so you have no way of changing its brightness")

    def screenshot(self):
        if self.battery > 0:
            if self.working:
                if self.screenshots_taken >= 1000:
                    print("You have reached the maximum amount of screen shots you could take")
                else:
                    self.screenshots_taken += 1
                    print("You take a screen shot of this moment to make it last")
            else:
                print("Sadly, the screenshot button no longer works due to the console being broken")
        else:
            print("The Switch is dead, so you can't screenshot anything")

    def play(self, time):
        if self.battery > 0:
            if self.working:
                if self.game.lower() != "home":
                    self.battery -= time + (self.brightness * .38) + (self.volume * .31)
                    print("You play %s for some time and you have a fun time" % self.game)
                    if self.battery <= 0:
                        self.battery = 0
                elif self.game.lower() == "home":
                    self.battery = self.battery * 1
                    print("You aren't currently playing any games")
            else:
                print("......You can't seriously be trying to play games on a broken console")
        else:
            print("You can't play games on a dead console")

    def smash(self):
        print("You take your Switch and for absolutely no reason...")
        print()
        print()
        print("YOU THROW IT AT THE HECKING WALL!")
        self.working = False

    def delete(self):
        if self.working:
            if self.battery > 0:
                if self.screenshots_taken >= 1:
                    print("You delete one of your screenshots to save space")
                    self.screenshots_taken -= 1
                elif self.screenshots_taken <= 0:
                    print("You have the absolute minimum amount of space possible")
                    self.screenshots_taken = 0
            else:
                print("Charge your console first")
        else:
            print("You can't delete any screenshots due to the fact that you broke your console")


my_switch = NintendoSwitch(35, "Smash Bros Design")

my_switch.open("kiRBy sTAr alLIes")
my_switch.open("Fortnite")

while a < 1001:
    my_switch.screenshot()
    a += 1
my_switch.change_bright(50)

my_switch.play(30)
my_switch.charge(120)
my_switch.open("super smash bros")
my_switch.play(12000)
my_switch.charge(1000000000000000)
my_switch.open("home")
my_switch.play(202020)

while a >= 0:
    my_switch.delete()
    a -= 1

my_switch.open("pokemon let's go")
my_switch.play(100000000000000000000000000)

my_switch.open("kiRBy sTAr alLIes")
my_switch.open("Fortnite")


my_switch.screenshot()

my_switch.change_bright(50)

my_switch.play(30)
my_switch.charge(120)
my_switch.open("super smash bros")
my_switch.play(12000)
my_switch.charge(1000000000000000)
my_switch.open("home")
my_switch.play(202020)

my_switch.delete()

my_switch.charge(100)

my_switch.smash()
my_switch.open("kiRBy sTAr alLIes")
my_switch.open("Fortnite")


my_switch.screenshot()

my_switch.change_bright(50)

my_switch.play(30)
my_switch.charge(120)
my_switch.open("super smash bros")
my_switch.play(12000)
my_switch.charge(1000000000000000)
my_switch.open("home")
my_switch.play(202020)

my_switch.delete()
