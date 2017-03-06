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
	#Metodo para insertar
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

					Listanombres=LN.Nombres()

					Listanombres.insertar(objeto)

					nodo=nm.NodoMatriz(Listanombres,letra,dominio)
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
							nodoaux2=nodoaux2.getSiguiente()

						nodo.setAnterior(nodoaux2)
						nodoaux2.setSiguiente(nodo)



					self.tamano=self.tamano+1


			elif self.listadominio.buscar(dominio)==None and self.listaletra.buscar(letra)!=None:

				self.listadominio.insertar(dominio)

				nodoauxL= self.listaletra.buscar(letra)

				Listanombres=LN.Nombres()

				Listanombres.insertar(objeto)

				nodo=nm.NodoMatriz(Listanombres,letra,dominio)
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
						nodoaux2=nodoaux2.getSiguiente()
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

				Listanombres=LN.Nombres()

				Listanombres.insertar(objeto)

				nodo=nm.NodoMatriz(Listanombres,letra,dominio)

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

				Listanombres=LN.Nombres()

				Listanombres.insertar(objeto)

				nodo=nm.NodoMatriz(Listanombres,letra,dominio)
		


				auxLista.setSiguiente(nodo)
				auxDominio.setAbajo(nodo)

				nodo.setArriba(auxDominio)
				nodo.setAnterior(auxLista)
				self.tamano=self.tamano+1
	#Metodo para construir el archivo txt y graficar en graphviz 
	def ConstruirTXT(self):
		#Creamos un archivo con nombre matriz
		f=open("C:\graficas\Matriz.txt","w")
		#Escribimos sobre el archivo el inicio de sentencia 
		f.write("digraph Matriz{ bgcolor=gray \n")
		f.write("node [fontcolor=\"white\", height=0.5, color=\"white\"]\n")
		f.write("[shape=tripleoctagon, style=filled, color=blue]")
		f.write("rankdir=LR \n")
		f.write("edge  [color=\"black\", dir=fordware]\n")
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
			f.write("\""+Actual.getValor()+"\""+"[style =\"filled\"; label=\""+Actual.getValor()+"\";pos= \""+str(contador)+",0!\"]\n")
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
		#Creamos un archivo con nombre matriz
		derecha=self.listadominio.getPrimero()
		actual=derecha
		#Instancia auxiliar para guardar posicion de letra
		while derecha!= None:
		#instanciamos abajo como primer valor para recorrer	
			abajo= self.listaletra.getPrimero()
			while abajo!=None:
				#si el valor de abajo es diferente de nulo  agrega la linea 
				if actual.getAbajo()!=None:
					actual=actual.getAbajo()
					#Escribimos el valor del nodo 
					f.write(actual.getValor().getPrimero().getValor()+"[shape=doubleoctagon,style =\"filled\"; label="+actual.getValor().getPrimero().getValor()+";pos= \""+str(self.posX(actual.getDominio()))+","+str(self.posY(actual.getLetra()))+"!\"]\n")
					self.imprimirPrimeros(actual.getValor(),f,actual.getLetra(),actual.getDominio())
				abajo=abajo.getAbajo()

			derecha=derecha.getSiguiente()
			actual=derecha

		'''--------------------------------Enlazar Cabeceras hacia derecha ----------------------------'''
		derecha=self.listadominio.getPrimero()
		abajo= self.listaletra.getPrimero()
		f.write("\n inicial->"+"\""+derecha.getValor()+"\""+"->inicial->"+abajo.getValor()+"->inicial;\n")

		first=True
		Actual=derecha
		while derecha!=None:

			if first==True:
				f.write(str("\""+Actual.getValor())+"\"")
				first=False
			else:
				f.write("->"+"\""+Actual.getValor()+"\"")

			contador=contador+1
			derecha=derecha.getSiguiente()
			Actual=derecha
		f.write(";")

		'''--------------------------------Enlazar cabeceras hacia izquierda----------------------------'''
		izquierda=self.listadominio.getUltimo()

		last=True
		Actual=izquierda

		while izquierda!=None:
			
			if last==True:
				f.write(str("\""+Actual.getValor())+"\"")
				last=False
				
			else:
				f.write("->"+"\""+Actual.getValor()+"\"")

			izquierda=izquierda.getAnterior()
			Actual=izquierda

		f.write(";\n")
		'''--------------------------------Enlazar laterales hacia abajo ----------------------------'''
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

		'''--------------------------------Enlazar laterales hacia arriba ----------------------------'''

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
			f.write("\""+derecha.getValor()+"\"")

			while abajo!=None:
				#ponemos una condicion si actual diferente de nulo recorrera hacia abajo 
				if actual.getAbajo()!=None:
					#derecha, luego hacia abajo
					actual=actual.getAbajo()
					#enlazar el valor en el archivo del valor actual con el de abajo 
					f.write("->"+actual.getValor().getPrimero().getValor())
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
					f.write("->"+actual.getValor().getPrimero().getValor())
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
				f.write(aux.getValor().getPrimero().getValor()+"->")
				aux=aux.getArriba()
			
			f.write( "\""+derecha.getValor()+"\"")
			f.write(";\n")
			derecha=derecha.getSiguiente()
			aux=derecha

		abajo=self.listaletra.getPrimero()
		aux=abajo

		while abajo!=None:
			

			while aux.getSiguiente()!=None:
				aux=aux.getSiguiente()
			while aux.getAnterior()!=None:
				f.write(aux.getValor().getPrimero().getValor()+"->")
				aux=aux.getAnterior()
			
			f.write(abajo.getValor())
			f.write(";\n")
			abajo=abajo.getAbajo()
			aux=abajo


		f.write("}")
		subprocess.Popen("fdp -Tpng C:\graficas\Matriz.txt -o C:\graficas\Matriz.png")
	#Metodo para obtener el valor en x en la matriz 
	def posX(self,nodo):
		x=1
		derecha=self.listadominio.getPrimero()

		while derecha!=None:
			if derecha.getValor()==nodo:
				return x 
			else:
				x=x+1
				derecha=derecha.getSiguiente()
	#Metodo para obtener el valor en y en la matriz
	def posY(self,nodo):

		y=1
		abajo= self.listaletra.getPrimero()
		while abajo!=None:
			if abajo.getValor()==nodo:
				return y
			else:
				y=y+1
				abajo=abajo.getAbajo()
	#Metodo para comparar la letra y el dominio del nodo 
	def Comparar(self, letra, dominio):
		nodoAux = self.listadominio.buscar(dominio)
		while nodoAux != None:
			if nodoAux.getLetra() == letra:
				return True
			else:
				nodoAux = nodoAux.getAbajo()
		return False
	#Metodo para graficar los nombres de la lista del nodo digase el hijo 
	def imprimirPrimeros(self,lista,f,letra,dominio):
		#Creamos un archivo con nombre matriz
		f=f
		cont2=self.posX(dominio)
		contador=self.posY(letra)
		if lista.getTamano()>1:
			auxiliar= lista.getPrimero()
			while auxiliar.getSiguiente()!=None :
				contador=contador+0.05
				cont2=cont2+0.05
				auxiliar=auxiliar.getSiguiente()
				aux=auxiliar
				f.write("\""+auxiliar.getValor()+"\""+"[shape=octagon, style =\"filled\"; label=\""+auxiliar.getValor()+"\";pos= \""+str(cont2)+","+str(contador)+"!\"]\n")
				
				#print auxiliar.getValor()
			f.write(";\n")

			auxiliar= lista.getPrimero()
			f.write(auxiliar.getValor())
			while auxiliar.getSiguiente()!=None :
				auxiliar=auxiliar.getSiguiente()
				aux=auxiliar

				f.write("->"+auxiliar.getValor())
				#print auxiliar.getValor()
			f.write(";\n")
			f.write(lista.getUltimo().getValor()+"")
			auxiliar= lista.getUltimo()

			while auxiliar.getAnterior()!=None :
				auxiliar=auxiliar.getAnterior()
				f.write("->"+auxiliar.getValor())
				#print auxiliar.getValor()
			f.write(";\n")
	#Metodo para separarCorreo
	def mandarCorreo(self,email):
		objeto=email.split("@")
		nombre = objeto[0]


		dominio=objeto[1]
		letra=nombre[:1]
		self.insertar(letra,dominio,nombre)
	#Metodo para separar correo para eliminar
	def eliminar(self,email):
		objeto=email.split("@")
		nombre = objeto[0]
		dominio=objeto[1]
		letra=nombre[:1]

		self.EliminarCorreo(letra,dominio,nombre)
	#Metodo para eliminar el correo
	def EliminarCorreo(self,letra,dominio,dato):
		auxLetra=self.listaletra.buscar(letra)
		auxDominio=self.listadominio.buscar(dominio)

		if auxLetra!=None and auxDominio!=None:
			aux = auxDominio
			while aux.getAbajo()!= None:
				aux=aux.getAbajo()
				if aux.getLetra()==letra:

					lista = aux.getValor()
					lista.eliminar(dato)

					if lista.getPrimero()==None:


						if self.Dominios(dominio)!=1:
							if aux.getAbajo() !=None:
								aux.getArriba().setAbajo(aux.getAbajo())
								aux.getAbajo().setArriba(aux.getArriba())

							elif aux.getAbajo()==None:
								aux.getArriba().setAbajo(None)

						else :

							self.listadominio.eliminar(dominio)
						if self.Letras(letra)!=1 :
							if aux.getSiguiente() !=None:
								aux.getAnterior().setSiguiente(aux.getSiguiente())
								aux.getSiguiente().setAnterior(aux.getAnterior())
							
							elif aux.getSiguiente()==None:
								aux.getAnterior().setSiguiente(None)

						else :
							self.listaletra.eliminar(letra)


					return True
					
			return False
	#Metodo para recorrer la cabecera de dominios
	def Dominios(self,nodo):
		contador=0
		derecha=self.listadominio.getPrimero()
		actual=derecha

		while derecha!= None:
			if derecha.getValor()==nodo:

				abajo= self.listaletra.getPrimero()
				while abajo!=None and actual.getAbajo()!=None:
					if actual.getAbajo()!=None:
						actual=actual.getAbajo()
					contador=contador+1
					abajo=abajo.getAbajo()
				break
			else:
				derecha=derecha.getSiguiente()
				actual=derecha
		return contador

	#Metodo para recorrer la cabecera de letras
	def Letras(self,nodo):
		contador=0
		abajo=self.listaletra.getPrimero()
		actual=abajo

		while abajo!= None:
			if abajo.getValor()==nodo:
				derecha= self.listaletra.getPrimero()
				while derecha!=None and actual.getSiguiente()!=None:
					if actual.getSiguiente()!=None :
						actual=actual.getSiguiente()
					contador=contador+1
					derecha=derecha.getSiguiente()
				break
			else:
				abajo=abajo.getAbajo()
				actual=abajo
		return contador
	#Metodo para buscar Dominio
	def PorDominio(self,dominio):
		arreglo="Inicio "+dominio + "#"
		derecha=self.listadominio.getPrimero()
		actual=derecha
		while derecha!= None:

			print derecha.getValor()

			if derecha.getValor()==dominio:

				abajo= self.listaletra.getPrimero()

				while abajo!=None and actual.getAbajo()!=None:

					if actual!=None:

						actual=actual.getAbajo()

						if actual.getValor().getPrimero().getSiguiente()!=None:

							auxiliar= actual.getValor().getPrimero()

							while auxiliar!=None :
								arreglo=arreglo+""+auxiliar.getValor()+"#"

								auxiliar=auxiliar.getSiguiente()
						else:		

							arreglo=arreglo+""+actual.getValor().getPrimero().getValor()+"#"
							
					abajo=abajo.getAbajo()

				break

			else:

				derecha=derecha.getSiguiente()

				actual=derecha
		arreglo=arreglo+"Fin "+dominio
		return arreglo
	#Metodo para buscar por Letra
	def PorLetra(self,letra):
		arreglo="Inicio "+letra +"#"

		abajo=self.listaletra.getPrimero()
		actual=abajo

		while abajo!= None:

			if abajo.getValor()==letra:

				derecha= self.listaletra.getPrimero()

				while derecha!=None and actual.getSiguiente()!=None:

					if actual.getSiguiente()!=None :

						
						actual=actual.getSiguiente()

						if actual.getValor().getPrimero().getSiguiente()!=None:

							auxiliar= actual.getValor().getPrimero()

							while auxiliar!=None :
								arreglo=arreglo+""+auxiliar.getValor()+"#"

								auxiliar=auxiliar.getSiguiente()
						else:		

							arreglo=arreglo+""+actual.getValor().getPrimero().getValor()+"#"

					derecha=derecha.getSiguiente()

				break

			else:

				abajo=abajo.getAbajo()

				actual=abajo
		arreglo=arreglo+"Fin "+letra
		return arreglo


	#Fin del programa 