#!/usr/bin/env python3

names = ["Paco", "Manuel", "Juan", "Mariano"]

print(names)

# Eliminar valores de la lista
names.remove("Paco")
print(names)

# Vacias lista
names.clear()
print(names)
print(len(names))

#----------------------------

# Eliminar el último valor de una lista con pop
names = ["Paco", "Manuel", "Juan", "Mariano"]

names.pop()
print(names)

names.pop(2) # Eliminaríamos a Juan
print(names)