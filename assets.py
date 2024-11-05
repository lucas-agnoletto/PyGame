import pygame


    
def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites
def load_assets():
    assets = {}

    personagem = pygame.image.load('assets/img/Gangster.png').convert_alpha()
    personagem = load_spritesheet(personagem,1,6)
    andar = pygame.image.load('assets/img/Gangster(caminhar).png').convert_alpha()
    andar = load_spritesheet(andar,1,10)
    atira = pygame.image.load('assets/img/Gangster(ataque).png').convert_alpha()
    atira = load_spritesheet(atira,1,4)
    
    
    escala = 1.5  
    nova_largura = int(personagem[0].get_width() * escala)
    nova_altura = int(personagem[0].get_height() * escala)

    # Personagem parado
    for i in range(len(personagem)):
        personagem[i] = pygame.transform.scale(personagem[i], (nova_largura, nova_altura))
    # Andando
    for i in range(len(andar)):
        andar[i] = pygame.transform.scale(andar[i], (nova_largura, nova_altura))
    
    # Atirando
    for i in range(len(atira)):
        atira[i] = pygame.transform.scale(atira[i], (nova_largura, nova_altura))
    
    # Listas para animação
    assets['andar'] = andar
    assets['personagem'] = personagem
    assets['atira'] = atira

    fundo = pygame.image.load('assets/img/fundo.png').convert_alpha()
    fundo_larg = int(fundo.get_width()*3)
    fundo_alt = int(fundo.get_height()*3)
    # Background
    assets['fundo'] = pygame.transform.scale(fundo,(fundo_larg,fundo_alt))
    return assets
