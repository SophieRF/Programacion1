#EJERCICIO 1
import funciones  
document_num = input("Ingrese su numero de documento: ")
if ( funciones.document(document_num)):
    print("la longitud es correcta")
else:
    print("longitud incorrecta")

import pytest
from funciones import document
@pytest.mark.parametrize("dni,dni_correct",[
    ("123456",False),
    ("12345678",True),
    ("1234567",True),
])
def test_document(dni, dni_correct):
    assert document(dni) == dni_correct

#ejercicio2
import funciones
chain = str(input("Ingrse una frase: "))
result = funciones.leng_last_word(chain)
print("Longitud de la última palabra:", result)

import pytest
from funciones import leng_last_word
@pytest.mark.parametrize("word, num",[
    ("algo con limon",5),
    ("lala",4),
    ("por el emperador",9),
])
def test_leng_last_word(word,num):
    assert leng_last_word(word) == num

#EJERCICIO #3
import funciones
first_name = input("Ingresar nombre de pila: ")
second_name = input("Ingresar segundo nombre, de no tenerlo ingrese 0: ")
last_name = input("Ingresar apellido: ")
last_name_long = len(last_name)
dni = ""
dni_3_digits = 0
print(funciones.user_name(first_name, second_name, last_name))
dni = input("Ingrese su DNI: ")
while(len(dni) != 7 and len(dni) != 8):
    dni = input("DNI inválido. Ingrese el correcto: ")

dni_3_digits = dni[:3]

final_id = "ID: " + first_name + str(last_name_long) + str(dni_3_digits)
print(final_id)

import pytest
from funciones import user_name
@pytest.mark.parametrize("name1, name2, lastname, fullname",[
    ("juanin","juan","harry","juanin juan harry"),
    ("juan","carlos","bodoque","juan carlos bodoque"),
    ("mario","0","hugo","mario hugo"),
])
def test_user_name (name1, name2, lastname, fullname):
    assert user_name (name1, name2, lastname) == "Nombre del usuario: " + fullname

# EJERCICIO 4
import funciones
number1 = int(input("Ingrese un numero entero: "))
while funciones.data_validation(number1) == False:
    number1 = int(input("Ingrese un numero entero: "))
number2 = int(input("Ingrese otro numero entero: "))
while funciones.data_validation(number2) == False:
    number2 = int(input("Ingrese otro numero entero: "))

multiple = funciones.is_multiple(number1,number2)
if multiple == number1:
    print(number1,"es multiplo de",number2)
elif multiple == number2:
    print(number2,"es multiplo de",number1)
elif multiple == True:
    print("Son multiplos.")
elif multiple == False:
    print("No son multiplos.")
import pytest
from funciones import data_validation, is_multiple

import pytest
from funciones import is_multiple, data_validation
@pytest.mark.parametrize('a,b,res',[
    (8,2,8),
    (5,2,False),
    (10,10,True),
    (3,6,6),
])
def test_is_multiple(a,b,res):
    assert is_multiple(a,b) == res

@pytest.mark.parametrize('a,res',[
(-1,False),
(2,True),
])
def test_data_validation(a,res):
    assert data_validation(a) == res

def test_data_validation(a,res):
    assert data_validation(a) == res

#EJERCICIO 5
import funciones
days = int(input("de cuantos dias desea saber la temperatura media"))

for day in range(days):
    min_tem = int(input("Cual es la temperatura minima?: "))
    max_tem = int(input("Cual es la temperatura maxima?: "))
    print("la temperatura media es ",funciones.temperature_middle(min_tem, max_tem),"º")

import pytest
from funciones import temperature_middle
@pytest.mark.parametrize("min_temperature, max_temperature, med_temperature",[
    (9,8,8.5),
    (10,5,7.5),
    (14,6,10),
])
def test_temperature_middle(min_temperature, max_temperature, med_temperature):
    assert temperature_middle(min_temperature, max_temperature) == med_temperature

#EJERCICIO 6
import funciones
sentence = input("INGRESE FRASE: ")
print("la frase separada es ", funciones.separator(sentence))

