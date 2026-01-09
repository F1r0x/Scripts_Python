#!/usr/bin/env python3

class Libro:

    bestseller_value = 5000
    IVA = 0.21

    def __init__(self, titulo, autor, precio):
        
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod # Decoradores
    def es_bestseller(total_ventas): # Libro.es_bestseller(mi_libro, total_ventas)
        return total_ventas > Libro.bestseller_value
    
    @classmethod # Decoradores
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA
    
class LibroDigital(Libro): # Hereda las propiedades de la clase Libro
    IVA = 0.10


mi_libro = Libro("Cómo ser un Lammer", "Marcelo", 17.5)
mi_libro_digital = LibroDigital("Cómo ser un HAcker", "Marcelo", 17.5)



print(f"\n [+] Título: {mi_libro.titulo}")
print(f"\n [+] Precio con IVA redondeado: {round(Libro.precio_con_iva(mi_libro.precio),2)}€") # Utiliza round para redondear a 2 cifras 
print(f"\n [+] Precio con IVA: {Libro.precio_con_iva(mi_libro.precio)}€")
print(f"\n [+] Precio con IVA digital: {LibroDigital.precio_con_iva(mi_libro_digital.precio)}€")

print(f"\n [+] Es un Bestseller? {Libro.es_bestseller(2000)}")
