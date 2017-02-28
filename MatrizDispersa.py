__author__ = "AndreeAvalos"

#Importamos la clase 
import NodoMatriz

nodo=NodoMatriz

class Matriz():
	def __init__(self):
		self.dato=None
		self.nodomatriz=None

	def crear(self,f,c):
		self.nodomatriz= nodo.NodoMatriz(0,0,0)
		self.nodomatriz.setSigFila(self.nodomatriz)
		self.nodomatriz.setSigColumna(self.nodomatriz)
		i=1
		aux=self.nodomatriz

		while i<=f:
			aux2= nodo.NodoMatriz(0,i,0)
			aux.setSigFila(aux2)
			aux2.setSigColumna(aux2)
			aux=aux2
			i=i+1

		aux2.setSigFila(self.nodomatriz)
		i=1
		aux2=self.nodomatriz

		while i<=c:
			nuevo=nodo.NodoMatriz(0,0,i)
			aux2.setSigColumna(nuevo)
			nuevo.setSigFila(nuevo)
			aux2=nuevo
			i=i+1
		aux2.setSigColumna(self.nodomatriz)


	def arriba(self,f,c):
		aux=self.nodomatriz.getSigColumna()
		while aux.getColumna()!=c:
			aux=aux.getSigColumna()

		aux1=aux.getSigFila()
		aux2=aux.getSigColumna()

		while aux1.getFila()<f and aux2.getFila()!=0:
			aux=aux1
			aux1=aux1.getSigFila()
			aux2=aux2.getSigColumna()

		if aux1.getFila()<f:
			return aux1
		else:
			return aux

	def izquierda(self,f,c):
		aux=self.nodomatriz.getSigFila()
		while aux.getFila()!=f:
			aux=aux.getSigFila()

		aux1=aux.getSigColumna()
		aux2=aux.getSigColumna()

		while aux1.getColumna()<c and aux2.getColumna()!=0:
			aux=aux1
			aux1=aux1.getSigColumna()
			aux2=aux2.getSigColumna()

		if aux1.getColumna()<c:
			return aux1
		else:
			return aux

	def add(self,dato,f,c):
		q=self.arriba(f,c)
		p=self.izquierda(f,c)
		nuevo=nodo.NodoMatriz(dato,f,c)
		nuevo.setSigFila(q.getSigFila)
		q.setSigFila(nuevo)
		nuevo.setSigColumna(p.getSigColumna())
		p.setSigColumna(nuevo)

	def imprimir(self):
		nca = 0
		ncc=0
		nt=0
		aux= self.nodomatriz.getSigColumna()

		while aux.getColumna()!=self.nodomatriz.getColumna():
			#print str(aux.getColumna())
			aux = aux.getSigColumna()
		aux=self.nodomatriz.getSigFila()

		while aux.getFila()!=self.nodomatriz.getFila():
			#print str(aux.getFila())+""
			o=aux
			e=aux.getSigColumna()

			while o!=e:
				nc=e.getColumna()
				nt=nc
				nf=e.getFila()
				if nf==nca:
					nc=nc-ncc
				print str(e.getDato())
				e=e.getSigColumna()
				nca=nf
				ncc=nt
			print" "
			aux=aux.getSigFila()