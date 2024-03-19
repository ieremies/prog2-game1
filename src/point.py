import pygame
import sys
import random
import player


class Point(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()    

widthponto = random.randint(0, 800)
heightponto = random.randint(0, 800)

