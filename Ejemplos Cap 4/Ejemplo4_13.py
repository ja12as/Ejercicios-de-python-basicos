'''Algoritmo para calcular el factorial de un
   número entero positivo'''

# INICIO

# Inicializa las variables.
factorial_de_n = 1
n = int(input("Dame el valor del entero positivo: \n"))

# Principio del ciclo for que efectúa el cálculo del factorial.
for k in range(2, n + 1):
    factorial_de_n = factorial_de_n*k    
# Termina ciclo for.

# Despliega el resultado:
print( "El factorial de ", n, " es ", factorial_de_n) 

# FIN                      
            

