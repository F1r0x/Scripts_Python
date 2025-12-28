#!/usr/bin/env python3

first_elements = [1, 3, 5, 7, 9] 
second_elements = [2, 4, 6, 8, 10]

## Unir listas
result = first_elements + second_elements
print(result) 
# Respuesta: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


## Asociar valores de las listas
result2 = zip(first_elements, second_elements)

for element in result2:
    print(element)
# Respuesta: 
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)
# (9, 10)
