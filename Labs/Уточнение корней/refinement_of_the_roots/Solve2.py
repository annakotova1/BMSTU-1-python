from scipy.misc import derivative
from scipy.optimize import newton as lib_newton
from time import time
from math import fabs, cos

#Данные для подсчета:
#0,1 - отрезок разбиения,
#2 - шаг,
#3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
#4 - максимальное кол-во иттераций

# !!!!! Вторая производная !!!!!

def dif_f(fun, x):
    CheckValue(fun,x)
    #print(fun, x)
    return cos(x)#derivative(fun, x)

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

    
def easy_newton(f, a, b, eps, m_i):
    x1 = b
    x2 = a
    if eps[0] == '1':
        con = eps[1] < fabs(x1-x2)
    elif eps[0] == '2':
        con = float(eps[1]) < f(x2)
    else:
        con = (float(eps[1]) < fabs(x1-x2)) and (float(eps[1]) < f(x2))
    
    m = dif_f(f, x2)
    i = 0
    error = 0
    while con:
        i += 1
        x1 = x2
        x2 = x1 - f(x1)/m
        if eps[0] == '1':
            con = float(eps[1]) < fabs(x1-x2)
        elif eps[0] == '2':
            con = float(eps[1]) < f(x2)
        else:
            con = (float(eps[1]) < fabs(x1-x2)) and (float(eps[1]) < f(x2))
        if i > m_i:
            error = 1
            break
    return x2, i, error

def time_n(fun, f, a, b, eps, m_i):
    n = 250
    t1 = time()
    for i in range(n):
        fun(f, a, b, eps, m_i)
    t2 = time()
    t = t2-t1
    return t

def time_l(f, a, b):
    n = 250
    t1 = time()
    for i in range(n):
        lib_newton(f, (a + b)/2)
    t2 = time()
    t = t2-t1
    return t


def CheckValue(f,a):
    try:
        f(a)
    except ZeroDivisionError:
        a += 0.000000001

def solve(f, data):
    results = []
    a = data[0]
    end = data[1]
    sh = data[2]
    while a < end:
        result = [[],[], []]
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
        x_e_n, i_e_n, e_e_n = easy_newton(f, a, b, data[3], data[4])
        x_l_n = lib_newton(f, (a + b)/2)

        y_n = f(x_n)
        y_e_n = f(x_e_n)
        y_l_n = f(x_l_n)

        t_n = time_n(newton, f, a, b, data[3], data[4])
        t_e_n = time_n(easy_newton, f, a, b, data[3], data[4])
        t_l_n = time_l(f, a, b)

        result[0]= [diapazon, x_n, y_n, i_n, t_n, e_n]
        result[1]= [diapazon, x_e_n, y_e_n, i_e_n, t_e_n, e_e_n]
        result[2]= [diapazon, x_l_n, y_l_n, None, t_l_n, 0]
        
        results.append(result)
        a = b

    return results
