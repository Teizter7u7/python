import random

# El rango del número aleatorio debe ser inclusivo del 1 al 100.
# random.randint(min, max) es más directo para esto.
numero_secreto = random.randint(1, 100)

def adivinar_numero():
    print("----------------------------------------------------------------")
    print("¡Estoy pensando en un número del 1 al 100! ¿Puedes adivinarlo?")
    print("¡Tranquilo! Te daré pistas para que sea más fácil.")
    print("----------------------------------------------------------------")

    intentos = 0 # Agregamos un contador de intentos para darle más interactividad
    adivinado = False # Usamos una bandera booleana para controlar el bucle

    while not adivinado: # El bucle continúa mientras no se haya adivinado el número
        try:
            num_posible = int(input("¿Cuál número crees que es? "))
            intentos += 1 # Incrementamos el contador de intentos

            if num_posible < 1 or num_posible > 100:
                print("¡Ups! El número debe estar entre 1 y 100. Intenta de nuevo.")
            elif num_posible == numero_secreto:
                print(f"¡Exacto! ¡Felicidades, ganaste en {intentos} intentos!")
                adivinado = True # Cambiamos la bandera para salir del bucle
            elif num_posible < numero_secreto:
                print("¡Nop! Te equivocas, el número en el que pienso es más **grande**.")
            elif num_posible > numero_secreto:
                print("¡Nop! Te equivocas, el número en el que pienso es más **chico**.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

# Llamamos a la función para iniciar el juego
adivinar_numero()