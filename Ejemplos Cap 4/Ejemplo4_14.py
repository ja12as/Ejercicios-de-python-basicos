'''Algoritmo para calcular la raíz cuadrada.'''

# INICIO

# Inicializa las variables.
x = 1
a = float(input("Dame el valor de a: \n"))

# Principio del ciclo for que efectúa el cálculo de la raíz de a.
for k in range(1, 10):
    x = (x + a/x)/2    
# Termina ciclo for.

# Despliega el resultado:
print( "La raíz cuadrada de ", a, " es ", x) 

# FIN                      
            

