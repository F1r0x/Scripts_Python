#!/usr/bin/env python3

first_number = 6
second_number = 8

# Suma
print(first_number + second_number)

# Resta
print(first_number - second_number)

# Multiplicar
print(first_number * second_number)

# Dividir
print(first_number / second_number)

# Resto
print(first_number % second_number)

# Potencia
print(first_number ** second_number)


# Gardar valor de la operación en una varibable
result =first_number ** second_number
print(result)

# Colocar puntos cada miles 1.679.616
print("{:,}".format(result).replace(",", "."))

# Colocar coma cada miles 1.679.616
print("{:,}".format(result))