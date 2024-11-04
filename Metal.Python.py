"""
AUTORES: Lucas Agnoletto, Matheus Chieppe e Lorenzo Stabile

DATA:

DESCRIÇÃO:
"""

import pygame, sprites
pygame.init()
pygame.mixer.init()

sprite_sheet = pygame.image.load("assets/character_spritesheet.png").convert_alpha()

# Extrai uma única frame (32x32) da sprite sheet na posição (0, 0)
frame1 = sprite_sheet.subsurface((0, 0, 32, 32))

# Exibe a frame extraída

