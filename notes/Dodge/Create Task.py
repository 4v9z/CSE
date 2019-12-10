#import random
# All sprites were created by me
# Super Smash Bros, Mario, and Luigi , as well as any other Mario characters referenced by
# Mario's costumes are properties owned by Nintendo

# Toby Fox owns sans and any Undertale character referenced in alternate costumes
# Credit to menu music goes to McLeodGames (uploaded to YouTube by SmashFlashSoundtrack)
# https://www.youtube.com/watch?v=LzxDZ-FHLEQ

# All other music is owned by Nintendo, The Pokemon Company, Microsoft, Toby Fox, or GameFreak

# Title music by EchoNotGecko -  https://www.youtube.com/watch?v=QFfAj5iix44
import pygame
import sys
import pygame

pygame.init()
black = (0, 0, 0)
blackish = (1, 1, 1)
white = (255, 255, 255)
generic_the_color = (42,0,69)
screen = pygame.display.set_mode([550,400])
sancrch = pygame.image.load("sans crounch.png").convert()
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
sanupb1 = pygame.image.load("sans upb1.png")
sanupb2 = pygame.image.load("sans upb2.png")
sanspecfall = pygame.image.load("sans spec fall.png")
sanupbl1 = pygame.image.load("sand upb1 left.png")
sanupbl2 = pygame.image.load("sans upb2 left.png")
sanspecfalll= pygame.image.load("sans spec fall left.png")
sansr = pygame.image.load("sans..png")
void = pygame.image.load("void.png")
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
SanBlaster = pygame.image.load("gasterblaster.png").convert()
SanBlastel = pygame.image.load("gasterblaster clone.png").convert
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
sans_sprites = [sansr, bonebair, beam, blast1r, blast2r, blast3r, blast4r, blast5r, blast6r, blast1l, blast2l, blast3l, blast4l, blast5l, blast6l,
                crchbone, sandsmash, sandair1, sandair2, sandair3, sanfsmash,sanfairbone, sanjab3, sanupb1, sanupb2, sanspecfall,
                sanupbl1, sanupbl2, sanspecfalll, sansl, sanback, sanbair, sancrchattck, sancrch, sandair, sanfair, getdownmrpres, sanfortossr, sanouch, sanidk, sanjab1bod,
                sanjab2bod, sanstahp, santele, sanuair, sanwalk, sanwalk2, sanuyeet, sansjab1, sansjab2, teleball, u_sansh, uairbone, heart, stahpball, downnow, rightheart, soulup, soulleft,
                stahpsoul, sanbackl, sanbairl, sancrchattckl, sancrchl, sandairl, sanfairl, getdownmrpresl, sanfortossl, sanouchl, sanidkl, sanjab1bodl, sanjab2bodl, sanstahpl, santelel,
                sanuairl, sanwalkl, sanwalkl2, sanuyeetl, sansjab1l, sansjab2l]
sanss_sprites = [sansr, bonebair, beam, blast1r, blast2r, blast3r, blast4r, blast5r, blast6r, blast1l, blast2l, blast3l, blast4l, blast5l, blast6l,
                crchbone, sandsmash, sandair1, sandair2, sandair3, sanfsmash,sanfairbone, sanjab3, sanupb1, sanupb2, sanspecfall,
                sanupbl1, sanupbl2, sanspecfalll, sansl, sanback, sanbair, sancrchattck, sancrch, sandair, sanfair, getdownmrpres, sanfortossr, sanouch, sanidk, sanjab1bod,
                sanjab2bod, sanstahp, santele, sanuair, sanwalk, sanwalk2, sanuyeet, sansjab1, sansjab2, teleball, u_sansh, uairbone, heart, stahpball, downnow, rightheart, soulup, soulleft,
                stahpsoul, sanbackl, sanbairl, sancrchattckl, sancrchl, sandairl, sanfairl, getdownmrpresl, sanfortossl, sanouchl, sanidkl, sanjab1bodl, sanjab2bodl, sanstahpl, santelel,
                sanuairl, sanwalkl, sanwalkl2, sanuyeetl, sansjab1l, sansjab2l]
def update_menu(b):
    if b:
        screen.blit(menu2, [0, 0])
        b = False
    elif not b:
        screen.blit(menu, [0, 0])
        b = True
    return b
# Child Algorithm 2
def figure_out_stage(stag):
    for places in range(len(levels)):
        if stag.destination == levels[places]:
            the_map = levels[places]
            return the_map
# Child Algorithm 1
def figure_out_chara(care_uh):
    for crctrs in range(len(the_people)):
        if care_uh.name == the_people[crctrs]:
            tehfighter = the_people[crctrs]
            return tehfighter

