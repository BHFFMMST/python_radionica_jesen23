"""
Zatražite od korisnika da unese tri broja, a zatim ih saberite. Ako je njihova suma
veća od 30, ispišite: “Suma je veća od 30!” U suprotnom, ispišite odgovarajuću poruku.
"""

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
c = int(input("Unesite treci broj: "))

suma = a + b + c

if suma > 30:
    print("Suma je veca od 30")
else:
    print("Suma je manja ili jednaka 30")
