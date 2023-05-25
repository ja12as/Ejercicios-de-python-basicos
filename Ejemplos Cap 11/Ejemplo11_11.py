''' Gráfica de stem'''

# Se importan las funciones necesarias.
from matplotlib.pyplot import title, stem, show
from numpy import pi, arange


# Se genera la gráfica.
stem(arange(-pi, pi))

# Se despliega la gráfica.
title('Grafica de stem')
show()
