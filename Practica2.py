__author__ = "AndreeAvalos"

#from flask import Flask
#app = Flask("Practica2")
print "====Esto es una Cola==="
import Cola
import Pila

pila2 = Cola

pila = pila2.Cola()

pila.insertar(5)
pila.insertar(4)
pila.insertar(3)
pila.insertar(2)
pila.insertar(1)

pila.imprimir()
print "===Esto es una Pila==="

pila2 = Pila

pila = pila2.Pila()

pila.insertar(5)
pila.insertar(4)
pila.insertar(3)
pila.insertar(2)
pila.insertar(1)

pila.imprimir()


#@app.route("/")
#def hellof():

#	return "Hello World!"

#if __name__ == "__main__":
# app.run()
