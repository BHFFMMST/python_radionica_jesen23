import math

n = int(input("Veličina liste, n = "))

lista = []
for i in range(n):
    lista.append(int(input(f"Unesite {i+1}. element liste: ")))

# prvi nacin 
# kvadrirana_lista = []
# for i in range(len(lista)):
#     kvadrirana_lista.append(lista[i]**2)


# NAPOMENA: ovo nismo radili na predavanju
# drugi nacin
# koristeci list comprehension, procitajte vise na https://www.geeksforgeeks.org/python-list-comprehension/
# kvadrirana_lista = [x**2 for x in lista]

# treci nacin
# koristeci map i lambda funkciju
# procitajte vise na https://www.geeksforgeeks.org/python-map-function/ i https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
kvadrirana_lista = list(map(lambda x: x**2, lista))

print("Polazna lista je: ", lista)
print("Kvadrirana lista je: ", kvadrirana_lista)
