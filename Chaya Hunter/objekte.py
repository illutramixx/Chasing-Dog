import pygame

from random import randint, choice

class Objekte(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        chaya_1 = pygame.image.load('chaya1.png').convert_alpha()
        chaya1_rect = chaya_1.get_rect(center = (20, 100))

        self.image = chaya_1
        self.rect = chaya1_rect
       

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
