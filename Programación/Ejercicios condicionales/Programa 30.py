#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif

var1=input("introduzcan una frase: ")
len=len(var1)
if len==11:
    print("la longitud de la frase es igual a 11")
elif len<11:
    print("la longitud de la frase es menor a 11")
elif len>11:
    print("la longitud de la frase es mayor a 11")

