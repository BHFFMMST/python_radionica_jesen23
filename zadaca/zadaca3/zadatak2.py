"""
Napisati kod koji će ispisati vaše ime 50 puta (prvo sa for petljom, a onda sa while petljom).
"""

ime = input("Unesite ime: ")

n = 10

for i in range(n):
    print(ime, end=" ")
print()

while n > 0:
    print(ime, end=" ")
    n -= 1
print()
