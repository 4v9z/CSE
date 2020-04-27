import pygame
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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


grass_ground = Ground("ground.png", 0, 470)


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
                          "\nThis lets you run faster at the cost of a reduced jump height")
                    self.collectedd = True
            else:
                print("Wat?")


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 52])
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.type = "d"
        self.rect.x = 310
        self.jumps = 1
        self.rect.y = 420
        self.touchin_ground = 0
        self.can_trans = False
        self.image.blit(pygame.image.load("Duck.png"), (0, 0))

    def move(self, shmovement):
        if 575 >= self.rect.x >= 5:
            self.rect.x = self.rect.x + shmovement
        if self.rect.x < 5:
            self.rect.x = 5
        if self.rect.x > 575:
            self.rect.x = 5

    def jump(self):
        if self.jumps == 1:
            self.jumps = 0
            if 495 >= self.rect.y >= 5:
                self.rect.y -= 80
            if self.rect.y < 5:
                self.rect.y = 420
            if self.rect.y > 495:
                self.rect.y = 420

    def gravity(self):
        self.touchin_ground = pygame.sprite.groupcollide(DuckSprites, Enviros, False, False)
        if len(self.touchin_ground) > 0:
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
DuckSprites = pygame.sprite.Group()
DuckSprites.add(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard)
Enviro1 = pygame.sprite.Group()
Enviro1.add(grass_ground)
Enviros = [grass_ground]

The_Faster_Mallard = power_up("CheetahPowUp.png", 420, 420, "Cheetah Orb")
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
                x = -5
            if event.key == pygame.K_RIGHT:
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
    screen.blit(basic_sky, [0, 0])
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.move(x)
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.gravity()
    PowerUps.draw(screen)
    Enviro1.draw(screen)
    DuckSprites.draw(screen)
    pygame.display.flip()
    The_Faster_Mallard.collected()
    if The_Faster_Mallard.collectedd:
        The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.can_trans = True
    FpS.tick(16)
