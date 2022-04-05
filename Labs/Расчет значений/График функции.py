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
#Нахождение max_v1 и max_v2, min_v1 и min_v2 

x = xn
max_y = 0
min_y = x*log10(x) - 1.2

min_v2 = x*x*x - 4*x*x + 10*x - 20

for i in range(number+1):
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

'''if max_v1>max_v2:
    max_y = max_v1
else:
    max_y = max_v2

if min_v1>min_v2:
    min_y = min_v2
else:
    min_y = min_v1'''

print(max_y,min_y)

#Рисуем ось y
delta = max_y - min_y
sh_zac = (delta)/(zac-1)

first_line = ' '*ot
second_line = ' '*ot + omc
y_zac = min_y - sh_zac
for i in range(zac): 
    y_zac += sh_zac
    plus = y_zac/fabs(y_zac)
    if fabs(y_zac)//1000:
        y_zac = fabs(y_zac)//1000
        y_zac = y_zac*1000 *plus
    type_y_zac = '.2'
    first_line += ('{:<'+str(int(l/zac))+type_y_zac+'}').format(y_zac)
    if i == (zac - 1):
        continue
    second_line += h*(int(l/zac-1)) + omc
    print(l,zac,i,)

print(first_line,second_line, sep = '\n')

x = xn

for i in range(number):
    plus = x/fabs(x)
    if fabs(x) // 1000:
        x = (fabs(x) // 1000)*1000*plus
    type_x = '.2f'
    new_line = '{:<'+str(ot)+type_x+'}'
    v1 = x*log10(x) - 1.2
    v2 = x*x*x - 4*x*x + 10*x - 20
    y1 = int(round((v1-min_y)/(max_y-min_y)*l))
    y2 = int(round((v2-min_y)/(max_y-min_y)*l))
    if y1<y2:
        ots_y1 = ' '*y1 + "'"
        ots_y2 = ' '*(y2-y1-1) + '*'
        new_line += ots_y1 + ots_y2
    elif y1 == y2:
        ots_y1 = ' '*y1 +('"')
        new_line += ots_y1
    else:
        ots_y1 = ' '*(y1-y2-1) + "'"
        ots_y2 = ' '*y2 +'*'
        new_line += ots_y2 + ots_y1
    #print(y1,v1,min_y,max_y)
    #print(y2,v2,)
    print(new_line.format(x))
    x +=sh
