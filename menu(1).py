import pygame
import os, sys
import time

from pygame.locals import *

import random
pygame.init()

#imagenes
pez=pygame.image.load("imagenes/pez.png")
frutilla=pygame.image.load("imagenes/frutilla.png")
guitarra=pygame.image.load("imagenes/guitarra.png")
banana=pygame.image.load("imagenes/banana.png")
manzana=pygame.image.load("imagenes/manzana.png")
leon=pygame.image.load("imagenes/leon.png")
arbol=pygame.image.load("imagenes/arbol.png")
argentina=pygame.image.load("imagenes/argentina.png")
auto=pygame.image.load("imagenes/auto.png")
avion=pygame.image.load("imagenes/avion.png")
barco=pygame.image.load("imagenes/barco.png")
bateria=pygame.image.load("imagenes/bateria.png")
bici=pygame.image.load("imagenes/bici.png")
burro=pygame.image.load("imagenes/burro.png")
cama=pygame.image.load("imagenes/cama.png")
computadora=pygame.image.load("imagenes/computadora.png")
elefante=pygame.image.load("imagenes/elefante.png")
flor=pygame.image.load("imagenes/flor.png")
gato=pygame.image.load("imagenes/gato.png")
hamburguesa=pygame.image.load("imagenes/hamburguesa.png")
helado=pygame.image.load("imagenes/helado.png")
huevos=pygame.image.load("imagenes/huevos.png")
luna=pygame.image.load("imagenes/luna.png")
pajaro=pygame.image.load("imagenes/pajaro.png")
perro=pygame.image.load("imagenes/perro.png")
pinguino=pygame.image.load("imagenes/pinguino.png")
rana=pygame.image.load("imagenes/rana.png")
sombrero=pygame.image.load("imagenes/sombrero.png")
taza=pygame.image.load("imagenes/taza.png")
vaca=pygame.image.load("imagenes/vaca.png")

#lista vacia para llenar mientras escribe el usuario
textousuario=[]

#variables de nivel, puntaje y tiempo
nivel = 1
puntaje = 0
tecla = ""
elejida = 0
elejida1 = 0
palabrausuario = ""
palabraactual = ""
fin = 0
tiempo = 0
puntajenivel = 0

#lista con las imagenes
lista_de_imagenes= [pez,frutilla,guitarra,banana,manzana,leon,arbol,auto,avion,barco,bateria,bici,burro,cama,computadora,elefante,flor,gato,hamburguesa,helado,huevos,luna,pajaro,perro,pinguino,rana,sombrero,taza,vaca]
lista_de_palabras= ["pez","frutilla","guitarra","banana","manzana","leon","arbol","auto","avion","barco","bateria","bici","burro","cama","computadora","elefante","flor","gato","hamburguesa","helado","huevos","luna","pajaro","perro","pinguino","rana","sombrero","taza","vaca"]
#agregamos un contador de imagenes mostradas
imagenes_mostradas=0
#elije una imagen al azar e incrementa el contador

#defino la funcion para eventos que sera llamada mientras cae la imagen
#tambien hara que cuando se pulse una tecla esta la imprima en la pantalla
def funcioneventos():
	global palabrausuario
	global palabraactual
	global x
	global fin
	global puntajenivel
	global puntaje
		
	eventos=pygame.event.get()
	for evento in eventos:
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		elif evento.type == KEYDOWN:
			#asigna la variable de la tecla pulsada
			tecla= evento.key
			#verifico que si no se pulsa enter Y que la tecla este entre los caracteres imprimibles
			if tecla != K_RETURN and tecla >= 32 and tecla <= 126:
				print (chr(tecla))
				palabrausuario = palabrausuario +chr(tecla)
				palabrausuario = palabrausuario.lower()
			elif tecla == K_RETURN:
				print (123)
				print (palabraactual)
				print (palabrausuario)
				fin=comparar()
				if palabraactual == palabrausuario:
					print (1234)
					puntaje = puntaje + puntajenivel
					return 301
							
			elif tecla == K_BACKSPACE and len(palabrausuario)>0:
				palabrausuario=palabrausuario[0:len(palabrausuario)-1]
			
	return 0		
