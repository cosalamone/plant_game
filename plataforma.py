import pygame
from constantes import *

class Plataforma:
    def __init__(self):
        pass


    def draw(self, screen):
        self.img = self.animation(self.frame)
        screen.blit(self.img, self.rect)