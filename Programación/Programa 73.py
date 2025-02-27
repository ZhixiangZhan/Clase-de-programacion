lista1=["casa","mesa","sol","sal","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
lista_repe=[]
lista_n_repe=[]

for x in lista2:
    if x in lista1:
        lista_repe.append(x)
    else:
        lista_n_repe.append(x)

print(f"Estan repetidas: {lista_repe}")
print(f"No estan repetidas: {lista_n_repe}")
