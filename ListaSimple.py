__author__ = "AndreeAvalos"

import NodoLista
Lista = NodoLista
import subprocess

class ListaSimple():

	def __init__(self):
		self.dato= None
		self.inicio= None
		self.ultimo = None
		self.tamano=0

	def Vacia(self):
		if self.inicio==None:
			return True

	def insertar(self, dato):
		nuevo = Lista.NodoLista(dato)

		if self.Vacia()==True:
			self.inicio=nuevo
			self.ultimo= nuevo
			self.ultimo.setEnlace(self.inicio)

		else:
			self.ultimo.setEnlace(nuevo)
			nuevo.setEnlace(self.inicio)
			self.ultimo=nuevo

		self.tamano=self.tamano+1


	def buscar(self,objeto):
		Actual=self.inicio
		contador=0
		if self.Vacia()==True:
			return "No Hay Elementos"
		else:
			while Actual!=self.ultimo:
				if Actual.getDato()==objeto:
					return "El dato se encontro en el indice: "+ str(contador)

				Actual=Actual.getEnlace()
				contador=contador+1
			if Actual.getDato()==objeto:
				return "El dato se encontro en el indice: "+ str(contador)

			return "Dato no encontrado"


	def eliminar(self,posicion):

		indice = int(posicion)

		if indice == 0:

			if self.inicio!=None:
				
				self.inicio = self.inicio.getEnlace()

			else:
				self.inicio=None


		elif indice > 0:
			if indice<self.tamano-1:
				if self.inicio!=None:
					print "entr3o"
					Actual = self.inicio
					final = indice-1
					for i in range(0,final):
						if Actual.getEnlace()!= self.ultimo:

							Actual=Actual.getEnlace()
						else:

							Actual=None

					if Actual.getEnlace() != None:
						Actual.setEnlace(Actual.getEnlace().getEnlace())
			elif indice==self.tamano-1:

				Actual=self.inicio
				while Actual.getEnlace()!=self.ultimo:
					Actual= Actual.getEnlace()
				print Actual.getEnlace().getDato()
				Actual.setEnlace(None)
				print Actual.getDato()
				print Actual.getEnlace()
				self.ultimo=Actual
				self.tamano=self.tamano-1




#Metodo al cual llamaremos para poder graficar con grapvhiz
	def GenerarGrafico(self):
	#Generamos y Abrimos el archivo de texto
		f=open("C:\graficas\Lista.txt","w")
		f.write("digraph ListaSimple{ \n")
	#Declaramos una variable auxiliar y la apuntamos al inicio
		Actual =self.inicio
		f.write(str(Actual.dato))
	#Recorremos los nodos en busca de llegar hasta el ultimo
		while Actual!=self.ultimo:
	#Si nuestra variable auxiliar es igual al inicio entonces imprime el primer nodo 
			if Actual==self.inicio:
				Actual
			else:
	#De lo contrario qu siga imprimiendo nodos
				f.write("->"+str(Actual.dato))
	#Hacemos que el nodo sea el siguiente
			Actual=Actual.getEnlace()
	#Al terminar el ciclo si el nodo actual es igual al ultimo que lo escriba
		if Actual==self.ultimo and Actual!=self.inicio:
			f.write("->"+str(self.ultimo.dato)+"}")
		else:
			f.write("}")

	#Ejecutamos el comando el subproceso	
		subprocess.Popen("dot -Tpng C:\graficas\Lista.txt -o C:\graficas\Lista.png")	