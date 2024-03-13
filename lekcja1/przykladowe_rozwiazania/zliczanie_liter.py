tekst = "ABC przykładowy tekst na potrzeby naszego programu"
print(tekst)
slowa = 1
litery = 0
slownik = {}
for znak in tekst:
    znak = znak.lower()
    if znak == ' ':
        slowa += 1
    else:
        litery += 1
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1

print("Slowa:", slowa, "Litery:", litery, "ilość liter:", slownik)
