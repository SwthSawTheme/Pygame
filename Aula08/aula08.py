import pygame
import os
from pygame.locals import *
from sys import exit

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
        self.animation = False
        
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_1.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_2.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_3.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_4.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_5.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_6.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_7.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_8.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_9.png"))
        self.sprites.append(pygame.image.load(r"Aula08\sprites\attack_10.png"))
        
        self.sprite_contador = 0
        self.image = self.sprites[self.sprite_contador]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
    
    def ataque(self):
        self.animation = True
    
    def update(self):
        if self.animation == True:
            self.sprite_contador += 0.45
            if self.sprite_contador >= len(self.sprites):
                self.sprite_contador = 0
                self.animation = False
            self.image = self.sprites[int(self.sprite_contador)]
            self.image = pygame.transform.scale(self.image,(128*3,64*3))

grupoSprites = pygame.sprite.Group()     
sapo = Sapo()
grupoSprites.add(sapo)

def game():
    while True:
        tela.fill(PRETO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
            if pygame.key.get_pressed()[K_SPACE]:
                sapo.ataque()
        
        grupoSprites.draw(tela)
        grupoSprites.update()
        pygame.display.flip()
        FPS.tick(30)
game()