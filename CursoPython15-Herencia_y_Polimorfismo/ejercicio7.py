#!/usr/bin/env python3

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"\nHola, soy {self.nombre} y tengo {self.edad} años"

class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    
    def saludo(self):
        print(f"\n{super().saludo()} y gano {self.salario}€ anuales.")

persona = Empleado("Alicia", "30", "35000")
print(persona.saludo())