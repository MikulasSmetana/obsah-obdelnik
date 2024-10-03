def obsah():
    a = int(input("Zadej velikost strany a v cm: "))
    b = int(input("Zadej velikost strany b v cm: "))
    obsah = a*b
    print(f"Obsah obdélníku o straně a {a}cm a b {b} je {obsah}.")

while True:
    obsah()