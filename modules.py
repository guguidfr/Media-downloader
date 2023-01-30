import subprocess
import re
modulos_en_el_sistema = subprocess.check_output("pip freeze", shell=True).decode("utf-8")
modulos_instalados = [module.strip() for module in modulos_en_el_sistema.split('\n')]
modulos_necesarios = ["pytube","bs4", "requests", "urllib3"]
modulos_cumplidos = [ re.sub("==[0-9.]*", "", x) for x in modulos_instalados if any(i in x for i in modulos_necesarios) ]
if len(modulos_cumplidos) == len(modulos_necesarios):
    print("Están instalados todos los módulos necesarios.")
else:
    print("Faltan módulos.")
    for modulo in modulos_cumplidos:
        if modulo in modulos_necesarios:
            modulos_necesarios.remove(modulo)
    print(f"Se van a instalar los siguientes módulos: {modulos_necesarios}")
    try:
        for modulo in modulos_necesarios:
            subprocess.run(["pip", "install", modulo],shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        print("No se han podido instalar los módulos modulos_necesarios.")