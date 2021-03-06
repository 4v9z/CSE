import pygame
import sys

pygame.init()
menu_theme = pygame.mixer.Sound("title_1.wav")
titletheme = pygame.mixer.Sound("t.wav")
starting = True
menuing = True
time2fight = False
s1 = True
s2 = False
gaming = True
screen = pygame.display.set_mode([550,400])
Mouse = [0]*2
schmoving = 0
moving = 0
title = pygame.image.load("title.png").convert()
stg_select = pygame.image.load("stage.png").convert()
menu = pygame.image.load("menu.png").convert()
crctr_select = pygame.image.load("character1.png").convert()
fightbar = pygame.image.load("FightBar.png").convert()
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

def clicking_on_stuff(button, ctr, stg):
    a = 0
    if button == 1:
        if ctr:
            tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
            if len(tappedacharacter) > 0:
                for crctrs in (tappedacharacter):
                    if not crctrs.m:
                        crctrs.m = True
                        if crctrs.n and b == crctrs.mural:
                            a = crctrs.mural2
                        else:
                            a = crctrs.mural
                    elif crctrs.m:
                        crctrs.m = False
            tappedacharacter = pygame.sprite.groupcollide(cursors, characterportraits, False, False)
            return a
        elif stg:
            tappedastage = pygame.sprite.groupcollide(stages, cursors, False, False)
            if len(tappedastage) > 0:
                for stagess in (tappedastage):
                    if stagess.m:
                        stagess.m = False
                    else:
                        stagess.m = True
                        a = stagess.mural
            return a
    if button == 3:
        tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
        if len(tappedacharacter) > 0:
            for crctrs in (tappedacharacter):
                if a == crctrs.mural:
                    if crctrs.n and b == crctrs.mural2:
                        return crctrs.mural3
                    else:
                        return crctrs.mural2
                elif a == crctrs.mural2:
                    if crctrs.n and b == crctrs.mural3:
                        return crctrs.mural4
                    else:
                        return crctrs.mural3
                elif a == crctrs.mural3:
                    if crctrs.n and b == crctrs.mural4:
                        return crctrs.mural5
                    else:
                        return crctrs.mural4
                elif a == crctrs.mural4:
                    if crctrs.n and b == crctrs.mural5:
                        return crctrs.mural6
                    else:
                        return crctrs.mural5
                elif a == crctrs.mural5:
                    if crctrs.n and b == crctrs.mural6:
                        return crctrs.mural7
                    else:
                        return crctrs.mural6
                elif a == crctrs.mural6:
                    if crctrs.n and b == crctrs.mural7:
                        return crctrs.mural8
                    else:
                        return crctrs.mural7
                elif a == crctrs.mural7:
                    if crctrs.n and b == crctrs.mural8:
                        return crctrs.mural
                    else:
                        return crctrs.mural8
                elif a == crctrs.mural8:
                    if crctrs.n and b == crctrs.mural:
                        return crctrs.mural2
                    else:
                        return crctrs.mural
        tappedacharacter = pygame.sprite.groupcollide(cursors, characterportraits, False, False)


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


