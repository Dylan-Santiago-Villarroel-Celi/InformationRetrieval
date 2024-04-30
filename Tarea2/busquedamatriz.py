import os
import pickle

# Cargar la matriz booleana desde el archivo
with open("matriz_booleana.pkl", "rb") as f:
    matriz_cargada = pickle.load(f)

# Directorio donde se encuentran los documentos de texto
directorio = "semana1/data"

# Obtener una lista de los nombres de archivo en el directorio
nombres_archivos = os.listdir(directorio)

# Función para buscar la palabra en la matriz booleana
def buscar_palabra(palabra, matriz):
    indices_archivos = []
    for fila in matriz:
        if fila[0] == palabra:
            for i in range(1, len(fila)):
                if fila[i]:
                    indices_archivos.append(i - 1)  # Restamos 1 para ajustar el índice de archivo
    return indices_archivos

# Pedir al usuario una palabra para buscar en la matriz
palabra_buscar = input("Ingresa una palabra para buscar en la matriz: ")

# Buscar la palabra en la matriz
indices_archivos_encontrados = buscar_palabra(palabra_buscar, matriz_cargada)

# Mostrar los nombres de archivo correspondientes a los índices encontrados
print("Archivos que contienen la palabra '{}' en la matriz booleana:".format(palabra_buscar))
for indice in indices_archivos_encontrados:
    print(nombres_archivos[indice])
