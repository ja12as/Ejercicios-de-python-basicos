x = 4
y = 0
if x == 4:
    y = 5
else:
    y = 2

if x == 4:
    y = 1
elif x == 5:
    y = 2
elif x == 6:
    y = 3
else:
    y = 5

if a > b: print("a es mayor que b")

for x in range(1, 3):
    print(x)

lista = ["uno", "dos", "tres"]
cad = ""
for ele in lista:
    cad += ele

for item in (1, 2, 3):
    print(item)
else:
    print("fin")

x = 0
y = 3
while x < y:
    print(x)
    x += 1

x = 0
y = 3
while x < y:
    print(x)
    x+=1
    if x == 2:
        break
    else:
        print("x es igual a 2")

for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)

with open(r'info.txt') as myfile:
    for line in myfile:
       print(line)

def test():
    print("test ejecutada")

def test2(a, b):
    a = 2
    b = 3

c = 5
d = 6
test2(c, d)
print("c={0}, d={1}". format(x, y))

def variable(lista):
    lista[0] = 3
lista = [1, 2, 3]
print(variable(lista))

a = 3
b = a
b = 2
print("a={0}, b={1}".format(a, b))

a = [0, 1]
b = a
b[0] = 1
print("a={0}; b={1}".format(a, b))

def test(a, b):
    a = 2
    b = 3
    return(a, b)

c, d = test(c, d)
variable(lista[:])

def fun(a, b=1):
    print(b)
fun(4)

def fun(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))
fun(c=5, b=3, a=1)

def fun(a, b, c=4):
    print("a={0}, b={1}, c={2}".format(a, b, c))

fun(1, 2, 4)
fun(a=1, b=2, c=4)
fun(a=1, b=2)
fun(1, 2)

def fun(*items):
    for item in items:
        print(item)

fun(1, 2, 3)
fun(5, 6)

t = ('a', 'b', 'c')
fun(t)

def fun(**params):
    print(params)

fun(x=5, y=8)
fun(x=5, y=8, z=4)

def print_record(nombre, apellido, **rec):
    print("Nombre: ", nombre)
    print("Apellidos:", apellidos)
    for k in rec:
        print("{0}: {1}".format(k, rec[k]))

print_record("Juan", "Coll", edad=43, localidad="Madrid")
print_record("Manuel", "Tip", edad=34)

def fun(x, y, z):
    print(x, y, z)

t = (1, 2, 3)
fun(*t)

d = {'y': 1, 'z': 2, 'x': 0}
fun(**d)

def fun(a=1, b=2, c=3):
    print(a, b, c)

d = {'a': 3, 'b': 4}
fun(**d)

def fun(x, y):
    print(x, y)

def fun(x):
    print(x)

fun(1, 3)
fun(4)
type(fun)

li = [lambda x:  x + 2, lambda x:  x + 3]
param = 4
for accion in li:
    print(accion(param))

lam = lambda x: x*5
print(lam(3))

def lam(x):
    return x*5

print(lam(3))

li = [1, 2, 3]
new_li = map(lambda x: x+2, li)
for item in new_li: print(item)

fun(x=1, li=[]):
    li.append(x)
fun()
fun(2)

def fun(x=1, li=None):
    if lis is None:
        lis = []
        lis.append(x)
        print(lis)

li = [3, 4]
fun(6, li)

import sys
sys.path

try:
    print(li[2])
except IndexError:
    print("Error: Índice no válido")

try:
    li[2]
except:
    print("Error: Índice no válido")
else:
    print("Sin error")
finally:
    print("Bloque ejecutado")

class ValorIncorrecto(Exception):
    def __init__(self, val):
        print(("{0} no permitido").format(val))

val = 8
if val > 5 and val < 9:
    raise ValorIncorrecto(val)

try:
    print(li[2])
except IndexError:
    import sys
    sys.exc.info()
