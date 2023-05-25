''' Gráfica del campo magnético alrededor de un alambre
    que conduce una corriente I.'''
# Se importa la biblioteca necesaria.
from pylab import *

# Límites de la gráfica para las coordenadas x, y.
xmax = 2.0
xmin=-xmax

NX = 5
ymax = 2.0
ymin = -ymax
NY = 5

# Componentes vectoriales y puntos
x=linspace(xmin,xmax,NX)
y = linspace(ymin, ymax, NY)
X, Y = meshgrid(x, y)

# La función del campo magnético.
S2 = X**2 + Y**2 # Este es el radio al cuadrado
Bx = -Y/(S2+0.001)
By = +X/(S2+0.001)

# Generación de la gráfica.
figure()
QP = quiver(X,Y,Bx,By)
quiverkey(QP, 0.85, .85,1.0, 'Campo magnético')

# Límites de los incrementos
dx=(xmax-xmin)/(NY-1.) 
dy=(ymax-ymin)/(NY-1.)
axis([xmin-dx, xmax+dx, ymin-dy, ymax+dy])

# Despliegue de la gráfica.
title('Campo magnético de un alambre con I=50 A')
xlabel('x (cm)')
ylabel('y (cm)')
show()
