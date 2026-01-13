#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")

class Gato(Animal):
        def hablar(self):
            return f"{gato.nombre} dice Miauu..."

class Perro(Animal):
        def hablar(self):
            return f"{perro.nombre} dice Guauu..."


gato = Gato("\nFirulais")
perro = Perro("\nMax")
gato2 = Animal("Mini")

print(gato.nombre)
print(gato.hablar())


print(perro.nombre)
print(perro.hablar())


# Ejemplo del error:
#print(gato2.nombre)
#print(gato2.hablar())
