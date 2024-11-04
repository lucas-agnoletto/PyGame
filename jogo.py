import pygame
from assets import load_assets
from config import FPS, ALT, LARG

pygame.init()


window = pygame.display.set_mode((LARG,ALT))
pygame.display.set_caption('Máfia 5')
rect = pygame.Rect
# blocos para haver colisão
blocos_horizont = [rect(0,440, 335, 10),rect(195,590,150,10),rect(94,729,360,10),rect(445,630,430,10),rect(880,530,210,10),rect(1090,630,300,10),rect(1350,530,60,10),rect(1405,440,350,10),rect(1750,490,340,10),rect(2090,630,200,10)] 
blocos_vert = [rect(440,650,10,100),rect(875,530,10,100),rect(1090,530,10,100),rect(1350,530,10,100),rect(1400,445,10,100),rect(1750,440,10,60),rect(2090,500,10,150),rect(2280,630,10,200)]
# carregar assets
assets = load_assets()

class Platform(pygame.sprite.Sprite):
    def __init__(self,position,size):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.mask = pygame.mask.Mask(size, True)

platforms_horizont = []
for bloco in blocos_horizont:
    platforms_horizont.append(Platform((bloco.x, bloco.y), (bloco.width, bloco.height)))


class Player(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['personagem']
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.mask.get_rect()
        

        self.rect.centerx = 240
        self.rect.bottom = 35
        self.speedx = 0
        self.speedy = 0
        self.assets = assets 
    
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > larg_fundo :
            self.rect.right = larg_fundo
        if self.rect.left < -60:
            self.rect.left = -60
        if self.rect.top < -70:
            self.rect.top = -70
        if self.rect.bottom > alt_fundo - self.rect.height:
            self.rect.bottom = alt_fundo - self.rect.height

player = Player(assets)


    
    
larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()

game = True
camera_x = 0
camera_y = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                player.speedx += 4
            if event.key == pygame.K_a:
                player.speedx -= 4
            if event.key == pygame.K_w:
                player.speedy -= 4
            if event.key == pygame.K_s:
                player.speedy += 4
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                player.speedx -= 4
            if event.key == pygame.K_a:
                player.speedx += 4
            if event.key == pygame.K_w:
                player.speedy += 4
            if event.key == pygame.K_s:
                player.speedy -= 4
     
    
    
    camera_x = player.rect.centerx - LARG // 2
    camera_y = player.rect.centery - ALT // 2
    
    

    
    camera_x = max(0, min(camera_x, larg_fundo - LARG)) # limita a camera 
    camera_y = max(0, min(camera_y, alt_fundo - ALT))

    
    

    window.fill((255, 255, 255))  
    window.blit(assets['fundo'],(-camera_x,-camera_y)) # atualiza o fundo
    pygame.draw.rect(window, (0,0,0), player.rect)
    window.blit(assets['personagem'], (player.rect.x - camera_x, player.rect.y - camera_y)) # atualiza o jogador
    player.update()

    for bloco in platforms_horizont:
        if pygame.sprite.collide_mask(player, bloco):
            player.rect.bottom = bloco.rect.top
            
    for bloco in blocos_horizont:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x,-camera_y))
    for bloco in blocos_vert:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x,-camera_y))
    
    

    pygame.display.flip()  # Atualiza a tela
    pygame.time.Clock().tick(FPS) 

pygame.quit()