#Main Algorithm
def load_a_fight(player1, player2,):
    the_mapp = 0
    p1 = ''
    p2 = ''
    for stags in stages:
        if stags.m:
            the_mapp = figure_out_stage(stags)
    for chara in characterportraits:
        if chara.m:
            p1 = figure_out_chara(chara)
            if player1 == p1:
                p1 = ""
        if chara.n:
            p2 = figure_out_chara(chara)
            if player2 == p2:
                p2 = ""
    stage_sprite = correspondance[the_mapp]
    screen.blit(stage_sprite, [0,0])
    if p1 == 'sans':
        return sans
    elif p1 == 'mario':
        return mario_sprites
    if p2 == 'sans':
        return sans
    elif p2 == "mario":
        return mario_sprites


def clicking_on_stuff(button, ctr, stg):
    a = 0
    if button == 1:
        if ctr:
            tappedacharacter = pygame.sprite.groupcollide(characterportraits, cursors, False, False)
            if len(tappedacharacter) > 0:
                for crctrs in (tappedacharacter):
                    if not crctrs.m:
                        crctrs.m = True
                        for i in p1fighters:
                            if crctrs.name == i.name:
                                i.chosen = True
                            else:
                                i.chosen = False
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


class batfeld(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge).convert()
        self.image = pygame.Surface([250, 125])
        self.image.set_colorkey(black)
        self.image.blit(img, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class platform(pygame.sprite.Sprite):
    def __init__(self, imge, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imge)
        self.image = pygame.Surface([80,20])
        self.image.blit(img,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


battlefield = batfeld('battlefield.png', 160, 220)
plat1 = platform("battfiel platform 1.png", 180, 150)
plat2 = platform("battfiel platform 2.png", 340, 150)
plat3 = platform("battfiel platform 3.png", 265, 100)



# sons = fighter(sans_sprites,"sons", False, False, 230, 170)
# This solely existed for me to check if some code worked


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


fdport = stgport("fd port.png", 102,60, 'fd', "Final Destination", "fd mural.png")


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

# p1fighters.add(sons)
sttagess = pygame.sprite.Group()
#for i in range(len(battlefield_sprites)):
    #sttagess.add(battlefield_sprites[i])
sttagess.add(battlefield)
sttagess.add(plat1)
sttagess.add(plat2)
sttagess.add(plat3)

class blaster(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = sprite
        self.image = pygame.Surface([20, 29])
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.attacking = False
        self.rect.y = y
        self.damage = 40
        self.knockback = 20

class SANS(pygame.sprite.Sprite):
    def __init__(self, sprite_list, name, p1, p2, x, y):
        pygame.sprite.Sprite.__init__(self)
        neutral_image = sprite_list[0]
        self.sprites = sprite_list
        self.image = pygame.Surface([60, 65])
        self.image.blit(neutral_image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.attacking = False
        self.play1 = p1
        self.play2 = p2
        self.rect.y = y
        self.damage = 0
        self.on_stage = True
        self.jumps = 2
        self.current_image = self.sprites[0]
        self.name = name
        self.direction = 0
        self.specialfall = False
        self.blasting = False
        self.vulnerable = True
        self.walk_time = pygame.time.get_ticks() + 16
        self.gravity = 10
        self.next_jump = pygame.time.get_ticks() - 15
        self.chosen = False

    def detect_where_u_are(self, a, b):
        if fightin:
            if self.play1:
                if len(a) > 0:
                    for i in (sttagess):
                        if self.rect.y == i.rect.y - 50:
                            self.on_stage = True
                else:
                    self.on_stage = False
                if self.on_stage:
                    self.jumps = 2
                elif self.on_stage == False:
                    if self.specialfall:
                        self.jumps = 0
                    else:
                        if self.jumps != 0:
                            self.jumps = 1
            elif self.play2:
                if len(b) > 0:
                    for i in (sttagess):
                        if self.rect.y == i.rect.y - 50:
                            self.on_stage = True
                else:
                    self.on_stage = False
                if self.on_stage:
                    self.jumps = 2
                elif self.on_stage == False:
                    if self.specialfall:
                        self.jumps = 0
                    else:
                        if self.jumps != 0:
                            self.jumps = 1

    def delete(self):
        self.kill()

    def attack(self, attacknum):
        if attacknum == 1:
            self.image = pygame.Surface([57, 500])
            self.image.blit(SanBlaster, (0, 0))
            self.
        if attacknum == 2:
            self.image = pygame.Surface([70, 65])
            self.image.blit(SanUSmash, (0, 0))
        if attacknum == 3:
            self.image = pygame.Surface([60, 65])
            self.image.blit(sanupb1, (0, 0))
            self.kill()
            self.rect.y += 90
            self.specialfall = True
            self.image.blit(sanspecfall, (0,0))
        if attacknum == 4:
            self.image = pygame.Surface([70, 65])
            self.image.blit(SHIELD, (0, 0))


    def jump(self):
        if time2smash:

            if self.jumps > 0:
                if pygame.time.get_ticks() > self.next_jump:
                    next_jump = pygame.time.get_ticks() + 64
                    if self.name == "sans":
                        if self.jumps != 0:
                            self.rect.y -= 40
                    if self.jumps == 1:
                        self.jumps = 0
                    if self.jumps == 2:
                        self.jumps = 1

    def grravity(self):
        if fightin:
            if self.on_stage:
                self.gravity = 0
            else:
                self.gravity = 2
            self.rect.y += self.gravity

    def Move1(self, schmovement):
            self.rect.x += schmovement
            if schmovement > 0:
                self.direction = 0
                self.image.blit(void, (0, 0))
                if self.current_image != self.sprites[45]:
                    self.image.blit(self.sprites[45], (0, 0))
                    self.current_image = self.sprites[45]
                else:
                    self.current_image = self.sprites[46]
                    self.image.blit(self.sprites[46],(0,0))
            elif schmovement < 0:
                self.image.blit(void, (0,0))
                self.direction = 1
                if self.current_image != self.sprites[75]:
                    self.image.blit(self.sprites[75], (0, 0))
                    self.current_image = self.sprites[75]
                else:
                    self.current_image = self.sprites[76]
                    self.image.blit(self.sprites[76], (0, 0))
#            hittingp1 = pygame.sprite.groupcollide(p1fighters, p2fighters, False, False)
#            hittingp2 = pygame.sprite.groupcollide(p2fighters, p1fighters, False, False)
#            if hittingp1:
#                sans.take_damage(20,40, 20)
#            if hittingp2:
#                sanss.take_damage(20,40,20)

    def take_damage(self, damage, velocityh, velocityv):
        self.damage += damage
        self.rect.y += velocityv * (.25 * self.damage)
        if self.on_stage:
            self.rect.y -= velocityv * (.25 * self.damage)
        self.rect.x += velocityh * (.25 * self.damage)






sans = SANS(sans_sprites, "sans", True, False, 234, 156)
sanss = SANS(sanss_sprites, "sans", False, True, 284, 156)
extremely_ready = 0
p1fighters = pygame.sprite.Group()
p1fighters.add(sans)
p2fighters = pygame.sprite.Group()
p2fighters.add(sanss)
levels = ["battlefield", 'fd']
battle_bg = pygame.image.load("battlefield bg.png")
fdbg = pygame.image.load("fd bg.png")
battlefield_sprites = [battle_bg]
the_people = ["mario", sans]

menu_theme = pygame.mixer.Sound("title_1.wav")
titletheme = pygame.mixer.Sound("t.wav")
m1 = pygame.mixer.Sound("Calamari.wav")
m2 = pygame.mixer.Sound("Ghirahim.wav")
m3 = pygame.mixer.Sound("Gourmet Race.wav")
m5 = pygame.mixer.Sound("MEGALOVANIA.wav")
m7 = pygame.mixer.Sound("Spiral Mountain.wav")
m8 = pygame.mixer.Sound("VS Bede.wav")
m9 = pygame.mixer.Sound("VS Marnie.wav")
m10 = pygame.mixer.Sound("VS Zacian.wav")
#m11 = pygame.mixer.Sound("VS Zacian(Slumbering Weald).wav")
starting = True
menuing = True

s1 = True
time2smash = False
fightin = False
s2 = False
gaming = True

Mouse = [0]*2
schmoving = 0
mooving = 0
moving = 0

mario_sprites = [] # I was going to come back to this later... No time now
time2fight = False
correspondance = {
    "battlefield": battle_bg, "sans": sans_sprites, 'final destination': fdbg
}
title = pygame.image.load("title.png").convert()
p1crctr = 0
p2crctr = 0
error = pygame.image.load("error message.png").convert()
stg_select = pygame.image.load("stage.png").convert()
menu = pygame.image.load("menu.png").convert()
crctr_select = pygame.image.load("character1.png").convert()
fightbar = pygame.image.load("FightBar.png").convert()
menu2 = pygame.image.load("menu2.jpg").convert()
crctrtext = pygame.font.Font(None, 26)
game_clock = pygame.time.Clock()
animationclock = pygame.time.Clock()
pygame.display.set_caption("SUPER SMASH BROS. PYTHON EDITION")


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
pygame.mouse.set_visible(False)
playing = False
z = 0
#music = [m1, m2, m3, m5, m7, m8, m9, m10]
#will_play = random.choice(music) # This somehow doesn't work...
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
titletheme.stop()
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
            if event.key == pygame.K_RIGHT:
                if fightin:
                    schmoving = 8
            if event.key == pygame.K_d:
                if fightin:
                    mooving = 8
            if event.key == pygame.K_LEFT:
                if fightin:
                    schmoving = -8
            if event.key == pygame.K_a:
                if fightin:
                    mooving = -8
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
                            for i in p2fighters:
                                if crctrs.name == i.name:
                                    i.chosen = True
                                else:
                                    i.chosen = False
                            if crctrs.m and a == crctrs.mural:
                                b = crctrs.mural2
                            else:
                                b = crctrs.mural
                        elif crctrs.n:
                            crctrs.n = False
                tappedacharacter = pygame.sprite.groupcollide(cursors, characterportraits, False, False)
            if event.key == pygame.K_w:
                moving = -5
            if event.key == pygame.K_s:
                moving = 5
            if event.key == pygame.K_a:
                if not fightin:
                    schmoving = -5
            if event.key == pygame.K_d:
                if not fightin:
                    schmoving = 5
        if event.type == pygame.KEYUP:
            mooving = 0
            for i in p1fighters:

                i.image.blit(void,(0,0))
                if i.direction == 0:
                    i.image.blit(i.sprites[0],(0,0))
                else:
                    i.image.blit(i.sprites[29],(0,0))
            schmoving = 0
            moving = 0
            if event.key == pygame.K_UP:
                if time2smash:
                    for i in p1fighters:
                        i.jump()
            if event.key == pygame.K_w:
                if time2smash:
                    sanss.jump()
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                if not ctr and not time2smash:
                    s1 = update_menu(s1)
            if event.key == pygame.K_f:
                if time2fight:
                    screen.blit(stg_select, [0,0])
                    stg = True
                    ctr = False
                if time2smash:
                    fightin = True
                    p1crctr = load_a_fight(p1crctr, p2crctr)
                    p2crctr = load_a_fight(p1crctr, p2crctr)
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
        if not time2smash:
            if s1:
                screen.blit(menu, [0,0])
            if not s1 or s2:
                screen.blit(menu2, [0,0])
    if ctr:
        for ctrs in characterportraits:
            characterportraits.draw(screen)

    p2cursor.Move(schmoving)
    p2cursor.Move2(moving)
    if fightin:
        for i in p1fighters:
            i.Move1(schmoving)
    if fightin:
        for i in p2fighters:
            i.Move1(mooving)

    if not ctr and not time2smash:
        if s1:
            s2 = False
        elif s2:
            s1 = False
    for crctrs in characterportraits:
        if crctrs.m:
            if not time2smash:
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
            if not time2smash:
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
                    input("wow! congraTs you found tHe hIdden Secret Awesome message! how 'Bout that yoU're so cool and Great!")
                stgsname = crctrtext.render(str(stags.name), 1, white)
                screen.blit(stgsname, (70, 370))
                extremely_ready += 1
        stages.draw(screen)
        cursors.draw(screen)
    if extremely_ready >= 1:
        screen.blit(fightbar, [0,200])
        time2smash = True

        #player(menu_theme, "stop")
        #if playing == True and z == 0:
            #playing = False

        #playing = player(will_play, playing)
        z += 1
        ctr = False
        stg = False
        time2fight = False
    if fightin:
        p1crctr = load_a_fight(p1crctr, p2crctr)
        p2crctr = load_a_fight(p1crctr, p2crctr)
        sttagess.draw(screen)
        for i in p1fighters:
            if i.chosen:
                p1fighters.draw(screen)
            else:
                i.delete()
                p1fighters.remove(i)
        for i in p2fighters:
            if i.chosen:
                p2fighters.draw(screen)
            else:
                i.delete()
                p2fighters.remove(i)
    onstage1 = pygame.sprite.groupcollide(p1fighters, sttagess, False, False)
    onstage2 = pygame.sprite.groupcollide(p2fighters, sttagess, False, False)
    for crctrs in p1fighters:
        crctrs.detect_where_u_are(onstage1, onstage2)
        crctrs.grravity()
    for crctrs in p2fighters:
        crctrs.detect_where_u_are(onstage1, onstage2)
        crctrs.grravity()

    if -10 > sans.rect.x or sans.rect.x > 555 or -10 > sans.rect.y or sans.rect.y > 410:
        input("P2 WINS!!")
        sys.exit()
    if -10 > sanss.rect.x or sanss.rect.x > 555 or -10 > sanss.rect.y or sanss.rect.y > 410:
        input("P1 WINS!!")
        sys.exit()
    print(sanss.rect.x)
    print(sanss.rect.y)



    pygame.display.flip()
    game_clock.tick(16)

