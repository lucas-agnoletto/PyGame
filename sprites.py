import pygame
from config import  LARG, ALT
from assets import load_assets






class Player(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['personagem']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 35
        self.speedx = 0
        self.speedy = 0
        self.assets = assets 
    
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > 0:
            self.rect.top = 0
        if self. rect.bottom > ALT:
            self.rect.bottom = ALT
    
    