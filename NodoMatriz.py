__author__ = "AndreeAvalos"

class NodoMatriz(object):
	def __init__(self,dato,fila,columna):
		self.fila=fila
		self.columna=columna
		self.dato=dato
		self.sigfila=None
		self.sigcolumna= None

	def getFila(self):
		return self.fila

	def getColumna(self):
		return self.columna

	def getDato(self):
		return self.dato

	def getSigFila(self):
		return self.sigfila

	def getSigColumna(self):
		return self.sigcolumna

	def setFila(self,letra):
		self.fila=fila

	def setColumna(self,dominio):
		self.columna=columna

	def setSigFila(self,nodo):
		self.sigfila=nodo

	def setSigColumna(self,nodo):
		self.sigcolumna=nodo
