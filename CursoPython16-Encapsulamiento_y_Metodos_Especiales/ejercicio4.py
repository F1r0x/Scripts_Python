#!/usr/bin/env python3

class Libro:

    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo

    # Utilizamos el método __str__ para retornar los valores del constructor
    def __str__(self):
        return f"El libro [{self.titulo}] es de {self.autor}"
    
    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo
        

libro1 = Libro("Juan", "Cómo ser Programador!")
libro2 = Libro("Pablo", "Cómo ser un Hacker!")
print(libro1)
print(libro2)
print(f"\n ¿Son iguales ambos libros? -> {libro1 == libro2}")
