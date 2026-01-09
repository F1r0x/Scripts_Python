#!/usr/bin/env python3

class Automovil:

    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def monovolumenes(cls, marca):
        return cls(marca, "Monovolumen")

    def __str__(self):
        return f"\n [+] La marca {self.marca} es y modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari"))
monovolumen = print(Automovil.monovolumenes("Volswagen"))

