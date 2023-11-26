import pygame
from clases.personaje.personaje import Personaje
from constantes import *
from funciones import mostrar_texto
import obtener_imagenes



class Planta(Personaje):
    def __init__(self):
        super().__init__(15,581,50,'planta','assets/Cactus_Sprite_Sheet_baby_.png',2,1)


    def update(self,screen) :
        self.draw(screen, self.animation)

    def draw(self,screen,animation):
        if (self.frame >= len(animation) - 1):
            self.frame = 0

        self.img = animation[self.frame]
        if self.visible == True:
            screen.blit(self.img, self.rect)
            self.frame += 1

        if self.vida >= 0:
            mostrar_texto(screen,f'VIDA PLANTA: {self.vida}', COLOR_BLANCO,(600, 10),25)