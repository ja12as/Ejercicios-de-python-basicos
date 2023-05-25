""" Este programa grafica una lista de puntos"""

#Se importan las bibliotecas y funciones necesarias
from matplotlib.pyplot import   plot, show, xlim, ylim
from matplotlib.pyplot import    legend



# Se grafica:
plot([5, 6, 7, 8], [1, 2, 5, 3])

# Se definen los límites de la gráfica:
xlim(-1, 12)
ylim(0, 8)

# Se muestra la gráfica.
show( )
