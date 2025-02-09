import random
var1=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
total_acumulado=0
var2=0
var3=""
var4=input("Quiere jugar una partida de blackjack? si: s  no: n :")
var5=0
while total_acumulado<21:
    
    if var4=="s":
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
        if total_acumulado==21:
            print("Has ganado")
            var4="n"
        if total_acumulado>21:
            print("Has perdido")
            total_acumulado=0
            var4="n"
            var5=1
        if var5==0:
            var4=input("Quieres otra carta? si: s  no: n :")  
        if var5!=0:    
            var4=input("Quiere jugar una partida de blackjack? si: s  no: n :")
    if var4=="n":
   
        if total_acumulado<21 and total_acumulado>15:
            total_acumulado=0
            print("Has sido un poco conservador")
            var4=input("Quiere jugar una partida de blackjack? si: s  no: n :")
        if total_acumulado<1 and total_acumulado>15:
            total_acumulado=0    
            print("Quizás tendrías que arriesgar un poco ¿no?")
            var4=input("Quiere jugar una partida de blackjack? si: s  no: n :")

        

    
    
    
    
    
   # var4=random.randint(1,13)
    #print("El dealer ha sacado: ",var1[var4-1])
    #total_acumulado_dealer+=var1[var4-1]
    #print(f"El total acumulado del dealer es: {total_acumulado_dealer}")
    #var2=input("Quieres otra carta? si: s  no: n :")
