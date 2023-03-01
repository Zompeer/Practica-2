import shutil
import random
import os
origen = str()

origen = str(input("Ingrese la ruta de extracción: "))

destino = origen+"_copia"
print("Ubicacion de copia: "+destino)
try:
    shutil.rmtree(destino)
except:
    pass
shutil.copytree(origen, destino)

for ruta, nombres_de_sub_carpetas, nombres_de_archivos in os.walk(destino):
    for nombre_archivo in nombres_de_archivos:
        if nombre_archivo.endswith('.txt'):
            ruta_archivo = os.path.join(ruta, nombre_archivo)
            #Leer y remplazar el contenido del archivo
            with open(ruta_archivo, 'r') as f:
                contenido = f.read()
            nuevo_contenido = ""
            for c in contenido:
                if c.isalpha():
                    nuevo_contenido += str(random.randint(0, 9))
                elif c.isdigit():
                    nuevo_contenido += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                else:
                    nuevo_contenido += c
            
            # Escribir el contenido modificado en el archivo copia
            with open(ruta_archivo, 'w') as f:
                f.write(nuevo_contenido)
print("Exito")
input()
