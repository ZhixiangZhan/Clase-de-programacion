var1=input("introduzca una letra: ")
x=var1.islower()
y=var1.isnumeric()
z=var1.isupper()
if x==True:
    print("la letra es minuscula")
if z==True:
    print("la letra es mayuscula")
if y==True:
    print("es un número")
elif x==False and z==False and y==False:
    print("es un simbolo")

