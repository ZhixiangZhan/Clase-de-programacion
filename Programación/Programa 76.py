lista1=["a","b","D","x","r","X","3","h","w","2","i"]
lista_num=[]
lista_alpha=[]
var1=0

for x in lista1:
    if x.isnumeric() == True:
        lista_num.append(x)
    if x.isalpha()==True:
        lista_alpha.append(x)
var1=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente:"))
if var1==1:
    lista_num.sort()
    lista_alpha.sort()       
    print(lista_num)
    print(lista_alpha)
    
if var1==2:
    lista_num.sort(reverse=True)
    lista_alpha.sort(reverse=True)
    print(lista_num)
    print(lista_alpha)