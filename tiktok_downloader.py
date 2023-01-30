import requests
from bs4 import BeautifulSoup # type: ignore
#import urllib3 // No hace falta este módulo si se va a guardar el archivo usando "with open(...)"
def Descargar(link):
    """
    El contenido de esta función se obtiene a partir del "cURL" de la página web que se usa para descargar los
    vídeo de TikTok.
    Si se quiere modificar debes hacer (todo desde el navegador):
        - Ir a "https://ssstik.io" y hacer un "POST" a la página insertando un enlace a un vídeo de TikTok
        - Antes de darle a "Descargar", abriremos las herramientas de desarrollador (F12) y miraremos en "Red" las peticiones que se hacen al darle al botón de "Descargar".
        - Cuando lo hayamos hecho, veremos que en la pestaña de "Red" nos encontraremos una petición que se llama "abc?url=dl". Haremos click derecho > copiar > copiar cono cURL (bash) // Esto está hecho habiendo seleccionado "bash", no sé si funcionará con la opción de "cmd".
        - Con el cURL copiado, iremos a "https://curlconverter.com/" y pegaremos el contenido del portapapeles para traducirlo a Python, obteniendo un código como el que está en estas líneas siguientes. Ese código se pega aquí debajo y se cambia el enlace que hay en "data" por el nombre de la variable que hemos definido al principio en el nombre de la función.
    """
    cookies = {
        '__cflb': '02DiuEcwseaiqqyPC5reXswsgyrfhBQenrpScztge3HjZ',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=02DiuEcwseaiqqyPC5reXswsgyrfhBQenrpScztge3HjZ',
        'dnt': '1',
        'hx-current-url': 'https://ssstik.io/es',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/es',
        'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
    }
    """
    No debería de haber problemas para descargar ningún vídeo de TikTok en cualquier otro sistema operativo aunque en 'user-agent' y 'sec-cg-ua-platform' ponga "Windows"; en caso de que no funcione, puedes probar a hacer lo que hay comentado al principio de esta función.
    """
    params = {
        'url': 'dl',
    }

    data = {
        'id': link, # <== Aquí se pone el nombre de la variable
        'locale': 'es',
        'tt': 'QnBzQkti',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data) # Definir la petición a la página web
    descarga = BeautifulSoup(response.text, "html.parser") # Hacer la petición y obtener el código html
    enlace = descarga.a["href"] #type: ignore # Obtener el primer enlace de descarga de la página web
    # print(enlace) # Esta línea se puede descomentar para mostrar por pantalla el enlace directo al vídeo
    return enlace # Devolver el enlace

url = "https://vm.tiktok.com/ZMYLtbB9B/" # Pon aquí el enlace al vídeo de TikTok que quieras.
# enlace = Descargar(url) # Se puede descomentar esta línea en caso de que queramos guardar el enlace en una variable, pero el programa funcionará igualmente si lo dejamos como está en la línea 54
ruta = "./" # Falta comprobar que la ruta existe
nombre = "tiktok.mp4" # Puedes poner el nombre que quieras al archivo. He probado las extensiones "mp4", "avi" y "mkv" y han funcionado. No garantizo que con otras funcione.
ruta_completa = ruta + nombre # Esto es la ruta final más el nombre del archivo
response = requests.get(f"{Descargar(url)}", stream=True) # Hacer la solicitud al enlace y obtener la información
if response.status_code == 200:
    with open(ruta_completa, "wb") as video:
        for bloque in response.iter_content(chunk_size=1024): # Obtener los bloques de 1024 bits (creo) del archivo que queremos descargar...
            if bloque: # (si obtenemos un bloque)
                video.write(bloque) # ...escribimos el bloque de bits.
else:
        print(f"Error al acceder a la página. Código de error: {response.status_code}")
# -----------------------------------------------------
"""
El siguiente bloque de código debería funcionar, aunque no sé exactamente por qué no funciona (porque lo he probado varias veces antes y ha funcionado a la perfección)
"""
"""
response = requests.get(Descargar(url), stream=True) #type: ignore
video = urllib3.PoolManager()
with video.request("GET", Descargar(url), preload_content=False) as resp, open(ruta_completa, "wb") as out_file:
    out_file.write(resp.read())
"""