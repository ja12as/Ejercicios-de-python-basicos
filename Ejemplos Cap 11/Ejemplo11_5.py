""" Este programa grafica las funciones seno y coseno."""

#Se importan las bibliotecas y funciones necesarias

from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import   plot, show, xlim, ylim, xticks
from matplotlib.pyplot import    legend

# Puntos donde se evalúan el seno y el coseno.
x = linspace( -pi, pi, 256)
y = sin(x)
z = cos(x)


# Realización de las gráficas.
plot(x, y, label = "seno")
plot(x, z, label = 'coseno')

# Letrero de la gráfica.
legend(loc = 'upper left')


# Límites y marcas.
ylim(-2, 2)
xticks( [ -pi, -pi/2, 0, pi/2, pi ],
        [ r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'] )

# Despliegue de la gráfica.
show( )

