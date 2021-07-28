#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Давай сыграем в камень-ножницы-бумага! Ты должен выбрать 'r' - камень/rock, 's' - ножницы/scissors или 'p' - бумага/paper. Все ясно? Поехали!")
variant = ['r', 's', 'p']

def new_game():
    while True:
        try:
            choise = int(input("Сыграем? Если да - введите 1, если нет - введите 0 "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if 0 <= choise <= 1:
                return choise
            print("Нужно ввести 1 или 0! Попробуйте снова.")

choise = new_game()
while choise == 1:
    var_comp = random.choice(variant)
    var_user = input('Выберите ваш вариант ')
    if var_user not in ['r', 's', 'p']:
        print ('Некорректный ввод, давайте снова')
        continue
    print('Мой вариант {}'.format(var_comp))
    if var_comp == var_user:
        print("Ничья!")
    elif var_comp == 'r' and var_user == 's' or var_comp == 's' and var_user == 'p' or var_comp == 'p' and var_user == 'r':
        print("Я победил! Ихххууу!")
    else:
        print("Ooo...я проиграл :(")          
    choise = new_game()
    
print('Всего доброго!')


# In[ ]:




