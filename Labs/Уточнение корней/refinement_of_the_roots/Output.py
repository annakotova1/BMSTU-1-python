#Ширина столбцов

w = [3, 13, 20, 10, 8, 6, 10, 3]

form = ['{:^' + str(w[0]) + '}',
        [('({:^' + str(int((w[1]-3)/2)) + '.1f};{:^' +
          str(int((w[1]-3)/2)) + '.1f})'),
         '{:^' + str(w[1]) + '}'],
        '{:^' + str(w[2]) + '}',
        '{:^' + str(w[3]) + '.7f}',
        '{:^' + str(w[4]) + '.0e}',
        '{:^' + str(w[5]) + '}',
        '{:^' + str(w[6]) + '.8f}',
        '{:^' + str(w[7]) + '}']


def SumAr(a):
    summa = 0
    for i in a:
        summa += i
    return summa

def Shapka():
    global w
    text = [['', '', '', '', '','', '',''],
            ['', '', '', '', '','Кол-во', '','Код'],
            ['№', 'Диапазон', 'Метод', 'x = ?', 'y = ?','', 'Время',''],
            ['', '', '', '', '','итер.', '','ош.'],
            ['', '', '', '', '','', '','']]

    first_line = '┌'
    for i in range(len(text[0])):
        first_line = first_line + '─'*w[i]
        if i != len(text[0])-1:
            first_line = first_line + '┬'
        else:
            first_line = first_line + '┐'

    shapka = [first_line]
    for j in text:
        shapka_line = '│'
        for i in range(len(j)):
            shapka_line = (shapka_line + '{:^' + str(w[i]) + '}│').format(j[i])
        shapka.append(shapka_line)

    finish_line = '├'
    for i in range(len(text[0])):
        finish_line = finish_line + '─'*w[i]
        if i != len(text[0])-1:
            finish_line = finish_line + '┼'
        else:
            finish_line = finish_line + '┤'
    shapka.append(finish_line)
    return shapka

# result = [3 результата (как массив снизу)]
# [диапазон, значение корня, значение функции, итерации, время, ошибка]

def sred_line(n):
    line = '├'
    for i in range(n):
        line = line + '─'*w[i]
        if i != n-1:
            line = line + '┼'
        else:
            line = line + '┤'
    return line

def line_tabl(n, result):
    global form
    methods = ['Ньютон','Упрощ. м. Ньютона','Из библиотеки']
    lines = []
    for res in result:
        line = '│'
        for i in range(1,len(res)):
            if res[i] == None:
                line = line + form[i+2].format('-') + '│'
                continue
            if res[5] == 1 and i != 5:
                line = line + ('{:'+str(w[i+2])+'}').format(' ') + '│'
            else:
                line = line + form[i+2].format(res[i]) + '│'
        lines.append(line)

    lines[0] = '│'+form[0].format(' ')+'│'+form[1][1].format(
        ' ')+'│'+form[2].format(methods[0])+lines[0]
    
    lines[1] = '│'+form[0].format(n)+'│'+form[1][0].format(
        result[1][0][0],result[1][0][1])+'│'+form[2].format(
            methods[1])+lines[1]
    
    lines[2] = '│'+form[0].format(' ')+'│'+form[1][1].format(
        ' ')+'│'+form[2].format(methods[2])+lines[2]
    
    return lines

def Error1(n, result):
    global form
    methods = ['Ньютон','Упрощ. м. Ньютона','Из библиотеки']
    lines = []
    for res in result:
        line = '│'
        for i in range(1,len(res)):
            if res[i] == None:
                line = line + form[i+2].format('-') + '│'
                continue
            line = line + ('{:'+str(w[i+2])+'}').format(' ') + '│'
        lines.append(line)

    lines[0] = '│'+form[0].format(' ')+'│'+form[1][1].format(
        ' ')+'│'+form[2].format(methods[0])+lines[0]
    
    lines[1] = '│'+form[0].format(n)+'│'+form[1][0].format(
        result[1][0][0],result[1][0][1])+'│'+form[2].format(
            methods[1])+lines[1]
    
    lines[2] = '│'+form[0].format(' ')+'│'+form[1][1].format(
        ' ')+'│'+form[2].format(methods[2])+lines[2]
    
    return lines

def output_results(results):
    global w
    if results:
        last_line = '└'
        for i in range(len(w)):
            last_line = last_line + '─'*w[i]
            if i != len(w)-1:
                last_line = last_line + '┴'
            else:
                last_line = last_line + '┘'
    
        lines = Shapka()
        for i, result in enumerate(results):
            lines += line_tabl(i+1, result)
            if i == len(results)-1:
                lines.append(last_line)
            else:
                lines.append(sred_line(len(w)))
        for line in lines:
            print(line)
        output_comments()
    else:
        print('Корней нет')
    

def output_comments():
    print('Код ошибки:')
    print('    0 - нет ошибки')
    print('    1 - превышено максимальное кол-во итераций')
    print('*Время указывается за 250 повторений одного метода')
    print('**3-ий метод - метод Ньютона из библиотеки, поэтому он не выдает \n'+
          '    кол-во итераций')
