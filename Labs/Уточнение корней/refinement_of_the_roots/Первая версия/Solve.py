from scipy.misc import derivative
from time import time
from math import fabs



#Данные для подсчета:
#0,1 - отрезок разбиения,
#2 - шаг,
#3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
#4 - максимальное кол-во иттераций


def dif_f(fun, x):
    return derivative(fun, x)



def newton(data, f):
    error = 0
    x1 = data[0]
    x2 = data[1]
    if '1' in data[2][0]:
        con = data[2][1] < fabs(x1-x2)
    if '2' in data[2][0]:
        con = data[2][1] < f(x2)
    i = 0
    while con:
        i += 1
        x1 = x2
        x2 = x1 - f(x1)/dif_f(f,x1)
        if '1' in data[2][0]:
            con = data[2][1] < fabs(x1 - x2)
        if '2' in data[2][0]:
            con = data[2][1] < f(x2)
        if i>data[3]:
            error = 1
            break
    return x2, i, error


def easy_newton(data, f):
    x1 = data[0]
    x2 = data[1]
    if '1' in data[2][0]:
        con = data[2][1] < fabs(x1-x2)
    if '2' in data[2][0]:
        con = data[2][1] < f(x2)
    m = dif_f(f,
              x2)
    i = 0
    error = 0
    while con:
        i += 1
        x1 = x2
        x2 = x1 - f(x1)/m
        if '1' in data[2][0]:
            con = data[2][1] < fabs(x1 - x2)
        if '2' in data[2][0]:
            con = data[2][1] < f(x2)
        if i > data[3]:
            error = 1
            break
    return x2, i, error


def solve(fun, data):
    a = data[0]
    b = data[1]
    i = 0
    results = []
    while a < b:
        i += 1
        d = [a, a + data[2], data[3][:], data[4]]
        res_newton, i_n, er_n = newton(d, fun)
        res_easy_newton, i_e_n, er_e_n = easy_newton(d, fun)
        results.append([i, a, a + data[2], [res_newton, res_easy_newton],
                  [fun(res_newton), fun(res_easy_newton)],[i_n, i_e_n],
                  [er_n, er_e_n]])
        a = a + data[2]
    return results
