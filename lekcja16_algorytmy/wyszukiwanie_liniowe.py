import random

my_list = []

for i in range(20):
    my_list.append(random.randint(1, 100))  # losowa liczba z zakresu 1-100

def linear_search(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i

print(my_list)
print(linear_search(my_list, 14))