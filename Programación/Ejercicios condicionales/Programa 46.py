# A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
var= input("Introduce una palabra: ")
palabra=var.casefold()
vocales = ""
consonantes = ""

for letra in palabra:
    if letra.lower() in "aeiouáéíóú":
        vocales += letra
    elif letra.isalpha():  
        consonantes += letra  
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
