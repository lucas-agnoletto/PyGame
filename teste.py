import pygame
from assets import load_assets
from config import FPS, ALT, LARG

pygame.init()

window = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption('Máfia 5')
rect = pygame.Rect

# Blocos para colisão
blocos_horizont = [
    rect(0, 440, 335, 10), rect(195, 590, 150, 10), rect(94, 729, 360, 10),
    rect(445, 630, 430, 10), rect(880, 530, 210, 10), rect(1090, 630, 300, 10),
    rect(1350, 530, 60, 10), rect(1405, 440, 350, 10), rect(1750, 490, 340, 10),
    rect(2090, 630, 200, 10)
]
blocos_vert = [
    rect(440, 650, 10, 100), rect(875, 530, 10, 100), rect(1090, 530, 10, 100),
    rect(1350, 530, 10, 100), rect(1400, 445, 10, 100), rect(1750, 440, 10, 60),
    rect(2090, 500, 10, 150), rect(2280, 630, 10, 200)
]

# Carregar assets
assets = load_assets()

# Cria um retângulo para o jogador
player_rect = assets['personagem'].get_rect()
player_rect.topleft = (35, 240)  # Posição inicial do jogador

larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()

game = True
camera_x = 0
camera_y = 0
player_speed = 4

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
    p_speedx = (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed
    p_speedy = (keys[pygame.K_s] - keys[pygame.K_w]) * player_speed

    # Salva a posição original do jogador
    original_rect = player_rect.copy()

    # Atualiza a posição do jogador na direção X
    player_rect.x += p_speedx

    # Verifica colisão após a movimentação na direção X
    for bloco in blocos_horizont + blocos_vert:
        if player_rect.colliderect(bloco):
            if p_speedx > 0:  # Movendo para a direita
                player_rect.right = bloco.left
            elif p_speedx < 0:  # Movendo para a esquerda
                player_rect.left = bloco.right

    # Atualiza a posição do jogador na direção Y
    player_rect.y += p_speedy + 5

    # Verifica colisão após a movimentação na direção Y
    for bloco in blocos_horizont + blocos_vert:
        if player_rect.colliderect(bloco):
            if p_speedy > 0:  # Movendo para baixo
                player_rect.bottom = bloco.top
            elif p_speedy < 0:  # Movendo para cima
                player_rect.top = bloco.bottom

    # Atualiza a posição da câmera
    camera_x = player_rect.x - LARG // 2
    camera_y = player_rect.y - ALT // 2

    # Limita o movimento da câmera
    camera_x = max(0, min(camera_x, larg_fundo - LARG))
    camera_y = max(0, min(camera_y, alt_fundo - ALT))

    window.fill((255, 255, 255))
    window.blit(assets['fundo'], (-camera_x, -camera_y))  # Atualiza o fundo
    window.blit(assets['personagem'], (player_rect.x - camera_x, player_rect.y - camera_y))  # Atualiza o jogador

    # Desenha os blocos considerando a posição da câmera
    for bloco in blocos_horizont:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x, -camera_y))
    for bloco in blocos_vert:
        pygame.draw.rect(window, (0, 255, 0), bloco.move(-camera_x, -camera_y))

    pygame.display.flip()  # Atualiza a tela
    pygame.time.Clock().tick(FPS)

pygame.quit()