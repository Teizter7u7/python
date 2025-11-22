import yt_dlp
import os
import ffmpeg
import subprocess
import tkinter


ventana = tkinter.Tk()
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text = "Descargar Musica De Youtube", bg = "purple")

etiqueta.pack(fill = tkinter.X)
boton1 = tkinter.Button(ventana, text = "Descargar")
boton1.pack()
ventana.mainloop()
print("\n\n-- Direccion (completa) de la carpeta en la cual se descargaran las canciones.")

Carpeta = "/home/rdev/Descargas/Musica"

def Creacion_Verificacion_carpeta(carpeta = Carpeta):
    if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print("-- Carpeta creada \n")
Creacion_Verificacion_carpeta()

def Descarga_del_video(url, carpeta = Carpeta):
    try:
        opciones = {
            'format' : 'bestaudio/best', #format lo uso para poner la calidad a descargar  bestaudio es la maxima calidad y best es lo que se usa como segundo si bestaudio no esta disponible
            'outtmpl' : f'{carpeta}/%(title)s.%(ext)s', # outtmpl se utiliza para varias cosas f'{carpeta} se usa para que se descargue en esa carpeta y %(title)s se usa para darle como nombre al archivo el titulo del video de yt %(ext)s esto lo que hace es poner el mismo formato si el video es webm el archivo es webm
            'quiet': True,
        }
        print("Descargando video de yt")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print("Descarga completa")
    except Exception as e:
        print(f"Ocurrio un error : {e}")


if __name__ == "__main__": # se usa para que si el script es usado en otro script importandolo no ejecute estas lineas de codigo dentro del if, innecesario pero es bueno haberlo aprendido
    url = input("Enlace del video: ")
    Descarga_del_video(url)

Conseguir_nombre_video_cmd = subprocess.getoutput("yt-dlp --print title " + url + " 2> /dev/null")
Nombre_video_yt = Conseguir_nombre_video_cmd

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
        ffmpeg.input(ruta_entrada_webm).output(ruta_salida_wav, vn=None, acodec='pcm_s16le').run(overwrite_output=True)

        print(f"Audio extraído exitosamente a: {ruta_salida_wav}")

    except ffmpeg.Error as e:
        print(f"Error al extraer el audio: {e.stderr.decode('utf8')}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Uso del script ---
if __name__ == "__main__":
    # Define las rutas de tus archivos
    nombre_archivo_webm = Nombre_video_yt + ".webm" # aca uso la variable que recoje el titulo del video y le añado un str con el formato del archivo
    ruta_carpeta_musica = Carpeta

    ruta_entrada_completa = os.path.join(ruta_carpeta_musica, nombre_archivo_webm)
    ruta_salida_completa = os.path.join(ruta_carpeta_musica, Nombre_video_yt + ".wav")
    extraer_audio_webm_a_wav(ruta_entrada_completa, ruta_salida_completa)
    os.remove(ruta_entrada_completa)