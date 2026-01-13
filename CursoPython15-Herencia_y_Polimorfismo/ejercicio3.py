#!/usr/bin/env python3

## CONCEPTO DE HERENCIA

# Clase Automovil
class Automovil():
    
    # Constructor
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo

    # Método describir
    def describir(self):
        return f"\n [+] Automóvil: {self.marca} {self.modelo}"

# Clase Moto que hereda el constructor de la clase Automovil
class Moto(Automovil):

    def describir(self):
        return f"\n [+] Motocicleta: {self.marca} {self.modelo}"


# Objetos 
porche = Automovil("Porche", "911")
honda = Moto("Honda", "CBR")

# Mostrar por pantalla
print(porche.describir())
print(honda.describir())