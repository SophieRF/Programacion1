class Motocicleta:
    state = "0 km"
    engine = False

    def __init__(self, color, license_plate, fuel_liters, number_wheels, brand, model, manufacturing_date, top_speed, weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.number_wheels = number_wheels
        self.brand = brand
        self.model = model
        self.manufacturing_date = manufacturing_date
        self.top_speed = top_speed
        self.weight = weight

    def arrancar(self):
        if self.engine == False:
            self.engine = True
            print("El motor ha arrancado")
        else:
            print("El motor ya se encuentra en marcha")

    def detener(self):
        if self.engine == True:
            self.engine = False
            print("El motor se ha detenido")
        else:
            print("El motor ya esta detenido")

    def conocer_precio(self):
        print(f'El precio de la motocicleta {self.brand} {self.model} es de ${self.price}.')