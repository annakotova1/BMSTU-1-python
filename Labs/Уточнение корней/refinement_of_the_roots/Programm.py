from Input import input_all_data
from Solve2 import solve
from math import sin
from Output import output_results

# Данные для подсчета:
# 0,1 - отрезок разбиения,
# 2 - шаг,
# 3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
# 4 - максимальное кол-во иттераций

def f(x):
    y = sin(x)
    return y


Data = input_all_data()
try:
    Results = solve(f, Data)
except ZeroDivisionError:
    print('Функция должна быть непрерывна и определена на заданном отрезке!!!')
else:
    output_results(Results)
print()
input('Нажмите Enter, чтобы выйти.')

