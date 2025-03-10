import random
var1=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
total_acumulado=0
total_acumulado1=0
var2=0
var3=""
var4=input("Quiere jugar una partida de blackjack? si: s  no: n :")
var5=0
var6="s"
while var4=="s":
    while total_acumulado<21:
        if total_acumulado>21:
            print("La banca ha ganado. Te has pasado de 21")
            var4=input("Quiere jugar otra partida de blackjack? si: s  no: n :")
        if var6=="s":
            var2=random.randint(1,13)
            var3=var1[var2-1]
            print("Tu carta es: ",var3)
               
            if var3=="J" or  var3=="Q" or  var3=="K":
                total_acumulado+=10
            if var3=="A":
                if total_acumulado<10:
                    total_acumulado+=11
                elif total_acumulado==10:
                    total_acumulado+=11
                elif total_acumulado>10:
                    total_acumulado+=1
            if var3!="A" and var3!="J" and var3!="Q" and var3!="K" :
                total_acumulado+=int(var3)
                    
            print(f"El total acumulado es: {total_acumulado}")
           
            var6=input("Quieres otra carta? si: s  no: n :")  
          
        if var6=="n":
            if total_acumulado1>21:
                print("Usted ha ganado.La banca se ha pasado de 21")
                var4=input("Quiere jugar otra partida de blackjack? si: s  no: n :")
            while total_acumulado1<21:
                var2=random.randint(1,13)
                var3=var1[var2-1]
                print("la carta de la banca es: ",var3)
                   
                if var3=="J" or  var3=="Q" or  var3=="K":
                    total_acumulado1+=10
                if var3=="A":
                    if total_acumulado1<10:
                        total_acumulado1+=11
                    elif total_acumulado1==10:
                        total_acumulado1+=11
                    elif total_acumulado1>10:
                        total_acumulado1+=1
                if var3!="A" and var3!="J" and var3!="Q" and var3!="K" :
                    total_acumulado1+=int(var3)
                        
                print(f"El total acumulado de la banca es: {total_acumulado1}")
                input
        
   
   
    if total_acumulado<21 and total_acumulado<total_acumulado1:
        print("La banca ha ganado con un total acomulado de {total_acumulado1}")
        var4=input("Quiere jugar otra partida de blackjack? si: s  no: n :")
    if total_acumulado1<21 and total_acumulado>total_acumulado1:
        print("Usted ha ganado con un total acomulado de {total_acumulado}")
        var4=input("Quiere jugar otra partida de blackjack? si: s  no: n :")
