import pygame

import random 

class Objekte(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()

        chaya_1 = pygame.image.load('graphics/chaya1.png').convert_alpha()
        chaya_2 = pygame.image.load('graphics/chaya2.png').convert_alpha()
        chaya_3 = pygame.image.load('graphics/chaya3.png').convert_alpha()
        self.chaya = [chaya_1, chaya_2, chaya_3]
        self.chaya_index = index
        self.image = self.chaya[self.chaya_index]
        self.rect = self.image.get_rect(center = (random.randint(0, 500), 10))
        

        
       

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
