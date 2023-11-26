import random
import pygame
from clases.personaje.personaje import Personaje
from clases.planta.planta import Planta
from constantes import *
from generar_random import generar_num_random
import obtener_imagenes

# caminar
# atacar
# herir

class Enemigo(Personaje):
    
    def __init__(self, x:int,y:int,vida:int,potencia_golpe:int,enemigo:str,path:str,columnas:int=0,filas:int= 0):
        if x == None:
            x = generar_num_random(500,1200)
        super().__init__(x,y,vida,enemigo,path,columnas,filas)
        self.potencia_golpe = potencia_golpe

    def walk(self,screen):
        self.draw(screen, self.animation)
        if self.rect.x < -10:
            self.rect.x = 1050
        else:
            self.rect.x += self.velocidad_caminar

    def esta_atacando(self, planta:Planta, player):
        if planta.rect.colliderect(self.rect):
            self.rect.x = planta.rect.x + 50
            planta.es_atacado(self)
            return 'GAME OVER'

    def update(self,screen):
        self.walk(screen)
        self.draw(screen, self.animation )

    def draw(self,screen,animation):
        if (self.frame >= len(animation) - 1):
            self.frame = 0
        self.img = animation[self.frame]
        # pygame.draw.rect(screen,COLOR_CELESTE,self.rect)
        if self.visible == True:
            screen.blit(self.img, self.rect)
            self.frame += 1