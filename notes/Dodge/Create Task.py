import pygame
import sys

pygame.init()

starting = True
screen = pygame.display.set_mode([550,400])
title = pygame.image.load("title.png").convert()
game_clock = pygame.time.Clock()
animationclock = pygame.time.Clock()
pygame.display.set_caption("SUPER SMASH BROS. PYTHON EDITION")

while starting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
            sys.exit()
        if event.type == pygame.KEYUP:
            starting = False
    screen.blit(title, [0, 0])
    pygame.display.flip()

print("pretend you're in the menu")
