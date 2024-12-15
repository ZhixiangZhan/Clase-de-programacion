#Contraseña versio 2
# Muestra las instrucciones para hacer la contraseña
print("la longitud de la clave debe tener 8 caracteres")
print("Debe de contener 3 números, 3 letras y 2 simbolos")
print("Debe de haber 2 minusculas y 1 mayuscula")
print("Dos números mayores o iguales a 1 y menores o iguales a 5")
print("Un número mayor o igual 6 y menor o igual 9")
print("Los simbolos deben de ser los siguientes: *, _, @, &, /, # ")

for contador in range (8):
    mayor_cinco=0
    menor_cinco=0
    numeric=0
    minus=0
    mayus=0
    simbol=0
    error=""
    password=input("Introduzca la clave: ")
    longitud=len(password)
    if longitud==8:
        for x in range(8):
            if password[x].islower()==True:
                minus=minus+1
            if password[x].isupper()==True:
                mayus=mayus+1
            if password[x].isnumeric()==True:
                if int(password[x])>=6 and int(password[x])<=9:
                    mayor_cinco+=1
                if int(password[x])>=1 and int(password[x])<=5:
                   menor_cinco+=1
            if password[x] in "&/#*_@":
                simbol=simbol+1
           
    
    if not minus==2:
         error=error+"(Error en la cantidad de minúsculas)"
    if not mayus==1:
         error=error+"(Error en la cantidad de mayúsculas)"
    if not menor_cinco==2:
         error=error+"(Error en la cantidad de números mayores o iguales 1 y menores o iguales 5 )"
    if not mayor_cinco==1:
         error=error+"(Error en la cantidad de números mayores o iguales 6 y menores o iguales 9)"
    if not simbol==2:
         error=error+"(Error en la cantidad o los requisitos de los símbolos)"
    if error=="":
         print("La clave está correcta")
    if error!="":
         print(error) 
    if not longitud==8:
        print("La clave no tiene la longitud establecida")