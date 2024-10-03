def obsah():
    a = int(input("Zadej velikost strany a v cm: "))
    b = int(input("Zadej velikost strany b v cm: "))
    if(a>0 and b>0):
        obsah = a*b
        print(f"Obsah obdélníku o straně a {a}cm a b {b} je {obsah}.")
    else:
        print("Špatné hodnoty, zkuste to znovu.")
        obsah()

obsah()