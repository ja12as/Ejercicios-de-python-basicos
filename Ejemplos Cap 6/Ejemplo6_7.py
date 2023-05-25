""" Algoritmo invierte lista.
    Recibe una lista de IDs y las muestra en orden inverso."""

# INICIO

# Inicialización de variables.
no_estudiante = [None]*5 # Se realiza para 5 estudiantes.

# Recibir los números de estudiante:
#Inicio del ciclo for:
for contador in range(5):
    print("\nDame el número de estudiante. \n")
    no_estudiante[contador] = int(input())
# Fin del ciclo Para.
    
# Se invierte el orden:
k = 4 # Último elemento de la lista.
# Se imprime el encabezado:
print("\nNos. de estudiante en orden inverso.\n")
#Inicia ciclo while:
while(k >= 0): # Cuando k sea negativo ya terminó.
    print("\n", no_estudiante[k]) # Se imprime el no. de estudiante.
    k = k - 1 # Se decrementa la variable k.
# Fin del ciclo Mientras.

# FIN