#funcion que imprime un texto segun el puntaje
def	ganar():
		if palabraactual == palabrausuario:
				texganaste= fuente.render("ganaste", True, (255,255,255))
				puntajesumado=" + "+str(puntajenivel)
				texganapuntos=fuente.render(str(puntajesumado), True, (255,255,255))
				ventana.blit(texganaste,(600,300))	
				ventana.blit(texganapuntos,(600,350))
				pygame.display.update()
				pygame.time.delay(1500)	
		
def comparar():
	global palabraactual
	global palabrausuario
	eventos=pygame.event.get()
	for evento in eventos:
		if evento.type == KEYDOWN:
			if evento.key == K_RETURN:
				if palabraactual == palabrausuario:
					return 400
	return 0
			
def puntajefinal():
	ventana.blit(ventananegra,(0,0))
	final1=fuente.render("el juego ha terminado!", True, (255,255,255))
	texpuntajefinal=fuente.render("tu puntaje final es: "+str(puntaje)+" puntos!",True,(255,255,255))
	ventana.blit(final1,(200,200))
	pygame.display.update()
	pygame.time.delay(1000)
	ventana.blit(texpuntajefinal,(200,250))
	pygame.display.update()
	pygame.time.delay(3000)
	return 
	
def calculotiempo(tiempo):
	#1 seg = 30 frames aprox
	if tiempo < 30:
		tiempo2=10
		return tiempo2
	elif tiempo >= 30 and tiempo<60:
		tiempo2=9
		return tiempo2
	elif tiempo >= 60 and tiempo<90:
		tiempo2=8
		return tiempo2
	elif tiempo >= 90 and tiempo<120:
		tiempo2 = 7
		return tiempo2
	elif tiempo >= 120 and tiempo<150:
		tiempo2 = 6
		return tiempo2
	elif tiempo >= 150 and tiempo<180:
		tiempo2 = 5
		return tiempo2
	elif tiempo >= 180 and tiempo<210:
		tiempo2 = 4
		return tiempo2
	elif tiempo >= 210 and tiempo<240:
		tiempo2 = 3
		return tiempo2
	elif tiempo >= 240 and tiempo<270:
		tiempo2 = 2
		return tiempo2
	elif tiempo >= 270 and tiempo<300:
		tiempo2 = 1
		return tiempo2
	elif tiempo >= 300:
		tiempo2 = 0
		return tiempo2	

def eligeimagen():	
	elegida=random.choice(range (len(lista_de_imagenes)))
	return elegida
	
def caidaimagen():
	global palabrausuario
	global palabraactual
	global puntaje
	global lista_de_imagenes
	global lista_de_palabras
	global fin
	global puntajenivel
	puntaje = 0
	lista_de_imagenes= [pez,frutilla,guitarra,banana,manzana,leon,arbol,auto,avion,barco,bateria,bici,burro,cama,computadora,elefante,flor,gato,hamburguesa,helado,huevos,luna,pajaro,perro,pinguino,rana,sombrero,taza,vaca]
	lista_de_palabras= ["pez","frutilla","guitarra","banana","manzana","leon","arbol","auto","avion","barco","bateria","bici","burro","cama","computadora","elefante","flor","gato","hamburguesa","helado","huevos","luna","pajaro","perro","pinguino","rana","sombrero","taza","vaca"]

	imagenes_mostradas=1
	while imagenes_mostradas < 6:
		palabrausuario = ""
		tiempo = 0
		
		#ventana.blit(textoingresado, (10,500))
		elejida1=eligeimagen()
		foto = lista_de_imagenes[elejida1]
		palabraactual = lista_de_palabras[elejida1]
		tiempo2=0
		x=0
		#este seria el ciclo donde cae la imagen, y se escribe la palabra
		#for x in range(0,300,1):
		while x <=300:
						
			#hago que renderize continuamente usando la funcion de calculotiempo
			texnivel=fuentepeque.render(str(imagenes_mostradas), True, (255,255,255))
			textiempo=fuentepeque.render(str(calculotiempo(tiempo)), True, (255,255,255))
			texpuntos=fuentepeque.render(str(puntaje), True, (255,255,255))
			palabra=fuente.render(str(palabrausuario), True, (255,255,255))
			#pego el texto con el tiempo restante
			ventana.blit(texnivel,(700,150))
			ventana.blit(textiempo,(700,100))
			ventana.blit(texpuntos,(710,50))
			ventana.blit(palabra,(30,530))
			ventana.blit(foto,(200,x))
			#variable que otorga el puntaje segun el tiempo restante
			puntajenivel = calculotiempo(tiempo)
			pygame.display.update()
			#pantalla base
			ventana.blit(copiavent,(0,0))
			tiempo = tiempo + 1
			pygame.time.delay(30)
			print (palabraactual)
			x = x + 1 + int(funcioneventos())
		ganar()	
		lista_de_imagenes.remove(foto)
		lista_de_palabras.remove(palabraactual)
		#imprimo el texto ingresado por el usuario(por ahora en consola pero para tener una referencia que funciona :D
		imagenes_mostradas=imagenes_mostradas+1
	puntajefinal()


