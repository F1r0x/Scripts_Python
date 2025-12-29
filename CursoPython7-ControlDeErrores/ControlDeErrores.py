#!/usr/bin/env python3
 
try:
    num = 5/0 # Error

# Manejo de errores con except:
except ZeroDivisionError:
    print("\nNo se puede dividir un número entre cero")
except TypeError:
    print("Las operaciones matemáticas sólo deben de realizarse con números.")

else:
    print(f"La división entre ambos números da como resultado {num}")

finally:
    print("Esto siempre se va a ejecutar.")