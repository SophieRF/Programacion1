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