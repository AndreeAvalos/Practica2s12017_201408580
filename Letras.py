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
		
		if self.vacio()==True:
			self.primero=nuevo
			self.ultimo= nuevo
			
		else:

			 letraInsertar = insertar[:1]
			 letraInsertar= ord(letraInsertar)

			 agregado=False	
			 Auxiliar= self.primero

			 while Auxiliar!= None:
			 	letracomparar = Auxiliar.getValor()[:1]
			 	letracomparar=ord(letracomparar)

			 	if letraInsertar>letracomparar:
			 		Auxiliar=Auxiliar.getAbajo()
			 	else:
			 		if Auxiliar==self.primero:
			 			nuevo.setAbajo(Auxiliar)
			 			Auxiliar.setArriba(nuevo)
			 			self.primero=nuevo
			 			agregado=True
			 			break
			 		else:

			 			nuevo.setArriba(Auxiliar.getArriba())
			 			Auxiliar.getArriba().setAbajo(nuevo)

			 			nuevo.setAbajo(Auxiliar)
			 			Auxiliar.setArriba(nuevo)
			 			agregado=True
			 			break
			 if agregado==False:
			 	self.ultimo.setAbajo(nuevo)
			 	nuevo.setArriba(self.ultimo)
				self.ultimo=nuevo

		self.tamano=self.tamano+1

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
	def eliminar(self,dato):
		if self.vacio()==False:
			nodoaux = self.primero

			while nodoaux!=None:
				if nodoaux.getValor()==dato:
					if nodoaux==self.primero:
						if nodoaux.getAbajo()!=None:
							self.primero=nodoaux.getAbajo()
							nodoaux.getAbajo().setArriba(None)
							self.tamano=self.tamano-1

							
						else:
							self.primero=(None)
							self.ultimo=(None)
							self.tamano=0


						break
					elif nodoaux== self.getUltimo():
						if nodoaux.getArriba()!=None:
						 	self.ultimo=nodoaux.getArriba()
						 	nodoaux.getArriba().setAbajo(None)
						 	self.tamano=self.tamano -1 

						else:
							self.primero=(None)
							self.ultimo=(None)
							self.tamano=0

						break
					else:
						nodoaux.getArriba().setAbajo(nodoaux.getAbajo())
						nodoaux.getAbajo().setArriba(nodoaux.getArriba())
						self.tamano=self.tamano-1


						break
				else:
					nodoaux=nodoaux.getAbajo()
