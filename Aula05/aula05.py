import pygame
from pygame.locals import *
import sys
from random import randint

width = 800
heigth = 600

pygame.init()

screen = pygame.display.set_mode((width,heigth))
FPS = pygame.time.Clock()


def game():
    x_red = width // 2
    y_red = heigth // 2
    
    x_blue = randint(100,700)
    y_blue = randint(100,500)
    
    pontos = 0
    fonte = pygame.font.SysFont("arial",40,True,False)
    
    while True:
        
        texto = fonte.render(f"Pontos:{pontos}",True,(255,255,255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()
        
        if pygame.key.get_pressed()[K_a]:
            x_red -= 12
        if pygame.key.get_pressed()[K_d]:
            x_red += 12
        if pygame.key.get_pressed()[K_w]:
            y_red -= 12
        if pygame.key.get_pressed()[K_s]:
            y_red += 12
        
        red_rect = pygame.draw.rect(screen,(255,0,0),(x_red,y_red,50,50))
        blue_rect = pygame.draw.rect(screen,(0,0,255),(x_blue,y_blue,50,50))
        
        if red_rect.colliderect(blue_rect):
            x_blue = randint(100,700)
            y_blue = randint(100,500)
            pontos += 10
        
        
        screen.blit(texto,(30,30))    
        pygame.display.update()
        screen.fill((0,0,0))
        FPS.tick(60)
game()