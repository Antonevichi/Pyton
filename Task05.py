#Задача №05. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
import os
os.system("cls")

n = abs(int(input('Введите любое целое число: ')))

print(bool(((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and n % 30 != 0))

print('\n')