var1=input("introduzca una letra: ")
x=var1.islower()
y=var1.isnumeric()
if x==True:
    print("la letra es minuscula")
if x==False and y==False:
    print("la letra es mayuscula")
if y==True:
    print("es un número")

