

class NodoLetra(object):
	def __init__(self, valor = None, siguiente = None, anterior = None, arriba = None, abajo = None):
		self.siguiente = siguiente
		self.anterior = anterior
		self.arriba = arriba
		self.abajo = abajo
		self.dato = valor

	def setSiguiente(self, valorAux):
		self.siguiente = valorAux
	def getSiguiente(self):
		return self.siguiente
	def getAnterior(self):
		return self.anterior
	def setAnterior(self, valorAux):
		self.anterior = valorAux

	def setValor(self,dato):
		self.dato=dato
	def setAbajo(self,abajo):
		self.abajo=abajo
	def setArriba(self,arriba):
		self.arriba=arriba

	
	def getAbajo(self):
		return self.abajo
	def getArriba(self):
		return self.arriba
		
	def getValor(self):
		return self.dato

	def getPrimero(self):
		return self.primero

	def setPrimero(self,primero):
		self.primero=primero

	def getUltimo(self):
		return self.ultimo

	def setUltmio(self,ultimo):
		return self.ultimo
