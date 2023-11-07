"""
Učitati dva prirodna broja, ako je prvi broj veći od drugog ispisati njihovu razliku, u
suprotnom ispisati njihov zbir.
"""

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))

if a > b:
    print(a - b)
else:
    print(a + b)
