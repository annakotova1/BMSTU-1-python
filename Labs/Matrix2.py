#Матрица 
#Найти минимальные элементы заданных строк матрицы 
#Переменные
#inp1,inp2,inp3,inp4,inp5error1,error2,error3,error4,out1,out2,out3,out4,matrica    
#- строки - подсказки
#error, lama- критерий ошибки
#m_c,m_r - максимальное кол-во строк и столбцов матрицы
#len_K - длина массива 
#num_rows - кол-во строк
#sr_arifm - реднее арифметическое
#max_len - максимальная длина строки в матрице
#num,t,z - номер элемента, текущий элемент, текущая сумма
#min_r,index_r - минимальный элемент массива R, и его индекс
#Массивы и матрица:
#X,K,Y - введенная матрица, введенный массив, массив мин. элементов строк м. 

from math import fabs
inp1 = 'Введите точность подсчета ряда: '
inp2 = 'Введите количество строк:  '
inp3 = 'Введите элементы {}-ой строки через пробел:\n'
inp4 = 'Введите массив, содержащий номера строк, \n'
inp5 = 'в которых необходимо найти минимальный элемент: '
error1 = 'Строк не может быть больше 10, повторите ввод:'
error2 = 'Элементов в строке не может быть больше 8, повторите ввод:'
error3 = 'В массиве К не может быть элементов больше, чем строк в матрице'
error4 = 'Массив К пуст'
matrica = '{:10.1f}'
out1 = 'Введенная матрица:'
out2 = 'Введенный массив:'
out3 = 'Массив минимальных элементов строк указанных в введенном массиве'
out4 = 'Среднее арифметическое элементов этого массива'

error = True
m_r = 10
m_c = 8

#Ввод количества строк

while error:
    num_rows = int(input(inp2))
    if num_rows > m_r:
        print(error1)
    else:
        error = False
        
#Ввод массива
X = []
for i in range(num_rows):
    error = True
    while error:
        X.append(list(map(float, input(inp3.format(i+1)).split())))
        if len(X[i]) <= m_c:
            error = False
        else:
            print(error2)

#Ввод массива
error = True
K = []
while error:
    K = list(map(int, input(inp4+inp5).split()))
    if len(K) > num_rows:
        print(error3)
        continue
    lama = False
    for i in K:
        if i > (len(X)):
            lama = True
            print(error5)
            break
    if lama:
        continue
    error = False
len_K = len(K)

Y = ['']*len_K

for i in range(len_K):
    x = K[i]-1
    for j in X[x]:
        if type(Y[i]) == float:
            if j < Y[i]:
                Y[i] = j
        else:
            Y[i] = j

summa = 0
for i in range(len_K):
    summa += Y[i]
sr_arifm = summa/len_K

#Вывод
print(out1)
for i in X:
    for j in i:
        print(matrica.format(j),end = '')
    print()
if len_K == 0:
    print(error4)
else:
    print()
    print(out2, K)
    print()
    print(out3, Y)
    print()
    print(out4, sr_arifm)
