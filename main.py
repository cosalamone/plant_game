import time
import pygame
import sys
from constantes import *
from clases.player.player import Player
from clases.planta.planta import Planta
from crear_enemigos import * 
from pruebas_db import * 


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

font_titulos = pygame.font.SysFont("Arial", 30, bold=True)
font_puntajes = pygame.font.SysFont("Arial", 30)

# Input
ingreso = ""  # donde se va a guardar lo que ingrese el usuario 
ingreso_rect = pygame.Rect(200, 200, 150, 40)

respuesta = obtener_top_puntajes()
respuesta = str(respuesta)
respuesta = respuesta.split('\n')

# region botones menu
jugar = 'JUGAR'
jugar_rect = pygame.Rect(200, 200, 225, 50)
puntos = 'VER PUNTAJES'
puntos_rect = pygame.Rect(500, 200, 250, 50)
# endregion

segundos = 0
# Timer
timer_segundos = pygame.USEREVENT   # en milesimas
pygame.time.set_timer(timer_segundos, 1000)

# region Musica
pygame.mixer.init()
audio_nivel1_2 = pygame.mixer.Sound('assets/audios/audio_nivel1_2.mp3')
audio_nivel3 = pygame.mixer.Sound('assets/audios/audio_nivel3.mp3')
volumen = 0.50
audio_nivel1_2.set_volume(volumen)
audio_nivel3.set_volume(volumen)
# endregion

# Fondo
img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')

# region Pantalla Puntajes
titulo_puntajes = 'ESTOS SON LOS MEJORES 5 PUNTAJES: '
titulo_puntajes_rect = pygame.Rect(200, 200, 150, 40)

# boton Volver
btn_volver = 'Volver'
btn_volver_rect = pygame.Rect(700, 500, 150, 50)

# superficie con transparencia
transparent_surface = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)

# Dibujar la superficie transparente
pygame.draw.rect(transparent_surface, COLOR_VERDE_TRANSPARENTE, (150, 150, 700, 400))
# endregion

# Jugador
player = Player(x=25,y=550,speed_walk=10) 

# region Enemigos
enemigos=[]

nivel1 = crear_enemigos_nivel1(6)
nivel2 = crear_enemigos_nivel2(8)
nivel3 = crear_enemigos_nivel3(12)
# endregion

# Planta
planta = Planta()

hayQueEsperar = 0

seccion = 'inicio'  # opciones: inicio, jugando, puntajes, cargando_puntos 
boton_jugar = None
boton_puntos = None
boton_volver = None
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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            elif event.key == pygame.K_RETURN:
                print("Texto ingresado:", ingreso)
                ingreso = ''
            else:
                ingreso += event.unicode  # Da el texto que se presionó en el teclado

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = (event.pos)
            boton_jugar = (x > 200 and x < 425) and (y > 200 and y < 250)
            boton_puntos = (x > 500 and x < 750) and (y > 200 and y < 250)
            boton_volver = (x > 700 and x < 850) and (y > 500 and y < 550)
            print("Se hizo clic en las coordenadas:", x, y)
                
    if seccion == 'inicio':
        screen.blit(img_background, img_background.get_rect())
        screen.blit(transparent_surface, (0, 0))


        pygame.draw.rect(screen, COLOR_VERDE_SECO, jugar_rect)
        pygame.draw.rect(screen, COLOR_VERDE_SECO, puntos_rect)


        jugar_surface = font_titulos.render(jugar, True, COLOR_BLANCO)
        puntos_surface = font_titulos.render(puntos, True, COLOR_BLANCO)

        # calculo la pos p/que quede centrado el texto
        jugar_texto_pos = (jugar_rect.centerx - jugar_surface.get_width() // 2, jugar_rect.centery - jugar_surface.get_height() // 2)
        puntos_texto_pos = (puntos_rect.centerx - puntos_surface.get_width() // 2, puntos_rect.centery - puntos_surface.get_height() // 2)

        screen.blit(jugar_surface, jugar_texto_pos)
        screen.blit(puntos_surface, puntos_texto_pos)

        if boton_jugar:
            seccion = 'jugando'
        if boton_puntos:
            seccion = 'puntajes'

        pygame.display.flip()

    if seccion == 'jugando': 

        # region Acciones con Teclado
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
        # endregion

        delta_ms = clock.tick(FPS) # limita la cantidad de veces x seg que se genera el while
        screen.blit(img_background,img_background.get_rect())
        if hayQueEsperar > 0:
            time.sleep(hayQueEsperar)
            hayQueEsperar = 0

        # region Niveles
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
                        MostrarTexto("¡Superaste el nivel 1! Iniciando Nivel 2", COLOR_BLANCO, (150,250))
                        hayQueEsperar = 2
                case 3: 
                    if enemigos != nivel3:
                        audio_nivel1_2.stop()
                        audio_nivel3.play()
                        enemigos = nivel3
                        MostrarTexto("¡Superaste el nivel 2! Iniciando el ÚLTIMO NIVEL", COLOR_VERDE, (150,250))
                        hayQueEsperar = 2
        # endregion 

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

    if seccion == 'puntajes':
        
        screen.fill(COLOR_NEGRO)
        screen.blit(img_background, img_background.get_rect())
        screen.blit(transparent_surface, (0, 0))

        pygame.draw.rect(screen, COLOR_VERDE_SECO, btn_volver_rect)
        titulo_puntajes_surface = font_titulos.render(titulo_puntajes, True, COLOR_BLANCO)
        btn_volver_surface = font_titulos.render(btn_volver, True, COLOR_BLANCO)

        btn_volver_pos = (btn_volver_rect.centerx - btn_volver_surface.get_width() // 2, btn_volver_rect.centery - btn_volver_surface.get_height() // 2)


        screen.blit(titulo_puntajes_surface, (200, 180))
        screen.blit(btn_volver_surface, btn_volver_pos)

        font_respuesta_surface = [font_puntajes.render(rta, True, COLOR_BLANCO) for rta in respuesta]
        # Obtener alturas de cada superficie
        line_heights = [surface.get_height() for surface in font_respuesta_surface]
        # Calcular la posición vertical de cada línea
        y_positions = [sum(line_heights[:i]) for i in range(len(respuesta))]

        for i, surface in enumerate(font_respuesta_surface):
            screen.blit(surface, (350, y_positions[i] + 250))

        if boton_volver:
            seccion = 'inicio'

        pygame.display.flip()

    if seccion == 'cargando_puntos':
        pass
# sonido_fondo.stop()
pygame.quit()


