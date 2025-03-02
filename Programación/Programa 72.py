lista = []
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
var1 = input("¿Quieres empezar a introducir letras? (s/n): ")

while var1.lower() == "s":
    letra = input("Introduce una letra: ")
    if letra.isalpha() and letra not in lista and letra.lower() not in vocales:
        lista.append(letra)
    else:
        print("Por favor, introduce una letra válida, no repetida y que no sea una vocal con o sin acento." )
    var1 = input("¿Quieres seguir introduciendo letras? (s/n): ")

print("Las letras introducidas son:", lista)

