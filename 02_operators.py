### Operadores Aritméticos ###

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División 
print(10 % 3) # Módulo (resto de la división)
print(10 // 3) # División entera (sin decimales)
print(2 ** 3) # Potencia (2 elevado a 3)
print(2 ** 3 + 3 - 7 / 1 // 4) # Operaciones combinadas

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5)) 
print("Hola " * 5) # Repite la cadena 5 veces
print("Hola " * (2 ** 3)) # Repite la cadena 8 veces
## print("Hola " * (2.5 * 2)) # Error porque da 5.0 ##

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(3 <= 4) # Menor o igual que
print(3 == 4) # Igual que
print(3 != 4) # Diferente de

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) #Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") # AND lógico
print(3 > 4 or "Hola" > "Python") # OR lógico
print(3 < 4 or "Hola" < "Python") # OR lógico (otro ejemplo)
print(3 < 4 and ("Hola" < "Python" and 4 == 4)) 
print(not (3 > 4)) # NOT lógico