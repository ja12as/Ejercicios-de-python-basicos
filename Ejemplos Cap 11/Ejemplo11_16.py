""" Se realiza una gráfica de superficie con su proyección
    sobre el plano x, y."""

# Se importan las bibliotecas y funciones necesarias.
from pylab import arange, sin, sqrt, meshgrid, figure, cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import  show

# Se define la figura y los ejes.
fig = figure()
ax = Axes3D(fig)

# Se definen el rango de X, Y y la rejilla.
X = arange(-4, 4, 0.25)
Y = arange(-4, 4, 0.25)
X, Y = meshgrid(X, Y)

# Se calcula la función.
R = sqrt(abs(X**3) + Y**2)
Z = sin(R)

#Parámetros de la gráfica
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2,2)

# Despliegue de la gráfica de superficie.
show()
