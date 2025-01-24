import random
import time
time0=time.time()
time1=0
time2=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
contador=0
while time2<3:
    time1=time.time()
    time2=time1-time0
    var1=random.randint(1,6)
    if var1==1:
        uno+=1
    if var1==2:
        dos+=1
    if var1==3:
        tres+=1
    if var1==4:
        cuatro+=1
    if var1==5:
        cinco+=1
    if var1==6:
        seis+=1
    
print(f"Duracion es: {time2}")
print(f"Uno: {uno}")
print(f"Dos: {dos}")
print(f"Tres: {tres}")
print(f"Cuatro: {cuatro}")
print(f"Cinco: {cinco}")
print(f"Seis: {seis}")

