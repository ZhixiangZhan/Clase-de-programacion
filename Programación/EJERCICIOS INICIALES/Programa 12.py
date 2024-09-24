#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var1=int(input("Introduzca el valor de la base mayor del trapecio isósceles:"))
var2=int(input("Introduzca el valor de la base menor del trapecio isósceles:"))
var3=int(input("Introduzca el valor de la altura del trapecio isósceles:"))
var4=int(input("Introduzca el valor de los lados del trapecio isósceles:"))
var_perimetro=var1+var2+2*var4
var_suma=var1+var2
var_producto=var_suma*var3
var_area=var_producto/2
print("El perimetro es: ",var_perimetro)
print("El area es: ",var_area)
          
