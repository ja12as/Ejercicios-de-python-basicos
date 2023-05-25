# Cálculo del saldo

#INICIO

print('Dame el saldo actual')
Saldo = float(input( ))

# Empieza la condición.
if( Saldo < 10,000.00 ):
    Saldo = Saldo*(1 + 0.03)
elif ( Saldo < 100,000.00 ):
    Saldo = Saldo*(1 + 0.04)
else:
    Saldo = Saldo*(1 + 0.06)
    # Fin del if anidado.
# Fin del if inicial.

print("\nEl saldo final es ", Saldo)

# FIN
      
