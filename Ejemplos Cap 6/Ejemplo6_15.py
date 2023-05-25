""" Serie de Fibonacci."""

# INICIO

# Inicialización de variables.
fib = [ ]
fib[0:1] = [0, 1]

# Cálculo de la serie:
for k in range(2, 10):
    fib.append(fib[k - 1] + fib[k - 2])


# Desplegar 10 elementos de fib.
print("\n", fib)

# FIN
