### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String  \n escapado"
print(my_scape_string)

#Formateo

name, surname, age = "Alejandro", "Navarro", 32

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Formateo con .format()
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Formateo con %s y %d
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Concatenación de cadenas
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #f-string

#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División 

language_slice = language[1:3]
print(language_slice) # Desde el índice 1 hasta el 3 (sin incluir el 3)

language_slice = language[1:]
print(language_slice) # Desde el índice 1 hasta el final

language_slice = language[-2]
print(language_slice) # Desde el índice -2 (segundo desde el final)

language_slice = language[0:6:2] 
print(language_slice) # Desde el índice 0 hasta el 6, saltando de 2 en 2

#Reverse

reversed_language = language[:: -1]
print(reversed_language)  # Invierte la cadena

#Funciones

print(language.capitalize()) #Convierte la primera letra en mayúscula
print(language.upper()) #Convierte toda la cadena en mayúsculas
print(language.count("t")) #Cuenta cuántas veces aparece la letra "t"
print(language.isnumeric()) #Comprueba si la cadena es numérica
print("1".isnumeric()) #Comprueba si la cadena "1" es numérica
print(language.lower()) #Convierte toda la cadena en minúsculas
print(language.upper().isupper()) #Comprueba si toda la cadena está en mayúsculas
print(language.startswith("Py")) #Comprueba si la cadena comienza con "Py"
print("Py" == "py") #no es lo mismo, diferencia entre mayúsculas y minúsculas