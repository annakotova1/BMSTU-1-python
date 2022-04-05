#Исследование реабилитационного оборудования

#Из полученных данных о передвижении кресла, получить весь путь пройденный креслом
#либо координату точки, в которой пациент покинул поле в первый раз, и время,
#когда это произошло, либо если пациент не покидал поле, то расстояние от
#наиболее удаленной точки до двери

#Тестовый пример

#Пример входных данных
#4
#0.0 5.0 3.0 0
#7.0 9.0 2.0 30
#10.0 100.0 4.0 60
#110.0 200.0 2.0 0
#3
#0.0 20.0 2.0 0
#500.0 600.0 1.0 270
#3000.0 3100.0 1.0 0
#7
#0.0 5.3 2.1 0
#19.8 35.6 2.7 346
#42.0 78.4 2.3 15
#1181.4 1192.1 1.7 117
#2107.0 2193.6 2.1 295
#2196.3 2201.2 2.0 298
#2704.3 2709.2 1.5 208

#Пример выходных данных
#Первый случай
#Пациент покинул ограниченный участок в точке (400.0,132.8)
#в момент времени 67.2 секунд.
#Общая пройденная дистанция составляет 559.0 футов.
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#Второй случай
#Пациент не пересекал границы области
#Максимальное расстояние, на которое пациент удалился от двери,
#равно 172.0 футов
#Общая проенная дистанция составляет 240.0 футов
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#Третий случай
#Пациент покинул ограниченный участок в точке (67.0,200.0)
#в момент времени 2191.4 секунд
#Общая пройденная дистанция составляет 354.7 футов
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#Импортирование необходимых функций из модуля math
from math import sin,cos,radians,sqrt

#Функция для ввода одного целого числа -
#количества строк с данными в новом блоке
#n - кол-во строк с данными
def InputInt():
    while True:
        n = input('Введите кол-во строк с данными: ')
        try:
            n = int(n)
        except ValueError:
            print('Число должно быть целым, повторите ввод:')
        else:
            break
    return n

#Функция для ввода одной строки данных
#Строка с данными - это четыре числа.
#1 - это время начала движения кресла
#2 - это время конца движения кресла
#3 - это скорость кресла
#4 - это азимут
#n - строка с данными
def InputLine():
    while True:
        n = input('Введите строку с данными: ')
        try:
            n = list(map(float, n.split()))
        except ValueError:
            print('Некорректный ввод, введите еще раз: ')
        else:
            if len(n)==4:
                break
            print('Должно быть 4 числа в строке. Повторите ввод:')
    return n

#Функция ввода блока данных
#Блок данных -
#кол-во строк с данными
#строки с данными
#ln_block - кол-во строк с данными
#new_line - строка с данными
#new_data - блок данных содержащий строки с данными
def InputBlock():
    ln_block = InputInt()
    new_data = []
    for i in range(ln_block):
        new_line = InputLine()
        new_data.append(new_line)
    return new_data

#Функция ввода всех данных
#new_data - Блок данных
#data - все введенные данные
def InputData():
    data = []
    while True:
        new_data = InputBlock()
        if new_data == []:
            break
        data.append(new_data)
    return data

#Функция высчитывания координат новой точки
#old_pt - координаты старой точки
#pt_data - строка данных для высчитывания этой точки
#delta_t - время движения кресла 
#alpha - азимут движения
#way - путь, пройденный креслом
#delta_x,delta_y - смещение координат новой точки относительно старой точки
#new_pt - координаты новой точки
def NewPoint(old_pt, pt_data):
    delta_t = pt_data[1] - pt_data[0]
    alpha = radians(pt_data[3])
    way = delta_t*pt_data[2]
    delta_x = sin(alpha)*way    
    delta_y = cos(alpha)*way    
    new_pt = [old_pt[0]+delta_x, old_pt[1]+delta_y]
    return new_pt,way

