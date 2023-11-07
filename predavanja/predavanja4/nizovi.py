import array as arr

# Nizovi
niz_int = arr.array('i', [1, 2, 5, 10, 9])
print(niz_int)

## Velicina niza - broj elemenata u nizu
print("Velicina niza je:", len(niz_int))

## Pristup elementima niza
print("Element na poziciji 0 je:", niz_int[0])
print("Element na poziciji 1 je:", niz_int[1])
print("Posljednji element je:", niz_int[-1])

## Ispis elemenata niza po vrijednosti
print("Elementi niza su:", end=" ")
for element in niz_int:
    print(element, end=" ")
print()

## Ispis elemenata niza po indeksu
print("Elementi niza su:", end=" ")
for i in range(len(niz_int)):
    print(niz_int[i], end=" ")
print()

## Slice operator - ispis dijela liste
print("Prva tri elementa liste su:", niz_int[:3])
print("Posljednja tri elementa liste su:", niz_int[-3:])

## Promjena elemenata niza
print(niz_int)
niz_int[0] = 10
print("Nakon promjene prvog elementa:", niz_int)

## Dodavanje elemenata na kraj niza
niz_int.append(10)
print("Nakon dodavanja elementa na kraj:", niz_int)

## Dodavanje elemenata na pocetak niza
niz_int.insert(0, 100)
print("Nakon dodavanja elementa na pocetak:", niz_int)

## Brisanje elemenata iz niza
niz_int.remove(10) # Brise element 100 tj. njegovo prvo pojavljivanje
print("Nakon brisanja elementa:", niz_int)

## Brisanje elemenata iz niza po indeksu
niz_int.pop(0) # Brise element na poziciji 0
print("Nakon brisanja elementa po indeksu:", niz_int)

## Indeks elementa u listi - vraca indeks prvog pojavljivanja elementa
print("Indeks elementa 10 u listi:", niz_int.index(10))

## Broj pojavljivanja elementa u nizu
print("Broj pojavljivanja broja 10 u nizu:", niz_int.count(10))

## Provjera da li se element nalazi u listi
print("Da li se broj 10 nalazi u listi:", 10 in niz_int)

## Append i extend
niz_int.append(1000)
print("Nakon append:", niz_int)

niz_int.extend([1, 2, 3])
print("Nakon extend:", niz_int)

## Sortiranje niza
print("Niz prije sortiranja:", niz_int)
sorted_niz = sorted(niz_int)
print("Niz nakon sortiranja:", sorted_niz)

## Sortiranje niza u obrnutom redoslijedu
print("Niz prije sortiranja:", niz_int)
sorted_niz = sorted(niz_int, reverse=True)
print("Niz nakon sortiranja:", sorted_niz)


## Nizovi float
niz_float = arr.array('f', [1.0, 2.0, 5.0, 10.0, 9.0])
print(niz_float)

## Nizovi karaktera
niz_char = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
print(niz_char)
print(niz_char[0])
