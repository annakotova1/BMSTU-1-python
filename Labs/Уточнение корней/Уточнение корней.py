Shapka = ['№ корня','Левая г. от.', 'Правая г. от.', 'Значение к.',
          'Значение функ.', 'Реальн. число ит.','Код Ошибки']

Errors = ['0 - корень найден',
          '1 - корень не найден за максимальное количество иттераций']

InputStrings = ['Введите левую границу интервала: ',
                'Введите правую границу интервала: ',
                'Введите шаг разбиения: ',
                'Введите точность вычислений eps1 (|x1-x2|<eps1) : ',
                'Введите точность вычислений eps2 (f(x0)<eps2) : ']

#Данные для подсчета:
#0,1 - отрезок разбиения,
#2 - шаг,
#3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
#4 - максимальное кол-во иттераций
Data = [None, None, None, ['1', 0.001, None], 100]

Menu = [['0 - Посчитать', Solve],
        ['1 - Изменить левую границу интервала', Left],
        ['2 - Изменить правую границу интервала', Rigth],
        ['3 - Изменить шаг разбиения', Sh],
        ['4 - Изменить точность вычислений eps1 (|x1-x2|<eps1)', Eps1],
        ['5 - Изменить точность вычислений eps2 (f(x0)<eps2)', Eps2],
        ['6 - Использовать eps1', UsedEps1],
        ['7 - Использовать eps2', UsedEps2]]

def F(x):
    y = x*x - 2 
    return y

def InputFloat(str1):
    while True:
        try:
            print(str1)
            n = float(input())
        except ValueError:
            print('Некоректный ввод, ожидалось рациональное число')
        else:
            return n

def InputInt(str1):
    while True:
        try:
            print(str1)
            n = int(input())
        except ValueError:
            print('Некоректный ввод, ожидалось целое число')
        else:
            return n


def Choise(array,data):
    for i in array:
        print(i[0])
        n = InputInt('Введите номер выбранного пункта: ')
        i[1](data)

def Solve():
    return True

def OutputTabl(shapka, znach):
    l = 13
    tabl = '{:^'+str(l)+'}|'
    print('|', end = '')
    for string in shapka:
        print(tabl.format(string), end = '')
    print()
    for i in znach:
        print('|', end = '')
        for j in i:
            print(tabl.format(j), end = '')
        print()
