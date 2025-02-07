import random
var1=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
total_acumulado=0
var3=0
var4=""
var2=input("Quiere jugar una partida de blackjack? si: s  no: n :")

while total_acumulado<21:
    
    if total_acumulado==21:
        print("Has ganado")
        
        
    if total_acumulado>21:
        print("Has perdido")
        
    if var2=="s":
        var3=random.randint(1,13)
        var4=var1[var3-1]
        if var4=="J" or  var4=="Q" or  var4=="K":
            total_acumulado+=10
        if var4=="A":
            if total_acumulado<10:
                total_acumulado+=11
            elif total_acumulado==10:
                total_acumulado+=11
            elif total_acumulado>10:
                    total_acumulado+=1
        if var4!="A" and var4!="J" and var4!="Q" and var4!="K" :
            total_acumulado+=int(var4)
            
     print("Tu carta es: ",var4)
     print(f"El total acumulado es: {total_acumulado}")
     var2=input("Quieres otra carta? si: s  no: n :")  
     
    
    
    if var2=="n":
   
        if total_acumulado<21 and total_acumulado>15:
                print("Has sido un poco conservador")
        if total_acumulado<1 and total_acumulado>15:
                print("Quizás tendrías que arriesgar un poco ¿no?")
        

    
    
    
    
    
   # var4=random.randint(1,13)
    #print("El dealer ha sacado: ",var1[var4-1])
    #total_acumulado_dealer+=var1[var4-1]
    #print(f"El total acumulado del dealer es: {total_acumulado_dealer}")
    #var2=input("Quieres otra carta? si: s  no: n :")