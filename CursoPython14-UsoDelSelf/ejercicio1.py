#!/usr/bin/env python3

# Clase Persona
class Persona:

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos_persona(self):
        print(f"\n[+] {self.nombre} tiene {self.edad} años.")

class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def datos_vehiculo(self):
        print(f"\n[+] El veículo es un {self.marca} de color {self.color}.")


juan = Persona("Juan", 20)
coche_rojo = Vehiculo("Jeep", "rojo") # Construyes la "Persona" juan con el nombre "Juan" y edad 20 años.
print(f"\n[+] {juan.nombre} tiene {juan.edad} años y tiene un {coche_rojo.marca} de color {coche_rojo.color}.")

juan.datos_persona()
coche_rojo.datos_vehiculo()

lola = Persona("Lola", 30)
print(f"\n[+] {lola.nombre} tiene {lola.edad} años.")