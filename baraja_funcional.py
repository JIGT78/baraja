# Reto: Fabricando una baraja
from random import randint

def crearBaraja():
    palos_baraja = ['o', 'c', 'e', 'b']
    numeros_baraja =['A', '1', '2', '3', '4', '5','6', '7', 'S','C', 'R']
    baraja=[]
    for palo in palos_baraja:
        for numero in numeros_baraja:
            baraja.append(numero + palo)
    return baraja

def mezclar(baraja):
    posicion_aleatoria = None
    valor_posicion_actual = None
    for posicion_actual in range(len(baraja)):
        posicion_aleatoria = randint(0, len(baraja)-1)
        valor_posicion_actual = baraja[posicion_actual]
        baraja[posicion_actual] = baraja[posicion_aleatoria]
        baraja[posicion_aleatoria] = valor_posicion_actual


# Probando funciones
nueva_baraja = crearBaraja()
print(nueva_baraja)
mezclar(nueva_baraja)
print(nueva_baraja)
