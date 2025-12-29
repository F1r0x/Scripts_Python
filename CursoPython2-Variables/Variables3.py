#!/usr/bin/env python3

my_ports = []

my_ports.append(22)  # my_ports = [22]        <-- Posición 0
my_ports.append(80)  # my_ports = [22,80]     <-- Posición 1
my_ports.append(443) # my_ports = [22,80,443] <-- Posición 2
my_ports.append(8080) 


# Utilizar for para iterar por cada elemento de la lista.
print("\n [+] Puertos principales:\n")
for port in my_ports:
    print("  [-] Puerto:", port)

print(f"\n La lista tiene un total de {len(my_ports)} elementos.")