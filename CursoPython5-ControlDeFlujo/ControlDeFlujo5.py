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
        print(value_in_elements)

# Respuesta: 
# [+] Vamos a desglosar la lista: [1, 2, 3]
# 1
# 2
# 3
# 
# [+] Vamos a desglosar la lista: [4, 5, 6]
# 4
# 5
# 6
# 
# [+] Vamos a desglosar la lista: [7, 8, 9]
# 7
# 8
# 9

