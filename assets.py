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
    # Fundo ajustes
    fundo = pygame.image.load('assets/img/fundo.png').convert_alpha()
    fundo_larg = int(fundo.get_width()*3)
    fundo_alt = int(fundo.get_height()*3)
    # Background
    assets['fundo'] = pygame.transform.scale(fundo,(fundo_larg,fundo_alt))
    # Para interface
    municao = pygame.image.load('assets/img/Munição(gangster).png').convert_alpha()
    municao = pygame.transform.scale(municao,(municao.get_width()*2,municao.get_height()*2))
    assets['munição'] = municao
    vida = pygame.image.load('assets/img/Vida.png').convert_alpha()
    vida = pygame.transform.scale(vida,(vida.get_width()*2,vida.get_height()*2))
    assets['vida'] = vida
    assets['bullet'] = pygame.image.load('assets/img/Munição(gangster).png').convert_alpha()
    # Sons
    assets['shot_sound'] = pygame.mixer.Sound('assets/som/Tiro.ogg')
    assets['trilha_sonora'] = pygame.mixer.Sound('assets/som/Track06.ogg')
    # ASSETS DO PLAYER:
    # Carrega e corta sprites
    personagem = pygame.image.load('assets/img/Gangster.png').convert_alpha()
    personagem = load_spritesheet(personagem,1,6)
    andar = pygame.image.load('assets/img/Gangster(caminhar).png').convert_alpha()
    andar = load_spritesheet(andar,1,10)
    atira = pygame.image.load('assets/img/Gangster(ataque).png').convert_alpha()
    atira = load_spritesheet(atira,1,4)
    pular = pygame.image.load('assets/img/Gangster(pulando).png').convert_alpha()
    pular = load_spritesheet(pular,1,10)
    ferido = pygame.image.load('assets/img/Gangster(machucado).png').convert_alpha()
    ferido = load_spritesheet(ferido,1,5)
    recarga = pygame.image.load('assets/img/Gangster(recarga).png').convert_alpha()
    recarga = load_spritesheet(recarga,1,17)
    morto = pygame.image.load('assets/img/Gangster(morto).png').convert_alpha()
    morto = load_spritesheet(morto,1,5)
    porrada = pygame.image.load('assets/img/Gangster(porrada).png').convert_alpha()
    porrada = load_spritesheet(porrada,1,3)
    # Define o tamanho do personagem
    escala = 1.5  
    nova_largura = int(personagem[0].get_width() * escala)
    nova_altura = int(personagem[0].get_height() * escala)

    # Ajustar escala:

    # Personagem parado
    for i in range(len(personagem)):
        personagem[i] = pygame.transform.scale(personagem[i], (nova_largura, nova_altura))
    # Andando e pulando
    for i in range(len(andar)):
        andar[i] = pygame.transform.scale(andar[i], (nova_largura, nova_altura))
        pular[i] = pygame.transform.scale(pular[i], (nova_largura, nova_altura))
    # Atirando
    for i in range(len(atira)):
        atira[i] = pygame.transform.scale(atira[i], (nova_largura, nova_altura))
    # Ferido
    for i in range(len(ferido)):
        ferido[i] = pygame.transform.scale(ferido[i], (nova_largura, nova_altura))
        morto[i] = pygame.transform.scale(morto[i], (nova_largura, nova_altura))
    # Recarga
    for i in range(len(recarga)):
        recarga[i] = pygame.transform.scale(recarga[i], (nova_largura, nova_altura))
    for i in range(len(porrada)):
        porrada[i] = pygame.transform.scale(porrada[i], (nova_largura, nova_altura))

    # Listas estados para animação
    assets['andar'] = andar
    assets['personagem'] = personagem
    assets['atira'] = atira
    assets['stop_shot'] = [atira[3]]
    assets['pular'] = pular
    assets['ferido'] = ferido
    assets['recarga'] = recarga
    assets['morto'] = morto
    assets['porrada'] = porrada

    # ASSETS DO INIMIGO1:
    # carregando os assets
    inimigo1 = pygame.image.load('assets/img/Inimigo1.png').convert_alpha()
    inimigo1 = load_spritesheet(inimigo1,1,7)
    ata_inimigo1 = pygame.image.load('assets/img/Inimigo1(ataque).png').convert_alpha()
    ata_inimigo1 = load_spritesheet(ata_inimigo1,1,12)
    ata2_inimigo1 = pygame.image.load('assets/img/Inimigo1(porrada).png').convert_alpha()
    ata2_inimigo1 = load_spritesheet(ata2_inimigo1,1,5)
    hurt_inimigo1 = pygame.image.load('assets/img/Inimigo1(machucado).png').convert_alpha()
    hurt_inimigo1 = load_spritesheet(hurt_inimigo1,1,4)
    morto_inimigo1 = pygame.image.load('assets/img/Inimigo1(morto).png').convert_alpha()
    morto_inimigo1 = load_spritesheet(morto_inimigo1,1,5)

     
     # Define o tamanho do inimigo
    escala = 1.5  
    nova_largura = int(inimigo1[0].get_width() * escala)
    nova_altura = int(inimigo1[0].get_height() * escala)

    # Ajustando a escala da imagem    
    for i in range(len(inimigo1)):
        inimigo1[i] = pygame.transform.scale(inimigo1[i], (nova_largura, nova_altura))
    for i in range(len(ata_inimigo1)):
        ata_inimigo1[i] = pygame.transform.scale(ata_inimigo1[i], (nova_largura, nova_altura))
    for i in range(len(hurt_inimigo1)):
        hurt_inimigo1[i] = pygame.transform.scale(hurt_inimigo1[i], (nova_largura, nova_altura))
    for i in range(len(morto_inimigo1)):
        morto_inimigo1[i] = pygame.transform.scale(morto_inimigo1[i], (nova_largura, nova_altura))
    for i in range(len(ata2_inimigo1)):
        ata2_inimigo1[i] = pygame.transform.scale(ata2_inimigo1[i], (nova_largura, nova_altura))

    # Adicionando
    assets['inimigo1'] = inimigo1
    assets['ata_inimigo1'] = ata_inimigo1
    assets['hurt_e1'] = hurt_inimigo1
    assets['morto_e1'] = morto_inimigo1
    assets['ata2_inimigo1'] = ata2_inimigo1
    return assets
