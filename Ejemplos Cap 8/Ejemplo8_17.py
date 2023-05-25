""" Obtención del máximo común divisor."""

# Función que máximo común divisor.
def mcd(a, b):
    k = 1
    for k in range(b, 0, -1):
        if (a%k == 0 and b%k == 0):
            print("El máximo común divisor es: ", k)
            break
    print("El máximo común divisor es: ", k) 
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Se reciben los valores de los dos números.
a = int(input("Dame el número mayor: "))
b = int(input("Dame el número menor: "))

# Se calcula llama la función mcd
mcd(a, b)             

# FIN
