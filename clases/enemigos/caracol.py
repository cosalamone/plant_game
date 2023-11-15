from clases.enemigos.enemigo import Enemigo


class Caracol(Enemigo):
    def __init__(self):
        super().__init__(510,510,30,10,'enemigo','assets/enemigos/Animations/Blazing Slug/BlazingSlugIdleSide.png',4,1)
        self.rect.y = 543

        self.velocidad_caminar = -2
    
    