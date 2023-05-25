x = 8
y = x

x = "test"

lista_1 = [9, 8, 7]
lista_2 = lista_1
lista_1[2] = 5

z = 35
type(z)
z = "ahora es una cadena de texto"

num_entero = 8
num_negativo = -78
num_real = 4.5
num_complejo = 3.2 + 7j
num_complex = 5J + 3
num_real = 0.5e-7
num_binario = 0b111
num_octal = 0o10
num_hex = 0xff

abs(-47, 67)

import math
math.sqrt(169)

hex(16)
oct(8)
bin(0xfe)

conjunto = set('846')
conjunto = {8, 4, 6}
conjunto_2 = set('785')
conjunto & conjunto_2
conjunto.intersection(conjunto_2)

duplicados = {2, 3, 6, 7, 6, 8, 2, 1}

cadena = "esto es una cadena de texto"
cad_multiple = """Esta cadena de texto
tiene más de una línea. En concreto, cuenta
con tres líneas diferentes"""

cad = b"cadena de tipo byte"
type(cad)
lat = bytearray("España", 'latin1')
print(lat)
bytearray("España", "utf16")
cadena = "comprobando el tipo str"
type(cadena)

cad = "es de tipo str"
cad.encode()
cad = b"es de tipo byte"
cad.decode()

cad = "Cadena de texto de ejemplo"
len(cad)
cad ="xyza"
cad.find("y")
cad = "Hola Mundo"
cad.replace("Hola", "Adiós")
cad = " cadena con espacios en blanco "
cad.strip()
cad.lstrip()
cad.rstrip()
cad2 = cad.upper()
print(cad2)
print(cad3.lower())
cad = "un ejemplo"
cad.capitalize()
cad = "primer valor;segundo;tercer valor"
cad.split(";")

"abc".join(',')

cad_concat = "Hola" + " Mundo!"
print(cad_concat)

"Hola " + cad2 + ". Otra " + cad3
"Hola {0}. Otra {1}".format(cad2, cad3)
"Hola {cad2}. Otra {cad3}".format(cad2=cad2, cad3=cad3)

num = 3
"Número: " + str(num)

print("Hola Mundo" * 4)

cad = "Nueva cadena de texto"
"x" in cad

cad = "Cadenas"
print(cad[2])

print(cad[:3])
cad[-2]
cad[3:]

t = (1, 'a', 3.5)
t[1]
t = (1, 3, 'c', )
t = (1, ('a', 3), 5.6)

for ele in t:
    print(ele)

('r', 2) * 3
('r', 2, 'r', 2, 'r', 2)

t = (1, 3, 7)
t.index(3)
t = (1, 3, 1, 5, 1,)
t.count(1)

lista = []
li = [2, 'a', 4]

for ele in li:
    print(ele)

li[1] = 'b'
li[2]
'a' in li
tuple(li)
li.append('nuevo')
li[4] = 23
li.insert(3, 'c')
li.insert(12, 'c')
li.insert(0, 'd')
li
['d', 2, 'a', 4]
del(li[1])
len(li)
li.remove('d')

lista = [3, 1, 9, 8, 7]
sorted(lista)
sorted(lista, reverse=True)
lista
lista.sort()
lista

lis = ['aA', 'Ab', 'Cc', 'ca']
sorted(lis)
sorted(lis, key=str.lower)

lista.reverse()
lista

lis = ['be', 'ab', 'cc', 'aa', 'cb']
lis.sort()
lis

lista = [ele for ele in (1, 2, 3)]
print(lista)
lista = []
for ele in (1, 2, 3):
    lista.append(ele)

matriz = [[1, 2, 3],[4, 5, 6]]
matriz[0][1]
matriz[0][1] = 33

diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario = dict(a=1, b=2, c=3)
diccionario['c']
diccionario['b'] = 28
diccionario['d'] = 4

for k, v in diccionario.items():
    print("clave={0}, valor={1}".format(k, v))
for k in diccionario.keys():
    print("clave={0}".format(k))
for v in diccionario.values():
    print("valor={0}".format(v))
for k in diccionario:
    print(k)
list(diccionario.keys())
list(diccionario.items())
del(diccionario['b'])

{k: k+1 for k in (1, 2, 3)}
{clave: 1 for clave in ['x', 'y', 'z']}

sorted(diccionario)
sorted(diccionario, reverse=True)











