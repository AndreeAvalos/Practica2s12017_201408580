__author__ = "AndreeAvalos"
import NodoMatriz
nm=NodoMatriz
import Letras
Ls=Letras
import Dominios
DM=Dominios
import ListaNombres
LN=ListaNombres
import subprocess

class Matriz(object):
	def __init__(self):
		self.listaletra=None
		self.listadominio = None
		self.listanombres= None
		self.tamano = 0

	def insertar(self,letra,dominio,objeto):
		if self.tamano ==0:
			self.listaletra=Ls.Letras()
			self.listadominio=DM.Dominio()
			Listanombres=LN.Nombres()

			Listanombres.insertar(objeto)

			nodo=nm.NodoMatriz(Listanombres,letra,dominio)

			self.listadominio.insertar(dominio)
			self.listaletra.insertar(letra)

			auxLetra=self.listaletra.buscar(letra)
			auxDominio=self.listadominio.buscar(dominio)

			

			auxLetra.setSiguiente(nodo)
			auxDominio.setAbajo(nodo)

			nodo.setArriba(auxDominio)
			nodo.setAnterior(auxLetra)

			self.tamano=self.tamano+1

		elif self.tamano>0:

			if self.listaletra.buscar(letra)!=None and self.listadominio.buscar(dominio)!=None:

				if self.Comparar(letra,dominio)==True:

					nodoauxD= self.listadominio.buscar(dominio)
					nodoaux =nodoauxD

					while nodoaux!=None:

						if nodoaux.getLetra()==letra:
							nodoauxD=nodoaux
							nodoaux=nodoaux.getAbajo()
						else:
							nodoaux=nodoaux.getAbajo()

					
					listanombres=nodoauxD.getValor()
					listanombres.insertar(objeto)


				else:
					nodoauxD= self.listadominio.buscar(dominio)
					nodoaux = nodoauxD.getAbajo()

					nodo=nm.NodoMatriz(objeto,letra,dominio)
					letrainsertar=letra[:1]
					letrainsertar=ord(letrainsertar)

					agregado = False
					while nodoaux !=None:
						print nodoaux.getLetra()
						letracomparar= nodoaux.getLetra()[:1]
						letracomparar=ord(letracomparar)
						if letrainsertar>letracomparar:
							nodoaux=nodoaux.getAbajo()
						else:
							nodo.setAbajo(nodoaux)
							nodo.setArriba(nodoaux.getArriba())
							nodoaux.getArriba().setAbajo(nodo)
							nodoaux.setArriba(nodo)
							agregado=True
							break
					if agregado==False:
						nodoaux= nodoauxD.getAbajo()
						while nodoaux.getAbajo()!=None:
							nodoaux=nodoaux.getAbajo()

						nodo.setArriba(nodoaux)
						nodoaux.setAbajo(nodo)

					nodoauxL= self.listaletra.buscar(letra)
					nodoaux2= nodoauxL.getSiguiente()

					letrainsertar=dominio[:1]
					letrainsertar=ord(letrainsertar)

					agregado=False
					while nodoaux2!=None:
						letracomparar=nodoaux2.getDominio()[:1]
						letracomparar=ord(letracomparar)

						if letrainsertar>letracomparar:
							nodoaux2=nodoaux2.getSiguiente()
						else:
							nodo.setSiguiente(nodoaux2)
							nodo.setAnterior(nodoaux2.getAnterior())
							nodoaux2.getAnterior().setSiguiente(nodo)
							nodoaux2.setAnterior(nodo)
							agregado=True
							break 
					if agregado ==False:
						nodoaux2=nodoauxL.getSiguiente()
						while nodoaux2.getSiguiente()!=None:
							nodoaux2=nodoaux2.setSiguiente()

						nodo.setAnterior(nodoaux2)
						nodoaux2.setSiguiente(nodo)



					self.tamano=self.tamano+1


			elif self.listadominio.buscar(dominio)==None and self.listaletra.buscar(letra)!=None:

				self.listadominio.insertar(dominio)

				nodoauxL= self.listaletra.buscar(letra)
				nodo=nm.NodoMatriz(objeto,letra,dominio)
				nodoaux2= nodoauxL.getSiguiente()

				letrainsertar=dominio[:1]
				letrainsertar=ord(letrainsertar)
				agregado=False

				while nodoaux2!=None:
					letracomparar=nodoaux2.getDominio()[:1]
					letracomparar=ord(letracomparar)

					if letrainsertar>letracomparar:
						nodoaux2=nodoaux2.getSiguiente()
					else:
						nodo.setSiguiente(nodoaux2)
						nodo.setAnterior(nodoaux2.getAnterior())
						nodoaux2.getAnterior().setSiguiente(nodo)
						nodoaux2.setAnterior(nodo)
						agregado=True
						break 

				if agregado ==False:
					nodoaux2=nodoauxL.getSiguiente()
					while nodoaux2.getSiguiente()!=None:
						nodoaux2=nodoaux2.setSiguiente()
					nodo.setAnterior(nodoaux2)
					nodoaux2.setSiguiente(nodo)

				auxDominio=self.listadominio.buscar(dominio)
				
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)

				self.tamano=self.tamano+1



			elif self.listadominio.buscar(dominio)!=None and self.listaletra.buscar(letra)==None:

				self.listaletra.insertar(letra)

				nodoauxD=self.listadominio.buscar(dominio)
				nodoaux=nodoauxD.getAbajo()

				nodo=nm.NodoMatriz(objeto,letra,dominio)

				letrainsertar=letra[:1]
				letrainsertar=ord(letrainsertar)

				agregado = False
				while nodoaux !=None:

					letracomparar= nodoaux.getLetra()[:1]
					letracomparar=ord(letracomparar)

					if letrainsertar>letracomparar:
						nodoaux=nodoaux.getAbajo()
					else:
						nodo.setAbajo(nodoaux)
						nodo.setArriba(nodoaux.getArriba())
						nodoaux.getArriba().setAbajo(nodo)
						nodoaux.setArriba(nodo)
						agregado=True
						break
				if agregado==False:
					nodoaux= nodoauxD.getAbajo()
					while nodoaux.getAbajo()!=None:
						nodoaux=nodoaux.getAbajo()
					nodo.setArriba(nodoaux)
					nodoaux.setAbajo(nodo)

				auxLetra=self.listaletra.buscar(letra)
				auxLetra.setSiguiente(nodo)

				nodo.setAnterior(auxLetra)

				self.tamano=self.tamano+1

			elif self.listadominio.buscar(dominio)==None and self.listaletra.buscar(letra)==None:

				self.listadominio.insertar(dominio)
				self.listaletra.insertar(letra)

				auxLista=self.listaletra.buscar(letra)
				auxDominio=self.listadominio.buscar(dominio)

				nodo=nm.NodoMatriz(objeto,letra,dominio)
		


				auxLista.setSiguiente(nodo)
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)
				nodo.setAnterior(auxLista)
				self.tamano=self.tamano+1

	def imprimir(self):
		derecha=self.listadominio.getPrimero()
		actual=derecha
		while derecha!= None:
			print"\n====Dominio "+derecha.getValor()+"====\n"
			abajo= self.listaletra.getPrimero()
			while abajo!=None:
				
				actual=actual.getAbajo()
				abajo=abajo.getAbajo()
				print actual.getValor()

			derecha=derecha.getSiguiente()
			actual=derecha

	def ConstruirTXT(self):
		#Creamos un archivo con nombre matriz
		f=open("C:\graficas\Matriz.txt","w")
		#Escribimos sobre el archivo el inicio de sentencia 
		f.write("digraph Matriz{ \n")
		#instanciamos derecha como primer nodo de la cabecera horizontal
		derecha= self.listadominio.getPrimero()
		Actual=derecha
		contador=1
		#Agregamos el apuntador principal
		f.write("inicial[style =\"filled\"; label=\"inicial\";pos= \"0,0!\"] \n")

		'''--------------------------------Obtener Cabeceras ----------------------------'''
		#recorremos hacia la derecha enumerando
		while derecha!=None:
			#Escribimos los dominios con posicion y texto en el archivo
			f.write(Actual.getValor()+"[style =\"filled\"; label="+Actual.getValor()+";pos= \""+str(contador)+",0!\"]\n")
			contador=contador+1
			#Obtenemos el siguiente nodo 
			derecha=derecha.getSiguiente()
			Actual=derecha
		'''--------------------------------Obtener Laterales ----------------------------'''
		contador=1

		#instanciamos abajo como primer nodo en lateral  
		abajo= self.listaletra.getPrimero()
		Actual=abajo

		while abajo!=None:
			#Escribimos las letras con posicion y text en el archivo 
			f.write(Actual.getValor()+"[style =\"filled\"; label="+Actual.getValor()+";pos= \"0,"+str(contador)+"!\"]\n")
			contador=contador+1
			#obtenemos el siguiente nodo 
			abajo=abajo.getAbajo()
			Actual=abajo

		'''--------------------------------Obtener Valores ----------------------------'''
		#Instanciamos el derecha como primer valor 
		derecha=self.listadominio.getPrimero()
		actual=derecha
		#Instancia auxiliar para guardar posicion de letra
		aux=self.listaletra.getPrimero()
		contador=1
		while derecha!= None:
		#instanciamos abajo como primer valor para recorrer	
			abajo= self.listaletra.getPrimero()

			while abajo!=None:
				#si el valor de abajo es diferente de nulo  agrega la linea 
				if actual.getAbajo()!=None and aux!=None:

					actual=actual.getAbajo()

					#print str(self.posX(derecha))+","+str(self.posY(aux))

					#Escribimos el valor del nodo 
					f.write(actual.getValor()+"[style =\"filled\"; label="+actual.getValor().getPrimero().getValor()+";pos= \""+str(self.posX(actual.getValor().getPrimero().getDominio()))+","+str(self.posY(actual.getValor().getPrimero().getLetra()))+"!\"]\n")
					aux=aux.getAbajo()
					contador=contador+1
				abajo=abajo.getAbajo()

			derecha=derecha.getSiguiente()
			aux=self.listaletra.getPrimero()
			actual=derecha

		'''--------------------------------Enlazar Cabeceras hacia derecha ----------------------------'''
		derecha=self.listadominio.getPrimero()
		abajo= self.listaletra.getPrimero()
		f.write("\n inicial->"+derecha.getValor()+"->inicial->"+abajo.getValor()+"->inicial;\n")

		first=True
		Actual=derecha
		while derecha!=None:

			if first==True:
				f.write(str(Actual.getValor()))
				first=False
			else:
				f.write("->"+Actual.getValor())

			contador=contador+1
			derecha=derecha.getSiguiente()
			Actual=derecha
		f.write(";")

		'''--------------------------------Enlazar Laterales hacia abajo----------------------------'''
		izquierda=self.listadominio.getUltimo()

		last=True
		Actual=izquierda

		while izquierda!=None:
			
			if last==True:
				f.write(str(Actual.getValor()))
				last=False
				
			else:
				f.write("->"+Actual.getValor())

			izquierda=izquierda.getAnterior()
			Actual=izquierda

		f.write(";\n")
		'''--------------------------------Enlazar Cabeceras hacia izquierda ----------------------------'''
		first=True
		Actual=abajo
		while abajo!=None:
			if first==True:
				f.write(str(Actual.getValor()))
				first=False
			else:
				f.write("->"+Actual.getValor())
			abajo=abajo.getAbajo()
			Actual=abajo
		f.write(";\n")

		'''--------------------------------Enlazar Cabeceras hacia arriba ----------------------------'''

		last=True
		arriba = self.listaletra.getUltimo()
		Actual=arriba
		while arriba!=None:
			if last == True:
				f.write(str(Actual.getValor()))
				last=False
			else:
				f.write("->"+Actual.getValor())
			arriba=arriba.getArriba()
			Actual=arriba

		f.write(";\n")


		'''--------------------------------Enlazar Valores hacia derecha----------------------------'''
		#instanciamos para estar en la primera posicion de los dominios 
		derecha=self.listadominio.getPrimero()
		#nodo auxiliar el cual recorrera de derecha hacia abajo
		actual=derecha

		while derecha!= None:
			#instanciamos el primero nodo de letras 
			abajo= self.listaletra.getPrimero()
			#escribimos en el archivo el primer valor
			f.write(derecha.getValor())

			while abajo!=None:
				#ponemos una condicion si actual diferente de nulo recorrera hacia abajo 
				if actual.getAbajo()!=None:
					#derecha, luego hacia abajo
					actual=actual.getAbajo()
					#enlazar el valor en el archivo del valor actual con el de abajo 
					f.write("->"+actual.getValor())
				#cambiar de nodo hacia el siguiente 
				abajo=abajo.getAbajo()
			#separacion de nombres con ;
			f.write(";\n")
			#recorremos la posicion del nodo hacia la derecha 
			derecha=derecha.getSiguiente()
			#el nodo auxiliar es igual al de la siguiente posicion 
			actual=derecha

		f.write("\n\n\n")

		'''--------------------------------Enlazar Valores hacia abajo----------------------------'''
		
		abajo=self.listaletra.getPrimero()
		actual=abajo
		while abajo!=None:
			derecha=self.listadominio.getPrimero()
			f.write(abajo.getValor())
			while derecha!=None:
				if actual.getSiguiente()!=None:
					actual=actual.getSiguiente()
					f.write("->"+actual.getValor())
				derecha=derecha.getSiguiente()
			f.write(";\n")
			abajo=abajo.getAbajo()
			actual=abajo


		f.write("\n\n\n")
		
		derecha=self.listadominio.getPrimero()
		aux=derecha

		while derecha!=None:

			while aux.getAbajo()!=None:
				aux=aux.getAbajo()
			while aux.getArriba()!=None:
				f.write(aux.getValor()+"->")
				aux=aux.getArriba()
			
			f.write( derecha.getValor())
			f.write(";\n")
			derecha=derecha.getSiguiente()
			aux=derecha

		abajo=self.listaletra.getPrimero()
		aux=abajo

		while abajo!=None:
			

			while aux.getSiguiente()!=None:
				aux=aux.getSiguiente()
			while aux.getAnterior()!=None:
				f.write(aux.getValor()+"->")
				aux=aux.getAnterior()
			
			f.write( abajo.getValor())
			f.write(";\n")
			abajo=abajo.getAbajo()
			aux=abajo


		f.write("}")
		subprocess.Popen("fdp -Tpng C:\graficas\Matriz.txt -o C:\graficas\Matriz.png")

	def posX(self,nodo):
		x=1
		derecha=self.listadominio.getPrimero()

		while derecha!=None:
			if derecha.getValor()==nodo:
				return x 
			else:
				x=x+1
				derecha=derecha.getSiguiente()

	def posY(self,nodo):

		y=1
		abajo= self.listaletra.getPrimero()
		while abajo!=None:
			if abajo.getValor()==nodo:
				return y
			else:
				y=y+1
				abajo=abajo.getAbajo()


	def Comparar(self, letra, dominio):
		nodoAux = self.listadominio.buscar(dominio)
		while nodoAux != None:
			if nodoAux.getLetra() == letra:
				return True
			else:
				nodoAux = nodoAux.getAbajo()
		return False

	def imprimirnombres(self):
		abajo=self.listaletra.getPrimero().getSiguiente()
		abajo=abajo.getValor().getPrimero()
		while abajo!=None:
			print abajo.getValor().getDominio()
			abajo=abajo.getSiguiente()
