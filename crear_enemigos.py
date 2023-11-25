import random
from clases.enemigos.caracol import Caracol
from clases.enemigos.enemigo import Enemigo
from clases.enemigos.hormiga import Hormiga
from clases.enemigos.mantis import Mantis# Enemigos

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
