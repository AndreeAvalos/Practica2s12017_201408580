import NodoDominio
nd=NodoDominio



class Dominio(object):
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
		nuevo=nd.NodoDominio(insertar)
		
		if self.vacio()==True:
			self.primero=nuevo
			self.ultimo= nuevo
			
		else:
			self.ultimo.setSiguiente(nuevo)
			self.ultimo=nuevo

		self.tamano=self.tamano+1
		
	

	def buscar(self,valor):
		if self.vacio()==False:
			aux=self.primero
			while aux!=None:
				if aux.getValor()==valor:
					return aux
				aux = aux.getSiguiente()
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