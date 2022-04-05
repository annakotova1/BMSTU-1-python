Shapka = ['№ корня','Левая г. от.', 'Правая г. от.', 'Значение к.',
          'Значение функ.', 'Реальн. число ит.','Код Ошибки']

Errors = ['0 - корень найден',
          '1 - корень не найден за максимальное количество иттераций']

InputStrings = ['Введите левую границу интервала: ',
                'Введите правую границу интервала: ',
                'Введите шаг разбиения: ',
                'Введите точность вычислений eps1 (|x1-x2|<eps1) : ',
                'Введите точность вычислений eps2 (f(x0)<eps2) : ']
LenStrings = 79
#Данные для подсчета:
#0,1 - отрезок разбиения,
#2 - шаг,
#3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
#4 - максимальное кол-во иттераций
Data = [None, None, None, ['1', 0.001, None], 100]

#Ввод данных 3 - функции:
#1 - ввод рац. числа, 2 - ввод целого числа,
#3 - ввод 3 элементов дата
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
        
def InputStartElData(data):
    strings = ['левую границу интервала: ',
                'правую границу интервала: ',
                'шаг разбиения: ']
    for i in range(len(strings)):
        data[i] = InputFloat('Введите ' + strings[i])

def Choise(menu, data):
    global LenStrings
    OutputData(data)
    while True:
        print('*'*LenStrings)
        for i in menu:
            print(i[0])
        n = InputInt('Введите выбранный пункт меню:')
        print('*'*LenStrings)
        if n == 0:
            break
        if n >= len(menu):
            print('Выбанного пункта в меню нет!')
            continue
        menu[n][1](data)
        OutputData(data)

def ChangeEps(data,):
    data[3][0] = NumberOfEps()
    if '1' in data[3][0]:
        data[3][1] = InputFloat('Введите eps1:')
    if '2' in data[3][0]:
        data[3][2] = InputFloat('Введите eps2:')

def NumberOfEps():
    strings = ['Введите \'1\', \'2\', \'12\':',
               '1 - Используется только eps1         |x1-x2|<eps1',
               '2 - Используется только eps2         f(x0)<eps2',
               '12 - Используются и eps1 и eps2']
    while True:
        for line in strings:
            print(line)
        n = input('Ввод:')
        if n in '12':
           break
    return n

def MaxItt(data):
    data[4] = InputInt('Введите максимальное кол-во иттераций: ')

def OutputData(data):
    strings = ['Левая граница интервала: ',
                'Правая граница интервала: ',
                'Шаг разбиения: ',
                'eps1 (|x1-x2|<eps1): ',
                'eps2 (f(x0)<eps2): ']
    for i in range(len(strings)-2):
        print(strings[i], data[i])
    i += 1
    if '1' in data[i][0]:
        print(strings[i], data[i][1])
    if '2' in data[i][0]:
        print(strings[i+1], data[i][2])

def InputAllData(data):
    menu = [['0 - Посчитать'],
        ['1 - Изменить точность', ChangeEps],        
        ['2 - Изменить максимальное кол-во иттераций', MaxItt]]
    InputStartElData(data)
    Choise(menu, data)

InputAllData(Data)

