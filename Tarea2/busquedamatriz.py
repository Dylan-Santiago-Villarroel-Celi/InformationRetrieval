import pickle

# Cargar la matriz booleana desde el archivo
with open("matriz_booleana.pkl", "rb") as f:
    matriz_cargada = pickle.load(f)

# Ahora puedes utilizar la matriz_cargada en tu programa
print("Matriz booleana cargada correctamente:")
for fila in matriz_cargada:
    print(fila)
