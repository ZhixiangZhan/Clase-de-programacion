#42. Imprime el siguiente patrón utilizando for:
var="*****"

for contador in range(len(var)):
    contador+=1
    print(var[0:contador])
for vuelta in range(len(var)):
    print(var[vuelta:3])