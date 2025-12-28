#!/usr/bin/env python3

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for elements in my_list:
    print(elements)

# Respuesta: 
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

for elements in my_list:
    print(f"\n[+] Vamos a desglosar la lista: {elements}")
    for value_in_elements in elements:
        print( value_in_elements)

# Respuesta: 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
