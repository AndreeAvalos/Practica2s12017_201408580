import Matriz 
import ListaSimple
import Cola
import Pila


matriz= Matriz.Matriz()
ls=ListaSimple.ListaSimple()
cola=Cola.Cola()
pila=Pila.Pila()


from flask import Flask, request, Response
app = Flask("Practica2")

#ma.insertar("r","hotmail.com","rodrigo")
#ma.insertar("r","hotmail.com","rosario")
#ma.insertar("r","hotmail.com","rosita")
#ma.insertar("c","mail.com","carlos")
#ma.mandarCorreo("ana@outlook.com")
#ma.mandarCorreo("re@yahoo.com")
#ma.mandarCorreo("beto@outlook.com")
#ma.mandarCorreo("andre@outlook.com")
#ma.mandarCorreo("rai@yahoo.com")
#ma.mandarCorreo("bela@outlook.com")
#ma.mandarCorreo("astrid@gmail.com")
#ma.mandarCorreo("celeste@yahoo.com")
#ma.mandarCorreo("armi@yahoo.com")


#print ma.PorDominio("outlook.com")
#print ma.PorLetra("a")


@app.route('/ListaSimple', methods = ['POST']) 
def lista():
	if str(request.form['tipo'])=="insertar":
		ls.insertar(str(request.form['informacion']))
		ls.GenerarGrafico()

	elif str(request.form['tipo'])=="eliminar":
		indice = int(request.form['informacion'])
		ls.eliminar(indice)
		ls.GenerarGrafico()

	elif str(request.form['tipo'])=="buscar":
		
		return str(ls.buscar(str(request.form['informacion']))) 



@app.route('/Matriz', methods = ['POST']) 
def matriz5():
	if str(request.form['tipo'])=="insertar":
		matriz.mandarCorreo(str(request.form['informacion']))
		matriz.ConstruirTXT()

	elif str(request.form['tipo'])=="eliminar":
		matriz.eliminar(str(request.form['informacion']))
		matriz.ConstruirTXT()

	elif str(request.form['tipo'])=="dominio":
		
		return str(matriz.PorDominio(str(request.form['informacion'])))

	elif str(request.form['tipo'])=="letra":
		
		return str(matriz.PorLetra(str(request.form['informacion'])))


@app.route('/Cola',methods = ['POST'])
def cola4():
	if str(request.form['tipo'])=="insertar":
		cola.queque(request.form['informacion'])
		cola.GenerarGrafico()

	elif str(request.form['tipo'])=="eliminar":
		r = str(cola.dequeque())
		cola.GenerarGrafico()
		return r
		



@app.route('/Pila',methods = ['POST'])
def pila4():
	if str(request.form['tipo'])=="push":
		pila.push(str(request.form['informacion']))
		pila.GenerarGrafico()

	elif str(request.form['tipo'])=="pop":
		r = str(pila.pop())
		pila.GenerarGrafico()
		return r
		


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')





