player1 = input("Первый игрок, представьтесь")
player2 = input("Второй игрок, представьтесь")


def new_game():
    while True:
        try:
            choice1 = int(input("Сыграем? Если да - введите 1, если нет - введите 0 "))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if 0 <= choice1 <= 1:
                return choice1
            print("Нужно ввести 1 или 0! Попробуйте снова.")


def table_stick():
    while True:
        try:
            choise2 = int(input("Введите количество палочек для игры (целое положительное число)"))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if 1 <= choise2:
                return choise2
            print("Нужно ввести целое положительное число! Попробуйте снова.")


def take_stick(player):
    while True:
        try:
            stick1 = int(input("{}, берите палочки. Введите число от 1 до 3 ".format(player)))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if 1 <= stick1 <= 3:
                return stick1
            print("Нужно ввести число от 1 до 3! Попробуйте снова.")


print('Правила: ходят по очереди, нужно взять одну, две или три палочки, кто возьмет последнюю, тот проиграл')

choise = new_game()
while choise == 1:
    table = table_stick()
    while table > 0:
        print(f'осталось {table} палочек')
        stick = take_stick(player1)
        table -= stick
        if table > 0:
            print(f'осталось {table} палочек')
            stick = take_stick(player2)
            table -= stick
        else:
            print(f'{player1}, вы проиграли')
            break
    else:
        print(f'{player2}, вы проиграли')
    choise = new_game()

print('Всего доброго!')
