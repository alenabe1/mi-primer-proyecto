### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))  # Imprime el tipo de la variable
print(type(my_other_dict))  # Imprime el tipo de la variable

my_other_dict = {"Nombre": "Alejandro", "Apellido": "Navarro", "Edad": 32, 1: "Python"}

my_dict = {
    "Nombre":"Alejandro",
    "Apellido":"Navarro",
    "Edad":32,
    "Lenguajes":{"Python","Swift", "Kotlin"},
    1:1.76
}

print(my_other_dict)  # Imprime el diccionario
print(my_dict)  # Imprime el diccionario

print(len(my_other_dict))  # Imprime la longitud del diccionario
print(len(my_dict)) # Imprime la longitud del diccionario

my_dict["Nombre"] = "alenabe"  # Cambia el valor de la clave "Nombre"
print(my_dict["Nombre"])

print(my_dict[1]) # Imprime el valor asociado a la clave 1

my_dict["Calle"] = "Calle Falsa 123"  # Añade una nueva clave "Calle" con su valor
print(my_dict)  # Imprime el diccionario después de añadir la nueva clave

del my_dict["Calle"]
print(my_dict)  # Imprime el diccionario después de eliminar la clave "Calle"

print("Navarro" in my_dict)  # Comprueba si "Navarro" es una clave en el diccionario, así no se obtiene el valor, ya que "Navarro" no es una palabra clave
print("Apellido" in my_dict)  # Comprueba si "Apellido" es una clave en el diccionario
print(my_dict ["Apellido"])  # Imprime el valor asociado a la clave "Apellido"

print(my_dict.items())  # Imprime los pares clave-valor del diccionario
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))  # Crea un nuevo diccionario con claves de la tupla y valores por defecto None
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)  # Imprime el nuevo diccionario con claves de la lista
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)  # Imprime el nuevo diccionario con claves de la lista
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) 
my_new_dict = dict.fromkeys(my_dict, "Navarro")  # Crea un nuevo diccionario con claves del diccionario original y valores por defecto como tupla
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))  # Imprime el tipo de los valores del diccionario

print(my_new_dict.values())  # Imprime los valores del nuevo diccionario
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))  # Convierte los valores del diccionario a una lista sin duplicados
print(tuple(my_new_dict))  # Convierte el diccionario a una tupla
print(set(my_new_dict))  # Convierte el diccionario a un conjunto