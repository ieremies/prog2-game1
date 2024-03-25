try:
    import pygame
except ImportError:
    print("Pygame não está instalado. Instale-o com 'pip3 install pygame'")
    print("Confira o README.md para mais informações.")
    exit()

import sys
import player
import point

# Inicializa o jogo
pygame.init()

# configurar player
p = player.Player()
group_player = pygame.sprite.Group()
group_player.add(p)

# Configura o display
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

# Define a cor branco(player)
white = (255, 255, 255)

# bolinhas
# TODO: Faça o mesmo processo que fizemos para criar um jogador
# Lembre de colocá-las num grupo
group_points = pygame.sprite.Group()
for _ in range(3):
    group_points.add(point.Point())


# Cria um relógio
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white)  # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed()
    p.move(keys)
    group_player.draw(screen)

    # TODO: Lembre de desenhas as bolinhas e atualizar a posição delas

    # TODO conferir colisão usando pygame.sprite.spritecollide(grupo1, grupo2, True)

    # TODO você pode usar sons da seguinte forma:
    # sound = pygame.mixer.Sound("sound.wav")
    # pygame.mixer.Sound.play(sound)
    # Você pode baixar sons de efeitos sonoros gratuitos em https://mixkit.co/free-sound-effects/
    # ou https://www.findsounds.com/category.html

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
