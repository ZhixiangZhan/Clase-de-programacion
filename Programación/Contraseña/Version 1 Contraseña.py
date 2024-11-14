#Contraseña versio 1
# Muestra las instrucciones para hacer la contraseña
print("la longitud de la clave debe tener enre 6 y 8 caracteres")
print("la posición 1 tiene que ser: Un número major o igual 1 y menor o igual 5")
print("la posición 2 tiene que ser: Una letra minúscula")
print("la posición 3 tiene que ser: Una letra mayúsculas")
print("la posición 4 tiene que ser: Uno de los siguientes simbolos *, _, @")
print("la posición 5 tiene que ser: Una letra minúscula")
print("la posición 6 tiene que ser: Un número major o igual 6 y menor o igual 9")
print("la posición 7 tiene que ser: Uno de los simbolos siguientes &, /, #")
print("la posición 8 tiene que ser: Un numero menor o igual 5")
# El input para que el usuario ponga la contraseña
password=input("Introduzca la clave: ")
#Variables
longitud=len(password)
minus1=password[1].islower()
mayus=password[2].isupper()
minus2=password[4].islower()
#contador de errores
error=0
#la condicion para empezar el programa
if not longitud<=8 and longitud>=6:
    print(f"Error, el password té una longitud de {longitud} caràcters i no compleix els requisits")
else:
    #Pongo el "if not" o "if... not in" para que si hay un errror de caracter en tal posicion se ponga como errror
    if not int(password[0])<=1 and int(password[0])>=5:
        print("Error en el caràcter 1")
        error=error+1
    if not minus1==True:
        print("Error en el caràcter 2")
        error=error+1
    if not mayus==True:
        print("Error en el caràcter 3") 
        error=error+1
    if password[3]not in"*_@" :
        print("Error en el caràcter 4") 
        error=error+1        
    if not minus2==True:
        print("Error en el caràcter 5")
        error=error+1
    if not int(password[5])>=6 and int(password[5])<=9:
        print("Error en el caràcter 6")
        error=error+1
# elif para saber si hay un caracter en la posicion 6        
    elif longitud==7:
        if password[6]not in"&/#":
            print("Error en el caràcter 7")
            error=error+1
# elif para saber si hay un caracter en la posicion 7       
    elif longitud==8:
        if not int(password[7])<=5:
            print("Error en el caràcter 8")
            error=error+1
# Si contador es igual a zero pondra que es correcto, si no es igual a zero no se mostrara el print de si esta correcto
    if error==0:
        print("El format del PASSWORD és correcte")
    
        
