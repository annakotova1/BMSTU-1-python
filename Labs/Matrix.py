#Матрица и бесконечный ряд
#Найти элементы матрицы меньшие суммы бесконечного ряда
#Переменные
#inp1,inp2,inp3,error1,error2,error3,out1,out2,out3 - строки - подсказки
#error - критерий ошибки
#m_c,m_r - максимальное кол-во строк и столбцов матрицы
#eps - точность подсчета бесконечного ряда
#num_rows - кол-во строк
#max_len - максимальная длина строки в матрице
#num,t,z - номер элемента, текущий элемент, текущая сумма
#min_r,index_r - минимальный элемент массива R, и его индекс
#Массив и матрица:
#Y,R - введенная матрица, массив элементов матрицы меньших z

from math import fabs
inp1 = 'Введите точность подсчета ряда: '
inp2 = 'Введите количество строк:  '
inp3 = 'Введите элементы {}-ой строки через пробел:\n'
error1 = 'Строк не может быть больше 8, повторите ввод:'
error2 = 'Элементов в строке не может быть больше 13, повторите ввод:'
error3 = 'Массив R пустой'
out1 = 'Сумма бесконечного ряда с точностью {} равна {:5.4f}'
out2 = 'Введенная матрица:'
out3 = 'Элементы этой матрицы, меньшие суммы бесконечного ряда:'
out4 = 'Минимальный элемент массива {} поменян местами с первым {}'
error = True
m_r = 8
m_c = 13

#Ввод точности и количества строк
eps = float(input(inp1))

while error:
    num_rows = int(input(inp2))
    if num_rows > m_r:
        print(error1)
    else:
        error = False
#Ввод массива и поиск самой длинной строчки
max_len = 0
Y = []
for i in range(num_rows):
    error = True
    while error:
        Y.append(list(map(float, input(inp3.format(i+1)).split())))
        if len(Y[i]) <= m_c:
            error = False
            if len(Y[i]) > max_len:
                max_len = len(Y[i])
        else:
            print(error2)

#Cчитаем сумму ряда z
num = 1
t = num * (num+1)
z = t
num +=1
while not fabs(t) < eps:
    t = t * (num+1)/(num-1)/(2*num-2)/(2*num-1)
    z += t
    num = num+1


#Ищем и записываем в массив элементы матрицы, меньшие summa
R = []
min_r = ''
index_r = 0
for f in range(max_len):
    for i in range(num_rows):
        if Y[i][f]:
            if Y[i][f] < z:
                R.append(Y[i][f])
                if type(min_r) == float:
                    if Y[i][f]<min_r:
                        min_r = Y[i][f]
                        index_r = len(R)-1
                else:
                    min_r = Y[i][f]
                    index_r = len(R)-1
if type(min_r) == float:
    R[0],R[index_r] = R[index_r],R[0]
    condition = False
else:
    condition = True
#Вывод
print()
print(out1.format(eps,z))
print()
print(out2)
for i in range(num_rows):
    print(Y[i])
print()
print(out3,R,sep = '\n')
if condition:
    print(error3)
else:
    print(out4.format(R[0],R[index_r]))
