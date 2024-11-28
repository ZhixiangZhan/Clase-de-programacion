#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
var=input("Introduzca una palabra: ")
var2=0
for recorer in var:
    var2=var2+1
    print(f" la posicion {var2} esta la letra: {recorer}")