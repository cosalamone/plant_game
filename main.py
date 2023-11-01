import pygame
import sys
from constantes import *
from player import Player


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')
# img_background = pygame.transform.scale(img_background,(ANCHO_VENTANA, ALTO_VENTANA))

player = Player(0,0,10,20)
plataforma = pygame.image.load('assets\plataforma\plataform (1).png')
plataforma = pygame.transform.scale(plataforma, (250,40))
flag_playing = True

while flag_playing:
    lista_events = pygame.event.get()
    for event in lista_events:
        if event.type == pygame.QUIT:
            flag_playing = False
            pygame.quit()
            sys.exit() # cierra la app

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and player.jumping == False:
        player.action = 'jump'
    
    elif teclas[pygame.K_RIGHT]:
        player.action='walk_right'
    
    elif teclas[pygame.K_LEFT]:
        player.action='walk_left'
    
    else:
        player.action='stand_up'




        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player.control('walk_right')

        # # if event.type == pygame.KEYUP:
        # #     if event.key == pygame.K_RIGHT:
        # #         player.control('stand_up_right')

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.control('walk_left')

        # # if event.type == pygame.KEYUP:
        # #     if event.key == pygame.K_LEFT:
        # #         player.control('stand_up_left')     

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         player.control('jump')
                

    # lista_teclas = pygame.key.get_pressed()
    # if True in lista_teclas:
    #     if lista_teclas[pygame.K_RIGHT]:
    #         player.walk_right[i]['rect'].x +40
    #         player.control('walk_right')

    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_RIGHT:
    #             player.control('stand_up')

    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             player.control('walk_left')

    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_LEFT:
    #             player.control('stand_up')  s
    screen.blit(img_background,img_background.get_rect())
    screen.blit(plataforma,plataforma.get_rect())
    player.update(screen)

    # player update -> verifica como el py interactua c/ nivel
    # enemigo update
    # player dibujar
    # dibujar nivel


    pygame.display.flip()
    # print(clock.tick(FPS))
    delta_ms = clock.tick(FPS) # limita la cantidad de veces x seg que se genera el while
