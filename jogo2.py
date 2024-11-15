import pygame
from assets import load_assets
from config import FPS, ALT, LARG
from intro import main

pygame.init()
pygame.mixer.init()
# MENU DO JOGO  
main()
window = pygame.display.set_mode((LARG,ALT))
pygame.display.set_caption('Máfia 5')
rect = pygame.Rect
# blocos para haver colisão
blocos_horizont = [rect(0,632,80,10),rect(0,440, 335, 10),rect(195,590,145,10),rect(94,729,360,10),rect(445,630,430,10),rect(875,530,217,10),rect(1090,630,300,10),rect(1200,260,390,10),rect(1350,530,60,10),rect(1405,440,350,10),rect(1750,490,345,10),rect(2090,630,200,10),rect(2600,530,60,10),rect(2650,490,530,10)] 
blocos_vert = [rect(75,640,10,100),rect(445,640,10,100),rect(875,540,10,100),rect(1090,535,10,100),rect(1350,530,10,100),rect(1400,445,10,100),rect(1746,445,10,60),rect(2090,500,10,150),rect(2280,630,10,200),rect(2600,542,10,500),rect(2650,500,10,40)]
# carregar assets
GRAVIDADE = 0.6

assets = load_assets()

# num das animaçoes do player
STILL = 0
WALK = 1
WALK_BACK = 2
SHOT = 3
JUMP = 4
FALLING = 5
LANDING = 6
RELOAD = 7
HURT = 8
STOP_SHOOTING = 9
DEAD = 10
CORONHADA = 11

# num da animaçoes do inimigo1
STILL_E1 = 0
SHOT_E1 = 1
HURT_E1 = 2
DEAD_E1 = 3
PUNCH_E1 = 4
# num das animações do inimigo2
STILL_E2 = 0
HURT_E2 = 1
DEAD_E2 = 2
PUNCH1 = 3
PUNCH2 = 4
PUNCH3 = 5
WALK_E2 = 6
RUN_E2 = 7
STANCE_E2 = 8     
# Medidas do background
larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()

fonte = pygame.font.Font('Sancreek-Regular.ttf', 48)

# Classe plataforma
class Platform(pygame.sprite.Sprite):
    def __init__(self,position,size):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.mask = pygame.mask.Mask(size, True)

platforms_horizont = []
for bloco in blocos_horizont:
    platforms_horizont.append(Platform((bloco.x, bloco.y), (bloco.width, bloco.height)))
platforms_vert = []
for bloco in blocos_vert:
    platforms_vert.append(Platform((bloco.x, bloco.y), (bloco.width, bloco.height)))

# Classe INIMIGO1

