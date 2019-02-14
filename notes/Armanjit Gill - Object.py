a = 0

class NintendoSwitch(object):
    def __init__(self, brightness=50, design="Red and Blue"):
        self.battery = 100
        self.brightness = brightness
        self.screenshots_taken = 0
        self.design = design
        self.on = True
        self.working = True
        self.volume = 10
        self.playing = False
        self.game = "Home"

    def charge(self, time):
        if self.working:
            if self.battery >= 100:
                print("It can't be charged any further, but you charge it anyways")
                return
            if self.battery > 100:
                print('You charge your Switch')
                self.battery = 100
            else:
                print("Alright, after %s minutes, the Switch now has %d%%" % (time, self.battery))
        else:
            print("Your Switch is broken... it can't be charged")

    def open(self, game):
        if self.working:
            if game.lower() in ["super smash bros", "splatoon", "kirby star allies", "mario odyssey",
                                "pokemon let's go", "mario party"]:
                self.game = game
                print("You opened up %s on your Switch" % self.game)
            elif game.lower() == "home":
                print("You go to the home menu")
                self.game = game
        else:
            print("You have broken the Switch... "
                  "\n HOW DO YOU EXPECT TO PLAY GAMES ON A BROKEN CONSOLE???????")

    def volume_change(self, volume):
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

    def brightness_change(self, change):
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

    def screenshot(self):
        if self.working:
            if self.screenshots_taken <= 1000:
                print("You have reached the maximum amount of screen shots you could take")
            else:
                self.screenshots_taken += 1
                print("You take a screen shot of this moment to make it last")
        else:
            print("Sadly, the screenshot button no longer works due to the console being broken")

    def play(self):
        if self.working:
            if self.game.lower() != "home":
                print("You play %s")


my_Switch = NintendoSwitch()
while a == 0:
    my_Switch.screenshot()
