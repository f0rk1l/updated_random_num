from random import randint
from pyautogui import alert, prompt, confirm
import os 
from colorama import init, Fore
import sys
##

init()
##

balance_color = confirm(text='выберите цвет текста',
						title='выбор цвета текста',
						buttons=['Красный', 'Зелёный', 'Белый'])

balance = 0

if balance_color == 'Красный':
	while True:

		os.system('color 4')
		os.system('cls')

		random_num = randint(1, 3)

		print(f'ваш баланс равен {balance}')

		num = prompt(text='введите число\n(введите "exit")',
			         title='ввод пароля')

		if num == "exit":
			alert(text='спасибо за игру!')
			os.system('color 7')
			os.system('cls')
			sys.exit()

		elif num == str(random_num):

			balance += 10
			alert(text=f'поздравляю! вы выиграли',
				  title='вы выиграли!')

		elif num != str(random_num):

			balance -= 10
			alert(text='вы проиграли',
				  title='вы проиграли')

elif balance_color == 'Зелёный':
	while True:

		os.system('color 2')
		os.system('cls')

		random_num = randint(1, 3)

		print(f'ваш баланс равен {balance}')

		num = prompt(text='введите число\n(введите "exit")',
			         title='ввод пароля')

		if num == "exit":
			alert(text='спасибо за игру!')
			os.system('color 7')
			os.system('cls')
			sys.exit()

		elif num == str(random_num):

			balance += 10
			alert(text=f'поздравляю! вы выиграли',
				  title='вы выиграли!')

		elif num != str(random_num):

			balance -= 10
			alert(text='вы проиграли',
				  title='вы проиграли')

if balance_color == 'Белый':
	while True:
		
		os.system('color 7')
		os.system('cls')

		random_num = randint(1, 3)

		print(f'ваш баланс равен {balance}')

		num = prompt(text='введите число\n(введите "exit")',
			         title='ввод пароля')

		if num == "exit":
			alert(text='спасибо за игру!')
			os.system('cls')
			sys.exit()

		elif num == str(random_num):

			balance += 10
			alert(text=f'поздравляю! вы выиграли',
				  title='вы выиграли!')

		elif num != str(random_num):

			balance -= 10
			alert(text='вы проиграли',
				  title='вы проиграли')