def menu():
	instrucciones1=fuente.render("escribi el nombre del objeto ", True, (255,255,255))
	instrucciones2=fuente.render("antes de que acabe el tiempo", True, (255,255,255))
	opcion1=fuente.render("presione enter para jugar", True, (255,255,255))
	opcion2=fuente.render("presione esc para salir", True, (255,255,255))
	ventana.blit(opcion1, (150,200))
	ventana.blit(opcion2, (150,250))
	ventana.blit(instrucciones1,(150,100))
	ventana.blit(instrucciones2,(150,150))
	pygame.display.update()
	while True:
		#bucle principal que detecta eventos frame por frame
		eventos=pygame.event.get()
		for evento in eventos:
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type==KEYDOWN:
				if evento.key == K_RETURN:
					caidaimagen()
					ventana.blit(ventananegra,(0,0))
					ventana.blit(opcion1, (150,200))
					ventana.blit(opcion2, (150,250))
					ventana.blit(instrucciones1,(150,100))
					ventana.blit(instrucciones2,(150,150))
					pygame.display.update()
				if evento.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				
def render(texto,booleano,color):
    fuentepeque.render(str(texto),booleano,color)


#aca iria el codigo que ejecuta el juego principal, despues se ve eso




pygame.init()

#seteamos resolucion de pantalla
ventana=pygame.display.set_mode((800, 600))
pygame.display.set_caption("adivina imagen")

#copio pantalla del menu (arriba de esto iria el fondo de pantalla del menu principal)
ventananegra = ventana.copy()

#declaro fuente un poco mas pequenia
fuentepeque=pygame.font.SysFont("Arial",25)

#dibujo la estructura del juego principal
pygame.draw.polygon(ventana, (255,255,255), ((0,500), (600,500), (600,0),(0,0)), 5)
#texpuntaje=fuentepeque.render("puntaje:", True, (255,255,255))
texpuntaje=render("puntaje",True,(255,255,255))
textiempo=fuentepeque.render("tiempo:", True, (255,255,255))
texnivel=fuentepeque.render("nivel:", True, (255,255,255))
#texpuntos = puntaje
texpuntos=fuentepeque.render(str(puntaje), True, (255,255,255))
ventana.blit(texpuntos,(660,50))
ventana.blit(texpuntaje,(620,50))
ventana.blit(textiempo,(620,100))
ventana.blit(texnivel,(620,150))

#se declara la fuente para usar en todo el juego
fuente=pygame.font.SysFont("Arial",48)

#texto de prueba (despues se saca, es para medir coordenadas)
#textoingresado=fuente.render("aqui iria la palabra ingresada por el usuario", True, (255,255,255))
#ventana.blit(textoingresado,(10,530))

#copio la pantalla de fondo
copiavent = ventana.copy()

#se pega la ventana del menu principal (por ahora todo negro)
ventana.blit(ventananegra,(0,0))

menu()
