import random
import time
import pygame
import sys
from clases.enemigos.caracol import Caracol
from clases.enemigos.enemigo import Enemigo
from clases.enemigos.hormiga import Hormiga
from clases.enemigos.mantis import Mantis
from constantes import *
from clases.player.player import Player
from clases.planta.planta import Planta


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

# ingreso = ""
# ingreso_rect = pygame.Rect(200,400,150,40)
# font_input = pygame.font.SysFont("Arial", 50)


#Fondo
img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')
pygame.draw.line(screen, COLOR_ROJO,(0,400), (ANCHO_VENTANA,400))

#Jugador
player = Player(x=25,y=550,speed_walk=10) 

#Enemigos

def generar_num_random():
    posicion_x = random.randint(500, 1200)
    return posicion_x
print(generar_num_random())

enemigos=[]

nivel1 = []
nivel1.append(Hormiga(generar_num_random()))
nivel1.append(Caracol(generar_num_random()))
nivel1.append(Hormiga(generar_num_random()))

nivel2 = []
nivel2.append(Caracol(generar_num_random()))
nivel2.append(Hormiga(generar_num_random()))
nivel2.append(Caracol(generar_num_random()))
nivel2.append(Hormiga(generar_num_random()))

nivel3 = []
nivel3.append(Caracol(generar_num_random()))
nivel3.append(Hormiga(generar_num_random()))
nivel3.append(Mantis(generar_num_random()))
nivel3.append(Caracol(generar_num_random()))
nivel3.append(Hormiga(generar_num_random()))

#Planta
planta = Planta()

hayQueEsperar = 0

def MostrarTexto (Texto, Color, Posicion):
    font = pygame.font.SysFont('Arial Narrow', 50)
    text = font.render(Texto, True, Color)
    screen.blit(text, Posicion)


flag_playing = True
nivel = 1
cambio_nivel = False
posicion_inicio = 35

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

    elif teclas[pygame.K_SPACE]:
        player.action = 'attack'
    
    else:
        player.action='stand_up'

    delta_ms = clock.tick(FPS) # limita la cantidad de veces x seg que se genera el while
    screen.blit(img_background,img_background.get_rect())
    if hayQueEsperar > 0:
        time.sleep(hayQueEsperar)
        hayQueEsperar = 0

    match(nivel):
            case 1:
                if enemigos != nivel1:
                    enemigos = nivel1
                    MostrarTexto("Iniciando Nivel 1", COLOR_BLANCO, (250,250))
                    hayQueEsperar = 2
            case 2: 
                if enemigos != nivel2:
                    enemigos = nivel2
                    MostrarTexto("¡Superaste el nivel 1! Iniciando Nivel 2", COLOR_BLANCO, (250,250))
                    hayQueEsperar = 2
            case 3: 
                if enemigos != nivel3:
                    enemigos = nivel3
                    MostrarTexto("¡Superaste el nivel 2! Iniciando el ÚLTIMO NIVEL", COLOR_VERDE, (250,250))
                    hayQueEsperar = 2

    for unEnemigo in enemigos:
        unEnemigo.update(screen)
        if player.action == 'attack':
            if unEnemigo.es_atacado(player) == 'muerto':
                enemigos.remove(unEnemigo)
                player.score += 150
        game_over = unEnemigo.esta_atacando(planta, player)
        if game_over:
            print(game_over)
        if len(enemigos) == 0:
            nivel += 1
            player.rect.x = 35
            cambio_nivel = True

            if nivel > 3:
                MostrarTexto("******** GANASTE !!  ********", COLOR_BLANCO, (250,250))
                hayQueEsperar = 10

    if planta.vida <= 0 or player.vida <= 0:
            MostrarTexto("******** GAME OVER ********", COLOR_ROJO, (250,250))
            hayQueEsperar = 10

    
    player.update(screen, posicion_inicio, cambio_nivel)
    planta.update(screen)
    cambio_nivel = False


    pygame.display.flip() # se pasa todo a lo que ve el usuario
    # print(clock.tick(FPS))


