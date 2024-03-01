import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height =800

screen = pygame.display.set_mode((screen_width, screen_height))
yellow = [255, 255, 255]
blue = [255, 255, 255]
pygame.display.set_caption('Game box')

    pygame.display.update()

pygame.quit()