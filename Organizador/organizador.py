# -- La idea es crear un script que organize los archivos por formato en carpetas especificas dentro de descargas como img, videos, audios y que si estas no existen las añada

import os
import magic
import shutil

dd = None
### --- Verificacion y creacion de las carpetas --- ###

def crear_carpeta(arg_directory):
    directory = arg_directory

    parent_dir = "C://Users//rdev//Downloads"

    path = os.path.join(parent_dir, directory)

    os.mkdir(path)
    print("Directory '%s' created" %directory)

def mover(arg1, arg2):
    shutil.move(arg1, arg2)

pathSec_1 = os.access("C://Users//rdev//Downloads//Videos", os.F_OK)
print("La carpeta Videos: ", pathSec_1)

pathSec_2 = os.access("C://Users//rdev//Downloads//Musica", os.F_OK)
print("La carpeta Musica: ", pathSec_2)

pathSec_3 = os.access("C://Users//rdev//Downloads//Imagenes", os.F_OK)
print("La carpeta Imagenes: ", pathSec_3)

if pathSec_1 == False:
    crear_carpeta("Videos")

if pathSec_2 == False:
    crear_carpeta("Musica")

if pathSec_3 == False:
    crear_carpeta("Imagenes")

os.chdir('C://Users//rdev//Downloads')

lista = list(filter(os.path.isfile, os.listdir()))
print(lista)
#for xx in lista:
#    dd = magic.from_file("C://Users//rdev//Downloads//Timeline 1.mp4", mime = True)
#    print(dd)
for x in lista:
    dy = x
    dd = magic.from_file(dy , mime = True)
    if dd == "image/jpeg":
        mover(dy, "Imagenes")
    elif dd == "video/mp4":
        mover(dy, "Videos")