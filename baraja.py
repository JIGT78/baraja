
# Creamos la clase baraja
from random import randint


class baraja:

    def __init__(self):
        palos_baraja = ['o', 'c', 'e', 'b']
        numeros_baraja = ['A', '1', '2', '3',
                          '4', '5', '6', '7', 'S', 'C', 'R']
        self.baraja = []
        for palo in palos_baraja:
            for numero in numeros_baraja:
                self.baraja.append(numero + palo)

    def barajar(self):
        posicion_aleatoria = None
        valor_posicion_actual = None
        for posicion_actual in range(len(self.baraja)):
            posicion_aleatoria = randint(0, len(self.baraja)-1)
            valor_posicion_actual = self.baraja[posicion_actual]
            self.baraja[posicion_actual] = self.baraja[posicion_aleatoria]
            self.baraja[posicion_aleatoria] = valor_posicion_actual

    def repartir(self, mano, jugadores):
        val = 1
        jugadores_manos = [[val for i in range(mano)]for j in range(jugadores)]
        if (mano * jugadores) > len(self.baraja):
            print("No hay suficientes cartas en la baraja: {}".format(
                len(self.baraja)))
        else:
            for man in range(mano):
                for jug in range(jugadores):
                    jugadores_manos[jug][man] = self.baraja[0]
                    del self.baraja[0]

        return jugadores_manos

    def __str__(self):
        return f'Baraja: {self.baraja}'

    def __repr__(self):
        return f'Objeto: {self.baraja}'
