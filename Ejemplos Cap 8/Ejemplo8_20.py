""" Cotizaciones de dolar y euro."""

# Función que calcula el máximo de un vector.
def mayor(n, x):
    mayor = 0 # Se inicializa el mayor.
    for k in range(n):
        if(x[k] > mayor):
            mayor = x[k]
    return mayor
# Termina la función.

# Función que obtiene el promedio de una lista.
def promedio(n, x):
    suma = 0 # Se inicializa la suma.
    for k in range(n):
        suma = suma + x[k] # Se suman todos los elementos del vector.

    promedio = suma/n # Se calcula el promedio.
    return promedio
        
# Termina la función.


# INICIO DEL ALGORITMO PRINCIPAL

# Se inicializan los datos:
semana = ['lunes', 'martes', 'miercoles','jueves','viernes']
moneda = [ [ ], [ ] ] # Inicialización de las cotizaciones de dolar y euro.
n = 5
print(moneda)
# Se leen las cotizaciones con un ciclo for:
for k in range(2):
    for dia in range(5):
        if (k == 0):
            print("Cotización del dolar del día", semana[dia])
        else:
            print("Cotización del euro del día", semana[dia])
        moneda[k] += [float(input( ))]

# Calcular promedios.
prom_dolar = promedio(n, moneda[0])
prom_euro = promedio(n, moneda[1])

# Buscar mayor de cada moneda.
mayor_dolar = mayor(n, moneda[0])
mayor_euro = mayor(n, moneda[1])

# Se agregan estos resultados a la matriz monedas.
moneda[0].append(prom_dolar)
moneda[0].append(mayor_dolar)
moneda[1].append(prom_euro)
moneda[1].append(mayor_euro)

# Despliega el encabezado de los resultados:
letrero = ['L', 'Ma', 'Mi', 'J', 'V', 'Prom', 'Mayor']
for k in range(7):
    print(letrero[k], "\t", end = " ")

# Despliega las cotizaciones, promedio y valores mayores.
for k in range(2):
    print()
    for j in range(7):
        print(moneda[k][j], "\t", end = " ")

# FIN
