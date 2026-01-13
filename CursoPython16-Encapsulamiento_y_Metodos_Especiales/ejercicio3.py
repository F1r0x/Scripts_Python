#!/usr/bin/env python3

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 #Atributo privado
    
    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje = kilometros
        else:
            print(f"\n [!] El coche no tiene km.")

    def mostrar_kilometraje(self):
        return f"\n El coche tiene {self.__kilometraje} km"

coche = Coche("Toyota", "Corolla")

coche.conducir(150)
print(coche.mostrar_kilometraje())