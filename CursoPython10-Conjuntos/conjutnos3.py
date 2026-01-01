#!/usr/bin/env python3

mi_conjuto = {1, 2, 3, 4, 5}
mi_segundo_conjunto = {3, 20, 7, 1}

# Intersecciones .intersection()
# Mostrar los datos que se reptiten entre conjuntos con intersection()
mi_conjuto_final = mi_conjuto.intersection(mi_segundo_conjunto)
print(mi_conjuto_final)

# Respuesta:
# {1, 3}


#-------------------------

# Uniones .union()
# También podemos unir los conjutos con .union()
mi_conjunto_unido = mi_conjuto.union(mi_segundo_conjunto)
print(mi_conjunto_unido)

# Respuesta:
# {1, 2, 3, 4, 5, 7, 20}

#--------------------------

# Incluidos .issubset()
# Podemos verificar si un conjunto contiene los valores de otro con .issubset()
print(mi_conjuto.issubset(mi_segundo_conjunto))
# En esta ocasión nos devolverá FALSE ya que hay elementos en el segundo conjunto
# que no se encuentran en el primero.

mi_conjuto = {1, 2, 3, 4, 5}
mi_segundo_conjunto = {3, 1, 2, 4, 5}
print(mi_conjuto.issubset(mi_segundo_conjunto))
# TRUE