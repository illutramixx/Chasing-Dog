import random
import pygame

from random import randint, choice
#from objekte import Objekte

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.is_animating = False
        self.animation = 100
        self.item_animation = 150
        self.is_item_animation = False

        nello_surf = pygame.image.load('graphics/nello.png').convert_alpha()
        nello_hit = pygame.image.load('graphics/nello_horny.png').convert_alpha()
        self.image1 = nello_hit


        self.nello = nello_surf
        self.image = self.nello
        self.rect = self.image.get_rect(center  = (250, 780))
        self.gravity = 0
        self.speed = 5


        self.chaya1 = 0
        self.chaya2 = 0
        self.chaya3 = 0

        self.text_font = pygame.font.SysFont('Impact', 20)
        self.text = self.text_font.render('', False,  (255, 215, 0))

        self.double_jump = 0
        self.fremdgehen = 0

        self.geld = 0
    
    def add_geld(self, geld):
        self.geld += geld
        print('Konto: ' + str(self.geld))
    
     
    def player_input(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:#and self.rect.bottom == 800:
            if self.rect.centery >= 700:
                self.gravity = -10
                self.double_jump= 0
            elif self.double_jump == 0:
                self.double_jump = 1
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

    def set_item(self, item):
        self.item_state = item
        match item:
            case 'ring':
                self.item_state = 'ring'
            case 'kondom':
                self.item_state = 'kondom'
            case 'geld':
                self.text =self.text_font.render('+ ' + str(random.randint(1, 10) * 50), False,  (255, 215, 0)) 
        self.is_item_animation = True
            
 
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 800:
            self.rect.bottom = 800


    def count_chaya(self, index):
        match index:
            case 0:
                self.chaya1 += 1
                self.chaya2 = 0
                self.chaya3 = 0

                if self.chaya1 == 1:
                    self.fremdgehen += 1
                else:
                    self.fremdgehen = 0 
                return self.chaya1
            case 1:
                self.chaya1 = 0
                self.chaya2 += 1
                self.chaya3 = 0

                if self.chaya2 == 1:
                    self.fremdgehen += 1
                else:
                    self.fremdgehen = 0         
                return self.chaya2
            case 2:
                self.chaya1 = 0
                self.chaya2 = 0
                self.chaya3 += 1

                if self.chaya3 == 1:
                    self.fremdgehen += 1
                else:
                    self.fremdgehen = 0  
                return self.chaya3
        return 0

    def treue_test(self):
        if self.fremdgehen == 3:
            print("Du HS")
        if self.chaya1 == 3:
            print('Du hast eine Freundin')
        if self.chaya2 == 3:
            print('Du hast eine Freundin')
        if self.chaya3 == 3:
            print('Du hast eine Freundin')

    
    def update(self):
        if self.is_animating == True and self.animation > 0:
            self.image = self.image1
            self.animation -= 1

        else:
            self.animation = 50
            self.is_animating = False
            self.image = self.nello

        if self.is_item_animation == True and self.item_animation > 0:
            self.image = pygame.Surface((self.image.get_width() + self.text.get_width(), self.image.get_height()+self.image.get_height()))

            self.text.blit(self.image, (self.rect.x, self.rect.y +30))
            print('-.--------------------------------------------')
            self.item_animation -= 1
        else:
            self.item_animation = 150
       # self.animation_state(hit, time)
        self.treue_test()
        self.player_input()
        self.apply_gravity()