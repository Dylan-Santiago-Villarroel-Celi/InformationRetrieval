import os
import string
import pickle

# Directorio donde se encuentran los documentos de texto
directorio = "semana1/data"

# Inicializamos un conjunto para almacenar las palabras únicas
palabras_unicas = set()

# Diccionario para almacenar los archivos de texto y sus palabras
archivos_palabras = {}

# Iteramos sobre los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".txt"):  # Nos aseguramos de que solo estemos leyendo archivos de texto
        with open(os.path.join(directorio, archivo), "r", encoding="utf-8") as file:
            # Leemos el contenido del archivo y lo convertimos a minúsculas
            contenido = file.read().lower()
            # Eliminamos signos de puntuación
            contenido = contenido.translate(str.maketrans("", "", string.punctuation))
            # Dividimos el contenido en palabras
            palabras = contenido.split()
            # Agregamos las palabras al conjunto de palabras únicas
            palabras_unicas.update(palabras)
            # Almacenamos las palabras del archivo en el diccionario
            archivos_palabras[archivo] = set(palabras)

# Crear la matriz booleana
matriz_booleana = []

# Iterar sobre cada palabra única y comprobar si está presente en cada archivo
for palabra in palabras_unicas:
    fila = [palabra]  # La primera columna es la palabra
    for archivo in archivos_palabras:
        if palabra in archivos_palabras[archivo]:
            fila.append(True)
        else:
            fila.append(False)
    matriz_booleana.append(fila)

# Imprimir la matriz booleana
# Guardar la matriz booleana en un archivo usando pickle
with open("matriz_booleana.pkl", "wb") as f:
    pickle.dump(matriz_booleana, f)

print("Matriz booleana guardada correctamente en 'matriz_booleana.pkl'")
