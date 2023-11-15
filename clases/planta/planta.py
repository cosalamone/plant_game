import pygame
from clases.personaje.personaje import Personaje
from constantes import *
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
        # pygame.draw.rect(screen,COLOR_GRIS_CLARO,self.rect)
        if self.visible == True:
            screen.blit(self.img, self.rect)
            self.frame += 1

        if self.vida >= 0:
            font = pygame.font.SysFont('Arial Narrow', 50)
            text = font.render(f'VIDA PLANTA: {self.vida}', True, COLOR_BLANCO)
            screen.blit(text, (600, 10))