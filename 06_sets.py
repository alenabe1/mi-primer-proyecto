### Sets ###

my_set = set()
my_other_set ={}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Alejandro", "Navarro", 32}
print(type(my_other_set)) #Ahora es un set, ya que una vez que se asigna un valor, se convierte en un set

print(len(my_other_set))  # Imprime la longitud del set

my_other_set.add("alenabe")  # Agrega un elemento al set
print(my_other_set)  # un set no es una estructura ordenada, por lo que no se puede acceder a un elemento por su índice

my_other_set.add("alenabe") #Un set no permite elementos duplicados, por lo que no se agregará de nuevo "alenabe"
print(my_other_set)

print("alenabe" in my_other_set)  # Comprueba si "alenabe" está en el set
print("alanabe" in my_other_set)  # Comprueba si "alanabe" está en el set, lo cual no es cierto

my_other_set.remove("alenabe")  # Elimina "alenabe" del set
print(my_other_set)  # Imprime el set después de eliminar "alenabe"

my_other_set.clear()
print(len(my_other_set))  # Imprime el set después de eliminar todos los elementos

del my_other_set  # Elimina el set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Alejandro", "Navarro", 32}
my_list = list(my_set)
print(my_list)  # Convierte el set en una lista y la imprime
print(my_list[0])  # Imprime el primer elemento de la lista, no es ordenado, por lo que no se puede garantizar que sea "Alejandro"

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)  # Une dos sets y crea un nuevo set
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScipt", "C#"}))  # Imprime el set resultante de unir varios sets e ignora duplicados

print(my_new_set.difference(my_set))  # Imprime los elementos que están en my_new_set pero no en my_set