#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
menores=int(input("cuantos menores hay: "))
adultos=int(input("cuantos adultos hay: "))
precio_m=6*menores
precio_a=10.8*adultos
print("El precio total del cine para adulto/s es: ","{:.1f}".format(precio_a),"€")
print("El precio total del cine para menor/es es: ",precio_m,"€")
