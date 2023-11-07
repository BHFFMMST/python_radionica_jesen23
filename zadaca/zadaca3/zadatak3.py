"""
Napisati kod koji će naći sumu svih brojeva koji se nalazi između a i b (uključujući i b).
"""

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
suma = 0

if b > a:
    for i in range(a, b+1):
        suma += i
    print("Suma brojeva od", a, "do", b, "je", suma)
elif a > b:
    for i in range(b, a+1):
        suma += i
    print("Suma brojeva od", b, "do", a, "je", suma)
else:
    print("Brojevi su jednaki.")
