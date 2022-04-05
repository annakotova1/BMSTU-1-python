# Таблица значений

# Расчет таблицы значений функций v1  v2

# Переменные:
# x - аргумент
# v1,v2 - значения двух функций
# v2_max, v2_min - максимальное и минимальное значения функции v2
# v,h,a1,a2,a3,a4,s1,s2,s3,s4,s5 - символы псевдографики
# l, m, k, s - длина столбца, кол-во пробелов в шапке, строка из пробелов,
#              пробелы для строк с аргументами

from math import sqrt, log10

v = chr(9474)    # │
h = chr(9552)    # ═
ulc = chr(9554)   # ╒
urc = chr(9557)   # ╕
olc = chr(9560)   #  ╘
orc  = chr(9563)   # ╛
mlc = chr(9566)   # ╞
mrc = chr(9569)   #  ╡
umc = chr(9572)   # ╤
omc = chr(9575)   #  ╧
mmc = chr(9578)   # ╪

inp1 = 'Ограничение: начальный и конечный аргументы должны быть положительными'
inp2 = '\nВведите начальный аргумент, шаг и конечный аргумент: '
error = True
while error:
    xn,sh,xk = map(float,input(inp1+inp2).split())
    if (xn>0) and (xk>0) and ((abs(xk-xn)/(xk-xn)) == (abs(sh)/sh)) and (
        (xk-xn)>=sh):
        error = False

l = 16

start_shapka = ulc+h*l+umc+h*l+umc+h*l+urc
first_line = v+'{:^'+str(l)+'}'+v+'{:^'+str(l)+'}'+v+'{:^'+str(l)+'}'+v
finish_shapka = mlc + h*l + mmc + h*l + mmc + h*l + mrc
print(start_shapka, first_line.format('x','V1','V2'), finish_shapka,
      sep = '\n')


x = xn
v2_max = 0
v2_min = x*x*x - 4*x*x + 10*x - 20

if xn > xk:
    condition = (x>=xk)
else:
    condition = (x<=xk)

while condition:
    v1 = x*log10(x) - 1.2
    v2 = x*x*x - 4*x*x + 10*x - 20

    if abs(x)//100000 == 0:
        type_x = 'f'
    else:
        type_x = 'e'

    if abs(v1)//1000 == 0:
        type_v1 = '.4f'
    else:
        type_v1 = '.2e'
        
    if abs(v2)//100000 == 0:
        type_v2 = 'f'
    else:
        type_v2 = 'e'

    new_line = (v+ '{:^'+str(l)+'.4'+type_x+'}' +v+ '{:^'+str(l)+
                type_v1+'}'+v+ '{:^'+str(l)+'.2'+type_v2+'}' +v)
    print(new_line.format(x,v1,v2))

    x = x + sh
    
    if xn > xk:
        condition = (x>=xk)
    else:
        condition = (x<=xk)

finish_of_table = olc + h*l + omc + h*l + omc + h*l + orc + '\n'

print( finish_of_table,
    'Разность между наименьшим и наибольшим значениями функции \n ',
      'V2 = x*x*x - 4*x*x + 10*x - 20 равна {:7.4f}'.format(v2_max - v2_min))
