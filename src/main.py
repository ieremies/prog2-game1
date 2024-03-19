import pygame
import sys
import random
import player

# Inicializa o jogo
pygame.init()

#configurar player
p = player.Player()
group_player = pygame.sprite.Group()
group_player.add(p)

# Configura o display
width = 800 
height = 800
widthponto = random.randint(0, 800)
heightponto = random.randint(0, 800)
screen = pygame.display.set_mode((width, height))


# Defini a cor branco(player)
white = (255, 255, 255)

# bolinhas
point_size = 15
point_x = widthponto // 2 - point_size // 2
point_y = heightponto // 2 - point_size // 2

# Cria um relógio
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white) # pinta a tela de branco

    # Confere se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # um dicionário: keys[pygame.K_w] é True se a tecla w foi pressionada
    keys = pygame.key.get_pressed() 

    p.move(keys)
    group_player.draw(screen)

    # Desenha o Ponto
    pygame.draw.rect(screen,(0, 0, 0), (point_x, point_y, point_size, point_size))




    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
