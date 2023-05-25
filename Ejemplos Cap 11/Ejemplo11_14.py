""" Se realiza una gráfica de alambre."""

# Se importan las bibliotecas y funciones necesarias.
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import cm, show, title, figure
from numpy import arange, sqrt, sin, meshgrid


# Se define la figura y los ejes.
fig = figure()
ax = fig.gca(projection = '3d')

# Se definen el rango de X, Y y la rejilla.
X = arange(-5, 5, 0.25)
Y = arange(-5, 5, 0.25)
X, Y = meshgrid(X, Y)

# Se calcula la función.
Z = sin(sqrt(X**2 + Y**2) )


#Parámetros de la gráfica
A = ax.plot_wireframe(X, Y, Z)


# Despliegue de la gráfica de superficie.
title("Gráfica de alambre")
show()
