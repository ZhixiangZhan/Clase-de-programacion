import random

listword=""

lista_letras=[]
lista_desorden=[]
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

valor_ran=random.choice(lista)
valor_ran="-".join(valor_ran)
lista_letras=valor_ran.split("-")

while len(lista_letras)>0:
    letra=random.choice(lista_letras)
    lista_desorden.append(letra)
    lista_letras.remove(letra)
    
print(lista_desorden)

