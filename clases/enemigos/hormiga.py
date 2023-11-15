from clases.enemigos.enemigo import Enemigo


class Hormiga(Enemigo):
    def __init__(self,x):
        super().__init__(500,500,20,5,'enemigo','assets/enemigos/Animations/Bloated Bedbug/BloatedBedbugIdleSide.png',4,1)
        self.rect.y = 543
        self.rect.x = x
        
        self.velocidad_caminar = -5
    
    