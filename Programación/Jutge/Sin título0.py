var1=input()
var2=input()
a=var1.casefold()
b=var2.casefold()
if len(a)>len(b):
    print(f"{a}>{b}")
if len(a)<len(b):
    print(f"{a}<{b}")
if len(a)==len(b):
    print(f"{a}={b}")
