try:
    import pygame
except ImportError:
    print("Pygame não está instalado. Instale-o com 'pip3 install pygame'")
    print("Confira o README.md para mais informações.")
    exit()

import sys
import player
import point
import nuvem

# Inicializa o jogo
pygame.init()

# configurar player
p = player.Player()
group_player = pygame.sprite.Group()
group_player.add(p)

# cria o primeiro ponto
group_point = pygame.sprite.Group()
group_point.add(point.Point())

# cria a primeira nuvem
group_nuvens = pygame.sprite.Group()
for _ in range(3):
    group_nuvens.add(nuvem.Nuvem())

# Configura o display
width = 400
height = 600
screen = pygame.display.set_mode((width, height))

# Define a cor branco(player)
white = (135, 206, 235)

# Cria um relógio
clock = pygame.time.Clock()
running = True

sound = pygame.mixer.Sound("sound.wav")

contador_point = 0
contador_nuvem = 0
limite_contador_point = 100
limite_contador_nuvem = 60

pontuacao = 0

while running:
    screen.fill(white)  # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    group_nuvens.update()
    group_nuvens.draw(screen)
    group_point.update()
    group_point.draw(screen)

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed()
    p.move(keys)
    group_player.draw(screen)

    contador_point += 1
    if contador_point == limite_contador_point:
        group_point.add(point.Point())
        contador_point = 0
        if limite_contador_point > 20:
            limite_contador_point -= 1

    contador_nuvem += 1
    if contador_nuvem == limite_contador_nuvem:
        group_nuvens.add(nuvem.Nuvem())
        contador_nuvem = 0

    if pygame.sprite.spritecollide(p, group_point, True):
        pygame.mixer.Sound.play(sound)
        # pisca a tela de vermelho
        screen.fill((255, 0, 0))
        pontuacao -= (height - p.rect.y) // 10

    # para cada ponto, se estiver depois do player, adiciona 1 ponto
    for po in group_point:
        if po.rect.y > p.rect.y:
            pontuacao += 1

    # desenha a pontuação
    font = pygame.font.Font(None, 36)
    text = font.render(str(pontuacao), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
