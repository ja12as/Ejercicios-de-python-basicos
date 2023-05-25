'''Algoritmo para dibujar un cuadrado con asteriscos.'''


# INICIO

# Inicializa las variables.
N = int(input("Escribe la dimensión N >=2 del cuadrado a dibujar:\n"))

# Escribe la primera línea de asteriscos.
for i in range(N ):
    print("*", end = ' ')

print() # Salta al siguiente renglón.

# Dibuja las partes laterales.
j = 1
while( j <= N - 2):
    for k in range(N):
        if ( k == 0 ):
            print('*', end = ' ') # Imprime un asterisco mas un espacio.
        elif (k == N - 1):
            print('*', end = '  ') # Imprime un asterisco mas dos espacios.
        else:
            print('  ', end = '') # Imprime  dos espacios.
    print() # Salta al siguiente renglón.
    j += 1
    # Fin del ciclo for.
    
# Fin del ciclo while.

# Dibuja el lado de abajo.
i = 0
while i < N:
    print("*", end = ' ') # Un asterisco mas un espacio.
    i += 1

# FIN                      
            

