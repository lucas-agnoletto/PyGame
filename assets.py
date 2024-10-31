import pygame
from sprites import load_spritesheet
    

def load_assets():
    assets = {}

    personagem = pygame.image.load('assets/img/Idle.png').convert_alpha()
    personagem = load_spritesheet(personagem,1,6)
    personagem = personagem[0]
    escala = 1.5  
    nova_largura = int(personagem.get_width() * escala)
    nova_altura = int(personagem.get_height() * escala)
    assets['personagem'] = pygame.transform.scale(personagem, (nova_largura, nova_altura))

    fundo = pygame.image.load('assets/img/mockup.png').convert_alpha()
    fundo_larg = int(fundo.get_width()*3)
    fundo_alt = int(fundo.get_height()*3)

    assets['fundo'] = pygame.transform.scale(fundo,(fundo_larg,fundo_alt))
    return assets
