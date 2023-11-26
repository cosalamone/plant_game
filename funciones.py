import pygame
from constantes import *



def mostrar_texto (screen, Texto, Color, Posicion, tamaño, fondo=False):

    font = pygame.font.SysFont('Arial', tamaño, bold=True)
    text = font.render(Texto, True, Color)
    text_rect = text.get_rect()
    text_width = max(text_rect.width,  Posicion[0]) 
    if fondo:
        transparent_surface = pygame.Surface((text_width, text_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(transparent_surface, COLOR_VERDE_SECO_TRANSPARENTE, text_rect)
        screen.blit(transparent_surface, Posicion)
    screen.blit(text, Posicion)