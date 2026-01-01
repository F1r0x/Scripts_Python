#!/usr/bin/env python3

my_ports = [22,80,443,8080,443]

my_ports.extend([84,85]) 
my_ports += [86, 87]


# Ordenar valores de la lista.
my_ports = sorted(my_ports)

# Eliminar de la lista el valor de la posición 0
del my_ports[0]


# Utilizar for para iterar por cada elemento de la lista.
print("\n [+] Puertos principales:\n")
for port in my_ports:
    print("  [-] Puerto:", port)

print(f"\n La lista tiene un total de {len(my_ports)} elementos.")


lista = (1, 2)
lista.append(3)
print(lista)


