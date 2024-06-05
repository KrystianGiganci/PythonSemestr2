import random
from sortowanie_babelkowe import bubble_sort

my_list = []

for i in range(30):
    my_list.append(random.randint(1, 100))  # losowa liczba z zakresu 1-100


def binary_search(lista, x):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high:
        mid = (low+high) // 2

        if lista[mid] > x:
            high = mid
        elif lista[mid] < x:
            low = mid
        elif lista[mid] == x:
            return mid


my_list = bubble_sort(my_list)
print(binary_search(my_list, 40))