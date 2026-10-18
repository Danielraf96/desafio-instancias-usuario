import json
from usuario import Usuario
 
usuarios = []
 
with open("usuarios.txt", "r", encoding="utf-8") as archivo, open("error.log", "w", encoding="utf-8") as log:
    for numero_linea, linea in enumerate(archivo, start=1):
        try:
            datos = json.loads(linea)
            usuario = Usuario(
                datos["nombre"],
                datos["apellido"],
                datos["email"],
                datos["genero"]
            )
            usuarios.append(usuario)
        except Exception as error:
            log.write(f"Error en la línea {numero_linea}: {error}\n")
 
print(f"Se crearon {len(usuarios)} instancias de Usuario correctamente.")
print("Revisa error.log para ver las líneas que fallaron.")