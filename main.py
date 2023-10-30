import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.init()
clock = pygame.time.Clock()

img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')
# img_background = pygame.transform.scale(img_background,(ANCHO_VENTANA, ALTO_VENTANA))

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # cierra la app

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.control('walk_right',5,0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.control(0,0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.control('walk_left',-5,0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.control(0,0)        

    player.update()
    player.draw(screen)

    # player update -> verifica como el py interactua c/ nivel
    # enemigo update
    # player dibujar
    # dibujar nivel


    pygame.display.flip()
    screen.blit(img_background,img_background.get_rect())
    # print(clock.tick(FPS))
    delta_ms = clock.tick(FPS) # limita la cantidad de veces x seg que se genera el while
