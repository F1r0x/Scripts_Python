#!/usr/bin/env python3

from functools import reduce

numeros = [1, 2, 3 ,4 ,5]

# Asigna con "reduce" los valores de la lista en orden
impares = reduce(lambda x, y: x*y, numeros)
print(impares)

# Primero: x*y = 1*2 = 2
# Segundo: x*y = 2*3 = 6
# Segundo: x*y = 6*4 = 24
# Segundo: x*y = 24*5 = 120
