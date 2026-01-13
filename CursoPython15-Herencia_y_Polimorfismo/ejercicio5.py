#!/usr/bin/env python3

class A:
    def __init__(self,x):
        self.x = x
        print(f"\n [+]Valor en x: {self.x}")

class B(A):
    def __init__(self, x, y):
        self.y = y
        super().__init__(x)
        print(f"\n [+]Valor en y: {self.y}")

b = B(2, 10)

# Valor en x: 2
# Valor en y: 10
