#49


secreta=input("itroduzca una palabra secreta: ")
for contador in range (len(secreta)):
    var=input("introduzca una letra: ")

    for x in range(len(secreta)):
        
        if var==secreta[x]:
            print("la letra esta en la posicion", x+1)
    
            
    if not var in secreta:
        print("la letra no existe")
        
