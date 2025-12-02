from pathlib import Path

# --- 1. Definir Rutas de Manera Moderna ---

# Usar Path.home() para obtener el directorio principal de forma más limpia
home_dir: Path = Path.home() 

# Nombres de las subcarpetas a buscar
carpeta_nombres: list[str] = ["Descargas", "Downloads"] 

carpeta_organizar: Path | None = None # Usar None si la carpeta no se encuentra

# --- 2. Buscar la Carpeta de Forma Eficiente ---
from pathlib import Path

# --- 1. Definir Rutas de Manera Moderna ---

# Usar Path.home() para obtener el directorio principal de forma más limpia
home_dir: Path = Path.home() 

# Nombres de las subcarpetas a buscar
carpeta_nombres: list[str] = ["Descargas", "Downloads"] 

carpeta_organizar: Path | None = None # Usar None si la carpeta no se encuentra

# --- 2. Buscar la Carpeta de Forma Eficiente ---

# Iterar sobre los nombres y detenerse cuando se encuentre un directorio existente
for nombre in carpeta_nombres:
    ruta_candidata: Path = home_dir / nombre # Esto une las rutas de forma correcta (Path / str)
    
    if ruta_candidata.is_dir():
        carpeta_organizar = ruta_candidata
        break # Detener la búsqueda tan pronto como se encuentre una

# --- 3. Manejar el Resultado ---

if carpeta_organizar:
    print(f"La carpeta a organizar es: {carpeta_organizar}")
else:
    print("Error: No se encontró la carpeta 'Descargas' ni 'Downloads' en el directorio principal.")

# Si necesitas la ruta como string (aunque Path es mejor), puedes usar:
# carpeta_organizar_str: str = str(carpeta_organizar)
# Iterar sobre los nombres y detenerse cuando se encuentre un directorio existente
for nombre in carpeta_nombres:
    ruta_candidata: Path = home_dir / nombre # Esto une las rutas de forma correcta (Path / str)
    
    if ruta_candidata.is_dir():
        carpeta_organizar = ruta_candidata
        break # Detener la búsqueda tan pronto como se encuentre una

# --- 3. Manejar el Resultado ---

if carpeta_organizar:
    print(f"La carpeta a organizar es: {carpeta_organizar}")
else:
    print("Error: No se encontró la carpeta 'Descargas' ni 'Downloads' en el directorio principal.")

# Si necesitas la ruta como string (aunque Path es mejor), puedes usar:
# carpeta_organizar_str: str = str(carpeta_organizar)