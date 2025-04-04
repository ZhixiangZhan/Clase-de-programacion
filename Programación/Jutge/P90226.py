var1=input()
lista=var1.split(" ")
a=lista[0].casefold()
b=lista[1].casefold()
if a>b:
    print(f"{a} > {b}")
elif a<b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")
