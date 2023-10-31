#1
class People:
    def _init_(self, name='', age=0, dni=0):
        self.__name=name
        self.__age=age
        self.__dni=dni


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,dni):
        self.__dni = dni

    def show(self):
        print(f'Nombre: {self.name}, Edad: {self.age}, DNI: {self.dni}')

    def adult(self):
        if self.age>17:
            return True
        else:
            return False

#2
class Account:

    def __init__ (self,titular,cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad


    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular


    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad


    def mostrar(self):
        print(f'Titular: {self.titular.name}\nCantidad: ${self.cantidad}')


    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad += cantidad

    def retirar(self,cantidad):
        self.__cantidad -= cantidad


#3
class Triangulo:
    def __init__(self, lado1, lado2, lado3):

        #Atributos de instancia
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        max_lado = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {max_lado}")


    def determinar_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")


#4
class Agenda:
    def __init__(self):
        self.contactos = []


    def agregar_contacto(self, name, phone, email):
        nuevo_contacto = {
            'nombre': name,
            'telefono': phone,
            'email': email
        }
        self.contactos.append(nuevo_contacto)
        print("Contacto agregado.")


    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía")
        else:
            for i, contacto in enumerate(self.contactos):
                print(f"{i + 1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")


    def buscar_contacto(self, name):
        encontrado = False
        for contacto in self.contactos:
            if contacto['nombre'] == name:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                encontrado = True
                break
        if not encontrado:
            print(f"Contacto con nombre '{nombre}' no encontrado.")


    def editar_contacto(self, name, new_phone, new_email):
        encontrado = False
        for contacto in self.contactos:
            if contacto['nombre'] == name:
                contacto['telefono'] = new_phone
                contacto['email'] = new_email
                print("Contacto editado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print(f"Contacto con nombre '{name}' no encontrado.")


    def cerrar_agenda(self):
        print("Agenda cerrada.")
