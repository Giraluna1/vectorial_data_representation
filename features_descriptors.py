"""
Esta vez nos centraremos en descriptores de características
en el contexto de la visión por computadora.

Imaginemos que queremos extraer descriptores de características
utilizando la técnica de Histogramas de Gradientes Orientados (HOG)
para un conjunto de imágenes de perros y gatos. Utilizaremos la
biblioteca scikit-image en Python para este ejercicio.

Aquí tienes el código incompleto que debes completar:
"""

from skimage.feature import hog
from skimage import io
import matplotlib.pyplot as plt

# Ruta a la imagen de un perro
dog_image_path = "ruta_a_la_imagen_del_perro.jpg"

# Ruta a la imagen de un gato
cat_image_path = "ruta_a_la_imagen_del_gato.jpg"

# Lee las imágenes
dog_image = io.imread(dog_image_path, as_gray=True)
cat_image = io.imread(cat_image_path, as_gray=True)

# Calcula los descriptores HOG para las imágenes
dog_hog_features, dog_hog_image = hog(dog_image, visualize=True, multichannel=False)
cat_hog_features, cat_hog_image = hog(cat_image, visualize=True, multichannel=False)

# Visualiza los descriptores HOG utilizando una paleta de colores
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(dog_image, cmap='gray')
axes[0, 0].set_title('Perro')
axes[0, 0].axis('off')
axes[0, 1].imshow(dog_hog_image, cmap='hot')
axes[0, 1].set_title('Perro - Descriptores HOG')
axes[0, 1].axis('off')
axes[1, 0].imshow(cat_image, cmap='gray')
axes[1, 0].set_title('Gato')
axes[1, 0].axis('off')
axes[1, 1].imshow(cat_hog_image, cmap='hot')
axes[1, 1].set_title('Gato - Descriptores HOG')
axes[1, 1].axis('off')

plt.show()

from skimage.feature import hog
from skimage import io
import matplotlib.pyplot as plt

# Ruta a la imagen de un perro
dog_image_path = "ruta_a_la_imagen_del_perro.jpg"

# Ruta a la imagen de un gato
cat_image_path = "ruta_a_la_imagen_del_gato.jpg"

# Lee las imágenes
dog_image = io.imread(dog_image_path, as_gray=True)
cat_image = io.imread(cat_image_path, as_gray=True)

# Calcula los descriptores HOG para las imágenes
dog_hog_features, dog_hog_image = hog(dog_image, visualize=True, multichannel=False)
cat_hog_features, cat_hog_image = hog(cat_image, visualize=True, multichannel=False)

# Visualiza los descriptores HOG utilizando una paleta de colores
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(dog_image, cmap='gray')
axes[0, 0].set_title('Perro')
axes[0, 0].axis('off')
axes[0, 1].imshow(dog_hog_image, cmap='hot')
axes[0, 1].set_title('Perro - Descriptores HOG')
axes[0, 1].axis('off')
axes[1, 0].imshow(cat_image, cmap='gray')
axes[1, 0].set_title('Gato')
axes[1, 0].axis('off')
axes[1, 1].imshow(cat_hog_image, cmap='hot')
axes[1, 1].set_title('Gato - Descriptores HOG')
axes[1, 1].axis('off')

plt.show()

# tu output debe ser como la imagen que esta en images/