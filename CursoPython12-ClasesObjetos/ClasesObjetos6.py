#!/usr/bin/env python3

class Libro:

    bestseller_value = 5000

    def __init__(self, titulo, autor, precio):
        
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod # Decoradores
    def es_bestseller(total_ventas): # Libro.es_bestseller(mi_libro, total_ventas)
        
        return total_ventas > Libro.bestseller_value

mi_libro = Libro("Cómo ser un Lammer", "Marcelo", "17.5")
print(f"\n [+] Título: {mi_libro.titulo}")
print(f"\n [+] Es un Bestseller? {Libro.es_bestseller(2000)}")