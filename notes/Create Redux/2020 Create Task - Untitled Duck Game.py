import pygame
import sys
from termcolor import colored
pygame.init()
filler = 0
var1 = False
var2 = False
black = (0, 0, 0)
blackish = (1, 1, 1)
white = (255, 255, 255)
generic_color = (42, 0, 69)
screen = pygame.display.set_mode([580, 500])
pygame.display.set_caption("Untitled Duck Game")
pygame.mouse.set_visible(False)
title_screen = pygame.image.load("duck title.png").convert()
basic_sky = pygame.image.load("environments.png").convert()
icon1 = pygame.image.load("Ducon.png")
icon2 = pygame.image.load("CDuckon.png")
icon3 = pygame.image.load("EDuckon.png")
titling = True
FpS = pygame.time.Clock()
PowerUps = pygame.sprite.Group()


class Ground(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([580, 30])
        self.image.set_colorkey(black)
        self.image.blit(img, (0, 0))
        self.type = "ground"
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Water(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([500, 30])
        self.image.set_colorkey(black)
        self.image.blit(img, (0, 0))
        self.type = "water"
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Lava(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([500, 30])
        self.image.set_colorkey(black)
        self.image.blit(img, (0, 0))
        self.type = "lava"
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LavaPlat(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([80, 20])
        self.image.set_colorkey(black)
        self.image.blit(img, (0, 0))
        self.type = "lava"
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class WaterPlat(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([80, 20])
        self.image.set_colorkey(black)
        self.type = "platform"
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Plat(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([80, 20])
        self.image.set_colorkey(black)
        self.type = "platform"
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Stake(pygame.sprite.Sprite):
    def __init__(self, imge, imge2, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([24, 25])
        self.img2 = pygame.image.load(imge2).convert()
        self.image.set_colorkey(black)
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pounded = False

    def updateimg(self):
        self.image.blit(self.img2, (0, 0))
        if not self.pounded:
            self.rect.y += 15


grass_ground = Ground("ground.png", 0, 470)
grass_ground2 = Ground("ground.png", 0, 470)
water = Water("water.png", 80, 480)
wplat1 = WaterPlat("waterplatform.png", 210, 405)
wplat2 = WaterPlat("waterplatform.png", 210, 345)
wplat3 = WaterPlat("waterplatform.png", 210, 285)
grass_platform1 = Plat("gplatform.png", 500, 405)
grass_platform2 = Plat("gplatform.png", 320, 390)
grass_platform3 = Plat("gplatform.png", 180, 360)
grass_platform4 = Plat("gplatform.png", 40, 330)
grass_platform5 = Plat("gplatform.png", 40, 250)
grass_platform6 = Plat("gplatform.png", 40, 170)
grass_platform7 = Plat("gplatform.png", 180, 140)
grass_shore1 = Plat("gplatform.png", 0,  480)
grass_shore2 = Plat("gplatform.png", 0,  480)
grass_shore3 = Plat("gplatform.png", 0,  480)
grass_shore4 = Plat("gplatform.png", 500,  480)
wplat4 = WaterPlat("waterplatform.png", 490, 350)
wplat5 = WaterPlat("waterplatform.png", 330, 335)
wplat6 = WaterPlat("waterplatform.png", 170, 320)
wplat7 = WaterPlat("waterplatform.png", 10, 275)
wplat8 = WaterPlat("waterplatform.png", 170, 220)
wplat9 = WaterPlat("waterplatform.png", 330, 175)
grass_platform8 = Plat("gplatform.png", 490, 125)
waterbutsmaller = Water("water.png", 80, 480)
waterbutsmaller.image = pygame.Surface([420, 20])
waterbutsmaller.image.set_colorkey(black)
waterbutsmaller.image.blit(pygame.image.load("water.png").convert(), (0, 0))
Stake_2 = Stake("stake3.png", "stake4.png", 260, 455)
Stake_2.image = pygame.Surface([24, 32])
Stake_2.image.set_colorkey(black)
Stake_2.image.blit(pygame.image.load("stake3.png").convert(), (0, 0))
Stake_3 = Stake("stake5.png", "stake6.png", 50, 465)
Stake_3.image = pygame.Surface([24, 32])
Stake_3.image.set_colorkey(black)
Stake_3.image.blit(pygame.image.load("stake3.png").convert(), (0, 0))
Enviro5 = pygame.sprite.Group()
Enviro5.add(waterbutsmaller)
Enviro5.add(grass_shore3)
Enviro5.add(grass_shore4)
Enviro5.add(Stake_2)


class power_up(pygame.sprite.Sprite):
    def __init__(self, imge, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([32, 32])
        self.image.set_colorkey(black)
        self.image.blit(self.img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.touchin_player = 0
        self.collectedd = False

    def collected(self):
        self.touchin_player = pygame.sprite.groupcollide(DuckSprites, PowerUps, False, False)
        if len(self.touchin_player) > 0:
            if self.name == "Cheetah Orb":
                if not self.collectedd:
                    print(colored("Congrats! Now you can become a Cheetah Duck!"
                                  "\nThis lets you run faster and run on water "
                                  "at the cost of a reduced jump height", "yellow"))
                    self.collectedd = True
                    self.kill()
            elif self.name == "Elephant Orb":
                if not self.collectedd:
                    print(colored("Congrats! Now you can become an Elephant Duck!"
                                  "\nThis lets you pound stakes into the ground in order to access secrets or "
                                  "open paths forwards, but you move slower than erosion and can jump just about as "
                                  "high as a duck with a brick on its back", "grey", "on_white"))
                    self.collectedd = True
                    self.kill()


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 48])
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.type = "d"
        self.rooms = 0
        self.rect.x = 310
        self.jumps = 1
        self.direction = 1
        self.rect.y = 420
        self.touchin_ground = 0
        self.rect.bottom = self.rect.y + 25
        self.can_trans = False
        self.runnin = False
        self.image.blit(pygame.image.load("Duck.png"), (0, 0))

    def move(self, schmovement):
        if self.type == "d":
            if 575 >= self.rect.x >= 5:
                self.rect.x = self.rect.x + schmovement
            if self.rect.x < 5:
                if self.rooms != 0:
                    self.rect.x = 570
                    self.rooms -= 1
                else:
                    self.rect.x = 5
            if self.rect.x > 575:
                self.rect.x = 5
                self.rooms += 1
            if self.direction == 1:
                self.image = pygame.Surface([40, 48])
                self.image.blit(pygame.image.load("Duck.png"), (0, 0))
                self.image.set_colorkey(black)
            else:
                self.image = pygame.Surface([40, 48])
                self.image.blit(pygame.image.load("DuckL.png"), (0, 0))
                self.image.set_colorkey(black)
        elif self.type == "c":
            self.image = pygame.Surface([40, 52])
            if self.runnin:
                if self.direction == 1:
                    self.image.blit(pygame.image.load("CDuckRun.png"), (0, 0))
                else:
                    self.image = pygame.Surface([40, 52])
                    self.image.blit(pygame.image.load("CDuckRunL.png"), (0, 0))
                    self.image.set_colorkey(black)
            else:
                if self.direction == 1:
                    self.image.blit(pygame.image.load("CDuck.png"), (0, 0))
                else:
                    self.image = pygame.Surface([40, 52])
                    self.image.blit(pygame.image.load("CDuckL.png"), (0, 0))
                    self.image.set_colorkey(black)
            self.image.set_colorkey(black)
            if 575 >= self.rect.x >= 5:
                self.rect.x = self.rect.x + (schmovement * 4)
            if self.rect.x < 5:
                if self.rooms != 0:
                    self.rect.x = 570
                    self.rooms -= 1
                else:
                    self.rect.x = 5
            if self.rect.x > 575:
                self.rect.x = 5
                self.rooms += 1
        elif self.type == "e":
            if 575 >= self.rect.x >= 5:
                self.rect.x = self.rect.x + (schmovement * .5)
            if self.rect.x < 5:
                if self.rooms != 0:
                    self.rect.x = 570
                    self.rooms -= 1
                else:
                    self.rect.x = 5
            if self.rect.x > 575:
                self.rect.x = 5
                self.rooms += 1
            if self.direction == 1:
                self.image = pygame.Surface([40, 48])
                self.image.blit(pygame.image.load("EDuck.png"), (0, 0))
                self.image.set_colorkey(black)
            else:
                self.image = pygame.Surface([40, 48])
                self.image.blit(pygame.image.load("EDuckL.png"), (0, 0))
                self.image.set_colorkey(black)

    def jump(self):
        if self.jumps == 1:
            self.jumps = 0
            if self.type == "d":
                if 495 >= self.rect.y >= 5:
                    self.rect.y -= 100
                if self.rooms != 0:
                    if self.rect.y < 5:
                        self.rect.y = 420
            elif self.type == "c":
                if 495 >= self.rect.y >= 5:
                    self.rect.y -= 40
                if self.rect.y < 5:
                    self.rect.y = 420
                if self.rect.y > 495:
                    self.rect.y = 420
            elif self.type == "e":
                if 495 >= self.rect.y >= 5:
                    self.rect.y -= 20
                if self.rect.y < 5:
                    self.rect.y = 420
                if self.rect.y > 495:
                    self.rect.y = 420

    def gravity(self):
        self.touchin_ground = pygame.sprite.spritecollide(self, Enviros, False)
        grav = 0
        if len(self.touchin_ground) > 0:
            if str(self.touchin_ground[0]) == "<Water sprite(in 1 groups)>" and self.rect.y > 490:
                print("You fell beneath the water, never to be seen again")
                return False
            if "<Lava" in str(self.touchin_ground[0]):
                if self.type == "d":
                    print("Duck tried to swim in lava")
                elif self.type == "c":
                    print("You may be able to run on water, but lava is too hot to trot (on)")
                elif self.type == "e":
                    print("Not only did you melt in the lava, but you also fell to the bottom of it")
                return False
            try:
                if "<Lava" in str(self.touchin_ground[1]):
                    if self.type == "d":
                        print("Duck tried to dip its toes in lava")
                    elif self.type == "c":
                        print("You may be able to run on water, but lava is too hot to trot (on), even if "
                              "you're just teetering on its edge")
                    elif self.type == "e":
                        print("You kind of tripped into the lava when you dipped your toes in it, you'd "
                              "be dead either way, but this is just overkill")
                    return False
            except IndexError:
                self.touchin_ground = self.touchin_ground
            if str(self.touchin_ground[0]) != "<Water sprite(in 1 groups)>":
                if str(self.touchin_ground[0]) != "<WaterPlat sprite(in 1 groups)>":
                    grav = 0
                    self.jumps = 1
                elif str(self.touchin_ground[0]) == "<WaterPlat sprite(in 1 groups)>":
                    if self.type == "c":
                        grav = 0
                        self.jumps = 1
                    else:
                        grav = 3
                        self.jumps = 0
            elif str(self.touchin_ground[0]) == "<Water sprite(in 1 groups)>":
                if self.type == "c":
                    grav = 0
                    self.jumps = 1
                else:
                    grav = 3
                    self.jumps = 0
            try:
                if str(self.touchin_ground[1]) == "<Water sprite(in 1 groups)>":
                    if self.type == "c":
                        grav = 0
                        self.jumps = 1
                if str(self.touchin_ground[1]) == "<WaterPlat sprite(in 1 groups)>":
                    if self.type == "c":
                        grav = 0
                        self.jumps = 1
            except IndexError:
                self.touchin_ground = self.touchin_ground
        else:
            grav = 3
            self.jumps = 0
        try:
            if str(self.touchin_ground[0]) == "<Stake sprite(in 1 groups)>":
                if self.type == "e":
                    self.touchin_ground[0].image = pygame.Surface([24, 13])
                    self.touchin_ground[0].updateimg()
                    self.touchin_ground[0].pounded = True
                    self.touchin_ground[0].image.set_colorkey(black)
        except IndexError:
            self.can_trans = self.can_trans
        self.rect.y += grav
        return True

    def transform(self, plan):

        if self.can_trans:
            if self.type == plan:
                print("I'm already what you need me to be")
            if plan == "c":
                self.image = pygame.Surface([40, 52])
                self.image.blit(pygame.image.load("CDuck.png"), (0, 0))
                self.image.set_colorkey(black)
                self.type = "c"
            elif plan == "d":
                self.image = pygame.Surface([40, 48])
                self.image.blit(pygame.image.load("Duck.png"), (0, 0))
                self.image.set_colorkey(black)
                self.type = "d"
            elif plan == "e":
                if The_Fatter_Mallard.collectedd:
                    self.image = pygame.Surface([40, 48])
                    self.image.blit(pygame.image.load("EDuck.png"), (0, 0))
                    self.image.set_colorkey(black)
                    self.type = "e"
                else:
                    print("Wait a minute, you want me to be an ELEPHANT?! "
                          "\nI can't do that until I find some cool, magic orb!")
        else:
            print("You fool, you can't achieve metamorphosis yet")


The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard = Duck()
x = 0
y = 0
The_Faster_Mallard = power_up("CheetahPowUp.png", 540, 180, "Cheetah Orb")
The_Fatter_Mallard = power_up("ElePowerUp.png", 235, 245, "Elephant Orb")

Stake_1 = Stake("stake1.png", "stake2.png", 500, 445)
lavapool1 = Lava("lava.png", 80, 480)
lplat1 = LavaPlat("lava plat.png", 40, 400)
lplat2 = LavaPlat("lava plat.png", 40, 300)
lplat3 = LavaPlat("lava plat.png", 40, 200)
lplat4 = LavaPlat("lava plat.png", 200, 200)
lplat5 = LavaPlat("lava plat.png", 360, 200)
lplat6 = LavaPlat("lava plat.png", 510, 200)
oplat1 = Plat("obsidianplat.png", 40, 400)
oplat2 = Plat("obsidianplat.png", 40, 300)
oplat3 = Plat("obsidianplat.png", 40, 200)
oplat4 = Plat("obsidianplat.png", 200, 200)
oplat5 = Plat("obsidianplat.png", 360, 200)
oplat6 = Plat("obsidianplat.png", 510, 200)
wholefloorislava = Lava("lava.png", 0, 480)
wholefloorislava.image = pygame.Surface([580, 20])
wholefloorislava.image.blit(pygame.image.load("lava.png"), (0, 0))
wholefloorislava.image.set_colorkey(black)
lavawall = Lava("lava.png", 560, 0)
lavawall.image = pygame.Surface([20, 500])
oplat7 = Plat("obsidianplat.png", 0, 120)
lplat7 = LavaPlat("lava plat.png", 80, 140)
lplat8 = LavaPlat("lava plat.png", 160, 160)
lplat9 = LavaPlat("lava plat.png", 240, 180)
lplat10 = LavaPlat("lava plat.png", 320, 200)
lplat11 = LavaPlat("lava plat.png", 400, 220)
lplat12 = LavaPlat("lava plat.png", 480, 360)
lplat13 = LavaPlat("lava plat.png", 500, 380)
lplat14 = LavaPlat("lava plat.png", 420, 400)
lplat15 = LavaPlat("lava plat.png", 340, 420)
lplat16 = LavaPlat("lava plat.png", 260, 440)
lplat17 = LavaPlat("lava plat.png", 180, 460)
lplat18 = LavaPlat("lava plat.png", 100, 480)
Enviro6 = pygame.sprite.Group()
Enviro6.add(oplat7)
Enviro6.add(lplat7)
Enviro6.add(lplat8)
Enviro6.add(lplat9)
Enviro6.add(lplat10)
Enviro6.add(lplat11)
Enviro6.add(lplat12)
Enviro6.add(lplat13)
Enviro6.add(lplat14)
wholefloorislava.image.blit(pygame.image.load("lavawall.png"), (0, 0))
wholefloorislava.image.set_colorkey(black)
DuckSprites = pygame.sprite.Group()
DuckSprites.add(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard)
Ducks = [The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard]
Enviro1 = pygame.sprite.Group()
Enviro2 = pygame.sprite.Group()
Enviro4 = pygame.sprite.Group()
Enviro4.add(lavapool1)
Enviro4.add(lplat1)
Enviro4.add(lplat2)
Enviro4.add(lplat3)
Enviro4.add(lplat4)
Enviro4.add(lplat5)
Enviro4.add(lplat6)
Enviro4.add(grass_shore2)
Enviro2.add(water)
Enviro2.add(grass_shore1)
Enviro3 = pygame.sprite.Group()
Enviro3.add(The_Fatter_Mallard)
Enviro3.add(wplat1)
Enviro3.add(wplat2)
Enviro3.add(wplat3)
Enviro3.add(Stake_1)
Enviro3.add(grass_ground)
Enviro1.add(The_Faster_Mallard)
Enviro1.add(grass_ground)
Enviro1.add(grass_platform1)
Enviro1.add(grass_platform2)
Enviro1.add(grass_platform3)
Enviro1.add(grass_platform4)
Enviro1.add(grass_platform5)
Enviro1.add(grass_platform6)
Enviro1.add(grass_platform7)
Enviros = [grass_ground, grass_platform1, grass_platform2, grass_platform3,
           grass_platform4, grass_platform5, grass_platform6, grass_platform7]


def updatescreen(x):
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 0:
        Enviro1.draw(screen)
        if len(Enviros) < 8:
            Enviros.append(grass_ground)
            Enviros.append(grass_platform1)
            Enviros.append(grass_platform2)
            Enviros.append(grass_platform3)
            Enviros.append(grass_platform4)
            Enviros.append(grass_platform5)
            Enviros.append(grass_platform6)
            Enviros.append(grass_platform7)
            if len(PowerUps) < 1:
                PowerUps.add(The_Faster_Mallard)
    else:
        try:
            Enviros.remove(grass_ground)
            Enviros.remove(grass_platform1)
            Enviros.remove(grass_platform2)
            Enviros.remove(grass_platform3)
            Enviros.remove(grass_platform4)
            Enviros.remove(grass_platform5)
            Enviros.remove(grass_platform6)
            Enviros.remove(grass_platform7)
            if len(PowerUps) == 1:
                PowerUps.remove(The_Faster_Mallard)
        except ValueError:
            x = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 1:
        Enviro2.draw(screen)
        if len(Enviros) < 2:
            Enviros.append(grass_shore1)
            Enviros.append(water)
    else:
        try:
            Enviros.remove(grass_shore1)
            Enviros.remove(water)
        except ValueError:
            x = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 2:
        Enviro3.draw(screen)
        if len(Enviros) < 5:
            Enviros.append(grass_ground2)
            Enviros.append(wplat1)
            Enviros.append(wplat2)
            Enviros.append(wplat3)
            Enviros.append(Stake_1)
            if len(PowerUps) < 1:
                PowerUps.add(The_Fatter_Mallard)
    else:
        try:
            Enviros.remove(grass_ground2)
            Enviros.remove(wplat1)
            Enviros.remove(wplat2)
            Enviros.remove(wplat3)
            Enviros.remove(Stake_1)
            if len(PowerUps) == 1:
                PowerUps.remove(The_Fatter_Mallard)
        except ValueError:
            x = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 3:
        Enviro4.draw(screen)
        if len(Enviros) < 8:
            if not Stake_1.pounded:
                Enviros.append(grass_shore2)
                Enviros.append(lavapool1)
                Enviros.append(lplat1)
                Enviros.append(lplat2)
                Enviros.append(lplat3)
                Enviros.append(lplat4)
                Enviros.append(lplat5)
                Enviros.append(lplat6)
            else:
                Enviros.append(grass_shore2)
                Enviros.append(lavapool1)
                Enviros.append(oplat1)
                Enviros.append(oplat2)
                Enviros.append(oplat3)
                Enviros.append(oplat4)
                Enviros.append(oplat5)
                Enviros.append(oplat6)
    else:
        try:
            if not Stake_1.pounded:
                Enviros.remove(grass_shore2)
                Enviros.remove(lavapool1)
                Enviros.remove(lplat1)
                Enviros.remove(lplat2)
                Enviros.remove(lplat3)
                Enviros.remove(lplat4)
                Enviros.remove(lplat5)
                Enviros.remove(lplat6)
            else:
                Enviros.remove(grass_shore2)
                Enviros.remove(lavapool1)
                Enviros.remove(oplat1)
                Enviros.remove(oplat2)
                Enviros.remove(oplat3)
                Enviros.remove(oplat4)
                Enviros.remove(oplat5)
                Enviros.remove(oplat6)
        except ValueError:
            x = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 4:
        Enviro5.draw(screen)
        if len(Enviros) < len(Enviro5):
            if not Stake_2.pounded:
                Enviros.append(grass_shore3)
                Enviros.append(grass_shore4)
                Enviros.append(Stake_2)
                Enviros.append(waterbutsmaller)
            else:
                Enviros.append(grass_shore3)
                Enviros.append(grass_shore4)
                Enviros.append(Stake_2)
                Enviros.append(waterbutsmaller)
                Enviros.append(wplat4)
                Enviros.append(wplat5)
                Enviros.append(wplat6)
                Enviros.append(wplat7)
                Enviros.append(wplat8)
                Enviros.append(wplat9)
                Enviros.append(grass_platform8)
    else:
        try:
            if not Stake_2.pounded:
                Enviros.remove(grass_shore3)
                Enviros.remove(grass_shore4)
                Enviros.remove(Stake_2)
                Enviros.remove(waterbutsmaller)
            else:
                Enviros.remove(grass_shore3)
                Enviros.remove(grass_shore4)
                Enviros.remove(Stake_2)
                Enviros.remove(waterbutsmaller)
                Enviros.remove(wplat4)
                Enviros.remove(wplat5)
                Enviros.remove(wplat6)
                Enviros.remove(wplat7)
                Enviros.remove(wplat8)
                Enviros.remove(wplat9)
                Enviros.remove(grass_platform8)
        except ValueError:
            x = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 5:
        Enviro6.draw(screen)
        if len(Enviros) < len(Enviro6):
            Enviros.append(oplat7)
            Enviros.append(lplat7)
            Enviros.append(lplat8)
            Enviros.append(lplat9)
            Enviros.append(lplat10)
            Enviros.append(lplat11)
            Enviros.append(lplat12)
            Enviros.append(lplat13)
            Enviros.append(lplat14)
    else:
        try:
            Enviros.remove(oplat7)
            Enviros.remove(lplat7)
            Enviros.remove(lplat8)
            Enviros.remove(lplat9)
            Enviros.remove(lplat10)
            Enviros.remove(lplat11)
            Enviros.remove(lplat12)
            Enviros.remove(lplat13)
            Enviros.remove(lplat14)
        except ValueError:
            x = 0


PowerUps.add(The_Faster_Mallard)
gaming = True
while titling:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titling = False
            gaming = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                titling = False
    screen.blit(title_screen, [0, 0])
    pygame.display.flip()
while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.direction = 0
                if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.type == "c":
                    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin = True
                x = -5
            if event.key == pygame.K_RIGHT:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.direction = 1
                if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.type == "c":
                    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin = True
                x = 5
            if event.key == pygame.K_UP:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.jump()
            if event.key == pygame.K_c:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.transform("c")
            if event.key == pygame.K_d:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.transform("d")
            if event.key == pygame.K_e:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.transform("e")
            if event.key == pygame.K_w:
                The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rect.y -= 200
            if event.key == pygame.K_u:
                x = -10
            if event.key == pygame.K_i:
                x = 10
        if event.type == pygame.KEYUP:
            x = 0
            y = 0
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin = False
    screen.blit(basic_sky, [0, 0])
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.move(x)
    updatescreen(filler)
    DuckSprites.draw(screen)
    if not The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin:
        if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.type == "c":
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image = pygame.Surface([40, 52])
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image.blit(pygame.image.load("CDuck.png"), (0, 0))
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image.set_colorkey(black)
    The_Faster_Mallard.collected()
    The_Fatter_Mallard.collected()
    if The_Faster_Mallard.collectedd:
        The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.can_trans = True
        screen.blit(icon1, [20, 20])
        screen.blit(icon2, [20, 55])
    if The_Fatter_Mallard.collectedd:
        screen.blit(icon3, [20, 80])
    pygame.display.flip()
    gaming = The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.gravity()
    FpS.tick(16)
    if Stake_1.pounded:
        if not var1:
            var1 = True
            Enviro4.remove(lplat1)
            Enviro4.remove(lplat2)
            Enviro4.remove(lplat3)
            Enviro4.remove(lplat4)
            Enviro4.remove(lplat5)
            Enviro4.remove(lplat6)
            Enviro4.add(oplat1)
            Enviro4.add(oplat2)
            Enviro4.add(oplat3)
            Enviro4.add(oplat4)
            Enviro4.add(oplat5)
            Enviro4.add(oplat6)
    if Stake_2.pounded:
        if not var2:
            var2 = True
            Enviro5.add(wplat4)
            Enviro5.add(wplat5)
            Enviro5.add(wplat6)
            Enviro5.add(wplat7)
            Enviro5.add(wplat8)
            Enviro5.add(wplat9)
            Enviro5.add(grass_platform8)
        Stake_2.image = pygame.Surface([24, 20])
        Stake_2.image.set_colorkey(black)
        Stake_2.image.blit(pygame.image.load("stake4.png").convert(), (0, 0))
    print(str(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rect.x) + " " + str(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rect.y))
print(colored("GAME OVER", "red"))
