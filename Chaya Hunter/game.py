

from sys import exit
from pygame.math import Vector2
import math
import time
import pygame
from objekte import Objekte

from player import Player



running = False
pygame.init()
screen = pygame.display.set_mode((500, 800)) # weite, höhe
pygame.display.set_caption('Chaya Hunter')
clock = pygame.time.Clock()

pygame.font.init()

#test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

background_surf = pygame.image.load('graphics/background.png')
background_surf = pygame.transform.scale(background_surf, (500,800))
background_rect = background_surf.get_rect(center = (250, 400))
 #start screen
start_surf = pygame.image.load('graphics/start.png')
start_surf = pygame.transform.scale(start_surf, (500,800))
start_rect = start_surf.get_rect(center = (250, 400))
    
title_surf = pygame.image.load('graphics/title.png').convert_alpha()
title_surf = pygame.transform.scale(title_surf, (300,150))
title_rect = title_surf.get_rect(center = (250, 600))

player = pygame.sprite.GroupSingle()
player.add(Player())

chaya_group = pygame.sprite.Group()



#Lebensanzeige vom Spieler 
#def life_player():
    #life_txt = 'graphics/heart' + str(life) + '.png'
    #heart_surf = pygame.image.load(life_txt)
    #heart_rect = start_surf.get_rect(center = (670, 1170))
    #screen.blit(heart_surf, heart_rect)


timer_interval = 1000 # 1sec
timer_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event_id, timer_interval)

timer_nello = pygame.USEREVENT + 2
pygame.time.set_timer(timer_nello, 700)

def collision_player_chaya():
    hit = False
    for chaya in chaya_group.sprites():
        if pygame.sprite.collide_rect(player.sprite, chaya):
            chaya.kill()
            hit = True
    return hit 

time = False
hit = True



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('hihi')
                    #laser_group.add(player.laser())
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == timer_event_id:
                chaya_group.add(Objekte())
                
            if event.type == timer_nello:
                if hit:
                    time = True
                else:
                    time = False
        else: 
            print('lol')
            #rocket_rect = rocket_surf.get_rect(center = (400, 200))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                running = True
                print('hi')
               
                
    if running:
        screen.blit(background_surf, background_rect)

        chaya_group.draw(screen)
        chaya_group.update()
        
        hit = collision_player_chaya()
     

        player.draw(screen)
        print(time)
        player.update(hit, time)

        

        

        #screen.blit(nello_surf, nello_rect)   
        

    else:
        print('hi')


     
    
    pygame.display.update()
    clock.tick(60) # loop nicht schnelles als 60*mal pro sec





