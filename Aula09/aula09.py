import pygame
import os
from pygame.locals import *

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))
FPS = pygame.time.Clock()
pygame.display.set_caption("DINO CRISIS")

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass
    
grupoSprites = pygame.sprite.Group()
dino = Dino()
grupoSprites.add(dino)


def game():
    
    while True:
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
        
        grupoSprites.draw(tela)
        grupoSprites.update()
        pygame.display.flip()
        FPS.tick(60)
game()