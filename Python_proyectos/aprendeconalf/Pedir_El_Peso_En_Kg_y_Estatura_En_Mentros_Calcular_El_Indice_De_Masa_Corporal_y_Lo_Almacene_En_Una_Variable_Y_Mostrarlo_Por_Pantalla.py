peso = input("Cual es tu peso en Kg: ")
estatura = input("Cual es tu estatura en mentros: ")
imc = round(float(peso) / (float(estatura) ** 2),2)

print(f"Tu índice de masa corporal: {imc}")