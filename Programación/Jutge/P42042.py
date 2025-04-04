letra=input()
vowel=["a","e","i","o","u"]
if letra.isalpha:
    if letra.isupper():
        print("uppercase")
    else:
        print("lowercase")
    if letra.lower() in vowel:
        print("vowel")
    else:
        print("consonant")
