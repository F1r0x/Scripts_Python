#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")

class Gato(Animal):
        def hablar(self):
            return f"Miauu..."

class Perro(Animal):
        def hablar(self):
            return f"Guauu..."

def hacer_hablar(objeto):
     print(f"{objeto.nombre} dice {objeto.hablar()}")

gato = Gato("\nFirulais")
perro = Perro("\nMax")
gato2 = Animal("Mini")

print(gato.nombre)
print(gato.hablar())


print(perro.nombre)
print(perro.hablar())

hacer_hablar(gato)
hacer_hablar(perro)


# Ejemplo del error:
#print(gato2.nombre)
#print(gato2.hablar())
