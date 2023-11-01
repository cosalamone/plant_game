import pygame
from constantes import *

def get_surface_from_spritsheet(path:str,columnas:int,filas:int,flip:bool=False):
    lista = []
    surface_img = pygame.image.load(path)
    fotograma_ancho = int(surface_img.get_width()/columnas)
    fotograma_alto = int(surface_img.get_height()/filas)
    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            # print(x,y,fotograma_alto, fotograma_ancho)
            surface_fotograma = surface_img.subsurface(x,y,fotograma_ancho,fotograma_alto)
            if flip == True:
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
            lista.append(surface_fotograma)

    return lista


class Player:
    def __init__(self,x:int,y:int,speed_walk:int,speed_run:int,) -> None:

        self.mirando_right = True
        self.action = 'quieto'
        self.img_walk_right = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.img_walk_left = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_walk.png',6,1,True)

        self.img_stand_up_right = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.img_stand_up_left = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_idle.png',4,1, True)
        
        self.img_jump_right = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_jump.png',6,1)
        self.img_jump_left = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_jump.png',6,1,True)
        self.jumping = False
        self.height_jump = -20
        self.limit_vel_caida = self.height_jump * -1
        self.gravity = 3

        self.img_hurt = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_hurt.png',3,1)
        self.img_death = get_surface_from_spritsheet('assets/characters/GraveRobber/GraveRobber_death.png',6,1)

        self.frame = 0
        self.lives = 3
        self.score = 0

        self.move_x = x
        self.move_y = y

        self.speed_walk = speed_walk 
        self.speed_run = speed_run


        self.animation = self.img_stand_up_right
        self.img = self.animation[self.frame]
        # self.img = pygame.transform.scale(self.img,(100,100))
        self.rect = self.img.get_rect()
        self.rect.x = 15
        self.rect.y = 500

    def control(self, velocidad_caminar):

        self.rect.x += velocidad_caminar 


        # if (self.action == 'walk_right'):
        #     self.mirando_right = True
        #     self.move_x = self.speed_walk
        #     # self.animation = self.img_walk_right
        #     self.frame = 0

        # elif (self.action == 'jump'):
        #     if not self.jumping:
        #         self.jumping = True
        #         #self.move_x = 0
        #         self.move_y = self.height_jump
        #         self.frame = 0

        # elif (self.action == 'walk_left'):
        #     self.mirando_right = False
        #     self.move_x = -self.speed_walk
        #     # self.animation = self.img_walk_left
        #     self.frame = 0

        # elif (self.action == 'stand_up'):
        #     # if self.mirando_right == True:
        #         # self.animation = self.img_stand_up_right
        #     # else:
        #     #     self.animation = self.img_stand_up_left

        #     self.move_x = 0
        #     self.move_y = 0
        #     self.frame = 0



        # elif (action == 'stand_up_left'):
        #     self.mirando_right = False
        #     self.animation = self.img_stand_up_left
        #     self.move_x = 0
        #     self.move_y = 0
        #     self.frame = 0


    def aplicar_gravedad(self, screen, lista_img):
        if self.jumping ==  True:
            self.draw(screen,lista_img) 
            self.rect.y += self.move_y
            if (self.move_y + self.gravity) < self.limit_vel_caida:
                self.move_y += self.gravity

            if self.rect.y >= 480:
                self.jumping = False
                self.move_y = 0
            else:
                self.jumping = True

    def update(self,screen):

        if self.action == 'walk_right':
            self.mirando_right = True
            if  not self.jumping:
                self.draw(screen,self.img_walk_right )
            self.control(self.speed_walk)

        elif self.action == 'walk_left': 
            self.mirando_right = False
            if not self.jumping:
                self.draw(screen,self.img_walk_left )
            self.control(self.speed_walk * -1)

        elif self.action == 'jump':
            if self.jumping == False:
                self.jumping = True
                self.move_y = self.height_jump

        elif self.action == 'stand_up':
            if not self.jumping:
                if self.mirando_right == True:
                    self.draw(screen,self.img_stand_up_right )
                elif self.mirando_right == False: 
                    self.draw(screen,self.img_stand_up_left )
        

        if self.mirando_right == True:
            self.aplicar_gravedad(screen, self.img_jump_right)
        else:
            self.aplicar_gravedad(screen, self.img_jump_left)

        # self.rect.x += self.move_x
        # self.rect.y += self.move_y

    def draw(self, screen, lista_animaciones):
            
        if (self.frame >= len(lista_animaciones) - 1):
            self.frame = 0

        self.img = lista_animaciones[self.frame]
        self.img = pygame.transform.scale(self.img,(130,130))
        screen.blit(self.img, self.rect)
        self.frame += 1
        
        if self.jumping == True  and self.frame == 2:
            self.frame = 0

