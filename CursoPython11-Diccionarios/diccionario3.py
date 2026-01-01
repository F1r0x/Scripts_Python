#!/usr/bin/nv python3

# Creamos una variable con un diccionario de números elevados a 2
cuadrados = {x: x**2 for x in range(6)}
print(f"\n{cuadrados}\n")

# Mostrar las claves del diccionario:
print(cuadrados.keys())

# Most<ar los valores del diccionario:
print(cuadrados.values())


# Imprimir del diciionario la clave y el valor:
for clave, valor in enumerate(cuadrados):
    print(f"\n El cuadrado de {clave} es {valor}")




