fich = open("fichero.txt")

fich = open("pruebas\fichero.txt")

fich = open("pruebas/fichero.txt")


from os import path
ruta_fich = path.join("pruebas", "fichero.txt")
fich = open(ruta_fich)


open("data.bin", "b+")


f_nuevo = open("nuevo.txt", "w")


fich = open("texto.txt", "w")
fich.write("Primera línea\n")
fich.write("Segunda línea\n")
fich.close()

lineas = ["Primera línea\n", "Segunda línea\n"]
fich.writelines(lineas)


fich = open("texto.txt", "w")
fich.read()
fich.seek(0)
fich.readlines(fich)
fich.seek(0)
fich.readline()


for line in open("texto.txt"):
    print(line)

with open("texto.txt") as fich:
    print(fich.read())

fich = open("test.bin", "bw")
fich.write(b"\x33\xFA\x1E")
fich.close()


fich = open("test.bin", "br")
fich.read(3)

fich.seek(-1, 2)
fich.read(1)

class Alumno:
    def __init__(self, nombre_completo, titulacion, edad):
       self.apellidos = nombre_completo['apellidos']
       self.nombre = nombre_completo['nombre']
       self.titulacion = titulacion
       self.edad = edad
    def __repr__(self):
       return repr(self.nombre, self.apellidos, self.titulacion)


nombre_completo = {"apellidos": "Rodriguez", "nombre": "Lucas"}
alumno = Alumno(nombre_completo, "Grado en Derecho", 21)


import pickle
with open("alumnos.bin", "wb") as fich:
    pickle.dump(alumno, fich)


with open("alumnos.bin", "rb") as fich:
    pickle.load(fich)


from xml.etree.ElementTree import parse
xml_doc = parse('albums.xml')
for ele in xml_doc.findall('titulo'):
       print(ele.text)


from xml.dom.minidom import parse, Node
xmltree = parse('albums.xml')
for nodo in xmltree.getElementsByTagName('titulo'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print(nodo_hijo.data)

import xml.sax.handler
class AlbumSaxHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.in_title = False

    def startElement(self, name, attributes):
        if name == 'titulo':
            self.in_title = True

    def characters(self, data):
        if self.in_title:
            print(data)

    def endElement(self, name):
        if name == 'titulo':
            self.in_title = False

import xml.sax
parser = xml.sax.make_parser()
sax_handler = AlbumSaxHandler()
parser.setContentHandler(sax_handler)
parser.parse('albums.xml')

import json
fich = open('albums.json')
line = fich.readline()
fich.close()
data = json.loads(line)

data['albums']['titulos']

data['albums']['titulos'].append("Rattle and Hum")
cad = json.dumps(data)
new_fich = open('albums_new.json', 'w')
new_fich.writeline(cad)
new_fich.close()

import yaml

data = yaml.load(open('servidores.yml'))

data['produccion']['puerto']

data['pruebas'] = {'IP': '192.168.2.8', 'puerto': 8004}

yaml.dump(data)

fich = open('new_servidores', 'w')
fich.write(yaml.dump(data))
fich.close()

import csv
with open('empleados.csv') as f:
    reader = csv.reader(f)
    for row in reader:
       print("Apellido: {0}; Nombre: {1}; Departamento: {2}; Ciudad: {3}".format(row[0], row[1], row[2], row[3]))

reader = csv.reader(f, delimiter='$')

fich = open('nuevo.csv', 'w')
fich_w = csv.writer(fich, delimiter='$')
empleados = [['Martínez', 'Juan', 'Administración', 'Barcelona'], ['López', 'María', 'Finanzas', 'Valencia']]
for empleado in empleados:
    fich_w.writerow(empleado)

fich.close()

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")

config.sections()

config['server2.domino2']['port']

config['server1.dominio1']['user']

config['server3.dominio3'] = {}
config['server3.dominio3']['protocol'] = 'ssh'
config['server3.dominio3']['timeout'] = '30'

with open('config.ini', 'w') as fich:
    config.write(fich)

for propiedad in config['server3.dominio3']:
    print(propiedad)

import zipfile
with zipfile.ZipFile('first.zip', 'w') as fzip:
    fzip.write('empleados.csv')
    fzip.write('fich.txt')
    fzip.write('test.dat')

fzip = zipfile.ZipFile('first.zip')
fzip.printdir()

fzip.namelist()

fzip.extractall(path="..")

info = fzip.infolist()
for arch in info:
    print(arch.filename, arch.date_time, arch.compress_size)

import gzip
with open('fich.dat', 'rb') as f_original:
    with gzip.open('fich.txt.gz', 'wb') as fich:
        fich.writelines(f_original)

datos_binarios = b"Este string es binario"
with gzip.open('nuevo.gz', 'wb') as fich:
    fich.write(datos_binarios)

datos_binarios = b"Comprimiendo cadena"
comprimidos = gzip.compress(datos_binarios)

import bz2
cad = b"Cadena binaria"
cad_comprimida = bz2.compress(cad)

cad_descomprimida = bz2.decompress(cad_comprimida)

with open('fich.dat', 'rb') as f_original:
    with bz2.BZ2File('fich.dat.bz2', 'wb') as fich:
        fich.writelines(f_original)

import tarfile
ftar = tarfile.open('first.tar.gz', 'w:gz')
ftar.add('empleados.csv')
ftar.add('fich.txt')
ftar.add('test.dat')
ftar.close()

ftar = tarfile.open('first.tar.gz', 'r:gz')
ftar.extractall()

ftar.list()

ftar.getnames()
