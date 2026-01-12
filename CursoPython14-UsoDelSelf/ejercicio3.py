#!/usr/bin/env python3

# Clase Calculadora
class Calculadora:

    # Constructor
    def __init__(self, valor):
       self.valor = valor


    # Suma
    def suma(self, valor2):
        print(self.valor + valor2)
        return self.valor + valor2
        

    def doblesuma(self, num2, num3):
        print(self.suma(num2) + self.suma(num3))

    def resta(self, valor2):
        print(self.valor - valor2)
    
    def mult(self, valor2):
        print(self.valor * valor2)
    
    def div(self, valor2):
        print(self.valor / valor2 if valor2 != 0 else f"\n[!] Error: No se puede dividir entre 0")


calc = Calculadora(5)
calc.suma(5)
calc.resta(5)
calc.mult(5)
calc.div(5)
calc.div(0)

calc.doblesuma(5, 5)

