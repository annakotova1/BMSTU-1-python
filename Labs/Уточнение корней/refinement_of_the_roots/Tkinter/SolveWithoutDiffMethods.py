from scipy.misc import derivative
from scipy.optimize import newton as lib_newton
from time import time
from math import fabs

#Данные для подсчета:
#0,1 - отрезок разбиения,
#2 - шаг,
#3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
#4 - максимальное кол-во иттераций


#Метод Ньютон

def newton(f, a, b, eps, m_i):
    error = 0
    x1 = a
    x2 = b
    
    if eps[0] == '1':
        con = eps[1] < fabs(x1-x2)
    elif eps[0] == '2':
        con = float(eps[1]) < f(x2)
    else:
        con = (float(eps[1]) < fabs(x1-x2)) and (float(eps[1]) < f(x2))
    i = 0
    while con:
        '''print(x2, end = '  ')
        print(x1, x2, f(x2), dif_f(f,x2), end = '  ')
        print()'''
        i += 1
        x1 = x2
        x2 = x1 - f(x1)/dif_f(f,x1)
        if eps[0] == '1':
            con = eps[1] < fabs(x1-x2)
        elif eps[0] == '2':
            con = float(eps[1]) < f(x2)
        else:
            con = (float(eps[1]) < fabs(x1-x2)) and (float(eps[1]) < f(x2))
        if x2>b:
            newton(f, b, a, eps, m_i)
            break
        if i>m_i:
            error = 1
            break

    #print('\n')
    return x2, i, error

#Время метода Ньютона
def time_n(fun, f, a, b, eps, m_i):
    n = 250
    t1 = time()
    for i in range(n):
        fun(f, a, b, eps, m_i)
    t2 = time()
    t = t2-t1
    return t

#Проверка на деление на 0
def CheckValue(f,a):
    try:
        f(a)
    except ZeroDivisionError:
        a += 0.000000001

#Решение уравнения и формирование результатов
def solve(f, data):
    results = []
    a = data[0]
    end = data[1]
    sh = data[2]
    
    while a < end:
        
        b = a+sh
        CheckValue(f,a)
        CheckValue(f,b)
        
        if b>end:
            b == end
        if f(a)*f(b)>0:
            a = b
            continue
        
        diapazon = [a, b]
        
        x_n, i_n, e_n = newton(f, a, b, data[3], data[4])

        y_n = f(x_n)

        t_n = time_n(newton, f, a, b, data[3], data[4])

        result = [diapazon, x_n, y_n, i_n, t_n, e_n]
        
        results.append(result)
        a = b

    return results
