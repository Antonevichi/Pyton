#33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from pydoc import replace
import random
k=2
lst = list()
lst_1=list()
def rand():                     
    r = random.randint(0, 101) 
    return r
def create_list(lst):              
    values = 3
    while values > 0:
        lst.append(rand())
        values= values - 1
    return lst
def polynominal(lst):             
    n = lst[0], '*x^2 +', lst[1],'*x + ',lst[2], '=', 0
    n = str(n)
    n_str = n.replace(",","").replace("'","").replace("(","").replace(")","")
    return n_str
create_list(lst)
create_list(lst_1)
print(polynominal(lst))
with open('polynom.txt', 'w') as data:
   data.write(polynominal(lst))