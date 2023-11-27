import pygame
from clases.personaje.personaje import Personaje
from constantes import *
from funciones import mostrar_texto
import obtener_imagenes

class Player(Personaje):
    def __init__(self,x:int,y:int,speed_walk:int,) -> None:
        super().__init__(x,y,150,'',None,0,0)
        self.mirando_der = True

        self.action = 'quieto'
        self.img_walk_right = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.img_walk_left = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_walk.png',6,1,True)

        self.img_stand_up_right = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.img_stand_up_left = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_idle.png',4,1, True)
        
        self.img_jump_right = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_jump.png',6,1)
        self.img_jump_left = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_jump.png',6,1,True)
        
        self.img_attack_right = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_attack2.png',6,1)
        self.jumping = False
        self.height_jump = -20

        self.limite_velocidad_caida = self.height_jump * -1
        self.gravity = 4

        self.img_hurt = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_hurt.png',3,1)
        self.img_death = obtener_imagenes.get_surface_from_spritsheet(
            './assets/characters/GraveRobber/GraveRobber_death.png',6,1)

        self.frame = 0
        self.score = 0

        self.visible = True

        self.potencia_golpe = 10

        self.speed_walk = speed_walk 

        self.animation = self.img_stand_up_right # animacion que se va a mostrar / al iniciar arranca con stand up
        self.img = self.animation[self.frame]

        self.rect = self.img.get_rect()
        self.rect.x = 35
        self.rect.y = 520

        self.rect_collision = pygame.Rect((60,90),(35,70))

    def walk(self, screen, walking):
        if walking == 'walk_right':
            self.mirando_der = True

            if not self.jumping:
                self.draw(screen, self.img_walk_right )
            self.control(self.speed_walk)

        elif walking == 'walk_left': 
            self.mirando_der = False
            if not self.jumping:
                self.draw(screen, self.img_walk_left )
            self.control(self.speed_walk * -1)

    def jump(self):
        if self.action == 'jump':
            if self.jumping == False:
                self.jumping = True
                self.move_y = self.height_jump

    def attack(self,screen):
        if self.action == 'attack':
            self.draw(screen, self.img_attack_right)

    def stand_up(self,screen,standing,posicion=False, cambio_nivel=False):
        if posicion and cambio_nivel:
            self.rect.x = posicion
        if standing == 'stand_up':
            if not self.jumping:
                if self.mirando_der == True:
                    self.draw(screen, self.img_stand_up_right )
                elif self.mirando_der == False: 
                    self.draw(screen, self.img_stand_up_left)

    def control(self, velocidad_caminar):
        self.rect.x += velocidad_caminar 


    def aplicar_gravedad(self, screen, lista_img):
        if self.jumping ==  True:
            self.draw(screen, lista_img) 
            self.rect.y += self.move_y
            if (self.move_y + self.gravity) < self.limite_velocidad_caida:
                self.move_y += self.gravity

            if self.rect.y >= 520:
                self.jumping = False
                self.move_y = 0
            else:
                self.jumping = True

        
    def update(self,screen, posicion_inicio, cambio_nivel=False):

        if self.action == 'walk_right': 
            self.walk(screen, 'walk_right')
        elif self.action == 'walk_left': 
            self.walk(screen, 'walk_left')
        elif self.action == 'stand_up':
            self.stand_up(screen,'stand_up', posicion_inicio,cambio_nivel )
        elif self.action == 'jump':
            self.jump()
        elif self.action == 'attack':
            self.attack(screen)
    
        if self.mirando_der == True:
            self.aplicar_gravedad(screen, self.img_jump_right)
        else:
            self.aplicar_gravedad(screen, self.img_jump_left)
        

    def draw(self, screen, lista_animaciones):
        if (self.frame >= len(lista_animaciones) - 1):
            self.frame = 0

        self.img = lista_animaciones[self.frame]
        self.img = pygame.transform.scale(self.img,(100,100))

        if self.visible == True:
            screen.blit(self.img, self.rect)
            self.frame += 1
        
            if self.jumping == True and self.frame == 2:
                self.frame = 0
        mostrar_texto(screen,f'SCORE: {self.score}', COLOR_BLANCO,(10, 10),25)

        
        if self.vida >= 0:
            mostrar_texto(screen,f'VIDA PLAYER: {self.vida}', COLOR_BLANCO,(240, 10),25)




