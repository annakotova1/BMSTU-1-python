# График функции

# Построить графики функций v1  v2

# Переменные:
# x - аргумент
# v1,v2 - значения двух функций
# v2_max, v2_min - максимальное и минимальное значения функции v2
# v,h,a1,a2,a3,a4,s1,s2,s3,s4,s5 - символы псевдографики
# l, m, k, s - длина столбца, кол-во пробелов в шапке, строка из пробелов,
#              пробелы для строк с аргументами

from math import sqrt, log10

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
    num = map(float,input('Введите количество засечек: ').split())
    if (num < 8) and (num>4):
        error = False
    else:
        print('Засечек должно быть от 4 до 8')


l = 16

max_v1 =
min_v1 =
max_v2 =
min_v2 = 
for i in range(xn,(xk+1),sh):
    
