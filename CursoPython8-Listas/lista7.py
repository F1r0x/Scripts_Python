#!/usr/bin/env python3

names = ["Paco", "Manuel", "Juan", "Mariano"]
edades = [20, 49, 19, 67]

for name, edad in zip(names, edades):
    print(f"{name} tiene {edad} años.")