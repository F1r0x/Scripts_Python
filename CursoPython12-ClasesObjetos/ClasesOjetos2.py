#!/usr/bin/env python3

class Animal:
    
    def __init__(self, nombre, animal):
        self.nombre = nombre
        self.animal = animal

    def descripcion(self):
        return f"\n {self.nombre} es un {self.animal}"

gato = Animal("Lolo", "Gato")
perro = Animal("Rex", "Perro")

print(gato.descripcion())
print(perro.descripcion())

gato.descripcion
perro.descripcion