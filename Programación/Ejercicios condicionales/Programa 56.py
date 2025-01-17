menu=["Menu","1. Bocadillo de calamares-9€","2. Bocadillo de chistorra-4.5€","3. Bikini de jamon-2.5€"]
acompañantes=["Acompañantes","1. Patatas finas-1.5€","2. Patatas gruesas-1.75€","3. Patatas rusticas-2€"]
bebidas=["Bebidas","1. Coca cola-2€","2. Aquarius-1.5€","3. Agua-1€"]
print(menu)
print(acompañantes)
print(bebidas)
var_pedidos=0
var_total=0
var_total_iva=0
var_total_descuento=0
menu_precios=[0,9,4.5,2.5]
acompañamientos_precios=[0,1.5,1.75,2]
bebidas_precios=[0,2,1.5,1]
var1=int(input("Que quieres de comer en el apartado de Menu ¡Indique el numero!: "))
var2=int(input("Que quieres de comer en el apartado de Acompañantes ¡Indique el numero!: "))    
var3=int(input("Que quieres de beber en el apartado de Bebidas ¡Indique el numero!: "))
var_total=var_total+menu_precios[var1]
var_total=var_total+acompañamientos_precios[var2]
var_total=var_total+bebidas_precios[var3]
var_pedidos+=1 
var_total_iva=var_total*1.10
var4=input("Quiere realizar otro pedido? si=s, no=n : ")
if var_total<20:
    var_descuento="No hay descuento"
if var_total<30 and var_total>20:
    var_descuento="Precio total con descuento de 15%: {var_total_iva*0.95}
if var_total>30:
    var_descuento="Precio total con descuento de 15%: {var_total_iva*0.85}


while var4=="s":   
    var1=int(input("Que quieres de comer en el apartado de Menu ¡Indique el numero!: "))
    var2=int(input("Que quieres de comer en el apartado de Acompañantes ¡Indique el numero!: "))    
    var3=int(input("Que quieres de beber en el apartado de Bebidas ¡Indique el numero!: "))
    var_total=var_total+menu_precios[var1]
    var_total=var_total+acompañamientos_precios[var2]
    var_total=var_total+bebidas_precios[var3]
    var_pedidos+=1 
    var_total_iva=var_total*1.10
    var4=input("Quiere realizar otro pedido? si=s, no=n : ")
    if var_total<20:
        var_descuento="No hay descuento"
    if var_total<30 and var_total>20:
        var_descuento="Precio total con descuento de 15%: {var_total_iva*0.95}"
    if var_total>30:
        var_descuento="Precio total con descuento de 15%: {var_total_iva*0.85}"
    
    
if var4=="n":
    print("RESUMEN")
    print("Numero de pedidos: ",var_pedidos)
    print("Total a pagar: ",var_total)
    print("Total con iva: ","{:.2f}".format(var_total_iva))
    print(var_descuento)

    