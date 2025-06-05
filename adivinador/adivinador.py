#intento1
import random
numero = random.randrange(0, 101)
def adivinar_numero():
    print("|- - estoy pensando en un numero del 1 al 100 tienes que adivinarlo \n|- - tranquilo te dare pistas para que sea mas facil")
    i = 0
    while i < 1:
        num_posible = int(input("|- - cual numero es: "))
        if num_posible == numero:
            print("|- - Exacto felicidades ganaste")
            i += 1
        elif num_posible < numero:
            print(" - Nop te equivocas es mas grande el numero en el que pienso")
        elif num_posible > numero:
            print(" - Nop te equivocas es mas chico el numero en el que pienso ")
adivinar_numero()