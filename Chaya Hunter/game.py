

import random
from sys import exit
from pygame.math import Vector2
import math
import time
import pygame
from items import Items
from objekte import Objekte



from player import Player

Height = 800
Width = 500

running = False
pygame.init()
screen = pygame.display.set_mode((500, 800)) # weite, höhe
pygame.display.set_caption('Chaya Hunter')
clock = pygame.time.Clock()

pygame.font.init()

#test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

background_surf = pygame.image.load('graphics/background.png').convert()
background_surf = pygame.transform.scale(background_surf, (500,800))
background_rect = background_surf.get_rect(center = (250, 400))
scroll = 0

tiles = math.ceil(Height/background_surf.get_height()) +1

 #start screen
start_surf = pygame.image.load('graphics/start.png')
start_surf = pygame.transform.scale(start_surf, (500,800))
start_rect = start_surf.get_rect(center = (250, 400))
    

player1 = Player()
player = pygame.sprite.GroupSingle()
player.add(player1)

chaya_group = pygame.sprite.Group()

item = pygame.sprite.Group()


timer_interval = 1000 # 1sec
timer_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event_id, timer_interval)

item_interval = 3000
item_event = pygame.USEREVENT + 2
pygame.time.set_timer(item_event, item_interval)



def collision_player_chaya():
    hit = False
    for chaya in chaya_group.sprites():
        if pygame.sprite.collide_rect(player.sprite, chaya):
            chaya.kill()
            hit = True
    return hit 

def collision_player_item():
    hit = False
    for i in item.sprites():
        if pygame.sprite.collide_rect(player.sprite, i):
            i.item_effect()
            i.kill()
            hit = True
    return hit

def move_background(scroll):
    
    i = 0
    while(abs(i) < tiles):
        screen.blit(background_surf,  (0, background_surf.get_height()*i - scroll))
        i -= 1
    scroll -= 3

    if abs(scroll) > background_surf.get_height():
        scroll = 0

    return scroll


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == timer_event_id:
                chaya_group.add(Objekte(random.randint(0, 2)))
            if event.type == item_event:
                item.add(Items(random.randint(0, 2)))
                
        else: 
            print('lol')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                running = True
                print('hi')
               
                
    if running:
        #screen.blit(background_surf, background_rect)
        scroll = move_background(scroll)

        chaya_group.draw(screen)
        chaya_group.update()

        item.draw(screen)
        item.update()
        
        collision_player_item()
        hit = collision_player_chaya()
        if hit:
            player1.animation_state()

        player.draw(screen)
        player.update()

    
        

    else:
        print('hi')


     
    
    pygame.display.update()
    clock.tick(60) # loop nicht schnelles als 60*mal pro sec





 