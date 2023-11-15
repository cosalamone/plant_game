from clases.enemigos.enemigo import Enemigo
from clases.player.player import Player


class Mantis(Enemigo):
    def __init__(self):
        super().__init__(510,510,30,15,'enemigo','assets/enemigos/Animations/Lethal Scorpion/LethalScorpionIdleSide.png',4,1)

        self.velocidad_caminar = -10
    
    def esta_atacando(self, planta, player:Player):
        if player.rect.colliderect(self.rect):
            player.es_atacado(self)
            self.rect.x = player.rect.x + 60

            return 'GAME OVER'