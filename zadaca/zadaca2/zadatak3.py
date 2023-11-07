""""
Unijeti dva realna broja, zatim uporediti cijele dijelove brojeva (cijeli dio broja 1.85 je
1). Ispisati onaj broj čiji je cjelobrojni dio veći, u slučaju da su cjelobrojni dijelovi
jednaki ispisati oba broja. (hint: Da biste odredili cijeli dio broja koristite konverziju u
cjelobrojni tip podatka.)
"""

a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))

a_int = int(a)
b_int = int(b)

if a_int > b_int:
    print(a_int, a)
elif a_int < b_int:
    print(b_int, b)
else:
    print(a_int, b_int)
    