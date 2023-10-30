import pygame
from constantes import *

def get_surface_from_spritsheet(path,columnas,filas):
    lista = []
    surface_img = pygame.image.load(path)
    fotograma_ancho = int(surface_img.get_width()/columnas)
    fotograma_alto = int(surface_img.get_height()/filas)
    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            # print(x,y,fotograma_alto, fotograma_ancho)
            surface_fotograma = surface_img.subsurface(x,y,fotograma_ancho,fotograma_alto)
            lista.append(surface_fotograma)

    return lista


class Player:
    def __init__(self) ->None:
        self.walk = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.stand_up = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.frame = 0
        self.lives = 3
        self.score = 0

        self.move_x = 0
        self.move_y = 0

        self.animation = self.walk
        self.img = self.animation[self.frame]
        self.rect = self.img.get_rect()

    def control(self,x=0,y=0):
        self.move_x = x
        self.move_y = y

    def update(self):
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0

        self.rect.x += self.move_x
        self.rect.y += self.move_y


    def draw(self, screen):
        self.img = self.animation[self.frame]
        screen.blit(self.img, self.rect)


