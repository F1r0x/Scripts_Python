#!/usr/bin/env python3

mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Incluir una tupla en una variable
# Se creará una nueva tupla con los valores pares
numeros_pares = tuple(i for i in mi_tupla if i % 2 == 0)

print(numeros_pares)

# Respuesta:
# (2, 4, 6, 8, 10)


