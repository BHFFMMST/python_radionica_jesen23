"""
Napisati kod koji će tražiti od korisnika da unese broj, a onda će vaš kod ispisati sve brojeve od 0
do tog unesenog broja.
"""

n = int(input("Unesite broj n: "))

for i in range(n):
    if i < n-1:
        print(i, end=", ")
    else:
        print(i)
print()
