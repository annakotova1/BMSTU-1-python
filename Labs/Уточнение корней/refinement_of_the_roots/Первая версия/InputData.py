

# Данные для подсчета:
# 0,1 - отрезок разбиения,
# 2 - шаг,
# 3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
# 4 - максимальное кол-во иттераций

#
def input_float(str1):
    while True:
        try:
            print(str1)
            n = float(input())
        except ValueError:
            print('Некоректный ввод, ожидалось рациональное число')
        else:
            return n


#
def input_int(str1):
    while True:
        try:
            print(str1)
            n = int(input())
        except ValueError:
            print('Некоректный ввод, ожидалось целое число')
        else:
            return n


#
def input_start_el_data(data):
    strings = ['левую границу интервала: ',
               'правую границу интервала: ',
               'шаг разбиения: ']
    for i in range(2):
        data[i] = input_float('Введите ' + strings[i])
    while True:
        data[2] = input_float('Введите ' + strings[2])
        if data[2] <= (data[1]-data[0]):
            break
        print('Шаг разбиения слишком велик!')


#
def check_sh(a, b, sh):
    try:
        int(fabs(b-a)/sh)
    except ValueError:
        con = True
    else:
        con = False


#
def choise(menu, data, len_strings):
    output_data(data)
    while True:
        print('*' * len_strings)
        for i in menu:
            print(i[0])
        n = input_int('Введите выбранный пункт меню:')
        print('*' * len_strings)
        if n == 0:
            break
        if n >= len(menu):
            print('Выбанного пункта в меню нет!')
            continue
        menu[n][1](data)
        output_data(data)


def change_eps(data, ):
    data[3][0] = number_of_eps()
    if '1' in data[3][0]:
        data[3][1] = input_float('Введите eps1:')
    if '2' in data[3][0]:
        data[3][2] = input_float('Введите eps2:')


def number_of_eps():
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


#
def max_itt(data):
    data[4] = input_int('Введите максимальное кол-во иттераций: ')


#
def output_data(data):
    strings = ['Левая граница интервала: ',
               'Правая граница интервала: ',
               'Шаг разбиения: ',
               'eps1 (|x1-x2|<eps1): ',
               'eps2 (f(x0)<eps2): ']
    for i in range(len(strings) - 2):
        print(strings[i], data[i])
    i += 1
    if '1' in data[i][0]:
        print(strings[i], data[i][1])
    if '2' in data[i][0]:
        print(strings[i + 1], data[i][2])


#
def input_all_data(data, len_strings):
    menu = [['0 - Посчитать'],
            ['1 - Изменить точность', change_eps],
            ['2 - Изменить максимальное кол-во иттераций', max_itt]]
    input_start_el_data(data)
    choise(menu, data, len_strings)
