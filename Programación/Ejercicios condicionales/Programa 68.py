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
error=0
intentos=0
print("Desesa introducir un passsword?  ")
var1=input("si= s, no= n  : ")
while var1=="s":  
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
        error+=1
    if not minus==2:
        error+=1
    if not mayus==1:
        error+=1
    if not numeric==3:
        error+=1
    if not simbol==2:
        error+=1
    if error==0:
         print("La clave esta correcta")
    if error!=0:
        print("el password esta incorrecto") 
    print("Quiere seguir introduciendo un passsword?  ")
    var1=input("si= s, no= n  : ")
    
    
    
