from clases.enemigos.enemigo import Enemigo
from generar_random import generar_num_random


class Hormiga(Enemigo):
    def __init__(self,x=None):        

        super().__init__(x,543,20,5,'enemigo','assets/enemigos/Animations/Bloated Bedbug/BloatedBedbugIdleSide.png',4,1)

        
        self.velocidad_caminar = - generar_num_random(5,10)
    
    