__author__ = "AndreeAvalos"

#from flask import Flask
#app = Flask("Practica2")
print "======Esto es una Cola======"
import Cola
import Pila
import ListaSimple

Cola2 = Cola

cola = Cola2.Cola()

cola.queue(1)
cola.queue(2)
cola.queue(3)
cola.queue(4)
cola.queue(5)
cola.GenerarGrafico()
cola.imprimir()

print"-----------queque-----------"
v1=cola.dequeque()
print str(v1)
print"----------------------------"
cola.imprimir()

print "======Esto es una Pila======"

pila2 = Pila

pila = pila2.Pila()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)
pila.GenerarGrafico()
pila.imprimir()
print"-----------pop--------------"
v1=pila.pop()
print str(v1)
print"----------------------------"
pila.imprimir()
print"========Lista Simple========="

lista2=ListaSimple
lista = lista2.ListaSimple()

lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)
lista.insertar(5)
lista.insertar(6)
lista.insertar(100)
lista.GenerarGrafico()

print"-------------------------"
print v1


#@app.route("/")
#def hellof():

#	return "Hello World!"

#if __name__ == "__main__":
# app.run()
