import random
status = True
a = random.randint(1, 9)
podejścia = 1
while status == True:
    b = input("Podaj liczbe z przedziału od 1 do 9")

    if b == a:
        print("Zgadłes! Potrzebowałeś " + str(podejścia) + " ruchów!")
        decyzja = input("Chcesz grać dalej? wpisz tak lub nie")
        if decyzja == 'nie':
            print("Koniec gry")
            status = False
        elif decyzja == 'tak':
            a = random.randint(1, 9)
    elif b < a:
        print("Liczba ktorej szukasz jest wieksza!")
        podejścia +=1
    elif b > a:
        print("Liczba ktorej szukasz jest mniejsza!")
        podejścia += 1
