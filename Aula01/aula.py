import pygame
from pygame.locals import *
import sys


largura = 700
altura = 600

pygame.init()

pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Game")


def game():
    while True:
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

game()