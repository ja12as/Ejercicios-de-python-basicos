from telnetlib import Telnet
tel = Telnet('localhost')

tel.read_until(b'login: ')

tel.write(b'usuario\n')

tel.read_until(b'Password: ')

tel.write(b'password\n')


tel.write(b'ls\n')

tel.write(b'exit\n')

tel.read_all()

tel.close()

from ftplib import FTP
con = FTP('ftp.miservidor.com')

con.login('usuario', 'password')

con.retrlines('LIST')

fich = open('prueba.json', 'rb')
con.storbinary('STOR test.json', fich)

fich.close()

fich = open('miprueba.json', 'wb')
con.retrbinary('RETR test.json', fich.write)

fich.close()

con.sendcmd('TYPE i')

con.size('myfile.txt')

con.quit()

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/mywebservice',)

servidor = SimpleXMLRPCServer(("localhost", 8080), requestHandler=RequestHandler)

def say_bye(name):
    return("Bye, bye {0}".format(name))

servidor.register_function(say_bye)

class MySer:
    def say_hello(self):
        return 'Hola Mundo!'

servidor.register_instance(MySer())

servidor.register_introspection_functions()

servidor.serve_forever()

from xmlrpc.client import ServerProxy
url = 'http://localhost:8080/mywebservice'
cli = ServerProxy(url)

cli.system.listMethods()

cli.say_hello()
cli.say_bye('Lucas')

from poplib import POP3
servidor = POP3('miservidor.com')

servidor.user('nombre_de_usuario')
servidor.pass_('password_de_usuario')

num = len(servidor.list()[1])
"El usuario tiene {0} mensajes".format(num)

i = 0
for i in range(num):
    for mensaje in servidor.retr(i+1)[1]:
        print(mensaje)

servidor.quit()

from poplib import POP3_SSL
ser = POP3_SSL('pop.gmail.com', 995)
ser.set_debuglevel(2)
ser.user('arturofernandezm@gmail.com')

ser.quit()

from smtplib import SMTP
servidor.SMTP('miservidor.com')

servidor.login('usuario', 'password')

email_from = 'miusuario@miservidor.com'
email_to = 'destinatario@miservidor.com'
email_body =  'Mensaje de prueba'
servidor.sendmail(email_from, email_to, email_body)

servidor.quit()

from imaplib import IMAP4
con = IMAP4()

con.login('usuario', 'password')

con.select()

tipo, datos = con.search(None, 'ALL')

tip, data = con.search(None, 'FROM', '"prueba@miservidor.com"')

for mensaje in datos[0].split():
    typ, data = con.fetch(mensaje, '(RFC822)')
    print('Mensaje {0}: {1}'.format(mensaje, data[0][1]))

con.close()
con.logout()


import urllib.request
url = 'http://weather.yahoo.com/spain/madrid/madrid-766273/?unit=c'
pagina = urllib.request.urlopen(url)

contenido = pagina.read()

auth = urllib.request.HTTPBasicAuthHandler()

auth.add_password(user='usuario', passwd='password')

opener = urllib.request.build_opener(auth)
urllib.request.install_opener(opener)
pagina = urllib.request.urlopen('http://localhost/login/')

opener = urllib.request.build_opener()
opener.addheaders([('User-agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8)')])
opener.open(url)

import http.cookiejar
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.open(url)

from lxml.html import fromstring
doc = fromstring(pagina)
ele = doc.find_class('fiveday-temps')
ele[0].text_content()
