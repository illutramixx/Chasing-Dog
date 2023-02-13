import pygame

from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_animating = False
        self.animation = 100

        nello_surf = pygame.image.load('graphics/nello.png').convert_alpha()
        nello_hit = pygame.image.load('graphics/nello_horny.png').convert_alpha()
        self.image1 = nello_hit
        #nello_surf = pygame.transform.scale(nello_surf, (30, 50))
        self.nello = nello_surf
        self.image = self.nello
        self.rect = self.image.get_rect(center  = (150, 100))
        self.gravity = 0
        self.speed = 5
    

     
    def player_input(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :#and self.rect.bottom == 800:
            self.gravity = -10
        if keys[pygame.K_a] and self.rect.left >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.bottom <= 800:
            self.rect.y += self.speed
        if keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_d] and self.rect.right <= 500:
            self.rect.x += self.speed       
     
    def animation_state(self):
        self.is_animating = True
            
 
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
        
    
    
    def update(self):
        if self.is_animating == True and self.animation > 0:
            self.image = self.image1
            self.animation -= 1

        else:
            self.animation = 50
            self.is_animating = False
            self.image = self.nello

       # self.animation_state(hit, time)
        self.player_input()
        self.apply_gravity()