import pygame
from constantes import *

def get_surface_from_spritsheet(path,columnas,filas,flip=False):
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
            if flip == True:
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
            lista.append(surface_fotograma)

    return lista


class Player:
    def __init__(self) ->None:
        self.walk_right = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.walk_left = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1,True)

        self.stand_up = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.frame = 0
        self.lives = 3
        self.score = 0

        self.move_x = 0
        self.move_y = 0

        self.animation = self.stand_up
        self.img = self.animation[self.frame]
        self.rect = self.img.get_rect()

    def control(self,action,x=0,y=0):
        self.move_x = x
        self.move_y = y
        if (action == 'walk_right'):
            self.animation = self.walk_right
            self.frame = 0
        if (action == 'walk_left'):
            self.animation = self.walk_left
            self.frame = 0

        if (action == 'stand_up'):
            self.animation = self.stand_up
            self.frame = 0


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


