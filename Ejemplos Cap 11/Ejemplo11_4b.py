""" Este programa grafica la función seno"""

#Se importan las bibliotecas y funciones necesarias
from numpy import linspace, pi, sin
from matplotlib.pyplot import   plot, show, xlim, ylim
from matplotlib.pyplot import   xticks

# Puntos donde se evalúa el seno.
x = linspace( -pi, pi, 256)
y = sin(x)

# Realización de la gráfica.
plot(x, y, label = "seno")


# Límites para el eje y.
ylim(-2, 2)

# Marcas para el eje x.
xticks( [ -pi, -pi/2, 0, pi/2, pi ],
        [ r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'] )

# Se despliega la gráfica.
show( )

