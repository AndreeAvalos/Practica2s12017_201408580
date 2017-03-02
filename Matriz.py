__author__ = "AndreeAvalos"
import NodoMatriz
nm=NodoMatriz
import Letras
Ls=Letras
import Dominios
DM=Dominios

class Matriz(object):
	def __init__(self):
		self.listaletra=None
		self.listadominio = None
		self.tamano = 0

	def insertar(self,letra,dominio,objeto):
		if self.tamano ==0:
			self.listaletra=Ls.Letras()
			self.listadominio=DM.Dominio()

			nodo=nm.NodoMatriz(objeto)

			self.listadominio.insertar(dominio)
			self.listaletra.insertar(letra)

			auxLista=self.listaletra.buscar(letra)
			auxDominio=self.listadominio.buscar(dominio)

			

			auxLista.setSiguiente(nodo)
			auxDominio.setAbajo(nodo)

			nodo.setArriba(auxDominio)
			nodo.setAnterior(auxLista)

			self.tamano=self.tamano+1

		else:
			if self.listaletra.buscar(letra)!=None and self.listadominio.buscar(dominio)!=None:

				aux1= self.listaletra.buscar(letra)
				aux2=self.listadominio.buscar(dominio)

				nodo= nm.NodoMatriz(objeto)

				aux1.setSiguiente(nodo)
				aux2.setAbajo(nodo)

				nodo.setArriba(aux2)
				nodo.setAnterior(aux1)

				self.tamano=self.tamano+1


			elif self.listadominio.buscar(dominio)==None and self.listaletra.buscar(letra)!=None:

				self.listadominio.insertar(dominio)

				auxLista= self.listaletra.buscar(letra)

				while auxLista.getSiguiente()!=None:
					auxLista=auxLista.getSiguiente()
				auxDominio=self.listadominio.buscar(dominio)

				nodo= nm.NodoMatriz(objeto)

				auxLista.setSiguiente(nodo)
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)
				nodo.setAnterior(auxLista)

				self.tamano=self.tamano+1


			elif self.listadominio.buscar(dominio)!=None and self.listaletra.buscar(letra)==None:

				self.listaletra.insertar(letra)

				auxLetra= self.listaletra.buscar(letra)

				auxDominio=self.listadominio.buscar(dominio)

				while auxDominio.getAbajo()!=None:
					auxDominio=auxDominio.getAbajo()


				nodo= nm.NodoMatriz(objeto)

				auxLetra.setSiguiente(nodo)
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)
				nodo.setAnterior(auxLetra)

				self.tamano=self.tamano+1

			elif self.listadominio.buscar(dominio)==None and self.listaletra.buscar(letra)==None:

				self.listadominio.insertar(dominio)
				self.listaletra.insertar(letra)

				auxLista=self.listaletra.buscar(letra)
				auxDominio=self.listadominio.buscar(dominio)


				nodo=nm.NodoMatriz(objeto)

				auxLista.setSiguiente(nodo)
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)
				nodo.setAnterior(auxLista)
				self.tamano=self.tamano+1

	def imprimir(self):
		derecha=self.listadominio.getPrimero()
		actual=derecha

		while derecha!= None:
			abajo= self.listaletra.getPrimero()

			while abajo!=None:
				if actual !=None:
					print actual.getValor()
					actual=actual.getAbajo()
				abajo=abajo.getAbajo()
			print"\nsiguiente dominio\n"
			derecha=derecha.getSiguiente()
			actual=derecha
