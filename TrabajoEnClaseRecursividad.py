#EJERCICIO 1
import random
def rat_jail(minutes, choice):
    new_choice = random.randint(1,3)
    if choice == 3:
        minutes += 7
        return "Salió de la jaula! Ha tardado: " + str(minutes) + " minutos"
    elif choice == 1:
        return rat_jail(minutes + 3 , new_choice)
    elif choice == 2:
        return rat_jail(minutes + 5, new_choice)

rand_paths = random.randint(1, 3)
time = 0
total_time = rat_jail(time, rand_paths)
print(total_time)

# EJERCICIO 2

def f(n):
    n=str(n)
    if len(n)<=1:
        return n
    return n[-1] + f(int(n[:-1]))

num = int(input("Ingrese un numero: "))
print(f(num))

