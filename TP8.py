# EJERCICIO 1
import tp7_fun


list_num=tp7_fun.list_assembly()


list_num1=list_num.copy()
print(tp7_fun.ejer1(list_num1))



# EJERCICIO 2
def selection_sort_words(word):
    len_word = len(word)

    for i in range(len_word - 1):
        # Suponemos que el elemento actual es el mínimo
        min_index = i

        # Comparamos con el resto de elementos para encontrar el mínimo alfabéticamente
        for j in range(i + 1, len_word):
            if word[j] < word[min_index]:  # Comparamos las cadenas
                min_index = j

        # Intercambiamos el mínimo encontrado con el elemento en la posición i
        word[i], word[min_index] = word[min_index], word[i]


# Ejemplo de uso
list_ordered = ["Sofi", "Arnold", "Camila", "Gian", "Gaby"]
selection_sort_words(list_ordered)
print("Palabras ordenadas alfabéticamente:", list_ordered)



# EJERCICIO 3
library = [{'titulo': 'Harry Potter y la Piedra Filosofal', 'autora': 'JK Rowling', 'año de publicacion': '1997'},
        {'titulo': 'Harry Potter y la Camara secreta', 'autora': 'JK Rowling', 'año de publicacion': '1998'},
        {'titulo': 'Harry Potter y el prisionero de Azkaban', 'autora': 'JK Rowling', 'año de publicacion': '1999'},
        {'titulo': 'Harry Potter y el Caliz de fuego', 'autora': 'JK Rowling', 'año de publicacion': '2000'},
        {'titulo': 'Harry Potter y la Orden del Fenix','autora': 'JK Rowling', 'año de publicacion': '2003'}
        ]
year_of_publication = []
for book in library:
        year_of_publication.append(book['año de publicacion'])


print(year_of_publication)


# EJERCICIO 4

import funciones
words = []
while True:
    words_input = input("Ingrese palabras (0 para salir): ")
    if words_input == '0':
        break
    elif words_input.isalpha():
        words.append(words_input)
    else:
        print("Ingrese una palabra.")


funciones.insertionSort(words)
print("Palabras ordenadas en orden ascendente segun su longitud: ", words)


# EJERCICIO 5
list_num5=list_num.copy()
print(tp7_fun.ejer5(list_num5))

# EJERCICIO 6
list_num6=list_num.copy()
print(tp7_fun.ejer6(list_num6))

# EJERCICIO 7

import funciones
words_and_numbers = []
words =[]
numbers = []

while True:
    list_input = input("Ingrese numeros y palabras (0 para salir): ").lower()
    if list_input == '0':
        break
    else:
        words_and_numbers.append(list_input)

for element in words_and_numbers:
    if element.isalpha():
        words.append(element)
    else:
        numbers.append(int(element))


words_and_numbers = funciones.bubbleSort(numbers) + funciones.insertionSort(words)


print("Números ordenados de menor a mayor y cadenas ordenadas alfabéticamente: ", words_and_numbers)


# EJERCICIO 8

import funciones


# Ejercicio 8
import random


while True:
    num = int(input("Ingrese cuantos numeros tendrá la lista (Entre 1 y 20): "))
    if num<1 or num>20:
        print("Ingrese numeros entre 1 y 20.")
    else:
        break


numbers_list = [0]*num


for i in range(num):
    numbers_list[i] = random.randint(1,200)


print("Lista desordenada: ")
for i in numbers_list:
    print(i,end=" ")


print("\nLista ordenada con Merge Sort: ")
funciones.mergeSort(numbers_list)
for i in numbers_list:
    print(i,end=" ")


# FUNCIONES
#cargado de datos de la lista
def list_assembly():
    list_num0=[]
    while True:
        p=int(input("Ingrese un numero (0 para salir): "))
        list_num0.append(p)
        if p==0:
            break
    print (list_num0)
    return list_num0

#1
def ejer1(list_num1):
    n = len(list_num1)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num1[j] > list_num1[j+1]:
                    list_num1[j], list_num1[j+1] = list_num1[j+1], list_num1[j]
    return list_num1

# 4 FUNCIONES

def insertionSort(li):
    n = len(li)

    if n <= 1:
        return li


    for i in range(1, n):
        key = li[i]
        j = i-1
        while j >= 0 and len(key) < len(li[j]):
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key


# 5 FUNCIONES
def ejer5(list_num2):
    n = len(list_num2)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num2[j] < list_num2[j+1]:
                    list_num2[j], list_num2[j+1] = list_num2[j+1], list_num2[j]
    return list_num2

# 6 FUNCIONES
def ejer6(list_num6):
    output = [0 for i in range(len(list_num6))]
    count = [0 for i in range(100)]
    for i in list_num6:
        count[i] += 1
    for i in range(1, 100):
        count[i] += count[i-1]
    for i in range(len(list_num6)):
        output[count[list_num6[i]]-1] = list_num6[i]
        count[list_num6[i]] -= 1
    return output

# 7 FUNCIONES

def insertionSort(word_list):
    if len(word_list) <= 1:
        return word_list
    else:    
        for i in range(1, len(word_list)):
            key = word_list[i]
            j = i-1
            while j >= 0 and key < word_list[j]:
                word_list[j+1] =  word_list[j]
                j -= 1
            word_list[j+1] = key
        return word_list




def bubbleSort(number_list):
    n = len(number_list)

    swapped = False

    for i in range(n-1):

        for j in range(0, n-i-1):
            if number_list[j] > number_list[j + 1]:
                swapped = True
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
        if not swapped:
            return number_list


# 8 FUNCIONES

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]


        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)


        # Fusiona las mitades ordenadas
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1


        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1


        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Crear una lista vacía para almacenar los números ingresados por el usuario
list_numbers_original = []


while True:
    number = int(input("Ingrese un número entero. Pulse 0 para salir: "))
    if number == 0:
        break
    else:
        list_numbers_original.append(number)


# Imprimir la lista original
print("Lista original:", list_numbers_original)


# Aplicar Merge Sort a la lista de números ingresados
merge_sort(list_numbers_original)


# Imprimir la lista ordenada
print("Lista ordenada:", list_numbers_original)



def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

