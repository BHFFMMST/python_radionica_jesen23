"""
Napisati program koji računa aritmetičku sredinu n unesenih brojeva.
"""

n = int(input("Unesite broj n: "))

suma = 0

for i in range(n):
    suma += int(input("Unesite broj: "))

print("Suma", suma)
print("Aritmeticka sredina je ", suma/n)
