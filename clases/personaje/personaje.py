import pygame
from constantes import *
import obtener_imagenes

class Personaje():
    def __init__(self,x:int,y:int,vida:int,enemigo:str,path:str,columnas:int=0,filas:int= 0):
        if path != None:
            self.img = obtener_imagenes.get_surface_from_spritsheet(path,columnas,filas,True,True,enemigo)
            self.frame = 0
            self.animation = self.img
            self.img = self.animation[self.frame]
            self.rect = self.img.get_rect() #obtener rectangulo de img
            self.rect.x = x
            self.rect.y = y  


        self.visible = True
        self.velocidad_caminar = 0

        self.vida = vida
        self.contador_ataques = 0

    def herido(self, daño):
        self.rect.x -= self.velocidad_caminar * 10
        self.vida -= daño
        print(self.vida)
        if self.vida <= 0:
            self.visible = False
            return 'muerto'
        
        
    def es_atacado(self, atacante):
        huboColision = atacante.rect.colliderect(self.rect)
        if self.visible == True and huboColision:
            self.contador_ataques += 1
            print('hubo colision',self.contador_ataques)
            return self.herido(atacante.potencia_golpe)

