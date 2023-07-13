"""
Ahora, te presentaré un ejemplo de código utilizando
la técnica de codificación one-hot en Python. Supongamos que
tenemos una lista de categorías de películas y queremos
representarlas como vectores one-hot:
"""
import numpy as np

categories = ['Acción', 'Comedia', 'Drama', 'Aventura']

# Crear una matriz de ceros para almacenar los vectores one-hot
num_categories = len(categories)
one_hot_matrix = np.zeros((num_categories, num_categories))

# Generar los vectores one-hot
for i, category in enumerate(categories):
    one_hot_matrix[i, i] = 1

print(one_hot_matrix)

"""
output:
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
  identificado correctamente cómo se representaría la categoría "Drama"
  en el vector one-hot utilizando el código proporcionado. El vector
  one-hot para la categoría "Drama" sería [0, 1, 0, 0]
"""