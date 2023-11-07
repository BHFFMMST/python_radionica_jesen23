# Liste
lista = [1, 2, 5, 10, 9]
print(lista)

## Velicina liste - broj elemenata u listi
print("Velicina liste je:", len(lista))

## Pristup elementima liste
print("Element na poziciji 0 je:", lista[0])
print("Element na poziciji 1 je:", lista[1])
print("Posljednji element je:", lista[-1])

## Ispis elemenata liste po vrijednosti
print("Elementi liste su:", end=" ")
for element in lista:
    print(element, end=" ")
print()

## Ispis elemenata liste po indeksu
print("Elementi liste su:", end=" ")
for i in range(len(lista)):
    print(lista[i], end=" ")
print()

## Slice operator - ispis dijela liste
print("Prva tri elementa liste su:", lista[:3])
print("Posljednja tri elementa liste su:", lista[-3:])

## Promjena elemenata liste
print(lista)
lista[0] = 10
print("Nakon promjene prvog elementa:", lista)

## Dodavanje elemenata na kraj liste
lista.append(10)
print("Nakon dodavanja elementa na kraj:", lista)

## Dodavanje elemenata na pocetak liste
lista.insert(0, 100)
print("Nakon dodavanja elementa na pocetak:", lista)

## Brisanje elemenata iz liste
lista.remove(10) # Brise element 100 tj. njegovo prvo pojavljivanje
print("Nakon brisanja elementa:", lista)

## Brisanje elemenata iz liste po indeksu
lista.pop(0) # Brise element na poziciji 0
print("Nakon brisanja elementa po indeksu:", lista)

## Indeks elementa u listi - vraca indeks prvog pojavljivanja elementa
print("Indeks elementa 10 u listi:", lista.index(10))

## Broj pojavljivanja elementa u listi
print("Broj pojavljivanja broja 10 u listi:", lista.count(10))

## Provjera da li se element nalazi u listi
print("Da li se broj 10 nalazi u listi:", 10 in lista)

## Append i extend
lista.append(1000)
print("Nakon append:", lista)

lista.extend([1, 2, 3])
print("Nakon extend:", lista)

## Sortiranje liste
print("Lista prije sortiranja:", lista)
sorted_lista = sorted(lista)
print("Lista nakon sortiranja:", sorted_lista)

## Sortiranje liste u obrnutom redoslijedu
print("Lista prije sortiranja:", lista)
sorted_lista = sorted(lista, reverse=True)
print("Lista nakon sortiranja:", sorted_lista)

## Razliciti tipovi podataka u listi
lista = [1, 2, 3, "string", 4.5, True]
print(lista)

## Liste u listi - matrice (dvodimenzionalne liste - 2D liste)
matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrica)

## Pristup elementima matrice
print("Element na poziciji [0][0] je:", matrica[0][0])
print("Element na poziciji [0][1] je:", matrica[0][1])
print("Element na poziciji [1][0] je:", matrica[1][0])

## Ispis elemenata matrice po vrijednosti
print("Elementi matrice su:")
for red in matrica:
    for element in red:
        print(element, end=" ")
    print()

## Ispis elemenata matrice po indeksu
print("Elementi matrice su:")
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        print(matrica[i][j], end=" ")
    print()

## Promjena elemenata matrice
print(matrica)

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if i == j:
            matrica[i][j] = 10
    
print("Nakon promjene elemenata na glavnoj dijagonali:")
print(matrica)
