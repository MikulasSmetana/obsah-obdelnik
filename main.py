def obsah():
    while True:
        try:    
            a = int(input("Zadej velikost strany a v cm: "))
            b = int(input("Zadej velikost strany b v cm: "))
            if(a>0 and b>0):
                obsah = a*b
                print(f"Obsah obdélníku o straně {a}cm a {b}cm je {obsah}.")
            else:
                print("Špatné hodnoty, zkuste to znovu.")
        except:
            print("Špatné hodnoty, zkuste to znovu.")
        else:
            break

obsah()