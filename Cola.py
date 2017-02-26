__author__ = "AndreeAvalos"

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

	def insertar(self, Dato):
		Actual=Nodo.NodoCola(Dato)

		if self.Vacia()==True:
			self.raiz = Actual
			self.ultimo=Actual
		else:
			self.ultimo.ultimo=Actual
			self.ultimo=Actual

	def imprimir(self):
		aux=self.raiz
		while aux!=None:
			print aux.dato
			aux=aux.ultimo