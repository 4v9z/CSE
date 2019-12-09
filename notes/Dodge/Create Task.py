import pygame
import sys
bonebair = pygame.image.load("Bair Bone.png")
beam = pygame.image.load("beam.png")
blast1r = pygame.image.load("blaster.png")
blast2r = pygame.image.load("blaster charge1.png")
blast3r = pygame.image.load("blaster charge2.png")
blast4r = pygame.image.load("blaster charge3.png")
blast5r = pygame.image.load("blaster charge4.png")
blast6r = pygame.image.load("blaster unleash.png")
blast1l = pygame.image.load("blaster left.png")
blast2l = pygame.image.load("blaster charge1 left.png")
blast3l = pygame.image.load("blaster charge2 left.png")
blast4l = pygame.image.load("blaster charge3 left.png")
blast5l = pygame.image.load("blaster charge4 left.png")
blast6l = pygame.image.load("blaster unleash left.png")
crchbone = pygame.image.load("crounchy bone.png")
sandsmash = pygame.image.load("d_smash blast.png")
sandair1 = pygame.image.load("dair blaster1.png")
sandair2 = pygame.image.load("dair blaster2.png")
sandair3 = pygame.image.load("dair blaster3.png")
sanfsmash = pygame.image.load("f smash Bone.png")
sanfairbone = pygame.image.load("fair bone.png")
sanjab3 = pygame.image.load("jab3.png")
sanshielr1 = pygame.image.load("sand shield.png")
sanshielr2 = pygame.image.load("sand shield p2.png")
sanupb1 = pygame.image.load("sans upb1.png")
sanupb2 = pygame.image.load("sans upb2.png")
sanspecfall = pygame.image.load("sans spec fall.png")
sanshiell1 = pygame.image.load("sans p1 shield left.png")
sanshiell2 = pygame.image.load("sans p2 shield left.png")
sanupbl1 = pygame.image.load("sand upb1 left.png")
sanupbl2 = pygame.image.load("sans upb2 left.png")
sanspecfalll= pygame.image.load("sans spec fall left.png")
sansr = pygame.image.load("sans..png")
sanback = pygame.image.load("sans back toss.png")
sanbair = pygame.image.load("sans bair.png")
sancrchattck = pygame.image.load("sans crouch attack.png")

sandair = pygame.image.load("sans dair.png")
sanfair = pygame.image.load("sans fair.png")
getdownmrpres = pygame.image.load("sans get down mr. president right.png")
sanfortossr = pygame.image.load("sans hand right.png")
sanouch = pygame.image.load("sans hit.png")
sanidk =pygame.image.load("sans idk right.png")
sanjab1bod = pygame.image.load("sans jab1 bod.png")
sanjab2bod = pygame.image.load("sans jab2 bod.png")
sanstahp = pygame.image.load("sans STAHP right.png")
santele = pygame.image.load("sans tele.png")
sanuair = pygame.image.load("sans up air.png")
sanwalk = pygame.image.load("sans walk1.png")
sanwalk2 = pygame.image.load("sans walk 2.png")
sanuyeet = pygame.image.load("sans yeet up from right.png")
sansjab1 = pygame.image.load("sansjab1.png")
sansjab2 = pygame.image.load("sansjab2.png")
teleball = pygame.image.load("teleball.png")
u_sansh = pygame.image.load("u_smash bone.png")
uairbone = pygame.image.load("uair bone.png")
heart = pygame.image.load("_3.png")
stahpball = pygame.image.load("_3 ball.png")
downnow = pygame.image.load("_3 down.png")
rightheart = pygame.image.load("_3 right.png")
soulup = pygame.image.load("_3 up.png")
soulleft = pygame.image.load("_333.png")
stahpsoul = pygame.image.load("nyeh_3.png")
sanbackl = pygame.image.load("sans to the right but from the left.png")
sanbairl = pygame.image.load("sans bair left... or right__.png")
sancrchattckl = pygame.image.load("sans crouch attck left.png")
sancrchl = pygame.image.load("sans crouch left.png")
sandairl = pygame.image.load("sans dair left.png")
sanfairl = pygame.image.load("sans fair left.png")
getdownmrpresl = pygame.image.load("sans get down mr. president left.png")
sanfortossl = pygame.image.load("sans hand left forward.png")
sanouchl = pygame.image.load("sans hurt left.png")
sanidkl =pygame.image.load("sans idk left.png")
sanjab1bodl = pygame.image.load("sans jab1 bod left.png")
sanjab2bodl = pygame.image.load("sans jab2 bod left.png")
sanstahpl = pygame.image.load("sans STAHP left.png")
santelel = pygame.image.load("sans telekinesis on left.png")
sanuairl = pygame.image.load("sans up air left.png")
sanwalkl = pygame.image.load("sans left walk 1.png")
sanwalkl2 = pygame.image.load("sans left walk 2.png")
sansl = pygame.image.load("sans left.png")
sanuyeetl = pygame.image.load("sans yeet to sky from left.png")
sansjab1l = pygame.image.load("sansjab1left.png")
sansjab2l = pygame.image.load("sansjab2 left.png")

