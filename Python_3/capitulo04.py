class First:
    pass

a = First()

class First:
    def __init__(self):
        print("Constructor ejecutado")

f = First()

def nuevo(self):
    print("Soy nuevo")

f = First()
f.nuevo()

class Moto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

bmw_r1000 = Moto("BMW", "r100", "blanca")
suzuki_gsx = Moto("Suzuki", "GSX", "negra")

def get_marca(self):
    marca = "Nueva marca"
    print(self.marca)

honda_cbr = Moto("Honda", "CBR", "roja")
honda_cbr.get_marca()

def acelerar(self, km):
    print("acelerando {0} km".format(km))

honda_cbr.acelerar(20)

class Moto:
    n_ruedas = 2
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

Moto.n_ruedas
m = Moto()
m.n_ruedas

from math import pi
class Circle:
    def __init__(self, radio):
        self.radio = radio
    @property
    def area(self):
        return pi * (self.radio ** 2)

c = Circle(25)
print(c.area)

def area(self):
    return pi * (self.radio ** 2)
area = property(area)

c.area = 23

@property
def radius(self):
    return self.__radio

@radio.setter
def radio(self, radio):
    self.__radio = radio

circulo = Circulo()
circulo.radio = 23
print(circulo.radio)

class Test:
    def _privado(self):
        print("Método privado")

t = Test()
t._privado

class Privado:
    def __ini__(self):
        self.__atributo = 1
 p = Privado
 p.__atributo
 p_Privado__atributo

class Padre:
    def __init__(self):
        self.__test = "Padre"

class Hijo:
    def __init__(self):
        self.__test = "Hijo"

class Test:
    def __init__(self):
        self.x = 8
    @classmethod
    def metodo_clase(cls, param1):
        print("Parámetro: {0}".format(param1))

Test.metodo_clase(6)
t = Test()
print(t.x)

t.metodo_clase(5)

Test().metodo_clase(3)

@staticmethod
def metodo_estatico(valor):
    print("Valor: {0}".format(valor))

t = Test()
 t.metodo_ estatico(33)

@staticmethod
def metodo_estatico(valor):
    print(self.x)

class Ini:
    def __new__(cls):
        print("new")
        return super(Test, cls).__new__(cls)
    def __init__(self):
        print("init")

obj = Ini()

def __new__(cls, x):
    return super(Test, cls).__new__(cls)
def __init__(self, x):
    self.x = x

t = Test("param")

def __del__(self):
    print("del")

class Coche:
    def __init__(marca="Porsche", modelo="911")
        self.marca = marca
        self.modelo = modelo
    def __repr__(self):
        return("{0}-{1}".format(self.marca, self.modelo))

c = Coche()
print(repr(c))

arr = repr(c).split("-")
d = Coche(arr[0], arr[1])

def __str__(self):
    return("{0} -> {1}".format(self.marca, self.modelo)

print(d)
def __gt__(self, objeto):
    if int(self.modelo) > int(objeto.modelo):
        return True
        return False

modelo_911 = Coche("Porsche", 911)
modelo_924 = Coche("Porsche", 924)
if modelo_924 > modelo_911:
    print("El {0} es un modelo superior".format(modelo_924.modelo))

class TestHash:
    pass
t = TestHash()
t.__hash__()
hash(t)
x = TestHash()
x.__hash__()
hash(x)
x == x
t == x

class TestBool:
    def __bool__():
        return False
t = TestBool()
t.__bool__()
bool(t)
if t: print("Es falso")

class Padre:
    def __init__(self):
        self.x = 8
        print("Constructor clase padre")
    def metodo(self):
        print("Ejecutando método de clase padre")

class Hija:
    def met_hija(self):
        print("Método clase hija")

h = Hija()
h.metodo()

def __init__(self):
    print("Constructor hija")
>> z = Hija()

class Vehiculo:
    n_ruedas = 2
    def __init__(self, marca, modelo):
        self.marca = marca
    self.modelo = modelo
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Moto(Vehiculo):
    pass
class Coche(Vehiculo):
    pass

c = Coche("Porsche", "944")
c.n_ruedas = 4
m = Moto("Honda", "Goldwin")
m.n_ruedas

class Mantenimiento(Persona, Personal):
    pass

class Pajaro:
    def desplazar(self):
        print("Volar")

class Serpiente:
    def desplazar(self):
        print("Reptar")

def mover(animal):
    animal.desplazar()
p = Pajaro()
s = Serpiente()

p.desplazar()
s.desplazar()
mover(p)
mover(s)

class Intro:
    def __init__(self, val):
        self.x = val
    def primero(self):
        print("Primero")
    def segundo(self):
        print("Segundo")

i = Intro("Valor")
dir(i)

isinstance(i, Intro)

if (i, 'x'): print("Instancia: i. Clase: Intro. Atributo: x")
if (i, 'z'): print("Atributo z no existe")

class Hijo(Intro):
    def tercero(self):
        print("Tercero")

h = Hijo()
dir(h)

if hasattr(h, 'x'): print("h puede acceder a x")
if isinstance(h, Intro):  print("h es instancia de Intro")

type(i)
type(h)

cad = "Cadena"
callable(cad)
def fun():
    return("fun")
callabe(fun)

callable(i)

class Test:
    def __init__(self):
        self.x = 3
        self.y = 4
        self.z = 5

attrs = {"x": 1, "y": 2, "z": 3}
t = Test()

for k, v in attrs.items():
    t.__setattr__(k, v

for k in attrs.keys():
    print("{0}={1}".format(k, t.__getattribute__(k))
