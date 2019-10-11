# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries
import random

# Define Classes (sprites) here


class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.timecreated = pygame.time.get_ticks()
        self.image = pygame.Surface([30, 30])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 670)
        self.rect.y = 0

    def setImage(self, graphicSelected):
        fallingObjectsImage = pygame.image.load(graphicSelected)
        self.image.blit(fallingObjectsImage, (0, 0))

    def moveFallingObjects(self, distance):
        if self.rect.y <= 470:
            self.rect.y = self.rect.y + distance

    def deleteFallingObjects(self):
        caught = pygame.sprite.groupcollide(allFallingObjects, charactersGroup, False, False)
        if self.rect.y > 470:
            self.kill()
            character.lives -= 1
        if len(caught) > 0:
            self.kill()
        else:
            return


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 68])
        self.image.set_colorkey(black)
        self.lives = 3

        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 420

        self.image.blit(pygame.image.load("Superhero2.png"), (0, 0))

    def moveCharacter(self, movement):
        if self.rect.x >= 5 and self.rect.x <= 645:
            self.rect.x = self.rect.x + movement
        if self.rect.x < 5:
            self.rect.x = 5
        if self.rect.x > 645:
            self.rect.x = 645

    def moveCharacter2(self,movement):
        if 410 >= self.rect.y >= 5:
            self.rect.y += movement
        if self.rect.y < 5:
            self.rect.y = 5
        if self.rect.y > 410:
            self.rect.y = 410


pygame.init()                               # Pygame is initialised (starts running)

screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
background_image = pygame.image.load("OrchardBackground.jpg").convert()
pygame.display.set_caption("Catch")       # Name your window
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black = (0,   0,   0)                 # Define some colors using rgb values.  These can be
white = (255, 255, 255)                 # used throughout the game instead of using rgb values.
font = pygame.font.Font(None, 36)

# Define additional Functions and Procedures here
allFallingObjects = pygame.sprite.Group()

nextApple = pygame.time.get_ticks() + 2500

charactersGroup = pygame.sprite.Group()
character = Character()
charactersGroup.add(character)
livesGroup = pygame.sprite.Group()
livesImg = pygame.image.load("Lives.png").convert()
movement = 0

score = 0

schmovement = 0

# -------- Main Program Loop -----------
while not done:

    if character.lives <= 0:
        done = True

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = -5
            if event.key == pygame.K_RIGHT:
                movement = 5
            if event.key == pygame.K_UP:
                schmovement = -5
            if event.key == pygame.K_DOWN:
                schmovement = 5
        if event.type == pygame.KEYUP:
            movement = 0
            schmovement = 0



    # Update sprites here


    if pygame.time.get_ticks() > nextApple:
        nextObject = FallingObject()
        nextObject.setImage("Apple.png")
        allFallingObjects.add(nextObject)
        nextApple = pygame.time.get_ticks() + random.randint(1000, 3000)
    for eachObject in (allFallingObjects.sprites()):
        eachObject.moveFallingObjects(6)
        collisions = pygame.sprite.groupcollide(allFallingObjects, charactersGroup, False, False)
        if len(collisions) > 0:
            score += 1
        eachObject.deleteFallingObjects()
        print(character.lives)

    character.moveCharacter(movement)
    character.moveCharacter2(schmovement)



    screen.blit(background_image, [0, 0])
    allFallingObjects.draw(screen)
    charactersGroup.draw(screen)
    if character.lives == 3:
        screen.blit(livesImg, (60, 10))
    if character.lives >= 2:
        screen.blit(livesImg, (35, 10))
    if character.lives >= 1:
        screen.blit(livesImg, (10, 10))
    textImg = font.render(str(score), 1, white)
    screen.blit(textImg,(10, 10))
    pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
    clock.tick(60)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.
