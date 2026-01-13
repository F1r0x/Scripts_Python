#!/usr/bin/env python3

class A:
    def saludo(self):
        return f"\n Saludos desde la clase A"


class B(A):
    def saludo(self):
        original = super().saludo()
        print(f"\n {original}, pero también desde la clase B")

saludo = B()
saludo.saludo()

