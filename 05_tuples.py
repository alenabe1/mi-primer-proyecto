### tuplas ###

my_tuple = tuple()
my_other_list = ()

my_tuple = (32, 1.76, "Alejandro", "Navarro", "Alejandro")
my_other_tupla = (35, 60,30)

print(my_tuple)  # Imprime la tupla
print(type(my_tuple))  # Imprime el tipo de la variable

print(my_tuple[0])  # Imprime el primer elemento de la tupla
print(my_tuple[-1])  # Imprime el segundo elemento de la tupla


print(my_tuple.count("alenabe")) # Cuenta cuántas veces aparece "alenabe" en la tupla
print(my_tuple.count("Alejandro"))  # Cuenta cuántas veces aparece "Alejandro" en la tupla
print(my_tuple.index("Navarro"))  # Imprime el índice de la primera aparición de "Alejandro" en la tupla

# my_tuple[1] = 1.80
print(my_tuple)  # Imprime la tupla después de cambiar el valor en la posición 1
# my_tuple[1] = 1.80  # Esto generará un error porque las tuplas son inmutables

my_sum_tuple = my_tuple + my_other_tupla  # Concatena las dos tuplas y las asigna a una nueva variable
print(my_sum_tuple)  # Imprime la tupla resultante de la concatenación

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))  # Convierte la tupla en una lista y muestra el tipo de la variable

my_tuple [4] = "alenabe"
my_tuple.insert(1, "Rojo")  # Inserta "Rojo" en la posición 1 de la lista
my_tuple = tuple(my_tuple) 
print(my_tuple)
print(type(my_tuple))  # Muestra el tipo de la variable después de la conversión


del my_tuple [2]  # Elimina el elemento en la posición 2 de la tupla convertida en lista

del my_tuple
# print(my_tuple)  # Esto generará un error porque la tupla ya no existe