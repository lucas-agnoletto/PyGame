import pygame
from assets import load_assets
from config import FPS, ALT, LARG

pygame.init()


window = pygame.display.set_mode((LARG,ALT))
pygame.display.set_caption('Máfia 5')
rect = pygame.Rect
# blocos para haver colisão
blocos_horizont = [rect(0,632,80,10),rect(0,440, 335, 10),rect(195,590,145,10),rect(94,729,360,10),rect(445,630,430,10),rect(875,530,217,10),rect(1090,630,300,10),rect(1200,260,390,10),rect(1350,530,60,10),rect(1405,440,350,10),rect(1750,490,345,10),rect(2090,630,200,10),rect(2600,530,60,10),rect(2650,490,530,10)] 
blocos_vert = [rect(75,640,10,100),rect(445,640,10,100),rect(875,540,10,100),rect(1090,535,10,100),rect(1350,530,10,100),rect(1400,445,10,100),rect(1746,445,10,60),rect(2090,500,10,150),rect(2280,630,10,200),rect(2600,542,10,500),rect(2650,500,10,40)]
# carregar assets
GRAVIDADE = 0.6

assets = load_assets()


STILL = 0
WALK = 1
WALK_BACK = 2
SHOT = 3
JUMP = 4
FALLING = 5
LANDING = 6
RECHARGE = 7
HURT = 8
STOP_SHOOTING = 9

# Medidas do background
larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()
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

# Classe jogador
class Player(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        assets['stop_atira'] = [assets['atira'][3],assets['atira'][0]]
        # Animacões
        self.animations = {
            STILL: assets['personagem'][0:7],
            WALK: assets['andar'][0:10],
            WALK_BACK: assets['andar'][0:9:-1],
            SHOT: assets['atira'][1:3],
            JUMP: assets['pular'][:6],
            FALLING: assets['pular'][5:6],
            LANDING: assets['pular'][8:],
            RECHARGE: assets['recarga'][0:18],
            HURT: assets['ferido'][0:5],
            STOP_SHOOTING: assets['stop_atira'][1:]

        }
        self.municao = 30
        self.JUMPING = False
        self.direction = True
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 35
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 200

        # Ticks de cada animacao
        self.animation_ticks = {
                STILL: 100,
                WALK: 100,      
                WALK_BACK: 100,  
                SHOT: 50,       
                JUMP: 150,                    
                RECHARGE: 300,   
                HURT: 200,       
                FALLING: 150,
                LANDING:10,
                STOP_SHOOTING:100   

                }
    
    def update(self):
        # Gravidade        
        if self.speedy > 0:
            self.state = FALLING

        self.speedy += GRAVIDADE
        self.on_ground = False
        
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
        for bloco in platforms_horizont:
            if pygame.sprite.collide_mask(self, bloco):
                
                if self.state != SHOT:
                    self.state = STILL
                self.rect.y -= self.speedy
                self.speedy = 0

                if self.speedy > 0:
                    self.state = LANDING
                    

                if self.speedx > 0 or self.speedx < 0:
                    self.state = WALK
              
        for bloco in platforms_vert:
            if pygame.sprite.collide_mask(self, bloco):
                self.rect.right -= self.speedx
                # if player.speedy > 0:
                self.rect.y -= self.speedy
                self.speedy = 0
    # Método de pulo
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL or self.state == WALK :
                self.speedy = -20
                self.state = JUMP
                self.JUMPING = True
    
    # Método para atirar
    def shot(self):
        if self.municao > 0:
            self.state = SHOT
            self.municao -= 1
        if self.municao <= 0:
            self.state = RECHARGE
            self.municao += 30


    
        

        
player = Player(assets)
larg_fundo = assets['fundo'].get_width()
alt_fundo = assets['fundo'].get_height()
clock = pygame.time.Clock()

game = True
while game:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
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
            if event.key == pygame.K_SPACE:
                player.shot()
                player.municao -= 1
                
                
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_d:
                player.speedx -= 4
                player.state = STILL
                player.direction = True
            if event.key == pygame.K_a:
                player.speedx += 4
                player.direction = False
                player.state = STILL
            if event.key == pygame.K_SPACE:
                player.state = STOP_SHOOTING

    camera_x = player.rect.centerx - LARG // 2
    camera_y = player.rect.centery - ALT // 2
    
    # limita a camera 
    camera_x = max(0, min(camera_x, larg_fundo - LARG)) 
    camera_y = max(0, min(camera_y, alt_fundo - ALT))
    
    window.fill((255, 255, 255))  
    window.blit(assets['fundo'],(-camera_x,-camera_y)) # atualiza o fundo
    window.blit(assets['munição'],(35,100))
    window.blit(assets['vida'],(50,50))
    # pygame.draw.rect(window, (0,0,0), player.rect)

    window.blit(player.image, (player.rect.x - camera_x, player.rect.y - camera_y)) # atualiza o jogador
    
    #     pygame.draw.rect(window, (0, 255, 0), (bloco.x, bloco.y, bloco.width, bloco.height))
    # for bloco in blocos_vert:
    #     pygame.draw.rect(window, (0, 255, 0), (bloco.x, bloco.y, bloco.width, bloco.height))
    
    player.update()
    
    
    pygame.display.update()  # Atualiza a tela
    