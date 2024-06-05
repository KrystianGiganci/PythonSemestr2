import random

my_list = []

for i in range(20):
    my_list.append(random.randint(1, 100))  # losowa liczba z zakresu 1-100


def bubble_sort(my_list):
    n = len(my_list)
    licznik_krokow = 0
    for j in range(n):
        for i in range(n-1):
            licznik_krokow += 1
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    # print(licznik_krokow)
    return my_list

# print(my_list)
sorted_list = bubble_sort(my_list)
print(sorted_list)
