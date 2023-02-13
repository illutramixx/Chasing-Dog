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
        self.rect = self.image.get_rect(center = (random.randint(0, 500), 0))
        
        
        
       
    def item_effect(self):
        match self.item_index:
            case 0:
                print('ring')
            
            case 1:
                print('kondom')

            case 2:
                print('geld')
   # def animation_state(self):
    #   self.animation_index += 0.1
   #    if self.animation_index >= len(self.frames): self.animation_index = 0
    #   self.image = self.frames[int(self.animation_index)]

    def update(self):
        #self.animation_state()
        self.rect.y -= -3
        self.destroy()


    def destroy(self):
        if self.rect.y <= -100:
            self.kill()
