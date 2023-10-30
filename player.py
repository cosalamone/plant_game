import pygame
from constantes import *

def get_surface_from_spritsheet(path:str,columnas:int,filas:int,flip:bool=False):
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
    def __init__(self,x:int,y:int,speed_walk:int,speed_run:int,gravity=0) -> None:
        self.walk_right = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.walk_left = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1,True)

        self.stand_up = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.frame = 0
        self.lives = 3
        self.score = 0

        self.move_x = x
        self.move_y = y

        self.speed_walk = speed_walk
        self.speed_run = speed_run

        self.gravity = gravity

        self.animation = self.stand_up
        self.img = self.animation[self.frame]
        # self.img = pygame.transform.scale(self.img,(100,100))
        self.rect = self.img.get_rect()
        self.rect.x = 15
        self.rect.y = 500

    def control(self,action:str):

        if (action == 'walk_right'):
            self.move_x = self.speed_walk
            self.animation = self.walk_right
            self.frame = 0

        elif (action == 'walk_left'):
                self.move_x = -self.speed_walk
                self.animation = self.walk_left
                self.frame = 0

        elif (action == 'stand_up'):
            self.animation = self.stand_up
            self.move_x = 0
            self.move_y = 0
            self.frame = 0


    def update(self):
        # va pasando de frames siempre y cuando no supere el maximo; sino regresa al primer frame
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0

        self.rect.x += self.move_x
        self.rect.y += self.move_y


    def draw(self, screen):
        self.img = self.animation[self.frame]
        self.img = pygame.transform.scale(self.img,(130,130))
        screen.blit(self.img, self.rect)