class cursor2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cursorimg = pygame.image.load("cursor2.png")
        self.image = pygame.Surface([32,32])
        self.image.set_colorkey(black)
        self.image.blit(cursorimg, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 200

    def Move(self,  direction):
        self.rect.x += direction

    def Move2(self,  direction):
        self.rect.y += direction


class stgport(pygame.sprite.Sprite):
    def __init__(self, image, x, y, the_stage, name, mural):
        pygame.sprite.Sprite.__init__(self)
        portimg = pygame.image.load(image)
        self.image = pygame.Surface([32, 32])
        self.image.set_colorkey(generic_the_color)
        self.image.blit(portimg, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destination = the_stage
        self.m = False
        self.mural = pygame.image.load(mural)
        self.name = name


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
        self.n = False
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
p2cursor = cursor2()
ready = 0
time_2_smash____phrasing_could_be_better = False
extremely_ready = 0
supermario = ctrport('mario crctr port.png', 70, 60, 'mario', "Mario.png", "Mario (1).png",
                     "Mario (2).png", "Mario (3).png", "Mario (4).png", "Mario (5).png", "Mario (6).png",
                     "Mario (7).png", 'mario')
sand_undertale = ctrport('sans crctr port.png', 102, 60, 'sans', "Sans.png", "Sans (1).png",
                     "Sans (2).png", "Sans (3).png", "Sans (4).png", "Sans (5).png", "Sans (6).png",
                     "Sans (7).png", 'sans')
the_most_basic_stage = stgport("batfeld.png", 70, 60, "battlefield", "Battlefield - Pythn", "battle ball.png")
characterportraits = pygame.sprite.Group()
stages = pygame.sprite.Group()
stages.add(the_most_basic_stage)
characterportraits.add(supermario)
characterportraits.add(sand_undertale)
characters = ['mario', 'sans']
pygame.mouse.set_visible(False)
playing = False
cursors = pygame.sprite.Group()
cursors.add(p1cursor)
cursors.add(p2cursor)
b = 0
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
stg = False
while menuing:
    playing = player(menu_theme, playing)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuing = False
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            Mouse = list(event.pos)
            p1cursor.Move(Mouse)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
                if len(tappedacharacter) > 0:
                    for crctrs in (tappedacharacter):
                        if b == crctrs.mural:
                            if crctrs.m and a == crctrs.mural2:
                                b = crctrs.mural3
                            else:
                                b = crctrs.mural2
                        elif b == crctrs.mural2:
                            if crctrs.m and a == crctrs.mural3:
                                b = crctrs.mural4
                            else:
                                b = crctrs.mural3
                        elif b == crctrs.mural3:
                            if crctrs.m and a == crctrs.mural4:
                                b = crctrs.mural5
                            else:
                                b = crctrs.mural4
                        elif b == crctrs.mural4:
                            if crctrs.m and a == crctrs.mural5:
                                b = crctrs.mural6
                            else:
                                b = crctrs.mural5
                        elif b == crctrs.mural5:
                            if crctrs.m and a == crctrs.mural6:
                                b = crctrs.mural7
                            else:
                                b = crctrs.mural6
                        elif b == crctrs.mural6:
                            if crctrs.m and a == crctrs.mural7:
                                b = crctrs.mural8
                            else:
                                b = crctrs.mural7
                        elif b == crctrs.mural7:
                            if crctrs.m and a == crctrs.mural8:
                                b = crctrs.mural
                            else:
                                b = crctrs.mural8
                        elif b == crctrs.mural8:
                            if crctrs.m and a == crctrs.mural:
                                b = crctrs.mural2
                            else:
                                b = crctrs.mural
            if event.key == pygame.K_TAB:
                tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
                if len(tappedacharacter) > 0:
                    for crctrs in (tappedacharacter):
                        if not crctrs.n:
                            crctrs.n = True
                            if crctrs.m and a == crctrs.mural:
                                b = crctrs.mural2
                            else:
                                b = crctrs.mural
                        elif crctrs.n:
                            crctrs.n = False
                tappedacharacter = pygame.sprite.groupcollide(cursors, characterportraits, False, False)
            if event.key == pygame.K_w:
                moving = -1
            if event.key == pygame.K_s:
                moving = 1
            if event.key == pygame.K_a:
                schmoving = -1
            if event.key == pygame.K_d:
                schmoving = 1
        if event.type == pygame.KEYUP:
            schmoving = 0
            moving = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                if not ctr:
                    s1 = update_menu(s1)
            if event.key == pygame.K_f:
                if time2fight:
                    screen.blit(stg_select, [0,0])
                    stg = True
                    ctr = False
                if time_2_smash____phrasing_could_be_better:
                    print()
            if event.key == pygame.K_z:
                if s1:
                    ctr = True
                    screen.blit(crctr_select, [0,0])
            if event.key == pygame.K_x:
                if ctr:
                    ctr = False
                    s1 = True
                    for crctrs in characterportraits:
                        crctrs.m = False
                        crctrs.n = False
                if stg:
                    ctr = True
                    stg = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            a = clicking_on_stuff(1, ctr, stg)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            a = clicking_on_stuff(3, ctr, stg)



    if ctr:
        screen.blit(crctr_select, [0, 0])
        if time2fight:
            screen.blit(fightbar, [0,200])
    else:
        if s1:
            screen.blit(menu, [0,0])
        if not s1 or s2:
            screen.blit(menu2, [0,0])
    if ctr:
        for ctrs in characterportraits:
            characterportraits.draw(screen)

    p2cursor.Move(schmoving)
    p2cursor.Move2(moving)

    if not ctr:
        if s1:
            s2 = False
        elif s2:
            s1 = False
    for crctrs in characterportraits:
        if crctrs.m:
            screen.blit(a, [60, 275])
            crctrsname = crctrtext.render(str(crctrs.name.upper()), 1, white)
            screen.blit(crctrsname, (200, 320))
            ready += 1
        else:
            if ready > 0:
                ready -= 1
        if crctrs.n:
            screen.blit(b, [300, 275])
            crctrsname = crctrtext.render(str(crctrs.name.upper()), 1, white)
            screen.blit(crctrsname, (420, 320))
            ready += 1
        else:
            if ready > 0:
                ready -= 1
    if ctr:
        cursors.draw(screen)


    if ready >= 2:
        if ctr:
            time2fight = True
    else:
        time2fight = False
    if stg:
        time2fight = False
        screen.blit(stg_select,[0,0])
        for stags in stages:
            if stags.m:
                screen.blit(a, [7, 71])
                stgsname = crctrtext.render(str(stags.name), 1, white)
                screen.blit(stgsname, (70, 370))
                extremely_ready += 1
        stages.draw(screen)
        cursors.draw(screen)
    if extremely_ready >= 1:
        screen.blit(fightbar, [0,200])
        time_2_smash____phrasing_could_be_better = True

    pygame.display.flip()