#Функция высчитывания координат
#points - массив с массивами координат для всех точек
#point - координаты текущей (обрабатываемой точки) точки
#ways - массив с путями
#way - путь до текущей точки
#line - строка данных
def AllPoints(data):
    points = [[200,0]]
    point = [200,0]
    ways = []
    for line in data:
        point,way = NewPoint(point, line)
        ways.append(way)
        points.append(point)
    return points,ways

#Функция для подсчета расстояния от введенной точки до двери
#Координаты двери (200,0)
#point1 - координаты введенной точки
#x1,y1,x2,y2 - координаты x и y введенной точки и двери соответственно
#rast - растояние от введенной точки до двери
def Rast(point1):
    x1,y1 = point1 
    x2,y2 = 200,0
    rast = sqrt((x1-x2)**2+(y1-y2)**2)
    return rast

#Функция для подсчета коэффицентов
#point1, point2 - координаты двух точек прямой
#k,m,b - коэффиценты прямой в уравнении m*y=k*x+b
#line - массив с коэффицентами прямой
def Line(point1,point2):
    try:
        k = (point1[1]-point2[1])/(point1[0]-point2[0])
    except ZeroDivisionError:
        k = 1
        m = 0
    else:
        m = 1
    b = point1[1] - k*(point1[0])
    line = [k, b, m]
    return line

#Функция для определения: находится ли точка в ограниченном поле
#point - координаты точки
#x,y - координаты точки
#x_line - вылет за границы по оси х, и указание за какую (0 или 400)
#y_line - вылет за границы по оси y, и указание за какую (0 или 200)
def InGround(point):
    x_line = False
    y_line = False
    x,y = point   
    if x<0:
        x_line = ['x',0]
    elif x>400:
        x_line = ['x',400]
    if y<0:
        y_line = ['y',0]
    elif y>200:
        y_line = ['y',200]
    return x_line,y_line

#Функция для поиска пересечения прямой, заданной двумя точками,
#и прямой, заданной одним из уравнений x=0, x=400, y=0, y=200
#point1 - первая точка первой прямой
#point2 - вторая точка первой прямой
#coord - данные о второй прямой 
#x,y - координата точки пересечения x или y (соответственно)
#point - точка пересечения
def FoundIntersect(point1,point2,coord):
    line = Line(point1,point2)
    if coord[0] == 'x':
        y = (coord[1]*line[0] + line[1])/line[2]
        point = [coord[1], y]
    else:
        x = (coord[1]*line[2] - line[1])/line[0]
        point = [x, coord[1]]
    return point

#Функция считает коэффицент соотношения отрезков М1М3 и М2М3,
#где М3 принадлежит М1М2 
#х1,х2,х3 - координаты точек соответсвенно М1М3 и М2М3
#coef - искомый коэффицент
def CoefCuts(x1,x2,x3):
    coef = (x3-x1)/(x2-x3)
    coef = coef/(coef+1)
    return coef

#Функция, которая считает время до момента, когда пациент покинул
#ограниченную область в первый раз
#line_data - строка данных
#coef - коэффицент отношения, в котором разбивается время
#delta_t - изменение времени
#time - время, когда покинул ограниченную область в первую
def Time(line_data,coef):
    delta_t = line_data[1]-line_data[0]
    time = coef*delta_t + line_data[0]
    return time

#Функция для подсчета расстояния от двери до наиболее удаленной точки
#points - все точки
#point - текущая точка
#max_rast - максимальное расстояние
#new_rast - текущее расстояние
def MaxRast(points):
    max_rast = 0
    for point in points:
        new_rast = Rast(point)
        if new_rast > max_rast:
            max_rast = new_rast
    return max_rast

