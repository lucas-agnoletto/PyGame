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

player_rect = assets['personagem'].get_rect()
larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()

game = True
camera_x = 0
camera_y = 0
p_speedx = 0
p_speedy = 0
player_x = 35
player_y = 240
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEMOTION:
            print(event)
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                p_speedx += 4
            if event.key == pygame.K_a:
                p_speedx -= 4
            if event.key == pygame.K_w:
                p_speedy -= 4
            if event.key == pygame.K_s:
                p_speedy += 4
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                p_speedx -= 4
            if event.key == pygame.K_a:
                p_speedx += 4
            if event.key == pygame.K_w:
                p_speedy += 4
            if event.key == pygame.K_s:
                p_speedy -= 4
    
    player_x += p_speedx
    player_y += p_speedy 

    camera_x = player_x - LARG // 2
    camera_y = player_y - ALT // 2
    
    camera_x = max(0, min(camera_x, larg_fundo - LARG)) # limita a camera 
    camera_y = max(0, min(camera_y, alt_fundo - ALT))
    
    window.fill((255, 255, 255))  
    window.blit(assets['fundo'],(-camera_x,-camera_y)) # atualiza o fundo
    window.blit(assets['personagem'], (player_x - camera_x, player_y - camera_y)) # atualiza o jogador
    for bloco in blocos_horizont:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x,-camera_y))
    for bloco in blocos_vert:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x,-camera_y))

    pygame.display.flip()  # Atualiza a tela
    pygame.time.Clock().tick(FPS) 

pygame.quit()