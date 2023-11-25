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
from generar_random import generar_num_random


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

# ingreso = ""
# ingreso_rect = pygame.Rect(200,400,150,40)
# font_input = pygame.font.SysFont("Arial", 50)
segundos = 0
# Timer
timer_segundos = pygame.USEREVENT   # en milesimas
pygame.time.set_timer(timer_segundos, 1000)
# Musica
pygame.mixer.init()
audio_nivel1_2 = pygame.mixer.Sound('assets/audios/audio_nivel1_2.mp3')
audio_nivel3 = pygame.mixer.Sound('assets/audios/audio_nivel3.mp3')


volumen = 0.50

audio_nivel1_2.set_volume(volumen)
audio_nivel3.set_volume(volumen)



# Fondo
img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')
pygame.draw.line(screen, COLOR_ROJO,(0,400), (ANCHO_VENTANA,400))

# Jugador
player = Player(x=25,y=550,speed_walk=10) 

# Enemigos

def crear_enemigos_nivel1(cantidad_enemigos):
    lista_enemigos = []
    for i in range(cantidad_enemigos):
        numero_random =random.randint(1, 10)
        match numero_random:
            case 1|2|3|4|5|6:
                lista_enemigos.append(Caracol())
                
            case 7|8|9|10: 
                lista_enemigos.append(Hormiga())

    return lista_enemigos

def crear_enemigos_nivel2(cantidad_enemigos):
    lista_enemigos = []
    for i in range(cantidad_enemigos):
        numero_random =random.randint(1, 10)
        match numero_random:
            case 1|2|3|4|5|6:
                lista_enemigos.append(Hormiga())
                
            case 7|8|9|10: 
                lista_enemigos.append(Caracol())

    return lista_enemigos

def crear_enemigos_nivel3(cantidad_enemigos):
    lista_enemigos = []
    for i in range(cantidad_enemigos):
        numero_random =random.randint(1, 10)
        match numero_random:
            case 1|2|3|4|5:
                lista_enemigos.append(Hormiga())
                
            case 6|7|8: 
                lista_enemigos.append(Caracol())
            
            case 9|10: 
                lista_enemigos.append(Mantis())

    return lista_enemigos

enemigos=[]

nivel1 = crear_enemigos_nivel1(6)

nivel2 = crear_enemigos_nivel2(8)

nivel3 = crear_enemigos_nivel3(12)

# Planta
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
        # if event.type == pygame.USEREVENT:
        #     if event.type == timer_segundos:
        #         segundos += 1
        #         volumen += 0.01
        #         audio_nivel1_2.set_volume(volumen)
        #     segundos = 0
        #     volumen = 0.02
        #     if event.type == timer_segundos:
        #         segundos += 1
        #         volumen += 0.01s
        #         audio_nivel3.set_volume(volumen)

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
                    audio_nivel1_2.play()
                    enemigos = nivel1
                    MostrarTexto("Iniciando Nivel 1", COLOR_BLANCO, (250,250))
                    hayQueEsperar = 2
                    
            case 2: 
                if enemigos != nivel2:
                    audio_nivel1_2.stop()
                    audio_nivel1_2.play()
                    enemigos = nivel2
                    MostrarTexto("¡Superaste el nivel 1! Iniciando Nivel 2", COLOR_BLANCO, (250,250))
                    hayQueEsperar = 2
            case 3: 
                if enemigos != nivel3:
                    audio_nivel1_2.stop()
                    audio_nivel3.play()
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
# sonido_fondo.stop()
pygame.quit()


