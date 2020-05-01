import pygame
import sys
pygame.init()
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


grass_ground = Ground("ground.png", 0, 470)
<<<<<<< HEAD
grass_ground2 = Ground("ground.png", 0, 470)
water = Water("water.png", 80, 480)
wplat1 = WaterPlat("waterplatform.png", 210, 405)
wplat2 = WaterPlat("waterplatform.png", 210, 345)
wplat3 = WaterPlat("waterplatform.png", 210, 285)
=======
>>>>>>> parent of 9f7f187... a
grass_platform1 = Plat("gplatform.png", 500, 405)
grass_platform2 = Plat("gplatform.png", 320, 390)
grass_platform3 = Plat("gplatform.png", 180, 360)
grass_platform4 = Plat("gplatform.png", 40, 330)
grass_platform5 = Plat("gplatform.png", 40, 250)
grass_platform6 = Plat("gplatform.png", 40, 170)
grass_platform7 = Plat("gplatform.png", 180, 140)


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
                    print("Congrats! Now you can become a Cheetah Duck!"
                          "\nThis lets you run faster and run on water "
                          "at the cost of a reduced jump height")
                    self.collectedd = True
                    self.kill()
            elif self.name == "Elephant Orb":
                if not self.collectedd:
                    print("Congrats! Now you can become an Elephant Duck!"
                          "\nThis lets you pound stakes into the ground in order to access secrets or"
                          "open paths forwards")
                    self.collectedd = True
                    self.kill()


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 52])
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

    def move(self, shmovement):
        if self.type == "d":
            if 575 >= self.rect.x >= 5:
                self.rect.x = self.rect.x + shmovement
            if self.rect.x < 5:
                self.rect.x = 570
                self.rooms -= 1
            if self.rect.x > 575:
                self.rect.x = 5
                self.rooms += 1
            if self.direction == 1:
                self.image = pygame.Surface([40, 52])
                self.image.blit(pygame.image.load("Duck.png"), (0, 0))
                self.image.set_colorkey(black)
            else:
                self.image = pygame.Surface([40, 52])
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
                self.rect.x = self.rect.x + (shmovement*4)
            if self.rect.x < 5:
                self.rect.x = 570
                self.rooms -= 1
            if self.rect.x > 575:
                self.rect.x = 5
                self.rooms += 1

    def jump(self):
        if self.jumps == 1:
            self.jumps = 0
            if self.type == "d":
                if 495 >= self.rect.y >= 5:
                    self.rect.y -= 80
                if self.rect.y < 5:
                    self.rect.y = 420
                if self.rect.y > 495 and str(self.touchin_ground[0]) != "<Water sprite(in 1 groups)>":
                    self.rect.y = 420
                else:
                    print("You fell below the water's surface, never to be seen again"
                          "\n GAME OVER")
                    sys.exit
            elif self.type == "c":
                if 495 >= self.rect.y >= 5:
                    self.rect.y -= 40
                if self.rect.y < 5:
                    self.rect.y = 420
                if self.rect.y > 495:
                    self.rect.y = 420

    def gravity(self):
        self.touchin_ground = pygame.sprite.spritecollide(self, Enviros, False)
        grav = 0
        if len(self.touchin_ground) > 0 and str(self.touchin_ground[0]) != "<Water sprite(in 1 groups)>":
            grav = 0
            self.jumps = 1
        else:
            grav = 3
        self.rect.y += grav

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
                self.image = pygame.Surface([40, 52])
                self.image.blit(pygame.image.load("Duck.png"), (0, 0))
                self.image.set_colorkey(black)
                self.type = "d"
        else:
            print("You fool, you can't achieve metamorphosis yet")


The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard = Duck()
x = 0
y = 0
<<<<<<< HEAD
The_Faster_Mallard = power_up("CheetahPowUp.png", 540, 180, "Cheetah Orb")
The_Fatter_Mallard = power_up("ElePowerUp.png", 260, 245, "Elephant Orb")
=======
>>>>>>> parent of 9f7f187... a
DuckSprites = pygame.sprite.Group()
DuckSprites.add(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard)
Ducks = [The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard]
PowerUps.add(The_Fatter_Mallard)
Enviro1 = pygame.sprite.Group()
<<<<<<< HEAD
Enviro2 = pygame.sprite.Group()
Enviro3 = pygame.sprite.Group()
Enviro3.add(wplat1)
Enviro3.add(wplat2)
Enviro3.add(wplat3)
Enviro3.add(grass_ground)

Enviro2.add(water)
Enviro2.add(grass_shore1)
Enviro1.add(The_Faster_Mallard)
=======
>>>>>>> parent of 9f7f187... a
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

The_Faster_Mallard = power_up("CheetahPowUp.png", 540, 180, "Cheetah Orb")
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
        if event.type == pygame.KEYUP:
            x = 0
            y = 0
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin = False
    screen.blit(basic_sky, [0, 0])
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.move(x)
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.gravity()
    PowerUps.draw(screen)
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 0:
        Enviro1.draw(screen)
        Enviros.append(grass_ground)
        Enviros.append(grass_platform1)
        Enviros.append(grass_platform2)
        Enviros.append(grass_platform3)
        Enviros.append(grass_platform4)
        Enviros.append(grass_platform5)
        Enviros.append(grass_platform6)
        Enviros.append(grass_platform7)
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
        except ValueError:
<<<<<<< HEAD
            filler = 0
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
            filler = 0
    if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.rooms == 2:
        Enviro3.draw(screen)
        if len(Enviros) < 4:
            Enviros.append(grass_ground2)
            Enviros.append(wplat1)
            Enviros.append(wplat2)
            Enviros.append(wplat3)
    else:
        try:
            Enviros.remove(grass_ground)
            Enviros.remove(wplat1)
            Enviros.remove(wplat2)
            Enviros.remove(wplat3)
        except ValueError:
            filler = 0
=======
            print()
>>>>>>> parent of 9f7f187... a
    DuckSprites.draw(screen)
    if not The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.runnin:
        if The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.type == "c":
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image = pygame.Surface([40, 52])
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image.blit(pygame.image.load("CDuck.png"), (0, 0))
            The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.image.set_colorkey(black)
    The_Faster_Mallard.collected()
    if The_Faster_Mallard.collectedd:
        The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.can_trans = True
        screen.blit(icon1, [20, 20])
        screen.blit(icon2, [20, 60])
    if The_Fatter_Mallard.collectedd:
        screen.blit(icon3, [20, 100])
    pygame.display.flip()
<<<<<<< HEAD
    # print(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.touchin_ground)
    gaming = The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.gravity()
    print(Enviros)
=======
    print(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.touchin_ground)
    try:
        print(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.touchin_ground[0])
    except IndexError:
        print("I AM ERROR")
>>>>>>> parent of 9f7f187... a
    FpS.tick(16)
