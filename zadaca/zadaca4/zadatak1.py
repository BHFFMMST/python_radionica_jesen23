import math

n = int(input("Veličina liste, n = "))

lista = []
for i in range(n):
    lista.append(int(input(f"Unesite {i+1}. element liste: ")))

print("Elementi liste su:", end=" ")
for i in range(len(lista)):
    print(lista[i], end=" ")
print()

print("Najveći element liste je ", max(lista) , " a najmanji ", min(lista))


suma = sum(lista) # koristimo built-in funkciju sum - https://docs.python.org/3/library/functions.html#sum
# ili
# suma = 0
# for i in range(len(lista)):
#     suma=suma+lista[i]
print("Suma elemenata liste je ", suma)



proizvod = math.prod(lista) # koristimo prod funkciju iz math modula - https://docs.python.org/3/library/math.html#math.prod
# proizvod = 1
# for i in range(len(lista)):
#     proizvod = proizvod * lista[i]
print("Proizvod elemenata liste je ", proizvod)


print("Aritmetička sredina elemenata liste je ", suma/len(lista))


lista_rastuca = sorted(lista)
print("Sortirana lista u rastućem poretku je: ", lista_rastuca)

lista_opadajuca = sorted(lista, reverse=True)
print("Sortirana lista u opadajućem poretku je: ", lista_opadajuca)
