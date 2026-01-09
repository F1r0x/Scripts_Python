#!/usr/bin/env python3

class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
       return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            print(f"\n [+] Los estudiantes {nombre} son mayores de edad {edad}")
            return cls(nombre, edad)
        
        else:
            print(f"\n [!] Erro: el estudiante {nombre} es menor de edad {edad}")

    @staticmethod
    def mostrar_estudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"\t[x] Estudiante número [{i+1}] llamado {estudiante.nombre}")


Estudiantes.crear_estudiante("Paco", 23)
Estudiantes.crear_estudiante("Marcos", 54)
Estudiantes.crear_estudiante("Juan", 14)
Estudiantes.crear_estudiante("Kico", 38)
Estudiantes.crear_estudiante("Alex", 27)
Estudiantes.crear_estudiante("Manuel", 15)

print(f"\n [+] Listando los usuarios existentes:\n")
Estudiantes.mostrar_estudiantes()