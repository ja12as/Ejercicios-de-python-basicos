'''Cálculo de interés.
   Este algoritmo calcula el interés
   simple y compuesto.'''

# INICIO
capital = float(input("Dame el capital: \n"))
tasa = float(input("Dame la tasa anual: \n"))
n = int(input("Dame el número de meses: \n"))

# Interés simple:
int_simple = capital*(1 + n*tasa)

# Interés compuesto:
int_compuesto = capital*pow(1 + tasa, n)

# Impresión de resultados:
print("Interés simple: %0.2f\n" %int_simple)
print("Interés compuesto: %0.2f\n" %int_compuesto)
