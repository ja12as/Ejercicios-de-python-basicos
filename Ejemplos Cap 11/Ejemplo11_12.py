''' Curva paramétrica'''

#Se importan las bibliotecas y funciones necesarias

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import title,figure,show,plot,legend
from numpy import linspace,sin,cos,pi

# Se define la figura y la proyección.
a = figure()
a.gca(projection = '3d')

# Valores de theta y radio vector r.
theta = linspace(-4*pi, 4*pi, 100)
r = linspace(0,pi,100)

# Valores de las coordenadas-
z = r
x = r*sin(theta)
y = r*cos(theta)

# Gráficación y letrero.
plot(x, y, z, label = 'curva parametrica')
legend()

# Despliegue de la curva.
show()
