lista = [1, 2, 3]

for ele in lista:
    print(ele)

for letra in "hola":
    print(letra)

for linea in open("fich.txt"):
    print(linea)

class CuentaAtras(object):
    def __init__(self, start):
        self.count = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

for ele in CuentaAtras(5):
    print(ele)


class Rango:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1

for ele in Rango(5,9):
    print(ele)

map(abs, (-1, 2, -3)

list(map(abs, (-1, 2, -3))

list(zip(("123", "abc")))

def cuenta_atras(ele):
    while ele > 0:
        yield n
        n -= 1

for ele in cuenta_atras(5):
    print(ele)

lista = [1, 2, 3]

(7*ele for ele in lista)

gen = (7*ele for ele in lista)
for ele in gen:
    print(ele)

def principal():
    x = 8
    def contenida():
       print(x)
    contenida()

principal()

def principal():
    x = 7
    def anidada():
        print(x)
    return anidada

res = principal()

res()

principal()

def contenedora(y):
    def anidada(z):
       return y + z
    return anidada

fun = contenedora(9)
fun(12)
21
fun(14)

otr = contenedora(1)
otr(2)

@firstDecorator
def funcion():
    print("Ejecutando la función")

def firstDecorator(obj):
    pass
res = firstDecorator(funcion)

class Decorador(object):
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("inicio", self.f.__name__)
        self.f()
        print("fin", self.f.__name__)

@Decorador
def funcion():
    print("soy función")

funcion()

def principal(f):
    def nueva():
        print("ini", f.__name__)
        f()
        print("fin", f.__name__)
    return nueva

@principal
def decorada():
    print("decorada")

decorada()

class Decorador(object):
    def __init__(self, f):
       self.f = f
    def __call__(self, *argumentos):
        print("inicio", self.f.__name__)
        self.f(*argumentos)
        print("fin", self.f.__name__)

@Decorador
def funcion(p1, p2, p3):
    print("soy función con argumentos", p1, p2, p3)

funcion("uno", "dos", "tres")

@decorator_args(1, 2, 3)
def fun(a, b):
    print ("fun args:", a, b)

def decorator_args(arg1, arg2, arg3):
    def wrap(f):
        print( "ini wrap()")
        def wrapped_f(*args):
            print( "ini wrapped_f")
            print( "decorator args:", arg1, arg2, arg3)
            f(*args)
            print( "fin wrapped_f")
        return wrapped_f
    return wrap

fun("p1", "p2")

@decorator_args(1, 2, 3)
def fun(a, b):
    print ("fun args:", a, b)

def lower(t): return t.lower()

texto = ["HOLA", "mUNdO", "AdiOS"]
list(map(lower, texto))

[cad.lower() for cad in texto]

def par(val):
    return (val%2) == 0

lista = [0, 3, 5, 6, 8, 9]
list(filter(par, lista))


def sumar(x, y):
    return x+y

from functools import reduce
lista = [1, 2, 3, 4]
reduce(sumar, lista)

import re
re.search(r"o", "hola")

m = re.search(r"o", "hola")
m.group()

m = re.search(r"\d\d\d", "hola402adios").group()
402
m = re.search(r"\d\d\d", "986hola").group()
986
m = re.search(r"\d\d\d", "adios123").group()
123
patron = re.compile("\d\d\d")
patron.search("hola402adios").group()
402
patron.search("986hola")
986
patron.search("adios123")


m = re.search(r"\d\d\d", "98x65adios")
if m is None: print("No existen coincidencias")

regex = re.compile(r"(\d+)-([A-Za-z]+")
m = regex.search("23-cDb")

m.group(1)
m.group(2)
m.group(0)

re.search(r" ^hola$", "adiosholaadios")
re.search(r"hola", "adiosholaadios")
re.findall(r"\d{3}", "345abcd78ghx678")
re.findall(r"([a-z]+)-(\d+)", "345abcd-78ghx-678")

re.sub(r"\d", "-", "345abcdef987")
re.sub(r"\d", "-", "345abcdef987", 3)
re.sub(r"(\w+)@(\w+)", r"\1@123", "abc@efg")
re.sub(r"(\w+)@(\w+)", r"\2@123", "abc@efg")
re.sub(r"ñ", "n", "niño")
cad = "Uno<a>Dos<b>Tres<c>Cuatro"
regex = re.compile(r"abc", re.IGNORECASE)
regex.search("124AbC")
regex = re.compile(r"^Text: (\d+)$", re. MULTILINE)
cad = "Text: 34\nText: 35\nText: aa\nText: 24\n"
regex.search(cad).group(1)

lista = [5, 1, 9, 8, 3]
sorted(lista)

cads = ["ca", "dc", "cb", "ab", "db"]
sorted(cads)
cads = ["ca", "Cc", "cb", "aB", "db"]
sorted(cads)

sorted(lista, reverse=True)

lista = ["abc", "de", "fghij"]
sorted(lista)
["abc", "de", "fghij"]
sorted(lista, key=len)

from operator import itemgetter
fun = itemgetter(2)
fun([1, 2, 3, 4])

lista = [("Madrid", 4), ("Barcelona", 1), ("Sevilla", 5), ("Valencia", 3)]
[("Madrid", 4), ("Barcelona", 1), ("Sevilla", 5), ("Valencia", 3)]
sorted(lista, key=itemgetter(1))

lista = [("a", 2), ("c", 2), ("b", 3), ("d", 3), ("z", 1), ("a", 1), ("d", 1)]
sorted(lista, key=itemgetter(0,1))
sorted(lista, key=itemgetter(1,0))

class Empleado:
    def __init__(self, apellidos, puesto, edad):
        self.apellidos = apellidos
        self.puesto = puesto
        self.edad = edad
    def __repr__(self):
        return repr((self.apellidos, self.puesto, self.edad))


empleados = [Empleado("Fernández", "Administración", 25),
             Empleado("Dominguez", "Finanzas", 38),
             Empleado("Amaro", "Contabilidad", 21)]

print(sorted(empleados, key=lambda empleado: empleado.apellidos))
print(sorted(empleados, key=lambda empleado: empleado.apellidos))
