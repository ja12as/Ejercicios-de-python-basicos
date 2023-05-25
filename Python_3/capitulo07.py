import MySQLdb

con = MySQLdb.connect('localhost', 'usuario', 'password', 'prueba')

cursor = con.cursor()

sql = "INSERT INTO(nombre, continente, habitantes, moneda) VALUES ('España', 'Europa', 47, 'Euro')"
cursor.execute(sql)

sql = "SELECT * FROM paises WHERE continente='Europa'"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
       print(row)


print(row[3])

cursor = con.cursor(MySQLdb.cursors.DictCursor)

for row in rows:
    print('País: {0}. Moneda: {1}'.format(row['nombre'], row['moneda']))

sql = "SELECT * FROM paises WHERE nombre='China'"
cursor = con.cursor()
cursor.execute(sql)
cursor.fetchone()

try:
    cursor.execute(sql)
    cursor.commit()
except MySQLdb.Error:
    con.rollback()

sql = "SELECT moneda, nombre FROM paises WHERE continente=%s"
cursor.execute(sql, ('Europa'))
cursor.execute(sql, ('Asia'))


con.close()

import psycopg2

con = psycopg2.connect('dbname=paises user=usuario password=password host=localhost')


sql = "UPDATE paises SET habitantes=205 WHERE nombre='Brasil'"'
cursor.execute(sql)


sql = 'SELECT nombre FROM paises WHERE habitantes > 80'
cursor.execute(sql)
cursor.fetchmany(2)

import cx_Oracle

cad_con = 'usuario/password@localhost/paises'
con = cx_Oracle.connect(cad_con)


cursor = con.cursor()

rows = cursor.fetchmany(numRows=3)

cursor = con.cursor()
sql = 'SELECT * FROM paises WHERE moneda= :moneda')
cursor.prepare(sql)
cursor.execute(None, {'moneda': 'Euro'})


cursor = con.cursor()
res = cursor.callfunc('miproc', cx_Oracle.NUMBER, ('x', 33))

import sqlite3

con = sqlite3.connect('paises.db')

cursor = con.cursor()

cursor.execute('select * from paises')
for pais in cursor:
       print(pais)

query = "INSERT INTO pais(nombre, continente, habitantes, moneda) VALUES ('Japón', 'Asia', 127, 'Yen')"
cursor.execute(query)
cursor.commit()

import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

cad_con = 'mysql://usuario:password@localhost/prueba'
engine = create_engine(cad_con)

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    continente = Column(String(20))
    habitantes = Column(Integer)
    moneda = Column(String(30))

    def __init__(self, nombre, continente, habitantes, moneda):
        self.nombre = nombre
        self.continente = continente
        self.habitantes = habitantes
        self.moneda = moneda

    def __repr__(self):
        return '<Pais('%s')>' % (self.nombre)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

p = Pais('Tailandia', 'Asia', 65, 'Baht')
session.add(p)
session.commit()

rows = session.query(Pais, Pais.nombre).all()
for row in rows:
    print(row.nombre)

res = session.query(Pais).filter(Pais.moneda == 'Euro')

session.query(Pais).order_by(Pais.id)

p.habitantes = 67
session.commit()

import sqlobject

class Pais(sqlobject.SQLObject):
    nombre = sqlobject.StringCol(length=100)
    continente = sqlobject.StringCol(length=20)
    habitantes = sqlobject.IntCol()
    moneda = sqlobject.StringCol(length=30)

db_cad = 'mysql://cruceros:cruceros@localhost/cruceros'
con = sqlobject.connectionForURI(db_cad)
sqlobject.sqlhub.processConnection = con

Pais.createTable()

Pais(nombre='Francia',continente='Europa',moneda='Euro', habitantes=66)

p = Pais.get(1)
p.nombre

p.set(habitantes=67)
p = Pais.get(1)
p.habitantes

paises = Pais.selectBy(continente='Europa')
from pais in paises:
    print(pais.nombre)

import redis

con = redis.StrictRedis(host='localhost', port=6379, db=0)

con.set('clave', 'valor')

con.get('clave')

con.delete('clave')

pool = redis.ConnectionPool()
con = redis.Redis(connection_pool=pool)

import pymongo

con = pymongo.Connection()
db = con.pruebas

pais = {'nombre': 'Alemania', 'habitantes': 82, 'continente': 'Europa', 'moneda': 'euro'}
paises = db.paises
paises.insert(pais)

paises.find_one({'nombre': 'Alemania'})

p_euro = paises.find({'moneda': 'Euro'})
for p in p_euro:
    print(p)

paises.find({'moneda': 'Euro'}).count()

import pycassa

from pycassa.pool import ConnectionPool
pool = ConnectionPool('mainspace')

pool = ConnectionPool('mainspace', ['192.168.0.3', '8080'])

from pycassa.columnfamily import ColumnFamily
col = ColumnFamily(pool, 'maincolumn')

col.insert('Alemania', {'habitantes': 82, 'continente': 'Europa', 'moneda': 'euro'})

col.get('Alemania')

col.multiget(['Alemania', 'Francia'])
