a=0
b=0
temperatura=int(input())
if temperatura<10:
    print("it's cold")
else:
    a=1
if temperatura<=0:
    print("water would freeze")    
if temperatura>30:
    print("it's hot")
elif temperatura>=100:
    print("water would boil")
else:
    b=1
if temperatura>=100:
    print("water would boil")
if a == 1 and b == 1:
    print("it's ok")