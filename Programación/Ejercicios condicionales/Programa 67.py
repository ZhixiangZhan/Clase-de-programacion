#Contraseña versio 2
# Muestra las instrucciones para hacer la contraseña
print("la longitud de la clave debe tener 8 caracteres")
print("Debe de contener 3 números, 3 letras y 2 simbolos")
print("Debe de haber 2 minusculas y 1 mayuscula")
print("Dos número mayor o igual 1 y menor o igual 5")
print("Un número mayor o igual 6 y menor o igual 9")
print("Los simbolos deben de ser los siguientes: *, _, @, &, /, # ")
numeric=0
minus=0
mayus=0
simbol=0
error=""
contador=0

while contador<3:  
    password=input("Introduzca la clave: ")
    longitud=len(password)
    if longitud==8:
        for x in range(8):
            if password[x].islower()==True:
                minus=minus+1
            if password[x].isupper==True:
                mayus=mayus+1
            if password[x].isnumeric==True:
                if int(password[x])>=1 and int(password[x])<=5:
                    numeric=numeric+1
                elif int(password[x])>=6 and int(password[x])<=9:
                    numeric=numeric+1
            if password[x] in "&/#*_@":
                simbol=simbol+1
           
    if not longitud==8:
        error+="(La clave no tiene la longitud establecida)"
        
    if not minus==2:
         error+="(Error en la cantidad de minusculas)"
    if not mayus==1:
         error+="(Error en la cantidad de mayusculas)"
    if not numeric==3:
         error+="(Error en la cantidad o los requisitos de los números)"
    if not simbol==2:
         error+="(Error en la cantidad o los requisitos de los simbolos)"
    if error=="":
         print("La clave esta correcta")
    if error!="":
        print("el password esta incorrecto") 
        print(error)
    contador+=1