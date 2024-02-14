import random
import time


gracz = 0
komputer = 0
while True:
    x = input()
    if x == '0':
        break
    elif x == 'o':
        x = "orzeł"
    elif x == 'r':
        x = "reszka"
    else:
        print("Proszę dokonać prawidłowego wyboru:")
        print("o - orzeł")
        print("r - reszka")
        print("0 - zakończenie gry")
        continue
    y = random.choice(["orzeł", "reszka"])
    for i in range(0, 3):
        print(3-i)
        time.sleep(1)
    print("Wynik rzutu: ", y)
    if x == y:
        gracz += 1
    else:
        komputer += 1

    print("Wyniki łącznie.")
    print("Użytkownik: ", gracz)
    print("Komputer: ", komputer)
