import pygame
from pygame.locals import *
import sys

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))
FPS = pygame.time.Clock()

pygame.init()

def game():
    x = largura // 2
    y = altura // 2

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()
                
        if pygame.key.get_pressed()[K_a]:
            x -= 5.5
        if pygame.key.get_pressed()[K_d]:
            x += 5.5
        if pygame.key.get_pressed()[K_w]:
            y -= 5.5
        if pygame.key.get_pressed()[K_s]:
            y += 5.5
        
        pygame.draw.rect(tela,(255,0,0),(x,y,50,50))
        pygame.display.update()
        FPS.tick(60)
        tela.fill((0,0,0))
game()