#Задача №12. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")


print('\nСловарь:', {x: 3 * x + 1 for x in range(1,
      int(input('Задайте количество элементов последовательности: '))+1)}, '\n')