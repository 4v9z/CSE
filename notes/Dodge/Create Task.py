import pygame
import sys

pygame.init()

menu_theme = pygame.mixer.Sound("title_1.wav")
titletheme = pygame.mixer.Sound("t.wav")
starting = True
menuing = True
s1 = True
s2 = False
gaming = True
screen = pygame.display.set_mode([550,400])
Mouse = [0]*2
title = pygame.image.load("title.png").convert()
menu = pygame.image.load("menu.png").convert()
crctr_select = pygame.image.load("character1.png").convert()
menu2 = pygame.image.load("menu2.png").convert()
game_clock = pygame.time.Clock()
animationclock = pygame.time.Clock()
pygame.display.set_caption("SUPER SMASH BROS. PYTHON EDITION")

black = (0, 0, 0)
white = (255, 255, 255)
generic_the_color = (42,0,69)

def update_menu(b):
    if b:
        screen.blit(menu2, [0, 0])
        b = False
    elif not b:
        screen.blit(menu, [0, 0])
        b = True
    return b


def player(a, b):
    if b == False:
        a.play()
        return True
    elif b == "stop":
        a.stop()


class cursor1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cursorimg = pygame.image.load("cursor.png")
        self.image = pygame.Surface([32,32])
        self.image.set_colorkey(black)
        self.image.blit(cursorimg, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 200

    def Move(self, Mouse):
        self.rect.x = Mouse[0]
        self.rect.y = Mouse[1]


class ctrport(pygame.sprite.Sprite):
    def __init__(self, image, x, y, crctr):
        pygame.sprite.Sprite.__init__(self)
        portimg = pygame.image.load(image)
        self.image = pygame.Surface([32, 32])
        self.image.set_colorkey(generic_the_color)
        self.image.blit(portimg, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.character = crctr


p1cursor = cursor1()
supermario = ctrport('mario crctr port.png', 70, 60, 'mario')
characterportraits = pygame.sprite.Group()
characterportraits.add(supermario)
pygame.mouse.set_visible(False)
playing = False
cursors = pygame.sprite.Group()
cursors.add(p1cursor)
while starting:
    playing = player(titletheme, playing)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
            sys.exit()
        if event.type == pygame.KEYUP:
            starting = False
    screen.blit(title, [0, 0])
    pygame.display.flip()
screen.blit(menu, [0, 0])
player(titletheme, "stop")
playing = False
ctr = False
while menuing:
    playing = player(menu_theme, playing)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuing = False
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            Mouse = list(event.pos)
            p1cursor.Move(Mouse)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                if not ctr:
                    s1 = update_menu(s1)
            if event.key == pygame.K_z:
                if s1:
                    ctr = True
                    screen.blit(crctr_select, [0,0])
    if ctr:
        screen.blit(crctr_select, [0, 0])
    else:
        if s1:
            screen.blit(menu, [0,0])
        if not s1 or s2:
            screen.blit(menu2, [0,0])
    if ctr:
        characterportraits.draw(screen)
        cursors.draw(screen)


    if not ctr:
        if s1:
            s2 = False
        elif s2:
            s1 = False
    pygame.display.flip()