#Функция для поиска точки первого выезда пациента за ограниченную область
#points – массив точек 
#data – массив со всеми введенными данными
#line_x, line_y – данные о пересечении верт. и гор. границ
#point1,point2 – первая точка за границей и предыдущая
#coef_x, point_x – данные о пересечении с гориз. границами
#coef_y, point_y – данные о пересечении с верт. границами
#coef, result_point – данные о пересечении с нужной границей
#time – время пересечения границы
def PointOnBorderline(points,data):
    for i in range(1,len(points)):
        point = points[i]
        line_x,line_y = InGround(point)
        if (line_x or line_y):
            break
    if not (line_x or line_y):
        return False,False
    point1 = points[i-1]
    point2 = points[i]
    if line_x:
        point_x = FoundIntersect(point1,point2,line_x)
        coef_x = CoefCuts(point1[0],point2[0],point_x[0])
    if line_y:
        point_y = FoundIntersect(point1,point2,line_y)
        coef_y = CoefCuts(point1[0],point2[0],point_y[0])
    if line_x and line_y:
        if coef_x>coef_y:
            coef = coef_y
            result_point = point_y
        else:
            coef = coef_x
            result_point = point_x
    elif line_x:
        coef = coef_x
        result_point = point_x
    else:
        coef = coef_y
        result_point = point_y
    time = Time(data[i-1], coef)
    return result_point, time

#Функция для подсчета суммы всего пути, пройденного креслом
#ways - все пути
#summa - сумма путей
def SummaWays(ways):
    summa = 0
    for way in ways:
        summa += way
    return summa

#Функция решает поставленную задачу для одного блока
#data - данные для блока
#points - точки в этом блоке
#ways - пути в этом блоке
#summa_ways - путь, пройденный креслом за этот блок наблюдений
#point_not_on_ground - точка первого выезда пациента из ограниченной зоны
#time - момент времени, в который пациент пересек границу в первый раз
#max_rast - расстояние от двери до наиболее удаленной от нее точки
#result - массив с ответом для заданного блока
def SolveForBlock(data):
    points, ways = AllPoints(data)
    summa_ways = SummaWays(ways)
    point_not_on_ground, time = PointOnBorderline(points,data)
    if not point_not_on_ground:
        max_rast = MaxRast(points)
        result = [summa_ways, max_rast]
    else:
        result = [summa_ways, point_not_on_ground, time]
    return result

#Функция для решения для всех блоков
#data - се введенные данные
#block_of_data - блок данных 
#results - результаты по всем блокам
#result - результат по текущему блоку
def SolveForAllData(data):
    results = []
    for block_of_data in data:
        result = SolveForBlock(block_of_data)
        results.append(result)
    return results

#Функция
#i - счетчик цикла
#results - результаты работы программы
def OutputResults(results):
    for i in range(len(results)):
        if i != 0:
            print('★'*44)
        print('{} случай'.format(i+1))
        if len(results[i]) == 2:
            OutputRast(results[i])
        else:
            OutputPointAndTime(results[i])
        OutputWays(results[i][0])

#Функция для вывода результата - расстояния
#result - результат который надо вывести
#l1, l2 - строки  для вывода
def OutputRast(result):
    l1 = 'Пациент не пересекал границы ограниченнной области.\n'
    l2 = 'Наибольшее расстояние от точки до двери равно {:.1f}.'.format(
        result[1])
    print(l1+l2)

#Функция для вывода результата - точки пересечения с границами поля
#l1, l2 - строка для вывода
#result - результат, который надо вывести
def OutputPointAndTime(result):
    l1 = 'Пациент пересек ограниченное поле в точке ({:.1f},{:.1f})'.format(
        result[1][0], result[1][1])
    l2 = 'в момент времени {:.1f}.'.format(result[2])
    print(l1+l2)

#Функция для вывода результата - всего пути пройденного креслом за этот блок
#l3 - строка для вывода
#result - результат, который надо вывести
def OutputWays(result):
    l3 = 'Путь, который преодолел пациент, равен {:.1f}'.format(result)
    print(l3)

    
#Data - все введенные данные
#Result - все полученные результаты
print('''Примечание: Строка с данными - это четыре числа.
1 - это время начала движения кресла
2 - это время конца движения кресла
3 - это скорость кресла
4 - это азимут''')
Data = InputData()
Result = SolveForAllData(Data)
OutputResults(Result)
