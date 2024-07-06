import pygame
import os
from pygame.locals import *
from sys import exit

from pygame.sprite import _Group

pygame.init()

PRETO = (0,0,0)
largura = 720
altura = 480

tela = pygame.display.set_mode((largura,altura))
FPS = pygame.time.Clock()
pygame.display.set_caption("SAPO")

class Sapo(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("sprites/attack_1.png"))
        self.sprites.append(pygame.image.load("sprites/attack_2.png"))
        self.sprites.append(pygame.image.load("sprites/attack_3.png"))
        self.sprites.append(pygame.image.load("sprites/attack_4.png"))
        self.sprites.append(pygame.image.load("sprites/attack_5.png"))
        self.sprites.append(pygame.image.load("sprites/attack_6.png"))
        self.sprites.append(pygame.image.load("sprites/attack_7.png"))
        self.sprites.append(pygame.image.load("sprites/attack_8.png"))
        self.sprites.append(pygame.image.load("sprites/attack_9.png"))
        self.sprites.append(pygame.image.load("sprites/attack_10.png"))
        self.sprite_contador = 0
        self.image = self.sprites[self.sprite_contador]

def game():
    
    tela.fill(PRETO)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
        
        pygame.display.flip()
        FPS.tick(30)
game()