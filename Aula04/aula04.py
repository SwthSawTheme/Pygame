import pygame
from pygame.locals import *
import sys
from random import randint

width = 800
height = 600

screen = pygame.display.set_mode((width,height))
FPS = pygame.time.Clock()
pygame.init()

def game():
    x_red = width // 2
    y_red = height // 2
    
    x_blue = randint(200,600)
    y_blue = randint(200,500)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()
        
        if pygame.key.get_pressed()[K_a]:
            x_red -= 12
        elif pygame.key.get_pressed()[K_d]:
            x_red += 12
        elif pygame.key.get_pressed()[K_w]:
            y_red -= 12
        elif pygame.key.get_pressed()[K_s]:
            y_red += 12
        
        red_rect = pygame.draw.rect(screen,(255,0,0),(x_red,y_red,100,100))
        blue_rect = pygame.draw.rect(screen,(0,0,255),(x_blue,y_blue,100,100))
        
        if red_rect.colliderect(blue_rect):
            x_blue = randint(200,600)
            y_blue = randint(200,500)
        
        pygame.display.update()
        screen.fill((0,0,0))
        FPS.tick(60)
game()