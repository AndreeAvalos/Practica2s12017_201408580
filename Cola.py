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

	def queue(self, Dato):
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