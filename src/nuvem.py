"""
Classe que implementa uma Nuvem.
"""

import pygame
import random


class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        """
        Inicializa a nuvem.
        """
        super().__init__()

        # Tamanho da nuvem
        self.width = 100
        self.height = 150

        # Carrega a imagem do ponto e a redimensiona
        self.image = pygame.image.load("img/nuvem.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Cria a "hitbox" do ponto
        self.rect = self.image.get_rect()

        # Posiciona o ponto em uma posição aleatória

        self.rect.x = random.randint(-50, 450)
        # A resolução de
        self.rect.y = -100

    def update(self):
        """
        Atualiza a posição do ponto.
        """
        self.rect.y = self.rect.y + 2

        # deleta o objeto se estiver fora da tela
        if self.rect.y > 700:
            self.kill()