import pytest
from funciones import separator
@pytest.mark.parametrize("sentence, sentence_separate",[
    ("algo con limon","a l g o   c o n   l i m o n"),
    ("lala","l a l a"),
    ("por el emperador","p o r   e l   e m p e r a d o r"),
])
def test_separator(sentence, sentence_separate):
    assert separator(sentence) == sentence_separate

# Ejercicio 7
import funciones
num=1
numbers_list = []
while num!=0:
    print("Ingrese sucesivamente numeros enteros (0 para terminar).")
    num=int(input("Numero: "))
    funciones.numbers_list.append(num)

values = funciones.max_min(numbers_list)
print(f'El mayor número de la lista es {values[0]} y el menor es {values[1]}')

import pytest
from funciones import max_min
@pytest.mark.parametrize('list,res',[
    ([1,15,5,-2],[15,-2]),
    ([1,2,3],[3,1]),
])
def test_max_min(list,res):
    assert max_min(list) == res

#ejercicio8
import funciones
radio = float(input("Ingrese el radio del circulo: "))
perimetro = funciones.calculo_perim(radio)
area = funciones.calculo_area(radio)
print("Perimetro:",perimetro)
print("Area:",area)

import pytest
from funciones import calculo_perim, calculo_area
@pytest.mark.parametrize("n,result_per",[
    (3,18.85),
    (5,31.41),
    (23,144.51),
])
def test_calculo_perim(n,result_per):
    assert calculo_perim(n)==result_per
@pytest.mark.parametrize("n,result_are",[
    (3,88.83),
    (5,246374),
    (23,5221.02),
])
def test_calculo_area(n,result_are):
    assert calculo_area(n)==result_are

#EJERCICIO 9
import funciones
attempts = 0

while attempts <= 3:
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")

    if funciones.login(username, password, attempts) is True:
        print("Inicio de sesión exitoso!")
        break
    else:
        attempts = funciones.login(username, password, attempts)
        remaining_attempts = 3 - attempts
        if remaining_attempts > 0:
            print("Inicio de sesión fallido. Intentos restantes: ", remaining_attempts)
        else:
            print("Se han agotado los intentos de inicio de sesión.")
            break


import pytest
from funciones import login
@pytest.mark.parametrize("user_name, password, attempts, result", [("usuario1", "asdasd", 1, True), ("Juan", "Pérez", 3, 4)])
def test_login(username, password, attempts, result):
    result = login(username, password, attempts)
    assert login(username, password, attempts) == result

# EJERCICIO 10
import funciones
shopping_cart = {3500: '20%', 14200: '35%', 5700: '10%', 12000: '20%', 7800: '10%'}


print("Su carrito de compras con precio y descuento a aplicar es:")
print(shopping_cart)


while True:
    choise = input("Presione T para ver el total con el descuento aplicado y C para cancelar la compra: ").upper()
    if choise == 'T':
        total_list = funciones.total(shopping_cart)
        print(f'El total de la compra es: ${total_list[0]}. Con el descuento aplicado es ${total_list[1]}')
        break
    elif choise == 'C':
        print("Compra cancelada")
        break
    else:
        print("Ingrese una opcion correcta")


import pytest
from funciones import total
@pytest.mark.parametrize('dic,res',[
    ({3500: '20%', 14200: '35%', 5700: '10%', 12000: '20%', 7800: '10%'},[43200,33780.0]),
])
def test_total(dic,res):
    assert total(dic) == res

#EJERCICIO 11
import funciones
numbers = [4,2,8,9,6]


print("-- primer lista --")
for number in numbers:
    print(number)


new_numbers = funciones.apply_function(funciones.product, numbers)
print("-- segunda lista --")
for number in new_numbers:
    print(number)


import pytest
from funciones import product, apply_function
@pytest.mark.parametrize("element, result", [(6, 12), (14, 28), (8, 16)])
def test_product(element, result):
    assert product(element) == result


def product(element):
    return element * 2
