#!/usr/bin/env python3

i = 0

print("\n [+] Bucle while:")
while i < 5:
    print(i)
    i += 1

print("\n [+] Bucle for:")
for i in range(10):
    if i == 5:
        break # Paramos el bucle al llegar a 5
    print(i)


print("\n [+] Bucle for hasta el 5:")
for i in range(10):
# Si incluimos el print delante del if también se nos mostrará el valor 5
    print(i)   
    if i == 5:
        break 
    

print("\n [+] Bucle saltandose el 5:")
for i in range(10):
# Si incluimos el print delante del if también se nos mostrará el valor 5
    print(i)   
    if i == 5:
        continue
     
