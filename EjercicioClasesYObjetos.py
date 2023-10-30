from Motocicleta import Motocicleta

moto_1 = Motocicleta("Moto1", "Negro ", 10, 2, "Rand_Brand", "Rand_Model", " ", " ", " " )
moto_2 = Motocicleta("Moto2", "Rojo ", 10, 2, "Rand_Brand2", "Rand_Model2", " ", " ", " " )
moto_1.arrancar()
moto_1.detener()
moto_1.price = "1234"
print("El precio de la motocicleta", moto_1.brand, ",", moto_1.model, "es de: $", moto_1.price)

moto_1.conocer_precio()
moto_2.conocer_precio() #No puede devolver este atributo, ya que no se le ha asignado a moto_2