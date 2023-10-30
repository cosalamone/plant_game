import pygame
from constantes import *



class Player:
    def __init__(self) ->None:
        self.walk = []
        self.stand_up = []
        self.frame = 0
        self.lives = 3
        self.score = 0

        self.animation = self.stand_up
        self.img = self.animation[self.frame]
        self.rect = self.img.get_rect()


