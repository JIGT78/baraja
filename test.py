import unittest
from baraja import baraja

baraja1 = baraja()
baraja2 = baraja()

print(baraja1)
print(baraja2)
baraja2.barajar()
print(baraja2)
baraja1.repartir(5, 2)
baraja1.repartir(6, 4)
baraja1.repartir(5, 3)
print(baraja1)
