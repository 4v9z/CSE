import pygame
pygame.init()
black = (0, 0, 0)
blackish = (1, 1, 1)
white = (255, 255, 255)
generic_color = (42,0,69)
screen = pygame.display.set_mode([580,500])
pygame.display.set_caption("Untitled Duck Game")
pygame.mouse.set_visible(False)
title_screen = pygame.image.load("duck title.png").convert()
basic_sky = pygame.image.load("environments.png").convert()

titling = True
FpS = pygame.time.Clock()


class ground(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([580, 30])
        self.image.set_colorkey(black)
        self.image.blit(img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


grass_ground = ground("ground.png", 0, 470)


class Duck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 52])
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 420
        self.touchin_ground = 0

        self.image.blit(pygame.image.load("Duck.png"), (0, 0))

    def move(self, shmovement):
        if 575 >= self.rect.x >= 5:
            self.rect.x = self.rect.x + shmovement
        if self.rect.x < 5:
            self.rect.x = 5
        if self.rect.x > 575:
            self.rect.x = 5

    def jump(self):
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
        else:
            grav = 3
        self.rect.y += grav


The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard = Duck()
x = 0
y = 0
DuckSprites = pygame.sprite.Group()
DuckSprites.add(The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard)
Enviro = pygame.sprite.Group()
Enviro.add(grass_ground)
Enviros = [grass_ground]
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
        if event.type == pygame.KEYUP:
            x = 0
            y = 0
    screen.blit(basic_sky, [0, 0])
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.move(x)
    The_Man_With_A_Plan_The_Mallard_Thats_A_Hazard.gravity()
    DuckSprites.draw(screen)
    Enviro.draw(screen)
    pygame.display.flip()
    FpS.tick(16)
