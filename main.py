import time
import pygame
import sys
from constantes import *
from clases.player.player import Player
from clases.planta.planta import Planta
from crear_enemigos import *
from funciones import mostrar_texto 
from puntajes_db import * 


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

font_titulos = pygame.font.SysFont("Arial", 30, bold=True)
font_puntajes = pygame.font.SysFont("Arial", 30)

# Input
ingreso = ''  # donde se va a guardar lo que ingrese el usuario 
ingreso_rect = pygame.Rect(500, 205, 150, 40)

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
tiempo = 0
font_timer = pygame.font.SysFont('Arial Narrow', 35)

# region Musica
pygame.mixer.init()
audio_nivel1_2 = pygame.mixer.Sound('./assets/audios/audio_nivel1_2.mp3')
audio_nivel3 = pygame.mixer.Sound('./assets/audios/audio_nivel3.mp3')
volumen = 0.50
audio_nivel1_2.set_volume(volumen)
audio_nivel3.set_volume(volumen)
# endregion

# Fondo
img_background = pygame.image.load('./assets/background/Forest of Illusion Files/Previews/Previewx3.png')

# region Pantalla Puntajes
titulo_puntajes = 'ESTOS SON LOS MEJORES 5 PUNTAJES: '
titulo_puntajes_rect = pygame.Rect(200, 200, 150, 40)

# boton Volver
btn_volver = 'Volver'
btn_volver_rect = pygame.Rect(700, 500, 150, 50)

# superficie con transparencia
transparent_surface = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
pygame.draw.rect(transparent_surface, COLOR_VERDE_TRANSPARENTE, (150, 150, 700, 400))
# endregion


def reiniciarJuego():
    global nivel, cambio_nivel, player, enemigos, nivel1, nivel2, nivel3, planta 
    global posicion_inicio, flag_playing, hayQueEsperar,  boton_jugar,boton_puntos,boton_volver
    global enter,cargar_datos,iniciando_timer,ingreso,datos_cargados,huboSegundosDeEspera

    datos_cargados = False
    hayQueEsperar = 0
    iniciando_timer = False
    boton_jugar = None
    boton_puntos = None
    boton_volver = None
    enter = False
    ingreso = ''
    cargar_datos = True
    flag_playing = True
    nivel = 1
    cambio_nivel = False
    huboSegundosDeEspera = None
    audio_nivel1_2.stop()
    audio_nivel3.stop()
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

    posicion_inicio = 35

reiniciarJuego()

modo = 'inicio'  # opciones: inicio, jugando, puntajes, cargando_puntos 

