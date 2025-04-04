letra=input()
letra_cambiada=""
    if letra.isalpha:
        if letra.isupper():
        letra_cambiada=letra.lower()
    elif letra.islower:
        letra_cambiada=letra.upper()
print(letra_cambiada)