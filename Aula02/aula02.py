import pygame
from pygame.locals import *
import sys

largura = 800
altura = 600

pygame.init()

tela = pygame.display.set_mode((largura,altura))

def game():
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()   
                
        pygame.draw.rect(tela,(255,0,0),(300,400,50,30))
        pygame.display.update()
game()