"""
Program ma zliczyć ile danych liter znajduje się w zdaniu
Przykładowe wyświetlanie:

ABC przykładowy tekst na potrzeby naszego programu
Slowa: 7 Litery: 44 ilość liter: {'a': 5, 'b': 2, 'c': 1, 'p': 3, 'r': 4,
'z': 3, 'y': 3, 'k': 2, 'l': 1, 'd': 1, 'o': 4, 'w': 1, 't': 3, 'e': 3,
's': 2, 'n': 2, 'g': 2, 'm': 1, 'u': 1}
"""


def count_letters(text):
    words = 1
    letters = 0
    dictionary = {}
    for letter in text:
        letter = letter.lower()
        if letter == ' ':
            words += 1
        else:
            letter += 1
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1

    print(f'Liczba słów: {words}, liczba liter: {letters}')


text = "ABC przykładowy tekst na potrzeby naszego programu"
count_letters(text)
