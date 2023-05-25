'''Programa: Suma de enteros.
   Usa la instrucción while (Mientras).
   Este algoritmo suma los enteros del 1 al N.'''

# INICIO
# Inicializa j y la suma:

suma = 0
j = 1

# Recibe el valor de N:

N = int(input("Dame el valor de N: \n"))

# Inicia el ciclo Mientras

while (j <= N):
    suma = suma + j
    j = j + 1 # Se incrementa el contador.
# Termina el ciclo Mientras

# Despliega el resultado:
print("La suma es: ", suma)

# FIN
    
