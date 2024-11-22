# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
palabra = input("Introduce una palabra: ")
vocales = ""
consonantes = ""

for letra in palabra:
    if letra in "aeiouáéíóú":
        vocales += letra
    elif letra.isalpha():  
        consonantes += letra  
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
