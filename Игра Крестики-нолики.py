#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def turn_check():
    while True:
        try:
            choise = int(input())            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if 0 <= choise <= 8:
                return choise
            print("Нужно ввести целое положительное число от 0 до 8! Попробуйте снова.")
    

class Game:
    
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = [i for i in range(board)]
        
    def draw_board(self):
        print('Текущая ситуация')
        print('-'*13)
        for i in range(3):
            print('|', self.board[0+i*3], '|', self.board[1+i*3], '|', self.board[2+i*3], '|')
            print('-'*13)
    
    def turn1(self):
        print(f'{self.player1}, ваш ход. Введите номер незанятого поля ')
        while 1 == 1:
            choise = turn_check()
            if self.board[choise] != 'o' and self.board[choise] != 'x':
                self.board[choise] = 'x'
                break
            else:
                print('Это поле занято! Попробуйте снова')
                continue
                
    def turn2(self):
        print(f'{self.player2}, ваш ход. Введите номер незанятого поля ')
        while 1 == 1:
            choise = turn_check()
            if self.board[choise] != 'o' and self.board[choise] != 'x':
                self.board[choise] = 'o'
                break
            else:
                print('Это поле занято! Попробуйте снова')
                continue
        
    def check(self):
        if self.board[0] == self.board[1] == self.board[2] or self.board[3] == self.board[4] == self.board[5] or self.board[6] == self.board[7] == self.board[8] or self.board[0] == self.board[3] == self.board[6] or self.board[1] == self.board[4] == self.board[7] or self.board[2] == self.board[5] == self.board[8] or self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            return 'WIN'
            
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

print('Правила: два игрока ходят по очереди. Первый ставит "х", второй ставит "о". Кто поставит 3 в ряд, тот победил')
choise = new_game()
while choise == 1:
    game = Game(input('Введите имя первого игрока '), input('Введите имя второго игрока '), 9)
    check = 0
    counter = 0
    game.draw_board()
    while check != 'WIN':
        game.turn1()
        counter += 1
        game.draw_board()
        if counter >= 5:
            check = game.check()
        if check == 'WIN':
            print(f'{game.player1} WIN')
            break
        if counter == 9:
            print('Ничья!')
            break
        game.turn2()
        counter += 1
        game.draw_board()
        if counter >= 5:
            check = game.check()
        if check == 'WIN':
            print(f'{game.player2} WIN')
    choise = new_game()   

print('Всего доброго!')

        
     
        
        
        
        
        


# In[ ]:





# In[ ]:




