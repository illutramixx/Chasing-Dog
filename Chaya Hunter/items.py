import random
import pygame

from random import randint, choice

class Items(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()


        ring  = pygame.image.load('graphics/ring.png').convert_alpha()
        kondom = pygame.image.load('graphics/kondom.png').convert_alpha()
        geld = pygame.image.load('graphics/geld.png').convert_alpha()
        self.item = [ring, kondom, geld]
        self.item_index = index
        self.image = self.item[self.item_index]
        self.rect = self.image.get_rect(center = (random.randint(10, 490), 0))
        
        
        
       
    def item_effect(self, player):
        match self.item_index:
            case 0:
                print('ring')
                return ''
            case 1:
                print('kondom')
                return ''
            case 2:
                print('geld')
                geld = random.randint(1,10) * 50
                player.add_geld(geld)
                return '+ ' + str(geld) + '$'
                




    def update(self):
        #self.animation_state()
        self.rect.y -= -3
        self.destroy()


    def destroy(self):
        if self.rect.y <= -100:
            self.kill()
