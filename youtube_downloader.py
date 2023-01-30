from pytube import YouTube
from pytube.cli import on_progress
# from pytube import exceptions # Descomenta el "from" si quieres intentar tratar las excepciones de pytube de manera "correcta".
"""
Para usar las excepciones de pytube, se usa el siguiente formato:
---------------------------------------------------------------------
try:
    video = yt.streams.first() # Obtener el primer stream del vídeo
except exceptions.VideoUnavailable:
    print("Vídeo no disponible")
---------------------------------------------------------------------
Esto solamente me ha funcionado con los vídeos que son en directo. Con otro tipo de error se ha ido al carajo.
"""
"""
****************************************************************************
* LAS EXCEPCIONES ESTÁN ROTAS. USAR UN "try-except" SIMPLE DE TODA LA VIDA *
****************************************************************************

Con un objeto de clase "YouTube" no se puede usar el método ".check_availability()" o se irá todo a la mierda y no funcionarán las excepciones.
Si queremos añadir una barra de progreso en la descarga, al instanciar un objeto de clase "YouTube" añadiremos "on_progress_callback" habiendo importado antes la función "on_progress". No importaremos "display_progress_bar" porque no nos hace falta y además que, si la importamos y la metemos la instanciar, también reventará todo.  
A la extensión "Pylance" se le va la pinza (al menos a mí) con el método .download() y dará errores con variables de entrada que son opcionales, por eso un "#type: ignore" junto al vídeo a descargar.  
A ".streams" se le puede añadir ".filter()" y dentro se le pueden aplicar filtros de todo tipo.  
"""
link="https://www.youtube.com/watch?v=PTIBTJYACYQ"
yt=YouTube(link,on_progress_callback=on_progress)
print(f"Preparando descarga de: {yt.title}")
try:
    videos=yt.streams.filter(progressive=True, type="video").get_highest_resolution() # <== Obtener los "streams" es lo que nos puede generar excepciones.  
    videos.download(filename="yt_video.mp4") #type: ignore
    # print("==>") # Podemos hacer un "print" después de la descarga para poner algo a la izquierda de la barar de progreso una vez completada la descarga.  
except:
    print("No se ha podido conseguir información del vídeo, por lo que no se va a descargar.")
"""
Ahora mismo el programa funciona y descarga un vídeo si está disponible. En caso de querer descargar alguno diferente al actual que está en la variable "link", basta con reemplazar el contenido.  
"""