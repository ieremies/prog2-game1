"""
Classe que implementa o Jogador.
"""

import pygame

screen_width = 400
screen_height = 600




# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 100
        self.height = 100

        # Carrega a imagem do jogador
        self.image = pygame.image.load("img/shrek.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Define essa propriedade chamada mov_speed
        self.mov_speed = 25

        # Cria a hitbox do jogador
        self.rect = self.image.get_rect()

        # Inicia ele no centro
        self.rect.center = (screen_width // 2, screen_height // 2)

    def move(self, keys):
        """
        Altera a posição do jogador baseado nas teclas pressionadas.
        """
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.mov_speed
        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += self.mov_speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.mov_speed
        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.mov_speed

        # TODO Se o seu jogador é na verdade um balão, ele não deveria se mover
        # mais rápido para baixo do que para cima?
