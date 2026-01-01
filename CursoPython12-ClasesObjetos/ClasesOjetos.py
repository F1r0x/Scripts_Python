#!/usr/bin/env python3
## POO (Object Oriented Programing)

# Una clase es una "plantilla" que almacenará los valores 
class Persona:

    ## Constructor
    # Definimos el constructor
    def __init__(self, nombre, edad): # Le pasamos dos parámetros (nombre, edad)
        # Crea los atributos del objeto. "self" representa el objeto que se está creando
        self.nombre = nombre
        self.edad = edad

    # Método Saludo
    def saludo(self): # Utilizamos self para acceder a los atributos de una clase
        # Utilizamos return para devolver un texto con nombre y edad.
        return f"Hola soy, {self.nombre} y tengo {self.edad} años"

mariano = Persona("Mariano",  28) 
print(mariano.saludo()) # Llamamos al método con paréntesis .saludo()

juan = Persona("Juan",  70)
print(juan.saludo())