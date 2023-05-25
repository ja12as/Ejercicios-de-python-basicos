""" Este programa grafica las funciones seno y coseno,
    cada una en una subfigura diferente."""

#Se importan las bibliotecas y funciones necesarias

from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import   plot, show, xlim, ylim, xticks, figure
from matplotlib.pyplot import    legend, subplot

# Puntos donde se evalúan el seno y el coseno.
x = linspace( -pi, pi, 256)
y = sin(x)
z = cos(x)

# Se define la subgráfica del seno.
subplot(2, 1, 1)

# Realización de la gráfica del seno.
plot(x, y, label = "seno")

# Letrero de la gráfica.
legend(loc = 'upper left')

# Se define la subgráfica del coseno.
subplot(2, 1, 2)

# Realización de la gráfica del coseno.
plot(x, z, label = 'coseno')

# Letrero de la gráfica.
legend(loc = 'upper left')


# Límites y marcas.
ylim(-2, 2)
xticks( [ -pi, -pi/2, 0, pi/2, pi ],
        [ r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'] )

# Despliegue de la gráfica.
show( )