levels = ["battlefield"]
plat1 = pygame.image.load("battfiel platform 1.png")
plat2 = pygame.image.load("battfiel platform 2.png")
plat3 = pygame.image.load("battfiel platform 3.png")
battlefield = pygame.image.load("battlefield.png")
battle_bg = pygame.image.load("battlefield bg.png")
battlefield_sprites = [plat1, plat2, plat3, battlefield, battle_bg]
the_people = ["mario", 'sans']
pygame.init()
menu_theme = pygame.mixer.Sound("title_1.wav")
titletheme = pygame.mixer.Sound("t.wav")
error = pygame.image.load("error message.png")
starting = True
menuing = True

s1 = True
time2smash = False
s2 = False
gaming = True
screen = pygame.display.set_mode([550,400])
Mouse = [0]*2
schmoving = 0
moving = 0
sancrch = pygame.image.load("sans crounch.png").convert()
sans_sprites = [sansr, bonebair, beam, blast1r, blast2r, blast3r, blast4r, blast5r, blast6r, blast1l, blast2l, blast3l, blast4l, blast5l, blast6l,
                crchbone, sandsmash, sandair1, sandair2, sandair3, sanfsmash,sanfairbone, sanjab3, sanshielr1, sanshielr2, sanupb1, sanupb2, sanspecfall, sanshiell1, sanshiell2,
                sanupbl1, sanupbl2, sanspecfalll, sansl, sanback, sanbair, sancrchattck, sancrch, sandair, sanfair, getdownmrpres, sanfortossr, sanouch, sanidk, sanjab1bod,
                sanjab2bod, sanstahp, santele, sanuair, sanwalk, sanwalk2, sanuyeet, sansjab1, sansjab2, teleball, u_sansh, uairbone, heart, stahpball, downnow, rightheart, soulup, soulleft,
                stahpsoul, sanbackl, sanbairl, sancrchattckl, sancrchl, sandairl, sanfairl, getdownmrpresl, sanfortossl, sanouchl, sanidkl, sanjab1bodl, sanjab2bodl, sanstahpl, santelel,
                sanuairl, sanwalkl, sanwalkl2, sanuyeetl, sansjab1l, sansjab2l]
time2fight = False
correspondance = {
    "battlefield": battlefield_sprites, "sans": sans_sprites
}
title = pygame.image.load("title.png").convert()
stg_select = pygame.image.load("stage.png").convert()
menu = pygame.image.load("menu.png").convert()
crctr_select = pygame.image.load("character1.png").convert()
fightbar = pygame.image.load("FightBar.png").convert()
menu2 = pygame.image.load("menu2.jpg").convert()
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

def figure_out_stage(stag):
    for places in range(len(levels)):
        if stag.destination == levels[places]:
            the_map = levels[places]
            return the_map

def figure_out_chara(care_uh):
    for crctrs in range(len(the_people)):
        if care_uh.name == the_people[crctrs]:
            tehfighter = the_people[crctrs]
            return tehfighter

