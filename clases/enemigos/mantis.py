from clases.enemigos.enemigo import Enemigo
from clases.player.player import Player
from generar_random import generar_num_random


class Mantis(Enemigo):
    def __init__(self,x=None):
        super().__init__(x,510,30,15,'enemigo','assets/enemigos/Animations/Lethal Scorpion/LethalScorpionIdleSide.png',4,1)

        self.velocidad_caminar = - generar_num_random(8,12)
        # self.rect.x = x
    
    def esta_atacando(self, planta, player:Player):
        if player.rect.colliderect(self.rect):
            player.es_atacado(self)
            self.rect.x = player.rect.x + 60

            return 'GAME OVER'