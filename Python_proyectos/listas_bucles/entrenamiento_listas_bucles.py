# Crear una lista de números y calcular su suma o promedio.

"""

Números = [2, 4, 5, 1, 7, 12]
suma_total = 0
for i in Números:
    suma_total += i
print(f"Suma total: {suma_total}")

"""

# Forma mas sencilla y rapida:

Números = [2, 4, 5, 1, 7, 12]

suma_total = sum(Números)

print(f"Suma total: {suma_total}")

# Calcular el promedio:

Promedio = suma_total / len(Números)
print(Promedio)