#!/usr/bin/env python3

numbers = [2, 4, 6, 8, 10]
todos_son_pares = True

for number in numbers:
    if number % 2 != 0: # Comprobamos si existe algún elemento impar.
        todos_son_pares = False # Al contempla un impar la variable pasa a valer False para siempre.

if todos_son_pares:
    print("Todos los elementos de la lista son pares.")
else:
    print("Algunos de los valores de la lista son impares.")