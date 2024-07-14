import sys
import os
import pygame
from pygame.locals import *
from random import randint

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))
FPS = pygame.time.Clock()
fonte = pygame.font.SysFont("arial",40,True,False)
pygame.mixer.music.load(os.path.join("Aula06","fundo.mp3"))
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

tock = pygame.mixer.Sound(os.path.join("Aula06","money.wav"))


def game():
    x_red = largura / 2
    y_red = altura / 2
    
    x_blue = randint(100,700)
    y_blue = randint(100,500)
    
    pontos = 0
    
    while True:
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
        
        tela.fill((0,0,0))
        
        rect_red = pygame.draw.rect(tela,(255,0,0),(x_red,y_red,50,50))
        rect_blue = pygame.draw.rect(tela,(0,0,255),(x_blue,y_blue,50,50))
        
        if rect_red.colliderect(rect_blue):
            x_blue = randint(100,700)
            y_blue = randint(100,500)
            pontos += 10
            tock.play()
            
        
        FPS.tick(60)
        texto = fonte.render(f"Pontos:{pontos}",True,(255,255,255))
        tela.blit(texto,(10,10))
        pygame.display.update()

game()