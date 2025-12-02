from os import path

nombre_archivo = "imagen.png"

_, extension = path.splitext(nombre_archivo)


print(nombre_archivo)
print(_)
print(extension)