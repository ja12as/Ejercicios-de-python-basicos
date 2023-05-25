""" Serie de Fibonacci."""

# Función que calcula la serie de Fibonacci.
def fibonacci(m):
    f0 = 0
    f1 = 1
    lista_fibo = [0, 1]

    # Ahora se calculan los restantes términos de la serie.
    # Se usa un ciclo for.
    for k in range(2, m):
        f = f0 + f1
        f0 = f1
        f1 = f
        lista_fibo.append(f)

    # Se despliega la serie.
    print("La serie de Fibonacci es: ", lista_fibo)
     
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Se recibe el valor de m.
m = int(input("Dame el valor de un entero positivo: "))
fibonacci(m)                

# FIN
