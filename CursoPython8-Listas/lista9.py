#!/usr/bin/env python3

names = ["Paco", "Manuel", "Juan", "Mariano"]

print(names)

# Inlcuir valores en la lista: Incluimos a Samuel en la segunda posición
names.insert(2, "Samuel")
print(names)

# Fusionar listas con .extedn()
more_names = ["Lola" ,"Alejandro"]
names.extend(more_names)
print(names)
