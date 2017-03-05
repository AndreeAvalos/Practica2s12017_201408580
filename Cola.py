__author__ = "AndreeAvalos"

import subprocess
import NodoCola
Nodo=NodoCola

class Cola():

	def __init__(self):
		self.raiz=None
		self.ultimo= None
		self.dato=None

	def Vacia(self):
		if self.raiz==None:
			return True

	def queque(self, Dato):
		Actual=Nodo.NodoCola(Dato)

		if self.Vacia()==True:
			self.raiz = Actual
			self.ultimo=Actual
		else:
			self.ultimo.ultimo=Actual
			self.ultimo=Actual

	def dequeque(self):

			self.dato = 0
			self.dato = self.raiz.dato
			if self.raiz==self.ultimo:
				self.raiz=self.ultimo=None
			else:
				self.raiz=self.raiz.ultimo

			return self.dato


	def imprimir(self):
		aux=self.raiz
		while aux!=None:
			print aux.dato
			aux=aux.ultimo

#Metodo al cual llamaremos para poder graficar con grapvhiz
	def GenerarGrafico(self):
	#Generamos y Abrimos el archivo de texto
		f=open("C:\graficas\Cola.txt","w")
		f.write("digraph Cola{ \n")
	#Creamos una variable auxiliar 
		aux=self.raiz
	#Recorremos la cola
		while aux!=None:
			if aux==self.raiz:
				f.write(str(aux.dato))
			else:
	#Escribimos el nodo en el archivo
				f.write("->"+str(aux.dato))
	#Pasamos al siguiente nodo
			aux=aux.ultimo
	#Imprimimos el final de accion 
		f.write("}")
	#Ejecutamos el comando
		subprocess.Popen("dot -Tpng C:\graficas\Cola.txt -o C:\graficas\Cola.png")	