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


# build up our point
po1 = point.Point()
group_point = pygame.sprite.Group()
group_point.add (po1)

nuv = nuvem.Nuvem()
group_nuvens = pygame.sprite.Group()
group_nuvens.add (nuv)

# Configura o display
width = 400
height = 600
screen = pygame.display.set_mode((width, height))

# Define a cor branco(player)
white = (135, 206, 235)

# bolinhas
# TODO: Faça o mesmo processo que fizemos para criar um jogador
# Lembre de colocá-las num grupo
group_points = pygame.sprite.Group()


for _ in range(3):
    group_points.add(point.Point())

# Cria um relógio
clock = pygame.time.Clock()
running = True

sound = pygame.mixer.Sound("sound.wav")

contador_burro = 0
contador_nuvem = 0
limite_contador_burro = 100

while running:
    screen.fill(white)  # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed()
    p.move(keys)
    
    
    group_nuvens.draw(screen)
    group_point.draw(screen)
    group_player.draw(screen)
    group_nuvens.update()
    group_point.update()

    contador_burro += 1
    if contador_burro == limite_contador_burro:
        group_point.add(point.Point())
        contador_burro = 0
        if limite_contador_burro > 20:
            limite_contador_burro -= 1

    limite_contador_nuvem = 60
    contador_nuvem += 1
    if contador_nuvem == limite_contador_nuvem:
        group_nuvens.add(nuvem.Nuvem())
        contador_nuvem = 0


    # TODO: Lembre de desenhas as bolinhas e atualizar a posição delas

    # TODO conferir colisão usando pygame.sprite.spritecollide(grupo1, grupo2, True)
    if pygame.sprite.spritecollide(p, group_point, True):
        pygame.mixer.Sound.play(sound)


    # TODO você pode usar sons da seguinte forma:
    
    
    # Você pode baixar sons de efeitos sonoros gratuitos em https://mixkit.co/free-sound-effects/
    # ou https://www.findsounds.com/category.html

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
