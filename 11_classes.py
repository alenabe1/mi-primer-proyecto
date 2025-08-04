### classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name # Propiedad privada

    def get_name ():
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Alejandro", "Navarro")
print(my_person.full_name)
print(my_person.get_name)
my_person.walk()

my_other_person = Person("Alejandro", "Navarro", "alenabe")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Noelia Ballester (Lia)"
print(my_other_person.full_name)

my_other_person.full_name = 777
print(my_other_person.full_name)