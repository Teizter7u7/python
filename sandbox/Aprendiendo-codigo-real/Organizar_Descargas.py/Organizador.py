from pathlib import Path
from config import carpeta_organizar
from formatos import formatos
from colorama import Fore

carpetasNo_creadas: list = []

def verificar_carpetas():
    for carpeta in formatos.keys():
        carpeta_actual: Path = carpeta_organizar / carpeta
        if not carpeta_actual.is_dir():
            print(Fore.YELLOW + f"no existe la carpeta: {carpeta}")
            carpetasNo_creadas.append(carpeta)

def crear_carpetas():
    for carpeta in carpetasNo_creadas:
        carpeta_actual: Path = carpeta_organizar / carpeta
        carpeta_actual.mkdir(exist_ok= True)
        print(Fore.LIGHTGREEN_EX + f"La carpeta {carpeta} ha sido creada")

def mover_archivo(origen: Path, destino: Path):
    Path(origen).rename(destino)

def organizar_archivos():
    for archivo in carpeta_organizar.iterdir():
        nombre: str = archivo.name
        formato: str = archivo.suffix.lower()
        if archivo.is_file():
            for categoria, formato2 in formatos.items():
                if formato in formato2:
                    mover_archivo(carpeta_organizar / nombre, carpeta_organizar / categoria / nombre)


verificar_carpetas()
crear_carpetas()
organizar_archivos()