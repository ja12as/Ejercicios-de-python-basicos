''' Gráfica polar.'''

# Se importan las bibliotecas necesarias.
from numpy import pi, arange, linspace
from matplotlib.pyplot import  subplot, plot,show, grid, title

# Valores de la variables y del radio vector.
theta = arange(0, 3, 0.01)
r =  2*pi * theta

# Generación de la gráfica polar.
subplot(111, polar=True)
plot(r, theta, color='r', linewidth=10)
grid(True)

# Desplegado de la gráfica.
title("Gráfica polar de r = 2$\pi\\theta$")
show()
