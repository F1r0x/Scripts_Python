#!/usr/bin/env python3

my_ports = [22,80,443,8080,443]

# Con .extend podemos añadir varios valores a la lista.
my_ports.extend([84,85]) 

# Esto es lo mismo que: my_ports = my_ports + [86, 87]
my_ports += [86, 87] 

# Utilizar for para iterar por cada elemento de la lista.
print("\n [+] Puertos principales:\n")
for port in my_ports:
    print("  [-] Puerto:", port)

print(f"\n La lista tiene un total de {len(my_ports)} elementos.")

