import pygame
import sys

# Inicialização do PyGame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('The Godfather Original Theme Song.mp3')


# Configurações da tela
LARGURA, ALTURA = 900, 550
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela de Menu")

# Carregar imagem de fundo
imagem_fundo = pygame.image.load("Imagem de Intro - PyGame.jpg")
nova_alt_fundo = imagem_fundo.get_height() * 0.7
nova_larg_fundo = imagem_fundo.get_width() * 0.7
imagem_fundo = pygame.transform.scale(imagem_fundo, (nova_larg_fundo, nova_alt_fundo))

# Carregar imagem de título
imagem_titulo = pygame.image.load("Título Game.png")
imagem_titulo = pygame.transform.scale(imagem_titulo, (400, 400))
posicao_imagem = (LARGURA + 100 , 0)

# Configurações do texto
fonte = pygame.font.Font('Sancreek-Regular.ttf', 48)  # Fonte e tamanho do texto
texto = "Press SPACE to start"
cor_texto = (255, 255, 255)  # Cor branca
cor_fundo_texto = (0, 0, 0)  # Cor preta para o fundo do texto
posicao_texto = (LARGURA // 2, ALTURA // 2 + 200)

# Variável para controlar o piscar do texto
mostrar_texto = True
tempo_mudanca = pygame.time.get_ticks()

# Função principal
def main():
    pygame.mixer.music.load('The Godfather Original Theme Song.mp3')
    pygame.mixer.music.play(loops=-1)
    global mostrar_texto, tempo_mudanca  # Declare as variáveis globais aqui
    rodando = True
    while rodando:
        tela.blit(imagem_fundo, (0, 0))  # Desenha a imagem de fundo
        tela.blit(imagem_titulo, (0, 0))

        # Verificar o tempo para alternar entre mostrar ou não o texto
        if pygame.time.get_ticks() - tempo_mudanca > 500:  # Alterna a cada 500 ms
            mostrar_texto = not mostrar_texto
            tempo_mudanca = pygame.time.get_ticks()

        # Desenhar o texto animado com retângulo de fundo
        if mostrar_texto:
            texto_surface = fonte.render(texto, True, cor_texto)
            texto_rect = texto_surface.get_rect(center=posicao_texto)
            
            # Desenhar o retângulo preto atrás do texto
            pygame.draw.rect(tela, cor_fundo_texto, texto_rect.inflate(20, 10))  # Aumenta um pouco o retângulo

            # Desenhar o texto sobre o retângulo preto
            tela.blit(texto_surface, texto_rect)

        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    rodando = False  # Sai do loop e inicia o jogo
                    pygame.mixer.music.stop()

        pygame.display.flip()  # Atualiza a tela
        pygame.time.Clock().tick(60)  # Controla a taxa de quadros (60 FPS)

# Executa a função principal
if __name__ == "__main__":
    main()
