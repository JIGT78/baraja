
# Creamos la clase baraja
from random import randint

class baraja:
    
    def __init__(self):
        palos_baraja = ['o', 'c', 'e', 'b']
        numeros_baraja =['A', '1', '2', '3', '4', '5','6', '7', 'S','C', 'R']
        self.baraja=[]
        for palo in palos_baraja:
            for numero in numeros_baraja:
                self.baraja.append(numero + palo)
        
    def __str__(self):
        return f'Baraja: {self.baraja}'

    def __repr__(self):
        return f'Objeto: {self.baraja}'