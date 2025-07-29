import os
import ffmpeg

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
    nombre_archivo_webm = "Palina - Позови меня с собой (cover) (slowed).webm"
    ruta_carpeta_musica = r"C:\Users\rdev\Downloads\Musica" # Usa 'r' para rutas raw o dobles barras invertidas

    ruta_entrada_completa = os.path.join(ruta_carpeta_musica, nombre_archivo_webm)
    ruta_salida_completa = os.path.join(ruta_carpeta_musica, "Palina - Позови меня с собой (cover) (slowed).wav")

    extraer_audio_webm_a_wav(ruta_entrada_completa, ruta_salida_completa)
    os.remove(ruta_entrada_completa)