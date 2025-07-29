import yt_dlp
import os
import ffmpeg
import subprocess

def descargar_musica(url,carpeta="C:/Users/rdev/Downloads/Musica"):
    global textourl1
    try:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        opciones = {
            'format' : 'bestaudio/best',
            'outtmpl' : f'{carpeta}/%(title)s.%(ext)s'
        }
        print("Descargando audio de youtube....")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print("Descarga completa!!!")
    except Exception as e:
        print(f"Ocurrio un error : {e}")
if __name__ == "__main__":
    url = input("Ingrese su enlace del video: ")
    descargar_musica(url)

textourl1 = subprocess.getoutput("yt-dlp --print title " + url)
text1 = textourl1

def extraer_audio_webm_a_wav(ruta_entrada_webm, ruta_salida_wav):
    try:
        # Verifica si el archivo de entrada existe
        if not os.path.exists(ruta_entrada_webm):
            print(f"Error: El archivo de entrada no existe en '{ruta_entrada_webm}'")
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
    os.listdir
    nombre_archivo_webm = text1 + ".webm"
    ruta_carpeta_musica = r"C:\Users\rdev\Downloads\Musica" # Usa 'r' para rutas raw o dobles barras invertidas

    ruta_entrada_completa = os.path.join(ruta_carpeta_musica, nombre_archivo_webm)
    ruta_salida_completa = os.path.join(ruta_carpeta_musica, text1 + ".wav")
    extraer_audio_webm_a_wav(ruta_entrada_completa, ruta_salida_completa)
    os.remove(ruta_entrada_completa)