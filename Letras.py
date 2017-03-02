import NodoLetra
nl=NodoLetra

class Letras(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.tamano = 0


	def vacio(self):
		if self.tamano==0:
			return True
		else: 
			return False

	def insertar(self,insertar):
		if self.vacio():
			self.insertarPrimero(insertar)
		else:
			self.insertarotro(insertar)

		self.tamano=self.tamano+1

	def insertarPrimero(self,insertar):
		nuevo=nl.NodoLetra(insertar)
		self.primero=nuevo
		self.ultimo= nuevo
		
	
	def insertarotro(self,insertar):
		nuevo=nl.NodoLetra(insertar)

		self.ultimo.setAbajo(nuevo)
		self.ultimo=nuevo

	def buscar(self,valor):
		if self.vacio()==False:
			aux=self.primero
			while aux!=self.ultimo.getAbajo():
				if aux.getValor()==valor:
					return aux
				aux = aux.getAbajo()
		else:
			return None
	def getPrimero(self):
		return self.primero

	def setPrimero(self,primero):
		self.primero=primero

	def getUltimo(self):
		return self.ultimo

	def setUltmio(self,ultimo):
		return self.ultimo