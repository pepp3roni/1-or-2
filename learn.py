from random import randint
vibor = int(input("Выбери 1 или 2: "))
cifra = randint(1,2)
if vibor != 1 and vibor != 2:
    print("Я не знаю такое число!")
    exit
elif vibor == cifra:
    print(f"Молодец, ты выбрал число {vibor}, и угадал!")
    exit
else:
    print("Не угадал!")