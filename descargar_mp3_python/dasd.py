import yt_dlp
import os

def Descarga_del_video(url,carpeta="C:/Users/rdev/Downloads/Musica"):
    global Nombre_video_yt
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
    Descarga_del_video(url)