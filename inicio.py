import pygame
import sys
from constantes import *
from pruebas_db import * 

pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')

# Fondo
img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')

# Titulo PUNTAJES
titulo_puntajes = 'ESTOS SON LOS MEJORES 5 PUNTAJES: '
titulo_puntajes_rect = pygame.Rect(200, 200, 150, 40)
# Crear una superficie con transparencia
transparent_surface = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)

# Dibujar un rectángulo gris en la superficie transparente
pygame.draw.rect(transparent_surface, COLOR_VERDE_TRANSPARENTE, (150, 150, 700, 400))

# Fonts
font_titulos = pygame.font.SysFont("Arial", 30, bold=True)
font = pygame.font.SysFont("Arial", 30)

# Input
ingreso = ""  # donde se va a guardar lo que ingrese el usuario 
ingreso_rect = pygame.Rect(200, 200, 150, 40)

respuesta = obtener_top_puntajes()
respuesta = str(respuesta)
respuesta = respuesta.split('\n')

reloj = pygame.time.Clock()
screen.blit(img_background, img_background.get_rect())

cargar_datos = True

correr = True
while correr:
    milis = reloj.tick(20)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            correr = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            elif evento.key == pygame.K_RETURN:
                print("Texto ingresado:", ingreso)
                ingreso = ''
            else:
                ingreso += evento.unicode  # Da el texto que se presionó en el teclado
    
    if cargar_datos:
        guardar_nuevo_puntaje('sdf',5730,4000)
        cargar_datos = False
        respuesta = obtener_top_puntajes()
        respuesta = str(respuesta)
        respuesta = respuesta.split('\n')    

    screen.fill(COLOR_NEGRO)
    screen.blit(img_background, img_background.get_rect())
    screen.blit(transparent_surface, (0, 0))

    titulo_puntajes_surface = font_titulos.render(titulo_puntajes, True, COLOR_BLANCO)

    screen.blit(titulo_puntajes_surface, (200, 180))

    # pygame.draw.rect(screen, COLOR_BLANCO, ingreso_rect, 2) # 2px de borde
    # font_input_surface = font.render(ingreso, True, COLOR_NEGRO)
    # screen.blit(font_input_surface, (ingreso_rect.x + 6, ingreso_rect.y + 4)) # para que quede bien encuadrado en el rectangulo del 'input'

    font_respuesta_surface = [font.render(rta, True, COLOR_BLANCO) for rta in respuesta]
    # Obtener alturas de cada superficie
    line_heights = [surface.get_height() for surface in font_respuesta_surface]
    # Calcular la posición vertical de cada línea
    y_positions = [sum(line_heights[:i]) for i in range(len(respuesta))]

    for i, surface in enumerate(font_respuesta_surface):
        screen.blit(surface, (350, y_positions[i] + 250))

    pygame.display.flip()