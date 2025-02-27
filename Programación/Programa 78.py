lista1=["a","b","D","x","r","X","3","h","w","2","i"]
var1=""

while True:
    eliminar=input("introduzca un valor numerico que quiera eliminar: ")
    if eliminar.isnumeric():
        if eliminar not in lista1:
            print("El valor introducido no está en la lista")
        else:
            lista1.remove(eliminar)
            print(lista1)
    else:
        print("introduzca un valor numerico")
    
    var1=input("Deseas introducir otro valor s/n: ")
    if var1 == "n":
        break


    
