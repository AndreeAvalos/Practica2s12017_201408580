__author__="AndreeAvalos"

class NodoMatriz(object):
	def __init__(self, valor = None, letra = None, dominio = None, siguiente = None, anterior = None, arriba = None, abajo = None):
		self.siguiente = siguiente
		self.anterior = anterior
		self.arriba = arriba
		self.abajo = abajo
		self.valor = valor
		self.letra = letra
		self.dominio = dominio

	def getValor(self):
		return self.valor

	def setValor(self, dato):
		self.valor = dato

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self, dato):
		self.siguiente = dato

	def getAnterior(self):
		return self.anterior

	def setAnterior(self, dato):
		self.anterior = dato

	def getArriba(self):
		return self.arriba

	def setArriba(self, dato):
		self.arriba = dato

	def getAbajo(self):
		return self.abajo

	def setAbajo(self, dato):
		self.abajo = dato

	def getLetra(self):
		return self.letra

	def setLetra(self, dato):
		self.letra = dato

	def getDominio(self):
		return self.dominio

	def setDominio(self, dato):
		self.dominio = dato