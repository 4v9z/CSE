import winsound
import pygame

winsound.PlaySound("The World Revolving.mp3", winsound.SND_ASYNC)

pygame.mixer.init()

jevil = pygame.mixer.Sound("The World Revolving.mp3")

pygame.mixer.Sound.play(jevil)