class Enemie1(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        
        #Animações inimigo1
        self.animations = {
            STILL_E1: assets['inimigo1'][0:],
            SHOT_E1: assets['ata_inimigo1'][5:],
            HURT_E1: assets['hurt_e1'][0:],
            DEAD_E1: assets['morto_e1'][0:],
            PUNCH_E1: assets['ata2_inimigo1'][0:]
        }
        self.state = STILL_E1
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.x = 1900
        self.rect.y = 300
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.lives = 30
        self.direction = True
        self.last_update = pygame.time.get_ticks()
        self.p_distance = self.rect.centerx + 60 - player.rect.centerx
        self.last_shot = pygame.time.get_ticks()
        

        self.animation_ticks = {
                STILL_E1: 100,
                SHOT_E1: 100,
                HURT_E1: 300,
                DEAD_E1: 100,
                PUNCH_E1: 100
                }
        
    def update(self):
        # Gravidade
        self.speedy += GRAVIDADE
        now = pygame.time.get_ticks()
        self.rect.x += self.speedx
        
      
        self.p_distance = self.rect.x - player.rect.x
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.frame_ticks = self.animation_ticks.get(self.state, 200)
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            
            # Reinicia a animação caso o índice da imagem atual seja inválido
            
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Obtém o quadro da animação atual
        if self.lives <= 0:
            self.state = DEAD_E1
            self.frame = 4
        self.image = self.animation[self.frame]
        
        
        # Atira se o player se aproxima e flipa a imagem se estiver do outro lado
        if self.lives > 0:
            if 60 < self.p_distance <= 300:
                self.state = SHOT_E1
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = False
                
                
                print(now - self.last_shot)
                if now - self.last_shot >= 1000:
                    new_bullet = Bullet(self.assets, self.rect.centery + 10, self.rect.centerx, self.direction)
                    self.last_shot = pygame.time.get_ticks()
                    player.groups['all_bullets'].add(new_bullet)
                    assets['pistol_sound'].set_volume(0.5)
                    assets['pistol_sound'].play()
                    if pygame.sprite.collide_mask(new_bullet,player):
                            player.lives -= 0.5
                            new_bullet.kill()
                            
            elif  -60 >= self.p_distance >= -300: 
                self.state = SHOT_E1
                if self.frame == 5:
                    self.direction = True
                    if now - self.last_shot >= 1000:
                        new_bullet = Bullet(self.assets, self.rect.centery + 10, self.rect.centerx, self.direction)
                        self.last_shot = pygame.time.get_ticks()
                        player.groups['all_bullets'].add(new_bullet)
                        assets['pistol_sound'].set_volume(0.5)
                        assets['pistol_sound'].play()
                        if pygame.sprite.collide_mask(new_bullet,player):
                            print('colidiu')
                            player.lives -= 0.5
                            new_bullet.kill()
                            
                   
            elif  0 < self.p_distance <= 60:
                self.image = pygame.transform.flip(self.image, True, False)
                self.state = PUNCH_E1
                if pygame.sprite.collide_mask(inimigo1,player):
                        assets['punch_sound'].play()
                        player.lives -= 0.02

            elif 0 >= self.p_distance > -60:
                self.state = PUNCH_E1
                if pygame.sprite.collide_mask(inimigo1,player):
                        assets['punch_sound'].play()
                        player.lives -= 0.02
                
            else:
                self.state = STILL_E1
        
class Enemie2(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.animations = {
            STILL_E2: assets['inimigo2'][0:],
            PUNCH1: assets['punch1'][0:],
            HURT_E2: assets['hurt_e2'][4:],
            DEAD_E2: assets['morto_e2'][0:],
            PUNCH2: assets['punch2'][0:],
            PUNCH3: assets['punch3'][0:],
            WALK_E2: assets['andando_e2'][0:],
            RUN_E2: assets['correndo_e2'][0:],
            STANCE_E2: assets['punch3'][0:3]
        }
        self.state = STILL_E2
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.x = 1200
        self.rect.y = 440
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.p_distancex = self.rect.centerx + 60 - player.rect.centerx
        self.p_distancey = self.rect.y - player.rect.y
        self.last_update = pygame.time.get_ticks()
        self.lives = 30
        self.i = 0 
        self.punches_tick = 500
        self.last_punch = pygame.time.get_ticks()
        self.animation_ticks = {
                STILL_E2: 100,
                PUNCH1: 80,
                PUNCH2: 80,
                PUNCH3: 80,
                HURT_E2: 100,
                DEAD_E1: 300,
                WALK_E2: 100,
                RUN_E2: 100
                }
    def update(self):
        self.speedy += GRAVIDADE
        now = pygame.time.get_ticks()
        
        self.rect.centerx += self.speedx
        self.p_distancex = self.rect.centerx - 35 - player.rect.centerx
        self.p_distancey = self.rect.centery - player.rect.centery
        
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.frame_ticks = self.animation_ticks.get(self.state, 200)
        # Se já está na hora de mudar de imagem...
        
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            
            # Reinicia a animação caso o índice da imagem atual seja inválido
            
            if self.frame >= len(self.animation):
                self.frame = 0
        
       
            
            
        socos = [PUNCH1,PUNCH2,PUNCH3]
        if now - self.last_punch > self.punches_tick:
            self.i += 1
            if self.i > 2:
                self.i = 0
            self.last_punch = now
            
        self.image = self.animation[self.frame]
        if self.lives <= 0:
            self.state = DEAD_E2
            self.frame = 4
            self.animation = self.animations[self.state]
        print(self.state, self.frame)
        self.image = pygame.transform.flip(self.image, True, False)
        if self.lives > 0:
            if abs(self.rect.y - player.rect.y) < 10: 
                if  0 < self.p_distancex and self.p_distancex < 200:
                    self.speedx -= 0.1
                    self.state = RUN_E2
                    
                elif -100 > self.p_distancex and self.p_distancex > -300:
                    self.image = self.image = self.animation[self.frame]
                    self.speedx += 0.1
                    self.state = RUN_E2
                
                elif 0 >= self.p_distancex and self.p_distancex > -56:
                    self.speedx = 0
                    self.state = socos[self.i]
                    if pygame.sprite.collide_mask(inimigo2,player):
                        player.lives -= 0.02
                        
                        if self.last_punch == now:
                            assets['punch_sound'].play()
                        
                        
                elif -60 >= self.p_distancex and self.p_distancex >= -100:
                    self.speedx = 0
                    self.image = self.animation[self.frame]
                    self.state = socos[self.i]
                    if pygame.sprite.collide_mask(inimigo2,player):
                        player.lives -= 0.02
                        if self.last_punch == now:
                            assets['punch_sound'].play()
                        

                else:
                    self.state = STILL_E2
                    self.speedx = 0
            else:
                self.state = STANCE_E2
                self.speedx = 0
        
              
         
        


# Classe jogador
class Player(pygame.sprite.Sprite):
    def __init__(self,assets,groups):
        pygame.sprite.Sprite.__init__(self)
        
        # Animacões
        self.animations = {
            STILL: assets['personagem'][0:7],
            WALK: assets['andar'][0:10],
            WALK_BACK: assets['andar'][0:9:-1],
            SHOT: assets['atira'][0:3],
            JUMP: assets['pular'][0:],
            FALLING: assets['pular'][5:6],
            LANDING: assets['pular'][8:],
            RELOAD: assets['recarga'][0:18],
            HURT: assets['ferido'][0:5],
            STOP_SHOOTING: assets['stop_shot'][0:],
            CORONHADA: assets['porrada'][0:]
        }
        self.municao = 50
        self.recarga = False
        self.direction = True
        self.state = STILL
        self.lives = 5
        self.start_recarga = pygame.time.get_ticks()
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = blocos_horizont[2].centerx
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.groups = groups
        self.recarga_ticks = 2500 
        self.shot_ticks = 100
        self.last_shot = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 200
        self.highest_y = self.rect.bottom
        # Ticks de cada animacao
        self.animation_ticks = {
                STILL: 100,
                WALK: 100,      
                WALK_BACK: 100,  
                SHOT: 50,       
                JUMP: 100,                    
                RELOAD: 140,   
                HURT: 200,       
                FALLING: 500,
                LANDING: 10,
                STOP_SHOOTING:100,
                CORONHADA: 50 

                }
    
    def update(self):
        # Gravidade       
        self.speedy += GRAVIDADE
        
        
        # Verifica os ticks
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.frame_ticks = self.animation_ticks.get(self.state, 200)
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            
            # Reinicia a animação caso o índice da imagem atual seja inválido
            
            if self.frame >= len(self.animation):
                self.frame = 0
           
        
            
            # Obtém o quadro da animação atual
        self.image = self.animation[self.frame]

        
            
        
        # Se a direção for 'False', inverte a imagem horizontalmente
        if not self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Nao deixar o boneco passar da tela
        
        if self.rect.top < -70:
            self.rect.top = -70
        if self.rect.bottom > alt_fundo + self.rect.height:
            self.rect.bottom = alt_fundo + self.rect.height

        if self.speedy < 0:
            self.highest_y = self.rect.bottom
        
        # Colisão entre player e bloco
        # Horizontais
        for bloco in platforms_horizont:
            if pygame.sprite.collide_mask(self, bloco):
                
                
                # Se pular e tiver um bloco em cima, nao é travado pelo bloco
                if self.speedy > 0:
                    if self.highest_y <= bloco.rect.top:
                        
                        self.rect.bottom = bloco.rect.top

                        self.highest_y = self.rect.bottom
                        
                        self.speedy = 0
                
                
                        

                # if self.speedx > 0 or self.speedx < 0:
                #     self.state = WALK
            
        # Verticais:
        for bloco in platforms_vert:
            if pygame.sprite.collide_mask(self, bloco):
                self.rect.right -= self.speedx
                if player.speedy > 0:
                    self.rect.y -= self.speedy
                    self.speedy = 0
    

    # Método de pulo
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        
        if self.speedy == 0:
            self.speedy = -20
            self.state = JUMP
        
        
    
    # Método para atirar
    def shot(self):

        now = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        elapsed_ticks = now - self.last_shot
        # Se houver munição disponível e não estiver recarregando
        if self.municao > 0 and not self.recarga and elapsed_ticks > self.shot_ticks :
            self.last_shot = now
            self.state = SHOT  # Defina o estado como "atirando"
            self.municao -= 1  # Reduz a munição em 1
            new_bullet = Bullet(self.assets, self.rect.centery + 30, self.rect.centerx, self.direction)
            # Adiciona os sprites da municao 
                        
            self.groups['all_bullets'].add(new_bullet)
            assets['shot_sound'].set_volume(0.1)
            assets['shot_sound'].play()
            
        
        # Se a munição acabar, inicie a recarga
        if self.municao <= 0 and not self.recarga:
            self.start_recarga = now  # Marca o tempo em que a recarga começa
            self.recarga = True  # Começa o processo de recarga
             
            
        # Verifica se o tempo de recarga já passou
        if self.recarga:
            self.state = RELOAD
            if now - self.start_recarga > self.recarga_ticks:
                self.municao = 60  # Recarrega munição
                self.recarga = False  # Termina a recarga
                self.state = STILL
                
# classe que representa os tiros
class Bullet(pygame.sprite.Sprite):
    def __init__(self,assets,bottom,centerx, direction):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = centerx
        self.rect.y = bottom
        if direction:
            self.speedx = 50
        else:
            self.speedx = -50

    def update(self):
        
        self.rect.x += self.speedx
        if self.rect.centerx > larg_fundo or self.rect.centerx < 0:
            self.kill()
        if pygame.sprite.collide_mask(self, inimigo2):
            inimigo2.lives -= 0.5
            print(inimigo2.lives)
        if pygame.sprite.collide_mask(self, inimigo1):
            inimigo1.lives -= 0.5
            print(inimigo1.lives)
       
        pygame.sprite.groupcollide(all_sprites, all_bullets, False, True, pygame.sprite.collide_mask)
        

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_bullets'] = all_bullets
groups['all_enemies'] = all_enemies
# chamando a classe player
player = Player(assets,groups)

# chamando a classe inimigo1
inimigo1 = Enemie1(assets)
all_sprites.add(inimigo1)
all_enemies.add(inimigo1)
# chamando a classe inmigo2
inimigo2 = Enemie2(assets)
all_sprites.add(inimigo2)
all_enemies.add(inimigo2)

# adicionando as plataformas no grupo all_sprites
for bloco in platforms_vert:
    all_sprites.add(bloco)
for bloco in platforms_horizont:
    all_sprites.add(bloco)

larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()
clock = pygame.time.Clock()

vidas = 5
font = pygame.font.Font('Sancreek-Regular.ttf', 48)
start_time = pygame.time.get_ticks()
game = True
assets['trilha_sonora'].play(loops=-1)
while game:
    
    clock.tick(FPS) 
    # Calcule o tempo decorrido 
    elapsed_ticks = pygame.time.get_ticks() - start_time # Converta o tempo decorrido para minutos e segundos 
    elapsed_seconds = elapsed_ticks / 1000
    minutes = int(elapsed_seconds // 60)
    seconds = int(elapsed_seconds % 60) 
    miliseconds = int((elapsed_ticks % 1000)//10)
    # Renderize o texto do cronômetro 
    timer_text = font.render(f'{minutes:02}:{seconds:02}:{miliseconds:02}', True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        key = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                player.speedx += 4
                player.state = WALK
                player.direction = True
            if event.key == pygame.K_a:
                player.speedx -= 4
                player.state = WALK
                player.direction = False
            if event.key == pygame.K_w:
                player.jump()

            if event.key == pygame.K_j:
                player.state = CORONHADA
                if pygame.sprite.collide_mask(player, inimigo1):
                    inimigo1.lives -= 2
                    
                if pygame.sprite.collide_mask(player, inimigo2):
                    inimigo2.lives -= 2
                    
                    
          
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d and player.state :
                player.speedx = 0
                player.state = STILL
                player.direction = True
            if event.key == pygame.K_a:
                player.speedx = 0
                player.direction = False
                player.state = STILL
            if event.key == pygame.K_SPACE:
                player.state = STILL
            if event.key == pygame.K_j:
                player.state = STILL

        if key[pygame.K_SPACE]:
            player.shot()
            
        #     player.speedx = 0
        # print(player.speedx)
    if player.lives <= 0:
        game = False
    if player.rect.bottom >= alt_fundo + player.rect.height:
        game = False
    camera_x = player.rect.centerx - LARG // 2
    camera_y = player.rect.centery - ALT // 2
    
    # limita a camera 
    camera_x = max(0, min(camera_x, larg_fundo - LARG)) 
    camera_y = max(0, min(camera_y, alt_fundo - ALT))
    
    window.fill((255, 255, 255))  
    window.blit(assets['fundo'],(-camera_x,-camera_y)) # atualiza o fundo
    window.blit(assets['munição'],(35,100))
    # Desenhando as vidas
    
    for i in range(round(player.lives)):
        window.blit(assets['vida'],(50 + i*40 ,50))
   

    texto = fonte.render(f'{player.municao} ∞ ', True, (255,255,255))
    window.blit(texto,(100,100))
    # pygame.draw.rect(window, (0,0,0), player.rect)
    for bullet in all_bullets:
        window.blit(bullet.image,(bullet.rect.x - camera_x,bullet.rect.y - camera_y))
    window.blit(player.image, (player.rect.x - camera_x, player.rect.y - camera_y)) # atualiza o jogador
    window.blit(inimigo1.image,(inimigo1.rect.x - camera_x,inimigo1.rect.y - camera_y))
    window.blit(inimigo2.image,(inimigo2.rect.x - camera_x,inimigo2.rect.y - camera_y))
    window.blit(timer_text, (750, 30))

    all_bullets.update()
    player.update()
    inimigo1.update()
    inimigo2.update()
    
    
    pygame.display.update()  # Atualiza a tela
    