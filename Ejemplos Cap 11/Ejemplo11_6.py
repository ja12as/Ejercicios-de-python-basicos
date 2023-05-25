""" Este programa grafica las funciones seno y coseno,
    cada una en una figura diferente."""

#Se importan las bibliotecas y funciones necesarias

from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import   plot, show, xlim, ylim, xticks, figure
from matplotlib.pyplot import    legend

# Puntos donde se evalúan el seno y el coseno.
x = linspace( -pi, pi, 256)
y = sin(x)
z = cos(x)

# Se define la ventana la figura 2.
a = figure(2)

# Realización de la gráfica del seno.
plot(x, y, label = "seno")

# Letrero de la gráfica.
legend(loc = 'upper left')

# Se define la nueva figura 20.
b = figure(20)

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

