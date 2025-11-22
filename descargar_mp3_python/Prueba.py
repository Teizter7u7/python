import yt_dlp
import os
import ffmpeg
import subprocess
import pyperclip
import sys

def Creacion_Verificacion_carpeta(carpeta):
    if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print("-- Carpeta creada \n")


def Descarga_del_video(url, carpeta):
    try:
        opciones = {
            'format' : 'bestaudio/best', #format lo uso para poner la calidad a descargar  bestaudio es la maxima calidad y best es lo que se usa como segundo si bestaudio no esta disponible
            'outtmpl' : os.path.join(carpeta, '%(title)s.%(ext)s'), # outtmpl se utiliza para varias cosas f'{carpeta} se usa para que se descargue en esa carpeta y %(title)s se usa para darle como nombre al archivo el titulo del video de yt %(ext)s esto lo que hace es poner el mismo formato si el video es webm el archivo es webm
            'quiet': True,
        }
        print("Descargando video de yt")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print("Descarga completa")
    except Exception as e:
        print(f"Ocurrio un error : {e}")


def extraer_audio_webm_a_wav(ruta_entrada_webm, ruta_salida_wav):
    try:
        # Verifica si el archivo de entrada existe
        if not os.path.exists(ruta_entrada_webm):
            print(f"Error: El archivo de entrada no existe en: '{ruta_entrada_webm}'")
            return

        # Comando FFmpeg para extraer audio:
        # -i: archivo de entrada
        # -vn: no incluir video
        # -acodec pcm_s16le: códec de audio PCM sin comprimir (estándar para WAV)
        ffmpeg.input(ruta_entrada_webm).output(ruta_salida_wav, vn=None, acodec='libmp3lame', map_metadata='0', q="0").run(overwrite_output=True)

        print(f"Audio extraído exitosamente a: {ruta_salida_wav}")

    except ffmpeg.Error as e:
        print(f"Error al extraer el audio: {e.stderr.decode('utf8')}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")




if __name__ == "__main__":

    print("\nTienes que elegir en donde van a descargarse las canciones")
    print("seleciona entre las opciones con los nùmeros")
    print("1 | Windows_Descargas_Musica\n2 | linux_Descargas_Musica\n3 | Personalizado")

    eleccion_ruta_usuario = input("Opcion a elegir: ")
    Carpeta = ""
    Nombre_user = os.getlogin()
    
    # --- Lógica para determinar la carpeta ---
    if eleccion_ruta_usuario == "1":
        Carpeta = f'C:/Users/{Nombre_user}/Downloads'
    elif eleccion_ruta_usuario == "2":
        Carpeta = f"/home/{Nombre_user}/Descargas/Musica"
    elif eleccion_ruta_usuario == "3":
        print("\n\n-- Direccion (completa) de la carpeta en la cual se descargaran las canciones.")
        Carpeta = input("-- direccion: ")
    else:
        # Usando la carpeta de Descargas/Musica por defecto como se había discutido
        print("Opción no válida. Usando la carpeta de descargas/Musica por defecto.")
        Carpeta = os.path.join(os.path.expanduser("~"), "Downloads", "Musica")
    # Se crea o verifica la carpeta antes de usarla
    Creacion_Verificacion_carpeta(Carpeta)
    url = ""
    contenido_portapapeles = ""
    try:
        contenido_portapapeles = pyperclip.paste().strip() 
    except Exception:
        pass 
        
    # 2. Muestra el menú y gestiona la entrada
    print("\n1 | Url manual")
    if contenido_portapapeles:
        print("2 | Portapapeles")
    
    UrlMetodo = input("Elige uno de los metodos: ")

    if UrlMetodo == "1":
        url = input("Pegar url: ")
    # 🌟 CORRECCIÓN 2: Solo asigna la URL si la opción 2 fue elegida Y el portapapeles NO está vacío 🌟
    elif UrlMetodo == "2" and contenido_portapapeles: 
        url = contenido_portapapeles
    else:
        # Esto captura la URL si el usuario la pegó directamente en el prompt de UrlMetodo
        # Y también maneja el caso donde eligen una opción inválida o vacía.
        if UrlMetodo not in ["1", "2"]:
            url = UrlMetodo
    
    if not url:
        print("No pegaste una url finalizando programa")
        sys.exit(1)
    # Se obtiene el nombre antes de la descarga para usarlo en la ruta
    Conseguir_nombre_video_cmd = subprocess.getoutput("yt-dlp --print title " + url + " 2> /dev/null")
    Nombre_video_yt = Conseguir_nombre_video_cmd

    # Se llama a la función con el argumento 'Carpeta'
    Descarga_del_video(url, Carpeta)

    # Define las rutas de tus archivos
    nombre_archivo_webm = Nombre_video_yt + ".webm"
    ruta_carpeta_musica = Carpeta

    ruta_entrada_completa = os.path.join(ruta_carpeta_musica, nombre_archivo_webm)
    ruta_salida_completa = os.path.join(ruta_carpeta_musica, Nombre_video_yt + ".mp3")
    
    extraer_audio_webm_a_wav(ruta_entrada_completa, ruta_salida_completa)
    
    # Se elimina el archivo WEBM original
    if os.path.exists(ruta_entrada_completa):
        os.remove(ruta_entrada_completa)