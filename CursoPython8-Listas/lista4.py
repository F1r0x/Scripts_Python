#!/usr/bin/env python3

attacks = ['Phishung', 'DDoS', 'Man In The Middle', 'SQL Inyection']

print(attacks)

# Iterar por los elementos de una lista
i = 0 # Contador

while i < len(attacks):
    print(f"\n[+] En la posición {i} tenemos el ataque: {attacks[i]}")
    i += 1
