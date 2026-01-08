#!/usr/bin/env python3

class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self): # Rectangulo.area()
        return self.ancho * self.alto
    
    def __str__(self): # String
        return f"\n [+] Propiedades del rectángulo: [Ancho: {self.alto}][Alto: {self.ancho}]"
    
    def __eq__(self, otro): # Igualador
        return self.ancho == otro.ancho and self.alto == otro.alto

        
     
rectangulo1 = Rectangulo(200, 100) # self
rectangulo2 = Rectangulo(300, 250) # otro
rectangulo3 = Rectangulo(300, 250) # otro


print(rectangulo1)
print(f"\n [+] El área es {rectangulo1.area} m2")

# Ejemplos con la función del Igualador
print(f"\n [+] Son igueles los recángulos? --> {rectangulo1 == rectangulo2}")
print(f"\n [+] Son igueles los recángulos? --> {rectangulo2 == rectangulo3}")
