lista=[]
var1=""
var1=input("Quieres empezar a introducir letras?: ")
while var1=="s":
    letra=input("introduzca una letra: ")
    
    if letra.isalpha()==True:
        if letra not in lista:
            lista.append(letra)
    
       
    var1=input("Quieres empezar a introducir letras?: ")
print(lista)