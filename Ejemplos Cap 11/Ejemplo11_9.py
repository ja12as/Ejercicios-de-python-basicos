''' Gráfica de pie'''

# Se importan las funciones necesarias.
from matplotlib.pyplot import figure,subplot,title,pie,show

# Se define cuantos segmentos tiene la gráfica de pie.
figure(1,figsize=(6,6))

# Valores.
fracs=[15,30,40,5,10]

# Se genera la gráfica.
pie(fracs, autopct = '%2.1i%%')

# Se despliega la gráfica.
title('Grafica de pie')
show()
