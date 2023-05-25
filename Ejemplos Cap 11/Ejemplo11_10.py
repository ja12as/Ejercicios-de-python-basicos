''' Gráfica de histograma'''

# Se importan las funciones necesarias.
from matplotlib.pyplot import title, hist, show
from numpy.random import normal

# Se generan los números aleatorios.
numeros_gaussianos = normal(size = 1000)


# Se genera la gráfica.
hist(numeros_gaussianos)

# Se despliega la gráfica.
title('Grafica de histograma')
show()
