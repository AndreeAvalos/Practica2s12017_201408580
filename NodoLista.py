__author__ = "AndreeAvalos"


class NodoLista(object):
	def __init__(self,dato):
		self.dato=dato
		self.enlace=None
	
	def getDato(self):
		return self.dato

	def getEnlace(self):
		return self.enlace

	def setEnlace(self,nodo):
		self.enlace=nodo

	def setDato(self,objeto):
		self.dato=objeto

	