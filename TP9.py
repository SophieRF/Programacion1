#1
from People import People
per1 = People()
per1.name = str(input("Ingrese su nombre: "))
per1.age = int(input("Ingrese su edad: "))
per1.dni = int(input("Ingrese su DNI: "))
per1.show()
if per1.adult()==True:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#2
from People import People
from Account import Account

person1 = People('Carlos',54,24505612)
client1 = Account(person1)
client1.mostrar()
client1.ingresar(500.5)
client1.mostrar()
client1.ingresar(-500)
client1.mostrar()
client1.retirar(100)
client1.mostrar()


#3
from Triangulo import Triangulo

ingreso1 = int(input("Coloque el valor del primer lado: "))
ingreso2 = int(input("Coloque el valor del segundo lado: "))
ingreso3 = int(input("Coloque el valor del tercer lado: "))

triang1 = Triangulo(ingreso1, ingreso2, ingreso3)

#Accedemos a los atributos del objeto
print(f' Valor lado 1: {triang1.lado1}, Valor lado 2: {triang1.lado2}, Valor lado 3: {triang1.lado3}')


triang1.imprimir_lado_mayor()
triang1.determinar_tipo_triangulo()

#4
from Agenda import *

agenda1 = Agenda()

while True:
    print("\n*** Agenda de Contactos ***")
    print("1. Agregar contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    opcion = input("Elija una opción (1/2/3/4/5): ")


    if opcion == "1":
        name = input("Nombre del contacto: ")
        phone = input("Teléfono del contacto: ")
        email = input("Email del contacto: ")
        agenda1.agregar_contacto(name, phone, email)

    elif opcion == "2":
        agenda1.listar_contactos()

    elif opcion == "3":
        name_to_search = input("Ingrese el nombre que desea buscar: ")
        agenda1.buscar_contacto(name_to_search)

    elif opcion == "4":
        name_to_edit = input("Nombre del contacto a editar: ")
        new_phone = input("Nuevo teléfono: ")
        new_email = input("Nuevo email: ")
        agenda1.editar_contacto(name_to_edit, new_phone, new_email)

    elif opcion == "5":
        agenda1.cerrar_agenda()
        break

    else:
        print("Opción no válida")

