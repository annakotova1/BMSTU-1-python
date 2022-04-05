import sys
try:
    infile = open('Praktikum_fayl_vvoda_dannykh.txt','rb')
except:
    print('Не удалось открыть файл для чтения, проверьте адрес файла или его свойства.')
    print('Перезапустите программу.')
    sys.exit()

A = []
A = infile.readlines()
for i in range(len(A)):
    A[i] = A[i].decode('utf-8')
infile.close()

print(A)

try:
    N = int(A[0])
except:
    print('Количество маяков должно быть целым числом. Исправьте данные в файле и перезапустите программу.')
    sys.exit()
if N < 2 or N > 30:
    print('Недопустимое количество маяков. Исправьте данные в файле и перезапустите программу.')
    sys.exit()

print(N)
'''
for i in range(1,len(A)):
    try:
        N2 = int(A[i])
        t = i
        break
    except:
        continue
if N2 < 1:
    print('Недопустимое количество сценариев. Исправьте данные в файле и перезапустите программу.')
    sys.exit()
if N2 != (len(A) - N - 2)//3:
    print('Некоректный ввод сценариев. Исправьте данные в файле и перезапустите программу.')
    sys.exit()
if t - 1 < N:
    print('В файле меньше маяков, чем должно быть. Исправьте данные в файле и перезапустите программу.')
    sys.exit()
if t - 1 > N:
    print('В файле больше маяков, чем должно быть. Исправьте данные в файле и перезапустите программу.')
    sys.exit()

X = [0]*N
Y = [0]*N
NAME = [0]*N
kolich = 0

for i in range(1,t):
    probel_NAME = A[i].index(' ')
    NAME[kolich] = A[i][:probel_NAME]
    probel_X = A[i].index(' ',probel_NAME + 1)
    try:
        X[kolich] = float(A[i][probel_NAME:probel_X])
    except:
        print('Некоректный ввод координаты X :',A[i][probel_NAME:probel_X],', исправьте данные в строке номер :',kolich + 2)
        print('Перезапустите программу.')
        sys.exit()
    try:
        Y[kolich] = float(A[i][probel_X:])
    except:
        print('Некоректный ввод координаты Y:',A[i][probel_X:],', исправьте данные в строке номер :',kolich + 2)
        print('Перезапустите программу.')
        sys.exit()
    kolich += 1

for i in range(t + 1,len(A),3):
    probel = A[i].index(' ')
    try:
        kurs = int(A[i][:probel])
    except:
        print('Некоректный ввод курса, значение курса должно быть целым. Исправьте данные в строке номер :',i + 1)
        sys.exit()
    try:
        speed = float(A[i][probel:len(A[i])])
    except:
        print('Некоректный ввод скорости, значение скорости должно быть действительным. Исправьте данные в строке номер :',i + 1)
        sys.exit()
    if kurs < 0 or kurs > 359:
        print('Некоректный ввод курса, значение курса должно быть в пределах от 0 до 359. Исправьте данные в строке номер :',i + 1)
        sys.exit()
    if speed <= 0:
        print('Некоректный ввод скорости, значение скорости должно быть большим 0. Исправьте данные в строке номер :',i + 1)
        sys.exit()
    
    probel = A[i+1].index(' ')
    try:
        time = float(A[i+1][:probel])
    except:
        print('Некоректный ввод времени, значение времени должно быть действительным. Исправьте данные в строке номер :',i + 2)
        sys.exit()
    probel2 = A[i+1].index(' ',probel + 1)
    name = A[i+1][probel + 1:probel2]
    try:
        q = NAME.index(name)
    except:
        print('Неверное имя маяка, исправьте данные в строке номер :', i + 2)
        sys.exit()
    try:
        corner = int(A[i+1][probel2:])
    except:
        print('Некоректный ввод угла, значение угла должно быть целым. Исправьте данные в строке номер :', i + 2)
        sys.exit()
    if time <= 0:
        print('Некоректный ввод времени, значение времени должно быть большим 0. Исправьте данные в строке номер :',i + 2)
        sys.exit()
    if corner < 0 or corner > 359:
        print('Некоректный ввод угла, значение угла должно быть в пределах от 0 до 359. Исправьте данные в строке номер :', i + 2)
        sys.exit()
        
    probel = A[i+2].index(' ')
    try:
        time2 = float(A[i+2][:probel])
    except:
        print('Некоректный ввод времени, значение времени должно быть действительным. Исправьте данные в строке номер :',i + 3)
        sys.exit()
    probel2 = A[i+2].index(' ',probel + 1)
    name2 = A[i+2][probel + 1:probel2]
    try:
        q1 = NAME.index(name2)
    except:
        print('Неверное имя маяка, исправьте данные в строке номер :', i + 3)
        sys.exit()
    try:
        corner2 = int(A[i+2][probel2:])
    except:
        print('Некоректный ввод угла, значение угла должно быть целым. Исправьте данные в строке номер :', i + 3)
        sys.exit()
    if time2 <= 0:
        print('Некоректный ввод времени, значение времени должно быть большим 0. Исправьте данные в строке номер :',i + 3)
        sys.exit()
    if corner2 < 0 or corner2 > 359:
        print('Некоректный ввод угла, значение угла должно быть в пределах от 0 до 359. Исправьте данные в строке номер :', i + 3)
        sys.exit()
    if time > time2:
        print('Время чтения второго маяка должно быть большим или равным времени чтения первого маяка.')
        sys.exit()
    if name == name2:
        print('Должно быть чтение двух разных маяков, а не одного и того же.')
        sys.exit()

'''
