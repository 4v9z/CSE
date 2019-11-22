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
crctrtext = pygame.font.Font(None, 26)
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
    def __init__(self, image, x, y, crctr, mural, mural2, mural3, mural4, mural5, mural6, mural7, mural8, name):
        pygame.sprite.Sprite.__init__(self)
        portimg = pygame.image.load(image)
        self.image = pygame.Surface([32, 32])
        self.image.set_colorkey(generic_the_color)
        self.image.blit(portimg, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.character = crctr
        self.m = False
        self.mural = pygame.image.load(mural)
        self.mural2 = pygame.image.load(mural2)
        self.mural3 = pygame.image.load(mural3)
        self.mural4 = pygame.image.load(mural4)
        self.mural5 = pygame.image.load(mural5)
        self.mural6 = pygame.image.load(mural6)
        self.mural7 = pygame.image.load(mural7)
        self.mural8 = pygame.image.load(mural8)
        self.name = name


p1cursor = cursor1()
supermario = ctrport('mario crctr port.png', 70, 60, 'mario', "Mario.png", "Mario (1).png",
                     "Mario (2).png", "Mario (3).png", "Mario (4).png", "Mario (5).png", "Mario (6).png",
                     "Mario (7).png", 'mario')
sand_undertale = ctrport('sans crctr port.png', 102, 60, 'sans', "Sans.png", "Sans (1).png",
                     "Sans (2).png", "Sans (3).png", "Sans (4).png", "Sans (5).png", "Sans (6).png",
                     "Sans (7).png", 'sans')
characterportraits = pygame.sprite.Group()
characterportraits.add(supermario)
characterportraits.add(sand_undertale)
characters = ['mario', 'sans']
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
a = ""
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
            if event.key == pygame.K_x:
                if ctr:
                    ctr = False
                    s1 = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
            if len(tappedacharacter) > 0:
                for crctrs in (tappedacharacter):
                    if not crctrs.m:
                        crctrs.m = True
                        a = crctrs.mural
                    elif crctrs.m:
                        crctrs.m = False
            tappedacharacter = pygame.sprite.groupcollide(cursors, characterportraits, False, False)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
            if len(tappedacharacter) > 0:
                for crctrs in (tappedacharacter):
                    if a == crctrs.mural:
                        a = crctrs.mural2
                    elif a == crctrs.mural2:
                        a = crctrs.mural3
                    elif a == crctrs.mural3:
                        a = crctrs.mural4
                    elif a == crctrs.mural4:
                        a = crctrs.mural5
                    elif a == crctrs.mural5:
                        a = crctrs.mural6
                    elif a == crctrs.mural6:
                        a = crctrs.mural7
                    elif a == crctrs.mural7:
                        a = crctrs.mural8
                    elif a == crctrs.mural8:
                        a = crctrs.mural


    if ctr:
        screen.blit(crctr_select, [0, 0])
    else:
        if s1:
            screen.blit(menu, [0,0])
        if not s1 or s2:
            screen.blit(menu2, [0,0])
    if ctr:
        for ctrs in characterportraits:
            characterportraits.draw(screen)
        cursors.draw(screen)


    if not ctr:
        if s1:
            s2 = False
        elif s2:
            s1 = False
    for crctrs in characterportraits:
        if crctrs.m:
            screen.blit(a, [60, 275])
            crctrsname = crctrtext.render(str(crctrs.name.upper()), 1, white)
            screen.blit(crctrsname, (100, 390))
    pygame.display.flip()
