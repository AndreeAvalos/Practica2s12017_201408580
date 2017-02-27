__author__ = "AndreeAvalos"

import subprocess
import	NodoPila
Nodo= NodoPila

class Pila():

	def __init__(self):
		self.inicio=None
		self.dato=None

	def Vacia(self):
		if self.inicio==None:
			return True

	def push(self, valor):
		nuevo=Nodo.NodoPila(valor)
		if self.Vacia()==True:
			nuevo.siguiente=None
			self.inicio=nuevo
		else:
			nuevo.siguiente=self.inicio
			self.inicio=nuevo

	def imprimir(self):
		actual=self.inicio
		while actual!= None:
			print actual.dato
			actual= actual.siguiente

	def pop(self):
		Dato=self.inicio.dato
		self.inicio	= self.inicio.siguiente
		return Dato

#Metodo al cual llamaremos para poder graficar con grapvhiz
	def GenerarGrafico(self):
	#Generamos y Abrimos el archivo de texto
		f=open("C:\graficas\Pila.txt","w")
		f.write("digraph Pila{ \n")
	#Declaramos una variable auxiliar y la apuntamos al inicio
		Actual =self.inicio
	#Recorremos los nodos en busca de llegar hasta el ultimo
		while Actual!=None:
	#Si nuestra variable auxiliar es igual al inicio entonces imprime el primer nodo 
			if Actual==self.inicio:
				f.write(str(Actual.dato))
			else:
	#De lo contrario qu siga imprimiendo nodos
				f.write("->"+str(Actual.dato))
	#Hacemos que el nodo sea el siguiente
			Actual=Actual.siguiente
	#Imprimimos para cerrar
		f.write("}")
	#Ejecutamos el comando el subproceso	
		subprocess.Popen("dot -Tpng C:\graficas\Pila.txt -o C:\graficas\Pila.png")	