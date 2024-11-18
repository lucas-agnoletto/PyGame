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
    # tiros
    bullet = pygame.image.load('assets/img/bullet.png').convert_alpha()
    bullet_scale = 0.1
    new_width = int(bullet.get_width()*bullet_scale)
    new_height = int(bullet.get_height()*bullet_scale)
    bullet = pygame.transform.scale(bullet,(new_width,new_height))
    assets['bullet'] = bullet

    # Sons
    assets['shot_sound'] = pygame.mixer.Sound('assets/som/Tiro.ogg')
    assets['trilha_sonora'] = pygame.mixer.Sound('assets/som/Track06.ogg')
    assets['pistol_sound'] = pygame.mixer.Sound('assets/som/single_shot.mp3')
    assets['punch_sound'] = pygame.mixer.Sound('assets/som/punch_sound2.mp3')
    assets['grito_morte'] = pygame.mixer.Sound('assets/som/player_grito_morte.mp3')
    assets['grito_morte'].set_volume(0.5)
    assets['grito_morte_enemie'] = pygame.mixer.Sound('assets/som/grito_morte_enemie.mp3')
    assets['perde_vida'] = pygame.mixer.Sound('assets/som/sofre_danosound.mp3')
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
    
    # ASSETS DO INIMIGO2
    inimigo2 = pygame.image.load('assets/img/Inimigo2.png').convert_alpha()
    inimigo2 = load_spritesheet(inimigo2,1,7)
    inimigo2_ata1 = pygame.image.load('assets/img/Inimigo2(ataque1).png').convert_alpha()
    inimigo2_ata1 = load_spritesheet(inimigo2_ata1,1,6)
    inimigo2_ata2 = pygame.image.load('assets/img/Inimigo2(ataque2).png').convert_alpha()
    inimigo2_ata2 = load_spritesheet(inimigo2_ata2,1,4)
    inimigo2_ata3 = pygame.image.load('assets/img/Inimigo2(ataque3).png').convert_alpha()
    inimigo2_ata3 = load_spritesheet(inimigo2_ata3,1,6)
    inimigo2_hurt = pygame.image.load('assets/img/Inimigo2(machucado).png').convert_alpha()
    inimigo2_hurt = load_spritesheet(inimigo2_hurt,1,4)
    inimigo2_morto = pygame.image.load('assets/img/Inimigo2(morto).png').convert_alpha()
    inimigo2_morto = load_spritesheet(inimigo2_morto,1,5)
    inimigo2_andando = pygame.image.load('assets/img/Inimigo2(andando).png').convert_alpha()
    inimigo2_andando = load_spritesheet(inimigo2_andando,1,10)
    inimigo2_correndo = pygame.image.load('assets/img/Inimigo2(correndo).png').convert_alpha()
    inimigo2_correndo = load_spritesheet(inimigo2_correndo,1,10)
    # ajuste escala
    for i in range(len(inimigo2)):
        inimigo2[i] = pygame.transform.scale(inimigo2[i], (nova_largura, nova_altura))
    for i in range(len(inimigo2_ata1)):
        inimigo2_ata1[i] = pygame.transform.scale(inimigo2_ata1[i], (nova_largura, nova_altura))
        inimigo2_ata3[i] = pygame.transform.scale(inimigo2_ata3[i], (nova_largura, nova_altura))
    for i in range(len(inimigo2_ata2)):
        inimigo2_ata2[i] = pygame.transform.scale(inimigo2_ata2[i], (nova_largura, nova_altura))
    for i in range(len(inimigo2_morto)):
        inimigo2_morto[i] = pygame.transform.scale(inimigo2_morto[i], (nova_largura, nova_altura))
    for i in range(len(inimigo2_hurt)):
        inimigo2_hurt[i] = pygame.transform.scale(inimigo2_hurt[i], (nova_largura, nova_altura))
    for i in range(len(inimigo2_andando)):
        inimigo2_andando[i] = pygame.transform.scale(inimigo2_andando[i], (nova_largura, nova_altura))
        inimigo2_correndo[i] = pygame.transform.scale(inimigo2_correndo[i], (nova_largura, nova_altura))
    assets['inimigo2'] = inimigo2
    assets['punch1'] = inimigo2_ata1
    assets['punch2'] = inimigo2_ata2
    assets['punch3'] = inimigo2_ata3
    assets['hurt_e2'] = inimigo2_hurt
    assets['morto_e2'] = inimigo2_morto
    assets['andando_e2'] = inimigo2_andando
    assets['correndo_e2'] = inimigo2_correndo

    #  ASSETS DO INIMIGO3
    inimigo3 = pygame.image.load('assets/img/Inimigo3.png').convert_alpha()
    inimigo3 = load_spritesheet(inimigo3,1,5)
    inimigo3_ata1 = pygame.image.load('assets/img/Inimigo3(ata1).png').convert_alpha()
    inimigo3_ata1 = load_spritesheet(inimigo3_ata1,1,5)
    inimigo3_ata2 = pygame.image.load('assets/img/Inimigo3(ata2).png').convert_alpha()
    inimigo3_ata2 = load_spritesheet(inimigo3_ata2,1,5)
    inimigo3_ata3 = pygame.image.load('assets/img/Inimigo3(ata3).png').convert_alpha()
    inimigo3_ata3 = load_spritesheet(inimigo3_ata3,1,4)
    inimigo3_run = pygame.image.load('assets/img/Inimigo3(correndo).png').convert_alpha()
    inimigo3_run = load_spritesheet(inimigo3_run,1,8)
    inimigo3_morto = pygame.image.load('assets/img/Inimigo3(morto).png').convert_alpha()
    inimigo3_morto = load_spritesheet(inimigo3_morto,1,4)
    for i in range(len(inimigo3)):
        inimigo3[i] = pygame.transform.scale(inimigo3[i], (nova_largura, nova_altura))
        inimigo3_ata1[i] = pygame.transform.scale(inimigo3_ata1[i], (nova_largura, nova_altura))
        inimigo3_ata2[i] = pygame.transform.scale(inimigo3_ata2[i], (nova_largura, nova_altura))
    for i in range(len(inimigo3_ata3)):
        inimigo3_ata3[i] = pygame.transform.scale(inimigo3_ata3[i], (nova_largura, nova_altura))
        inimigo3_morto[i] = pygame.transform.scale(inimigo3_morto[i], (nova_largura, nova_altura))
     
    for i in range(len(inimigo3_run)):
        inimigo3_run[i] = pygame.transform.scale(inimigo3_run[i], (nova_largura, nova_altura))
    
    assets['run_e3'] = inimigo3_run
    assets['inimigo3'] = inimigo3
    assets['ata1_e3'] = inimigo3_ata1
    assets['ata2_e3'] = inimigo3_ata2
    assets['ata3_e3'] = inimigo3_ata3
    assets['morto_e3'] = inimigo3_morto
    

    return assets