while flag_playing:
    lista_events = pygame.event.get()
    for event in lista_events:
        if event.type == pygame.QUIT:
            flag_playing = False
            pygame.quit()
            sys.exit() # cierra la app

        if event.type == pygame.USEREVENT:
            if event.type == timer_segundos:
                if modo == 'jugando' and iniciando_timer:
                    if huboSegundosDeEspera > 0:
                        huboSegundosDeEspera -= 1
                    else:    
                        segundos += 1

        elif event.type == pygame.KEYDOWN and modo == 'cargando_puntos':
            if event.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                enter = True
            else:
                ingreso += event.unicode  # Da el texto que se presionó en el teclado

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = (event.pos)
            boton_jugar = (x > 200 and x < 425) and (y > 200 and y < 250)
            boton_puntos = (x > 500 and x < 750) and (y > 200 and y < 250)
            boton_volver = (x > 700 and x < 850) and (y > 500 and y < 550)

    if hayQueEsperar > 0:
        time.sleep(hayQueEsperar)
        huboSegundosDeEspera = hayQueEsperar
        hayQueEsperar = 0
    
    if modo == 'inicio':
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
            modo = 'jugando'
        if boton_puntos:
            modo = 'puntajes'

    elif modo == 'jugando': 

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

        iniciando_timer = True  # Comienza el temporizador después de la espera

        # region Niveles
        match(nivel):
                case 1:
                    if enemigos != nivel1:
                        audio_nivel1_2.play()
                        enemigos = nivel1
                        mostrar_texto(screen,"Iniciando Nivel 1",COLOR_BLANCO,(350,250),50,True)
                        hayQueEsperar = 2                       
                case 2: 
                    if enemigos != nivel2:
                        audio_nivel1_2.stop()
                        audio_nivel1_2.play()
                        enemigos = nivel2
                        mostrar_texto(screen,"¡Superaste el nivel 1! Iniciando Nivel 2", COLOR_BLANCO,(150,250),35,True)
                        hayQueEsperar = 2
                case 3: 
                    if enemigos != nivel3:
                        audio_nivel1_2.stop()
                        audio_nivel3.play()
                        enemigos = nivel3
                        mostrar_texto(screen,"¡Superaste el nivel 2! Iniciando el ÚLTIMO NIVEL",COLOR_VERDE,(80,250),35,True)
                        hayQueEsperar = 2
        # endregion 

        for unEnemigo in enemigos:
            unEnemigo.update(screen)
            if player.action == 'attack':
                if unEnemigo.es_atacado(player) == 'muerto':
                    enemigos.remove(unEnemigo)
                    player.score += 150
            game_over = unEnemigo.esta_atacando(planta, player)

            if len(enemigos) == 0:
                nivel += 1
                player.rect.x = 35
                cambio_nivel = True

                if nivel > 3:
                    mostrar_texto(screen,"******** GANASTE !!  ********",COLOR_BLANCO,(250,250),35,True)
                    hayQueEsperar = 3
                    modo = 'cargando_puntos'


        if planta.vida <= 0 or player.vida <= 0:
            mostrar_texto(screen,"******** GAME OVER ********", COLOR_ROJO,(250,250),35,True)
            hayQueEsperar = 3
            modo = 'cargando_puntos'
        
        mostrar_texto(screen,f'TIEMPO: {str(segundos)}',COLOR_BLANCO,(850, 10),25)
        player.update(screen, posicion_inicio, cambio_nivel)
        planta.update(screen)
        cambio_nivel = False

    elif modo == 'puntajes':

        screen.blit(img_background, img_background.get_rect())
        screen.blit(transparent_surface, (0, 0))
        
        respuesta = obtener_top_puntajes()
        # respuesta = str(respuesta).upper()
        # respuesta = respuesta.split('\n')
        

        mostrar_texto(screen,'ESTOS SON LOS MEJORES 5 PUNTAJES: ', COLOR_BLANCO,(200, 180),30, True)
        mostrar_texto(screen,'Nombre    -    Puntaje    -    Tiempo',COLOR_BLANCO,(250, 230),30, True)


        # lista de superficies con los nombres
        font_nombre_surface = [font_puntajes.render(rta['nombre'], True, COLOR_BLANCO) for rta in respuesta]
        font_puntos_surface = [font_puntajes.render(str(rta['puntos']), True, COLOR_BLANCO) for rta in respuesta]
        font_tiempo_surface = [font_puntajes.render(str(rta['tiempo']), True, COLOR_BLANCO) for rta in respuesta]
        # obtiene el hight de cada surface de la lista
        linea_height = [surface.get_height() for surface in font_nombre_surface]
        suma_alturas = 0
        y_positions = []

        for altura in linea_height:
            suma_alturas += altura
            y_positions.append(suma_alturas)

        for i, surface in enumerate(font_nombre_surface):
            screen.blit(surface, (280, y_positions[i] + 270))
        for i, surface in enumerate(font_puntos_surface):
            screen.blit(surface, (450, y_positions[i] + 270))
        for i, surface in enumerate(font_tiempo_surface):
            screen.blit(surface, (650, y_positions[i] + 270))

        pygame.draw.rect(screen, COLOR_VERDE_SECO, btn_volver_rect)
        # creo la supfcie del texto
        btn_volver_surface = font_titulos.render(btn_volver, True, COLOR_BLANCO)
        # calculo la ubicacion del btn
        btn_volver_pos = (btn_volver_rect.centerx - btn_volver_surface.get_width() / 2, btn_volver_rect.centery - btn_volver_surface.get_height() / 2)
        screen.blit(btn_volver_surface, btn_volver_pos)

        if boton_volver:
            modo = 'inicio'

    elif modo == 'cargando_puntos':
        screen.blit(img_background, img_background.get_rect())
        screen.blit(transparent_surface, (0, 0))

        mostrar_texto(screen,'Ingrese su nombre:', COLOR_BLANCO, (200,200),30)
        mostrar_texto(screen, f'Puntos a cargar: {player.score}', COLOR_BLANCO, (200,280),30)

        pygame.draw.rect(screen, COLOR_BLANCO, ingreso_rect, 2) # 2px de borde
        font_input_surface = font_puntajes.render(ingreso, True, COLOR_BLANCO)
        screen.blit(font_input_surface, (ingreso_rect.x + 6, ingreso_rect.y + 4)) # para que quede bien encuadrado en el rectangulo del 'input'

        if ingreso != '' and cargar_datos and enter:
            ingreso = ingreso.upper()
            guardar_nuevo_puntaje(ingreso,player.score,segundos)
            cargar_datos = False 
            mostrar_texto(screen,'Se guardaron sus datos', COLOR_BLANCO, (200,350), 35)
            hayQueEsperar = 2
            datos_cargados = True

        elif datos_cargados:
            reiniciarJuego()
            modo = 'inicio'
                
    pygame.display.flip()  # se pasa todo a lo que ve el usuario
pygame.quit()
