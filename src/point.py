"""
Classe que implementa um Ponto que o jogador deve desviar.
"""

import pygame
import random


class Point(pygame.sprite.Sprite):
    def __init__(self):
        """
        Ao ser instanciado, cria um ponto em uma posição aleatória.
        """
        super().__init__()

        # Tamanho do ponto
        self.width = 40
        self.height = 40

        # Carrega a imagem do ponto e a redimensiona
        self.image = pygame.image.load("img/pedra.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Cria a "hitbox" do ponto
        self.rect = self.image.get_rect()

        # Posiciona o ponto em uma posição aleatória

        self.rect.x = random.randint(50, 350) * 1
        # A resolução de
        self.rect.y = -50

        self.velocidade = 2

    def update(self):
        """
        Atualiza a posição do ponto.
        """

        self.rect.y = self.rect.y + self.velocidade
        self.velocidade = self.velocidade + 0.5

        if self.rect.y > 700:
            self.kill()
