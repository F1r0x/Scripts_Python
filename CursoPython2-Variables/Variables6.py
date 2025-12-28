#!/usr/bin/env python3

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(mi_lista)

print(mi_lista[-0:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mi_lista[:0])  # []
print(mi_lista[:-0])  # []
print(mi_lista[:3])   # [1, 2, 3] 
print(mi_lista[3:])   # [4, 5, 6, 7, 8, 9, 10]
print(mi_lista[:-3])  # [1, 2, 3, 4, 5, 6, 7]
print(mi_lista[-3])   # 8
print(mi_lista[:6])   # [1, 2, 3, 5, 6]
print(mi_lista[2:])   # [3, 4, 5, 6, 7, 8, 9, 10]
print(mi_lista[:-1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mi_lista[4:7])  # [5, 6, 7]
print(mi_lista[-3:])  # [8, 9, 10]
print(mi_lista[-1:])  # [10]

