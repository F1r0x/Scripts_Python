#!/usr/bin/env python3

# Las tuplas a diferencia de las listas son inmutables
# Con las tublas inser(), extend(), remove(), append()... no funcionan
example = (1, "test", [1, 2, 3], 4, True, {'manzanas': 1, 'peras': 3}, 5)

print(example)
print(example[3])
print(example[5:])

