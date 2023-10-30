#TP8
#1

num=int(input("Ingrese un numero: "))
print("Cantidad de digitos:",tp8_fun.dig(num))

#2

'''Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.'''
import funct
num_b = int(input("Ingrese un número entero: "))
num_n = int(input("Ingrese otro número entero para verificar si es potencia del anterior: "))


result = funct.num_power(num_b, num_n)
print(result)

#3

string_a = "Hola que tal como estas"
string_b = "a"
print(funciones.positions_strings(string_a, string_b))


# 4

import funciones


# Ejercicio 4
while True:
    num = int(input("Ingrese un numero natural: "))
    if num<1:
        print("Ingrese un numero natural.")
    else:
        break
if funciones.even(num) == True:
    print ("El numero es par")
else:
    print("El numero es impar")

#5
import funciones


numbers_list = []
while True:
    number = int(input('Ingrese numeros enteros a la lista (0 para terminar): '))
    if number == 0:
        break
    else:
        numbers_list.append(number)


print(numbers_list)
position=0
greater_num = 0
print(f'El mayor numero ingresado es {funciones.greater_element(numbers_list,position,greater_num)}')

#6

import funciones


# Ejercicio 6
numbers_list = [1,2,3,4,5,6,7]
new_list=[]
print(numbers_list)
repeat_n_times = int(input('Cuantas veces quiere replicar los elementos de la lista?: '))
size = len(numbers_list)


funciones.repeat(numbers_list,repeat_n_times,new_list)


print(new_list)

#7

while True:
    n=int(input("Ingrese un numero n: "))
    p=int(input("Ingrese un numero p: "))
    if n>0 and p>0:
        break
    else:
        print("No puede ingresar 0")
print("Resultado:",tp8_fun.mul(n,p))

#8
import funciones


row = int(input("Coloque el valor de la fila: "))
column = int(input("Coloque el valor de la columna: "))
result = funciones.pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} es: {result}")

# 9
char_list= []
while True:
    characters = input('Ingrese distintos caracteres (0 para terminar): ')
    if characters == '0':
        break
    else:
        char_list.append(characters)


len_combination = int(input('Ingrese la longitud de las cadenas a combinar: '))


print(funciones.combinations(char_list, len_combination))



#10
paper = int(input("Ingrese el numero de la hoja: A"))
print("Las medidas de las hojas A",paper,"son:",tp8_fun.sheet(paper))

#FUNCIONES
#1 fun
def dig(num,coun=0):
    while True:
        if num<1:
            if coun==0:
                coun= coun+1
                return coun
            return coun
        else:
            num=num//10
            coun= coun+1
            return dig(num,coun)

#2 fun

def num_power(num_b, num_n):

    if num_n < num_b:
        return False
    if num_n == num_b:
        return True
    if num_n % num_b == 0:
        return num_power(num_b,(num_n//num_b))
    return False

#3 fun
def positions_strings(a, b, start=0, result=None):
    if result is None:
        result = []


    index = a.find(b, start)
    if index != -1:
        result.append(index)
        positions_strings(a, b, index + 1, result)
    return result

# 4 funciones
def even(num):
    if num == 0:
        return True
    else:
        return odd(num-1)


def odd(num):
    if num == 0:
        return False
    else:
        return even(num-1)

#5 fun

def greater_element(numbers_list, position,greater_number):
    if position==len(numbers_list):
        return greater_number
    else:
        if position == 0:
            greater_number = numbers_list[0]
            return greater_element(numbers_list,position+1,greater_number)
        else:
            if greater_number<numbers_list[position]:
                greater_number = numbers_list[position]
                return greater_element(numbers_list,position+1,greater_number)
            else:
                return greater_element(numbers_list,position+1,greater_number)


# 6 funciones
def repeat(li,times,new_li):
    counter=len(li)
    if times==0:
        return new_li.sort()
    else:
        add_elements(li,counter,times,new_li)



def add_elements(li,counter,times,new_li):
    if counter == 0:
        repeat(li,times-1,new_li)
    else:
        element = li[len(li)-counter]
        new_li.append(element)

        add_elements(li,counter-1,times,new_li)

# 7 fun
def mul(n,p,res=0):
    while True:
        if n==0:
            return res
        else:
            res=res+(p*n)
            n=n-1
            return mul(n,p,res)

# 8 fun
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)


#9 fun

def combinations(lista, k, prefix=""):
    if k == 0:
        print(prefix)
        return
    for char in lista:
        combinations(lista, k - 1, prefix + char)


# 10 fun
def sheet(paper,a=0,long=841,broad=1189):
    while True:
        if a==paper:
            return long,broad
        else:
            a=a+1
            if a%2==0:
                long=long//2
            else:
                broad=broad//2
            return sheet(paper,a,long,broad)