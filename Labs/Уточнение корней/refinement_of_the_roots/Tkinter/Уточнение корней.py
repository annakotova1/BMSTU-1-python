from tkinter import *
import matplotlib.pyplot as plt
from SolveWithoutDiffMethodsAndEps import solve
from math import sin

def f(x):
    y = sin(x)
    return y

def diff2f(x):
    y = -sin(x)
    return y

def WindowOfParametres():
    window = Tk()
    widgets = []

    title = Label(text = "Уточнение корней", font = (22))
    label_input_data = Label(text = "Ведите данные:")
    title.grid(row = 0, column = 0, columnspan = 2)
    label_input_data.grid(row = 1, column = 0, columnspan = 2)
    widgets.append(title)
    widgets.append(label_input_data)

    text = ["Введите функцию", "Введите вторую производную функции",
            "Левая граница интервала: ", "Правая граница интервала: ",
            "Шаг: ", "Точность: ", "Максимальное кол-во иттераций:"]
    strings = []
    strs = ["sin(x)", "-sin(x)","1","10","1","0.001","100"]

    for i in range(len(text)):
        string = StringVar()
        string.set(strs[i])
        strings.append(string)

    for i in range(len(text)):
        label = Label(text = text[i])
        entry = Entry(textvariable = strings[i])
        label.grid(row = i+2, column = 0)
        entry.grid(row = i+2, column = 1)
        widgets.append([label, entry])

    button_table = Button(text = "Вывести таблицу значений",
                          command = OutputTable)
    button_graph = Button(text = "Вывести график функции",
                          command = OutputGraph)
    
    button_table.grid(row = len(text)+2, column = 0)
    button_graph.grid(row = len(text)+2, column = 1)

    widgets.append([button_table, button_graph])

    return {'root': window, 'widgets': widgets}

def OutputTable():
    parametres = get_parametres(windows[0])
    #print(parametres, '\n')
    condition_of_input = check_parametres(parametres)
    #print(condition_of_input, '\n')
    
    results = solve(f, parametres)
    #print(results)
    root = Tk()  #DrawTable(len(results))
    DrawShapka(root)
    DrawResult(root, results)

'''
def DrawTable(rows):
    setting = [9, 42, 34, 27, 25, 34, 15]
    settings = [10, 42, 34, 27, 25, 34, 15]
    for i in range(len(settings)):
        setting[i] = ' ' * setting[i]
    y = 21
    columns = 7
    root = Tk()
    st = ' '
    for i in range(rows*2+1):
        for j in range(columns*2+1):
            if (i%2 == 0) or (j%2 == 0):
                string = '   '
            else:
                string = ' '* settings[j//2]
            if (i%2 == 0) and (j%2 == 1):
                string = st*settings[j//2]
            x = 4 + 4*Place(settings, i, setting)
            label = Label(root, text = string)
            label.place(x = x, y = y)
            #print([i,j])
    return root
'''

def Place(settings, j, text):
    summ = settings[0]/2 - (len(text[0])/2) + 1
    #print(summ, end = '  ')
    for i in range(1, len(settings)):
        if j < i:
            break
        #print('(', summ, '- (', settings[i-1], '-', len(text[i-1]), ')/2', '+',
        #      settings[i-1], '+' , '(', settings[i], '-', len(text[i]),')/2')


        summ = (summ - (settings[i-1]-len(text[i-1]))/2 + settings[i-1] +
                (settings[i]-len(text[i]))/2)-i*0.7
        #print(summ, end = '  ')
    #print(summ)
    return summ

def DrawShapka(window):
    text = ['№', 'Диапазон', 'x = ?', 'y = ?','Кол-во итер.',
            'Время','Код ош.']
    setting = [22, 100, 250, 363, 438, 565, 655]
    settings = [10, 42, 34, 27, 25, 34, 15]
    y = 21
    for i in range(len(text)):
        label = Label(window, text = text[i])
        #print(settings, i, text)
        x = 4 + 4*Place(settings, i, text)
        label.place(x = setting[i], y = y)
        #print(setting[i])

def DrawResult(root, results):
    setting = [23, 100, 240, 360, 470, 550, 670]
    y = 21
    for i, result in enumerate(results):
        text = CompliteText(i, result)
        for j in range(len(setting)):
            label = Label(root, text = text[j])
            label.place(x = setting[j], y = y*(i*2+3))

def CompliteText(i, result):
    form = ['{:}',
        '({:.1f}; {:.1f})',
        '{:.6f}',
        '{:.0e}',
        '{:}',
        '{:.6f}',
        '{:}']
    text = [str(i+1)]
    for i in range(len(result)):
        if i == 0:
            text.append(form[i+1].format(result[i][0], result[i][1]))
        else:
            text.append(form[i+1].format(result[i], result[i]))
    #print(text)
    return text
        

def OutputGraph():
    #print('I will use matplotlib there!')
    parametres = get_parametres(windows[0])
    diapason = [int(parametres[0]), int(parametres[1])]
    DrawGraphic(f, diapason)
    

def DrawGraphic(f, interval):
    function = 'y = sin(x)'
    x = []
    y = []
    sh = (interval[1] - interval[0])/100
    i = interval[0] - sh
    while i<interval[1]:
        i += sh
        x.append(i)
        y.append(f(i))
    #print(x)
    #print(y)
    plt.plot(x, y, '.-b', label='График sin(x)' , linewidth = 2)
    plt.axis('equal')

    x1 = []
    y1 = []
    sh = (interval[1] - interval[0])/100
    i = interval[0] - sh
    while i<interval[1]:
        i += sh
        print(round(diff2f(i), 4))
        if round(diff2f(i), 1) == 0:
            x1.append(i)
            y1.append(f(i))
    print(x1,y1)
    plt.scatter(x1, y1, color = 'r', label='Точки перегиба' , linewidth = 5)
    plt.legend()
    plt.title('{}'.format(function))
    plt.show()

def get_parametres(window):
    parametres = []

    for i in range(4, 9):
        parametr = window['widgets'][i][1].get()
        parametres.append(parametr)

    return parametres

def check_parametres(parametres):
    condition = True
    for i in range(5):
        if i != 3:
            try:
                parametres[i] = int(parametres[i])
            except:
                condition = False
                break
        else:
            try:
                parametres[i] = float(parametres[i])
            except:
                condition = False
                break
    return condition

def main():
    windows.append(WindowOfParametres())

    
windows = []
main()
