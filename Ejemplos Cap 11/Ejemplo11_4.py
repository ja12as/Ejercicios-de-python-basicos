""" Este programa grafica la función seno"""

#Se importan las bibliotecas y funciones necesarias
from numpy import linspace, pi, sin
from matplotlib.pyplot import   plot, show, xlim, ylim

# Puntos donde se evalúa el seno.
x = linspace( -pi, pi, 256)
y = sin(x)

# Realización de la gráfica.
plot(x, y, label = "seno")


# Límites para el eje y.
ylim(-2, 2)

# Se despliega la gráfica.
show( )

