""" Obtención de los dígitos de un número."""

# Función que suma los dígitos.
def adicion(caso):
    suma = 0 # Inicializa la suma a cero.
    for k in range(caso):
        suma =  suma + lista_digitos[k]
    # Regresa la suma.
    return suma
     
# Termina la función.

# Función que multiplica los dígitos.
def multiplicacion(caso):
    producto = 1 # Inicializa el producto a la unidad.
    for k in range(caso):
        producto = producto*lista_digitos[k]
    # Regresa el producto.
    return producto    
# Termina la función.


# Función que obtiene los dígitos.
def digitos(numero):
    global lista_digitos
    if (numero <= 10):
        caso = 1
    elif (numero <= 100):
        caso = 2
    elif (numero <= 1000):
        caso = 3
    elif (numero <= 10000):
        caso = 4
    elif (numero <= 100000):
        caso = 5
    else:
        caso = 6

    for k in range(caso):
        lista_digitos.append(numero%10) # Obtiene el residuo.
        numero = numero//10 # Obtiene el cociente.
    # Los dígitos están almacenados en el vector list_digitos.
    # El número de dígitos es el valor de caso..
    return caso    
# Termina la función.

# Función que compara la suma y la multiplicación.
def comparacion(suma, producto):
    resultado = False # Supone que No son iguales..
    if (suma == producto):
        resultado = True
    # Regresa el resultado.
    return resultado    
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Datos iniciales:
lista_digitos = [ ]
numero = int(input("Dame un número: "))
# Se calcula la lista de dígitos.
caso = digitos(numero)

# Se calcula la suma y el producto y se comparan:
suma = adicion(caso)
producto = multiplicacion(caso)
resultado = comparacion(suma, producto)

# Se checa si la suma y el producto son iguales.
if(resultado):
    print("El número SÍ cumple la condición.")
else:
    print("El número NO cumple la condición.")              

# FIN
