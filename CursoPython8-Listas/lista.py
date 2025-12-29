#!/usr/bin/env python3

puertos_tcp = [21, 22, 80, 443, 8080, 445, 69]
# Incluir elementos en una lista
puertos_tcp.append(1337)

print(f"\n[+] Puertos TCP: {puertos_tcp}")
print(f"\n[+] Nº de Puertos: {len(puertos_tcp)}")

for puerto in puertos_tcp:
    print(f"Este es el puerto {puerto}")

puertos_tcp.sort()
print(puertos_tcp)