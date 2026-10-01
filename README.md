# Cybersecurity Scripts

Este repositorio contiene scripts sencillos desarrollados en Python relacionados con tareas básicas de ciberseguridad.

El objetivo del proyecto es practicar la automatización de tareas y aplicar conceptos vistos durante mi formación en Seguridad en Tecnologías de la Información.

## Herramienta incluida

### SHA-256 Hash Checker

El script `hash_checker.py` permite calcular el hash SHA-256 de cualquier archivo almacenado en el equipo.

Un hash funciona como una huella digital que permite identificar un archivo y verificar su integridad. Si el contenido de un archivo es modificado, su hash también cambiará.

Este tipo de procedimiento puede utilizarse en áreas como análisis forense digital, respuesta a incidentes y verificación de archivos.

## Requisitos

Para ejecutar el programa es necesario contar con:

- Windows, Linux o macOS.
- Python 3 instalado.
- Una terminal o consola de comandos.

No es necesario instalar librerías adicionales, ya que el programa utiliza módulos incluidos con Python.

## Instrucciones de uso

### 1. Descargar el repositorio

El repositorio puede descargarse directamente desde GitHub o mediante Git:

```bash
git clone URL-DEL-REPOSITORIO
```

### 2. Entrar a la carpeta

```bash
cd Cybersecurity-Scripts
```

### 3. Ejecutar el programa

En Windows:

```bash
python hash_checker.py
```

En algunos sistemas Linux puede utilizarse:

```bash
python3 hash_checker.py
```

### 4. Introducir el archivo

El programa solicitará la ruta del archivo que se desea analizar.

Ejemplo:

```text
C:\Users\Usuario\Desktop\prueba.txt
```

### 5. Resultado

El programa calculará y mostrará el hash SHA-256 del archivo.

Ejemplo:

```text
=== SHA-256 Hash Checker ===

Ingresa la ruta del archivo que deseas analizar:
C:\Users\Usuario\Desktop\prueba.txt

Archivo encontrado.

SHA-256:
7b1e8a9f86a41316dcd86e9cc633e89a...
```

## Aplicación en ciberseguridad

El cálculo de hashes permite comprobar la integridad de archivos y detectar modificaciones.

Por ejemplo, durante un análisis forense se puede obtener el hash de una evidencia digital y posteriormente volver a calcularlo. Si ambos hashes son iguales, se puede demostrar que el archivo no fue modificado durante el análisis.

## Tecnologías utilizadas

- Python 3
- hashlib
- os
- SHA-256

## Objetivos de aprendizaje

Con este proyecto practiqué:

- Uso básico de Python.
- Lectura de archivos.
- Generación de hashes.
- Verificación de integridad.
- Automatización de tareas.
- Documentación de herramientas mediante GitHub.

## Uso

Este proyecto fue desarrollado con fines académicos y educativos.

## Autor

Luis Valdez  
Estudiante de Seguridad en Tecnologías de la Información
