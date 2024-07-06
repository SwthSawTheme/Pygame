import os
import pygame
import time
from random import randint
from sys import exit
from pygame.locals import *

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))

pygame.mixer.music.load(os.path.join("Aula07","fundo.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound(os.path.join("Aula07","money.wav"))

fonte = pygame.font.SysFont("arial",40,True)
FPS = pygame.time.Clock()    

def game():
    x_red = largura // 2
    y_red = altura // 2
    
    x_blue = randint(100,700)
    y_blue = randint(100,500)
    
    pontos = 0
    
    def drawCobra(corpo:list):
        for parte in corpo:
            pygame.draw.rect(tela,(255,0,0),(parte[0],parte[1],20,20))

    corpo = []
    
    tamanho_cobra = 1
    
    while True:
     
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
     
        tela.fill((0,0,0))
        
        keys = pygame.key.get_pressed()
        
        if keys[K_LEFT]:
            x_red -= 10
        if keys[K_RIGHT]:
            x_red += 10
        if keys[K_UP]:
            y_red -= 10
        if keys[K_DOWN]:
            y_red += 10
        if keys[K_SPACE]:
            x_blue = randint(100,700)
            y_blue = randint(100,500)
            pontos += 300
            sound.play()
            time.sleep(0.1)
        
        rect_red = pygame.draw.rect(tela,(255,0,0),(x_red,y_red,20,20))
        rect_blue = pygame.draw.rect(tela,(255,0,255),(x_blue,y_blue,20,20))
        
        cabeca = [x_red,y_red]
        corpo.append(cabeca)
        
        drawCobra(corpo)
        
        if len(corpo) > tamanho_cobra:
            del corpo[0]
        
        if rect_red.colliderect(rect_blue):
            x_blue = randint(100,700)
            y_blue = randint(100,500)
            pontos += 10
            sound.play()
            corpo.append(cabeca)
            tamanho_cobra += 1
            
        
        if x_red > largura:
            x_red = -50
        elif x_red < -50:
            x_red = largura
        if y_red > altura:
            y_red = -50
        elif y_red < -50:
            y_red = altura
        
        
        FPS.tick(60)
        texto = fonte.render(f"Pontos:{pontos}",True,(255,255,255))
        tela.blit(texto,(10,10))
        pygame.display.update()
        
game()