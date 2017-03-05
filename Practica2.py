import Matriz 
ma= Matriz.Matriz()
#ma.insertar("r","hotmail.com","rodrigo")
#ma.insertar("r","hotmail.com","rosario")
#ma.insertar("r","hotmail.com","rosita")
#ma.insertar("c","mail.com","carlos")
ma.mandarCorreo("andree@gmail.com")
ma.mandarCorreo("david@outlook.com")
ma.mandarCorreo("elefante@outlook.com")
ma.mandarCorreo("perro@yahoo.com")
ma.mandarCorreo("pedro@yahoo.com")
ma.mandarCorreo("pablo@yahoo.com")


ma.ConstruirTXT()
ma.eliminar("pablo@yahoo.com")
ma.ConstruirTXT()







