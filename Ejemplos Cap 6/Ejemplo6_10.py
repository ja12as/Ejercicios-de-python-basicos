""" Suma de los elementos de un vector."""

# INICIO

# Inicialización de variables.
suma = 0
vector = [None]*5

# Lee el vector y realiza la suma.
#Inicio del ciclo for:
for contador in range(5):
    vector[contador] = int(input("Dame un elemento: \n"))
    # Realiza la suma:
    suma = suma + vector[contador]
# Fin del ciclo Para.
    

# Se imprime la suma:
print("\n Suma = ", suma)


# FIN
