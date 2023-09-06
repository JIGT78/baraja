# Reto: Fabricando una baraja

def crear_baraja():
    palos_baraja = ['o', 'c', 'e', 'b']
    numeros_baraja =['A', '1', '2', '3', '4', '5','6', '7', 'S','C', 'R']
    baraja=[]
    for palo in palos_baraja:
        for numero in numeros_baraja:
            baraja.append(numero + palo)
            
    return baraja

# Probando funciones
nueva_baraja = crear_baraja()
print(nueva_baraja)

