# График функции

# Построить графики функций v1  v2

# Переменные:
# x - аргумент
# v1,v2 - значения двух функций
# v2_max, v2_min - максимальное и минимальное значения функции v2
# v,h,a1,a2,a3,a4,s1,s2,s3,s4,s5 - символы псевдографики
# l, m, k, s - длина столбца, кол-во пробелов в шапке, строка из пробелов,
#              пробелы для строк с аргументами

from math import sqrt, log10,fabs

#Запоминаем необходимые символы псевдографики
v = chr(9474)    # │
h = chr(9472)    # ─
ulc = chr(9484)   # ┌
urc = chr(9488)   # ┐
olc = chr(9492)   #  └
orc = chr(9496)   # ┘
mlc = chr(9500)   # ├
mrc = chr(9508)   #  ┤
umc = chr(9516)   # ┬
omc = chr(9524)   #  ┴
mmc = chr(9532)   # ┼

#Вводим начальный,конечный аргументы, шаг, кол-во засечек,
#и проверяем введенные данные на ошибки
inp1 = 'Ограничение: начальный и конечный аргументы должны быть положительными'
inp2 = '\nВведите начальный аргумент, шаг и конечный аргумент: '
error = True
while error:
    xn,sh,xk = map(float,input(inp1+inp2).split())
    if (xn>0) and (xk>0) and ((abs(xk-xn)/(xk-xn)) == (abs(sh)/sh)) and (
        (xk-xn)>=sh):
        error = False
error = True
while error:
    zac = int(input('Введите количество засечек: '))
    if (zac <= 8) and (zac>=4):
        error = False
    else:
        print('Засечек должно быть от 4 до 8')

#Задаем ширину графика и отступ
l = (65//(zac-1))*(zac-1)
ot = 8 

#Количество аргументов в  данном промежутке с таким шагом
number = int((xk-xn)/sh+1) 
#Нахождение max_y и min_y 

x = xn
max_y = 0
min_y = x*log10(x) - 1.2

for i in range(number):
    v1 = x*log10(x) - 1.2
    v2 = x*x*x - 4*x*x + 10*x - 20
    if v1<min_y:
        min_y = v1
    if v2<min_y:
        min_y = v2
    if v1>max_y:
        max_y = v1
    if v2>max_y:
        max_y = v2
    x +=sh

#Расчет оси х
if min_y == 0:
    ox_y = 0
elif max_y == 0:
    ox_y = l
elif min_y/fabs(min_y) != max_y/fabs(max_y):
    vx = 0
    ox_y = int(round((vx-min_y)/(max_y-min_y)*l))
else:
    ox_y = -1

#Рисуем ось y
delta = max_y - min_y
sh_zac = (delta)/(zac-1)

first_line = ' '*ot
second_line = ' '*ot + omc
y_zac = min_y - sh_zac
for i in range(zac): 
    y_zac += sh_zac
    if y_zac == 0:
        plus = 1
    else:
        plus = y_zac/fabs(y_zac)
    if fabs(y_zac)//10000:
        y_zac = fabs(y_zac)//1000
        y_zac = y_zac*1000 *plus
    type_y_zac = '.2f'
    first_line += ('{:<'+str(int(l/(zac-1)))+type_y_zac+'}').format(y_zac)
    if i == (zac - 1):
        continue
    #second_line += h*(int(l/(zac-1))-1) + omc
    for j in range(int(l/(zac-1))-1):
        if ox_y == (j + (int(l/(zac-1))-1)*i):
            new_symbol = umc
        else:
            new_symbol = h
        second_line += new_symbol
        print(i,j,(int(l/(zac-1))-1))
    if (int(l/(zac-1))-1)*(i+1)==ox_y:
        second_line += mmc
    else:
        second_line += omc
    
print(first_line,second_line, sep = '\n')


    
x = xn
for i in range(number):
    type_x = '.2f'
    v1 = x*log10(x) - 1.2
    v2 = x*x*x - 4*x*x + 10*x - 20
    #print(v1,v2,max_y,min_y,((v1-min_y)/(max_y-min_y)*l))
    y1 = int(round((v1-min_y)/(max_y-min_y)*l))
    y2 = int(round((v2-min_y)/(max_y-min_y)*l))

    #print(y2,v2,max_y,min_y)
    
    sign = x/fabs(x)
    if fabs(x) // 1000:
        x = (fabs(x) // 100)*100*sign

    new_line = ('{:>' + str(ot-2) + '.2f}').format(x) + '  '
    new_symbol = ''
    

    for i in range(l+1):
        if ox_y == i:
            new_symbol = v
        if y1 == i:
            new_symbol = "'"
        if y2 == i:
            new_symbol = '*'
        if y1 == y2 and y1 == i:
            new_symbol = '"'
        if new_symbol == '':
            new_symbol = ' '
        new_line += new_symbol
        new_symbol = ''
    print(new_line)
    x +=sh
