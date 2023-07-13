"""
Ahora, para continuar practicando, te propongo un ejercicio.
Supongamos que tienes una lista de palabras:
["manzana", "banana", "naranja", "pera"]. Queremos representar
estas palabras utilizando incrustaciones de palabras (word embeddings)
utilizando la biblioteca gensim en Python. Tu tarea es completar el
siguiente código para generar las incrustaciones de palabras:
"""

from gensim.models import Word2Vec

words = ["manzana", "banana", "naranja", "pera"]

# Crear un modelo Word2Vec
model = Word2Vec(sentences=[words], vector_size=5, window=2, min_count=1, sg=1)

# Obtener las incrustaciones de palabras para todas las palabras
word_embeddings = [model.wv[word] for word in words]

print(word_embeddings)

"""
[array([-0.03632035,  0.0575316 ,  0.01983747, -0.1657043 , -0.18897636],
      dtype=float32), array([ 0.1476101 , -0.03066943, -0.09073226,  0.13108103, -0.09720321],
      dtype=float32), array([-0.14233617,  0.12917745,  0.17945977, -0.10030856, -0.07526743],
      dtype=float32), array([-0.01072454,  0.00472863,  0.10206699,  0.18018547, -0.186059  ],
      dtype=float32)]


    Cada incrustación de palabras es un vector numérico de 5 dimensiones
    que captura las relaciones semánticas entre las palabras en función del
    contexto en el que aparecen en el conjunto de datos utilizado para entrenar el modelo Word2Vec.
      """

