""" Matriz de ventas departamentales."""

# Importa la biblioteca de números aleatorios.
import random

# INICIO

# Inicializa la matriz de ventas con números aleatorios.
gasto = [[random.randint(0, 10) for i in range(12) ] for j in range(5)]

# Inicializa las matrices.
gasto_mensual = [0]*12
gasto_depto = [0]*5
gasto_total = 0


# Desplegar la matriz gasto de ventas:
print("\nLa matriz de ventas es: ")
for k in range(5): # Itera los renglones.
    print()
    for j in range(12): # Itera las columnas.
        print(gasto[k][j], end = ',\t')
        
# Realiza la suma mensual:
for mes in range(12): 
    for depto in range(5):
        gasto_depto[depto] = gasto_depto[depto] + gasto[depto][mes]
print("\nGastos por departamento\n")
print(gasto_depto)

# Calcula gasto mensual:
for depto in range(5):
    for mes in range(12): 
        gasto_mensual[mes] = gasto_mensual[mes]  + gasto[depto][mes]
print("\nGastos por mes\n")
print(gasto_mensual)
        
# Gasto total de todo el año:
for mes in range(12): 
    gasto_total = gasto_total + gasto_mensual[mes]
print("\nGasto total: ", gasto_total)


                
# FIN
