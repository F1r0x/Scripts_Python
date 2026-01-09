#!/usr/bin/env python3

class Calculadora:

    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2
    
    def multiplicacion(num1, num2):
        return num1 * num2

    def división(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[+] Erro: No se puede dividir un número entre 0"


print(Calculadora.suma(2, 8))
print(Calculadora.resta(8, 4))
print(Calculadora.multiplicacion(8, 4))
print(Calculadora.división(8, 4))