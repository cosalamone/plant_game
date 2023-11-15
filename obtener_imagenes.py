import pygame

def get_surface_from_spritsheet(path:str,columnas:int,filas:int,flip:bool=False,agrandar:bool=False,elemento:str=''):
    lista = []
    surface_img = pygame.image.load(path)
    if agrandar == True:
        if elemento == 'enemigo':
            surface_img = pygame.transform.scale(surface_img,(220,90))
        elif elemento == 'planta':
            surface_img = pygame.transform.scale(surface_img,(160,50))

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