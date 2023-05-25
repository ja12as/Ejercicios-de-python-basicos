""" Este algoritmo convierte un número de decimal a binario."""

# Función que lee el número.
def leer( ):
    numero = int(input("Dame el número a convertir: "))
    return numero
# Termina la función.

# Función que realiza las divisiones.
def dividir(numero):
    binario = [ ] # Lista donde se almacenan los bits.
    cociente = numero # Inicializa el cociente.
    # Ciclo Mientras para obtener los bits.
    while(cociente > 0):
        residuo = cociente%2
        cociente = cociente//2
        binario.append(residuo)
        
    return binario
# Termina la función.

# Función que muestra el número binario.
def desplegar(binario):
    binario = list(reversed(binario))
    print("El resultado es: ", binario)

# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

numero = leer()
binario = dividir(numero)
desplegar(binario)

# FIN
