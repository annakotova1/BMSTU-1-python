from math import fabs
def input_float(str1):
    while True:
        try:
            #print(str1)
            n = float(input(str1+' '))
        except ValueError:
            print('Некоректный ввод, ожидалось рациональное число.')
        else:
            return n

def input_int(str1):
    while True:
        try:
            #print(str1)
            n = int(input(str1))
        except ValueError:
            print('Некоректный ввод, ожидалось целое число.')
        else:
            return n


def input_diapazon():
    while True:
        a = input_float('Введите левую границу интервала(a):')
        b = input_float('Введите правую границу интевала(b):')
        if a>b:
            print('Так как a>b, то a и поменяны местами: a,b = b,a')
            a,b = b,a
        if a == b:
            print('Интервал отсутствует. Введите данные еще раз.')
            continue
        break
    return a,b

def choise_eps():
    while True:
        print('Введите 1, либо 2, либо 12 ',
          'в зависимости от формулы подсчета точности:',
          '1  -  |x1-x2|<eps',
          '2  -  f(x0)<eps',
          '12 -  (|x1-x2|<eps) and (f(x0)<eps)', sep = '\n')
        num = input()
        if num in '12':
            break
        else:
            print('Некорректный ввод')
    return num

def input_eps(eps, max_it):
    a = input_float('Введите точность подсчета:')
    if a < 0:
        print('Точность подсчета взята по модулю')
        a = fabs(a)
    if a != 0:
        eps[1] = a
    else:
        print(('Точность не может быть равна нулю!'+
            'Взята точноть по умолчанию: {}').format(eps[0]))
    eps[0] = choise_eps()

def input_max_it(eps, max_it):
    while True:
        max_it = input_int('Введите максимальное кол-во иттераций:')
        if max_it < 1:
            print('Некорректный ввод, число итераций - натуральное число')
            continue
        break

def menu():
    eps = ['1', 0.0001]
    max_it = 100
    menu = [['1 - Посчитать'],
            ['2 - Изменить точность', input_eps],
            ['3 - Изменить максимальное кол-во итераций', input_max_it]]
    print()
    print('По умолчанию:')
    n = 1
    
    while n != 0:
        
        if eps[0] == '1':
            string = '(|x1-x2|<eps)'
        elif eps[0] == '2':
            string = '(f(x0)<eps)'
        else:
            string = '(|x1-x2|<eps) and (f(x0)<eps)'

        print('Точность {}: {}'.format(string, eps[1]))
        print('Максимальное кол-во итераций: {}'.format(max_it))

        for point in menu:
            print(point[0])
        while True:
            n = input_int('Введите выбранный пункт меню: ')
            if 0 < n < len(menu)+1:
                n = n-1
                break
            print('Такого пункта в меню нет.')
        print()
        if n == 0:
            break
        menu[n][1](eps, max_it)
        print()
    return eps, max_it

    
def input_all_data():
    
    data = []
    a,b = input_diapazon()
    sh = input_float('Введите шаг разбиения:')
    eps, max_it = menu()
    data= [a, b, sh, eps, max_it]
    return data
