import hashlib
import os

def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    try:
        with open(ruta_archivo, "rb") as archivo:
            while True:
                bloque = archivo.read(4096)

                if not bloque:
                    break

                sha256.update(bloque)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


print("=== SHA-256 Hash Checker ===")

ruta = input("Ingresa la ruta del archivo que deseas analizar: ")

if os.path.isfile(ruta):
    hash_archivo = calcular_sha256(ruta)

    print("\nArchivo encontrado.")
    print("SHA-256:")
    print(hash_archivo)

else:
    print("\nError: El archivo no existe.")
