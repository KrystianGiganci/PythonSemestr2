"""
Należy napisać program, który z listy pokaże nam najmniejszą
i największą liczbę.

Uwaga!
Nie korzystamy z gotowych funkcji min()/max(), tylko tworzymy własne.
"""


def find_min_max(lista):
    max_num = lista[0]
    min_num = lista[0]
    # TODO
    return max_num, min_num


lista = [4, 1, 4, 5, 6, 6, -4]
max_num, min_num = find_min_max(lista)
print(f'Największa liczba to: {max_num}.')
print(f'Najmniejsza liczba to: {min_num}.')
