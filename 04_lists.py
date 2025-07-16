### lists ###

my_list = list()
my_other_list = []

print(len(my_list))  # Imprime la longitud de la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))  # Imprime la longitud de la lista

my_other_list = [32, 1.76, "Alejandro", "Navarro"]

print(type(my_list))  # Imprime el tipo de la variable
print(type(my_other_list))  # Imprime el tipo de la variable

print(my_other_list[0]) # Imprime el primer elemento de la lista
print(my_other_list[1]) # Imprime el segundo elemento de la lista
print(my_other_list[-1]) # Imprime el último elemento de la lista
print(my_other_list[-3])  # Imprime el cuarto elemento de la lista
print(my_other_list[-4]) # Imprime el tercer elemento de la lista
print(my_other_list[3])  # Imprime los dos primeros elementos de la lista
print(my_list.count(30))  # Cuenta cuántas veces aparece el número 30 en la lista
print(my_other_list.count("Alejandro"))  # Cuenta cuántas veces aparece "Alejandro" en la lista

age, height, name, surname = my_other_list  # Asigna los valores de la lista a variables
print(name)  # Imprime el nombre

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # Asigna los valores de la lista a variables, pero puede cambiar el orden inicial creando errores
print(age)

print(my_list + my_other_list)  # Concatena las dos listas

print([1, 2, 3, 4]) # Imprime una lista de números del 1 al 4
#print(my_list - my_other_list)  # Resta las dos listas, lo cual no es válido y generará un error

my_other_list.append("Navarro")
print(my_other_list)  # Imprime la lista después de agregar "Navarro"

my_other_list.insert(1, "Azul")  # Inserta "Azul" en la posición 1 de la lista
print(my_other_list)

my_other_list [1] = "Rojo"  # Cambia el valor en la posición 1 de la lista a "Azul"
print(my_other_list)  # Imprime la lista después de cambiar el valor

my_other_list.remove("Rojo")  # Elimina "Rojo" de la lista
print(my_other_list)  # Imprime la lista después de eliminar "Rojo"

my_list.remove(30)  # Elimina la primera aparición del número 30 de la lista
print(my_list)  # Imprime la lista después de eliminar el número 30

print(my_list.pop())
print(my_list)  

my_pop_element = my_list.pop(2)  # Elimina y devuelve el elemento en la posición 2 de la lista
print(my_pop_element)  # Imprime el elemento eliminado
print(my_list)

del my_list[2]
print(my_list)  # Elimina el elemento en la posición 2 de la lista

my_new_list = my_list.copy()

my_list.clear()  # Elimina todos los elementos de la lista
print(my_list)  # Imprime la lista después de eliminar todos los elementos
print(my_new_list)  # Imprime la copia de la lista original

my_new_list.reverse()  # Invierte el orden de los elementos en la lista y la imprime
print(my_new_list)  # Imprime la lista invertida

my_new_list.sort()  # Ordena la lista en orden ascendente
print(my_new_list)  # Imprime la lista ordenada

print(my_new_list[1:2])  # Imprime una porción de la lista, desde el índice 1 hasta el índice 2 (exclusivo)

my_list = "Hola Python"
print(my_list)  # Imprime el contenido de my_list, que ahora es una cadena de texto
print(type(my_list))  # Imprime el tipo de la variable, que ahora es str