import pygame
from assets import load_assets
from config import FPS, ALT, LARG
pygame.init()


window = pygame.display.set_mode((LARG,ALT))
pygame.display.set_caption('Titulo')
rect = pygame.Rect
# blocos para haver colisão
blocos_chao = [rect(0,440, 335, 10),rect(195,590,150,10),rect(94,729,330,10),rect(445,630,420,10)] 
blocos_par = [rect(875,530,10,100)]
assets = load_assets()


larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()

game = True
camera_x = 0
camera_y = 0
p_speedx = 0
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEMOTION:
            print(event)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  
        camera_x += 3
    if keys[pygame.K_d]:  
        camera_x -= 3
    if keys[pygame.K_w]:
        camera_y += 5
    if keys[pygame.K_s]:
        camera_y -= 5  
    p_speedx = 0
    if LARG>camera_x > 0  :
        camera_x = 0
        p_speedx += 3
    if camera_x < -1900:
        camera_x += 3
        p_speedx += 3
        
    if camera_y < -280:
        camera_y +=5

    if camera_y > 0:
        camera_y = 0
    
    window.fill((255, 255, 255))  
    window.blit(assets['fundo'],(camera_x,camera_y))
    window.blit(assets['personagem'],(0 + p_speedx,ALT/2))
    for bloco in blocos_chao:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(camera_x,camera_y))
    for bloco in blocos_par:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(camera_x,camera_y))
    pygame.display.flip()  # Atualiza a tela
    pygame.time.Clock().tick(FPS) 

pygame.quit()