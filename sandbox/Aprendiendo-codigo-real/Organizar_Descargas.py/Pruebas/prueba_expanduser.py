import os

home_directory = os.path.join(os.path.expanduser("~"), "Downloads", "loco")

crear_carpeta = os.mkdir(home_directory)
print(home_directory)