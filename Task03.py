#Задача №3.	Вывести на экран числа от -N до N
import os
os.system("cls")

n = int(input('Введите любое целое число: '))
m = -n
while m<=n:
    print(m, end=' ')
    m+=1
n = abs(int(input('Введите любое целое число: ')))

for i in range(-n, n+1):
    print(i, end=' ')

print('\n')