__author__ = "AndreeAvalos"


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

