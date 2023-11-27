from clases.enemigos.enemigo import Enemigo
from funciones import generar_num_random


class Caracol(Enemigo):
    def __init__(self,x=None):
        super().__init__(x,543,30,10,'enemigo','./assets/enemigos/Animations/Blazing Slug/BlazingSlugIdleSide.png',4,1)


        self.velocidad_caminar = - generar_num_random(2,7)
    
    