@pytest.mark.parametrize("product, numbers, result", [(product, [2,4,5], [4,8,10]), (product, [3,5,7], [6,10,14]), (product, [1,12,6], [2,24,12])])
def test_apply_function(product, numbers, result):
    assert apply_function(product, numbers) == result

#EJERCICIO12
import funciones
phrase = input("Ingrese una frase: ")
words = phrase.split(" ")


keys = (funciones.define_keys(words))
print(funciones.transform_dict(words))


import pytest
from funciones import define_keys, transform_dict
@pytest.mark.parametrize("all_keys",[
    ("Buenas tardes"),
])
def test_define_keys(all_keys):
    assert define_keys(all_keys)==all_keys


@pytest.mark.parametrize("all_words, dict_text",[
    (["Buenas"], {"Buenas": 6})
])
def test_transform_dict(all_words,dict_text):
    assert transform_dict(all_words)==dict_text

#EJERCICIO13
import funciones
import math
vector = []
prompt = 1
while (prompt >= 1 and prompt <= 3):
    prompt += 1
    digit = input("Ingrese valor del vector")
    vector.append(digit)


print("El módulo del vector es: " , funciones.vector_module(int(vector[0]), int(vector[1]), int(vector[2])))


import pytest
from funciones import vector_module
@pytest.mark.parametrize("x, y, z, expected_result", [
(0, 0, 0, 0), (3, 4, 0, 5), (-2, -3, -6, 7)])
def test_vector_module(x, y, z, expected_result):
    assert vector_module(x, y, z) == expected_result

#ejercicio14
import funciones
num = int(input("Ingrese un numero: "))
if funciones.es_primo(num) == True:
    print(num,"es un numero primo")
else:
    print(num,"no es un numero primo")


import pytest
from funciones import es_primo
@pytest.mark.parametrize("n, bool",[
    (4,False),
    (9,True),
    (10,False),
])
def test_es_primo(n,bool):
    assert es_primo(n) == bool

#ejercicio15
import funciones
cont=0
while True:
    number=int(input("Ingrese un numero (0 para salir): "))
    cont+=1
    if number == 0:
        print("Has ingresado",cont-1,"numeros")
        break
    else:
        fact5  = funciones.factorial(number)
        print("El factorial de",number,"es:",fact5)


import pytest
from funciones import factorial
@pytest.mark.parametrize("n, fact",[
    (4,24),
    (9,362880),
    (3,6),
])
def test_factorial(n, fact):
    assert factorial(n) == fact

#EJERCICIO 16
import funciones
number = int(input("Ingrese un número entero "))
digit = int(input("Ingrese un digito "))


print("La cantidad de veces que se repite el número ", digit, " es de: ", funciones.frecuency(number, digit))


import pytest
from funciones import frecuency
@pytest.mark.parametrize("number, digit, counter",[
    (23,3,1),
    (277,7,2)
])
def test_frecuency(number,digit,counter):
    assert frecuency(number,digit)==counter

#EJERCICIO17
while True:
    number = int(input('Ingrese un número primo. Para salir, ingrese un no primo '))
    digit = int(input('Ingrese un dígito '))
    #Seccion para saber si el número primo ingresado es el más grande
    major_number = 0
    if number > major_number:
        major_number = number

    #Sección verificación números primos
    counter = 0
    for i in range(1,number+1):
        if number % i == 0:
            counter += 1
    if counter==2:
        print(number,'es primo')
        print('La suma es: ', funciones.addiging_digits(number))
        print('Las veces que se repite el dígito ', digit, ' son ' , funciones.frecuency(number, digit), ' veces')
    else:
        print("No es un número primo")
    break                

#Sacar el factorial del mayor primo ingresado
factorial = 1
for i in range (1, major_number + 1):
    factorial *= 1


print(f"El factorial de {major_number} es {factorial}")


import pytest
from funciones import addiging_digits
@pytest.mark.parametrize("number,add_numbers",[
    (23,5),
    (7,7),
])
def test_addiging_digits(number,add_numbers):
    assert addiging_digits(number)==add_numbers
