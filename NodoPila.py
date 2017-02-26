class NodoPila(object):
	def __init__(self,dato):
		self.siguiente=None
		self.dato=dato

	def getInicio(self):
		return self.siguiente

	def getDato(self):
		return self.dato