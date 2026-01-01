#!/usr/bin/env python3

mi_conjuto = {1, 2, 3, 4, 5}
print(mi_conjuto)

# Añadir un valor al conjunto (En ocasiones no respeta el orden)
mi_conjuto.add(8)
print(mi_conjuto)

# {1, 2, 3, 4, 5}
# {1, 2, 3, 4, 5, 8}

mi_conjuto.update({6, 7})
print(mi_conjuto)

# {1, 2, 3, 4, 5, 6, 7, 8}

mi_conjuto.remove(8)
print(mi_conjuto)

# mi_conjuto.remove(8) # Si tratamos de usar remove con un valor que no existe nos dará error
# print(mi_conjuto)   

# Para eliminar valores y que no muestre error en caso de no existir utilizar discard()

mi_conjuto.discard(8)
print(mi_conjuto) # Aquí el 8 ya no existe pero no muestra error

mi_conjuto.discard(6)
print(mi_conjuto)






