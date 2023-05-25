""" Identificación de palíndromos."""

# Función que lee la frase.
def lectura( ):
    frase = input("Dame la frase sin espacios: ")
    lista = [ ] # Inicializa la lista.
    for k in range(len(frase)):
        lista.append(frase[k])
    print(lista)
    return lista
# Termina la función.

# Función que checa la frase. Para hacer esto genera la frase invertida.
def checar(lista):
    max = len(lista)
    frase = list(reversed(lista))
    # Inicializa el índice del ciclo y el contador.
    numero = 0
    contador = 0
    # Ciclo Mientrass.
    while(numero + 1 <= max/2):
        if ( frase[numero] == lista[numero]):
            contador += 1
        numero += 1 # Se incrementa el índice del ciclo Mientras.
    # Fin del ciclo.
        
    if (contador == max//2):
        print("La frase es palindromo.")
    else:
        print("La frase NO es palindromo.")
        
# Termina la función.


# INICIO DEL ALGORITMO PRINCIPAL

lista = lectura()
checar(lista)

# FIN