def load_a_fight():
    the_mapp = 0
    p1 = 0
    p2 = 0
    pl1 = ''
    pl2 = ''
    for stags in stages:
        if stags.m:
            the_mapp = figure_out_stage(stags)
    for chara in characterportraits:
        if chara.m:
            p1 = figure_out_chara(chara)
            pl1 = chara.name
        if chara.n:
            p2 = figure_out_chara(chara)
            pl2 = chara.name
    stage_sprites = correspondance[the_mapp]
    p1sprites = correspondance[p1]
    p2sprites = correspondance[p2]
    if len(stage_sprites) > 3:
        screen.blit(stage_sprites[4], [0,0])
        screen.blit(stage_sprites[0], [180,150])
        screen.blit(stage_sprites[1], [340,150])
        screen.blit(stage_sprites[2], [265, 100])
        screen.blit(stage_sprites[3], [160, 220])
    if pl1 == 'sans':
        screen.blit(p1sprites[0], [260, 170])


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


class fighter(pygame.sprite.Sprite):
    def __init__(self, sprite_list, name, play1, play2):
        pygame.sprite.Sprite.__init__(self)
        neutral_image = pygame.image.load(sprite_list[0])
        self.image = pygame.Surface([60, 65])
        self.image.blit(neutral_image, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 10
        self.on_stage = True
        self.jumps = 2
        self.name = name
        self.specialfall = False
        self.p1 = play1
        self.p2 = play2

    def detect_where_u_are(self):
        onstage1 = pygame.sprite.groupcollide(p1fighters, sttagess, False, False)
        onstage2 = pygame.sprite.groupcollide(p1fighters, sttagess, False, False)
        if self.p1:
            if len(onstage1) > 0 and self.rect.y > 0:
                self.on_stage = True
            else:
                self.on_stage = False

    def jump(self):
        if self.on_stage:
            jumps = 2
        elif not self.on_stage and not self.specialfall:
            jumps = 1
        else:
            jumps = 0
        if jumps > 0:
            jumps -= 1
            if self.name == "sans":
                print()




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
extremely_ready = 0
p1fighters = pygame.sprite.Group()
p2fighters = pygame.sprite.Group()
sttagess = pygame.sprite.Group()
#for i in range(len(battlefield_sprites)):
    #sttagess.add(battlefield_sprites[i])
#for i in range(len(sans_sprites)):
    #p1fighters.add(sans_sprites[i])
    #p2fighters.add(sans_sprites[i])
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
                if time2smash:
                    load_a_fight()
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
            tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
            if len(tappedacharacter) > 0:
                for crctrs in (tappedacharacter):
                    if a == crctrs.mural:
                        if crctrs.n and b == crctrs.mural2:
                            a = crctrs.mural3
                        else:
                            a = crctrs.mural2
                    elif a == crctrs.mural2:
                        if crctrs.n and b == crctrs.mural3:
                            a = crctrs.mural4
                        else:
                            a = crctrs.mural3
                    elif a == crctrs.mural3:
                        if crctrs.n and b == crctrs.mural4:
                            a = crctrs.mural5
                        else:
                            a = crctrs.mural4
                    elif a == crctrs.mural4:
                        if crctrs.n and b == crctrs.mural5:
                            a = crctrs.mural6
                        else:
                            a = crctrs.mural5
                    elif a == crctrs.mural5:
                        if crctrs.n and b == crctrs.mural6:
                            a = crctrs.mural7
                        else:
                            a = crctrs.mural6
                    elif a == crctrs.mural6:
                        if crctrs.n and b == crctrs.mural7:
                            a = crctrs.mural8
                        else:
                            a = crctrs.mural7
                    elif a == crctrs.mural7:
                        if crctrs.n and b == crctrs.mural8:
                            a = crctrs.mural
                        else:
                            a = crctrs.mural8
                    elif a == crctrs.mural8:
                        if crctrs.n and b == crctrs.mural:
                            a = crctrs.mural2
                        else:
                            a = crctrs.mural



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
            try:
                screen.blit(a, [60, 275])
            except TypeError:
                screen.blit(error, [60, 275])
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
                try:
                    screen.blit(a, [7, 71])
                except TypeError:
                    print("wow! CongraTs you found tHe hIdden Secret Awesome message! How 'Bout thAt you're so cool and Great!")
                stgsname = crctrtext.render(str(stags.name), 1, white)
                screen.blit(stgsname, (70, 370))
                extremely_ready += 1
        stages.draw(screen)
        cursors.draw(screen)
    if extremely_ready >= 1:
        screen.blit(fightbar, [0,200])
        time2smash = True
        load_a_fight()
    pygame.display.flip()

