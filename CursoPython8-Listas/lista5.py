#!/usr/bin/env python3

attacks = ['Phishung', 'DDoS', 'Man In The Middle', 'SQL Inyection']

## Enumerar listas incluyendo sus índices
#  En este caso el índice lo guardamos en la variable i
for i, attack in enumerate(attacks):
    print(f"Para la posición {i} tendríamos el ataque: {attack}")