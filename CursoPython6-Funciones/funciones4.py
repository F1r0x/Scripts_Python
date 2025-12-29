#!/usr/bin/env python3

mi_lista = [1, 2 ,3 ,4 ,5]


cuadrados = map(lambda x: x**2, mi_lista)

# Podemos representarlo con for
for numero in cuadrados:
    print(numero)

# También podemos representarlo con listas
cuadrados = list(map(lambda x: x**2, mi_lista))
print(cuadrados)

# Mostrar únicamente los número pares
cuadrados_pares = list(filter(lambda x: x % 2 == 0, mi_lista))
print(cuadrados_pares)