"""
Es necesario instalar:
    - "requests" => pip install requests
    - "BeautifulSoup" => pip install bs4
    - "urllib3" => pip install urllib3
"""
import requests
from bs4 import BeautifulSoup
import urllib3
# Rellenar el campo del formulario y hacer una solicitud POST
url = 'https://twdown.net/download.php' # Página web para descargar el vídeo
tweet = 'https://twitter.com/pincheotaku/status/1618167625787531264' # Enlace al tweet. Puedes poner el que quieras aquí, pero no he comprobado qué pasa si pones un enlace a un tweet que tenga más de un vídeo
response = requests.post(url, data={'URL':tweet}) # Solicitud a la página web.
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # Obtener el código de la página web
    link = soup.find('td').find('a', href=True)['onclick'] # Obtener el primer enlace de redirección al vídeo que queremos descargar #type: ignore
    inicio = link.find("https") # Posición de 'https' en el enlace #type: ignore
    fin = link.find(")") # Posición de ')' en el enlace #type: ignore
    link_recortado = link[inicio:fin-1] # Link ya recortado del 'href'
    ruta = "./" # Ruta a la carpeta/directorio
    nombre = "tweet.mp4" # Nombre y extensión del archivo
    ruta_completa = ruta + nombre # Ruta completa al archivo
    video = urllib3.PoolManager() 
    with video.request("GET", link_recortado, preload_content=False) as resp, open(ruta_completa, "wb") as out_file:
        out_file.write(resp.read())
else:
    print(f"Error al acceder a la página. Código de error: {response.status_code}")