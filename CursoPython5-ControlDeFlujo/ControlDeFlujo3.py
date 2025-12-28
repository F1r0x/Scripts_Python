#!/usr/bin/env python3

nombres = ["Juan", "Manu", "Lara", "Jaime"]

for i, nombre in enumerate(nombres):
    print(f"En la posición {i+1} está {nombre}")
    # Sumamos i+1 para que la cuenta de enumerate no empiece por 0.