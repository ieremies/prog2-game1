"""
Classe que implementa um Ponto que o jogador deve coletar.
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
        self.width = 50
        self.height = 50

        # Carrega a imagem do ponto e a redimensiona
        self.image = pygame.image.load("img/donkey.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Cria a "hitbox" do ponto
        self.rect = self.image.get_rect()

        # Posiciona o ponto em uma posição aleatória
        
        self.rect.x = random.randint(50, 350) * 1
        #A resolução de 
        self.rect.y = -50

    def update(self):
        """
        Atualiza a posição do ponto.
        """
        self.rect.y = self.rect.y + 5

        # TODO: da forma como está, o que acontece?
        # TODO: como fazer com que o ponto apareça no topo da tela e "caia"?
