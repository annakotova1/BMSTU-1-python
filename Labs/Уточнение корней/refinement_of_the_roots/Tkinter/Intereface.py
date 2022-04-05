from tkinter import *
import matplotlib.pyplot as plt
from Solve2 import solve
from math import sin

class WindowInputData():
    errorlabel = None
    def __init__(self):
        self.root = Tk()
        self.root.title = 'Уточнение корней'
        self.Title = Label(text = 'Введите значения', font = ' 20')        
        self.leftborderlabel = Label(self.root,
                                     text = 'Левая граница интервала (а): ')
        self.rightborderlabel = Label(self.root,
                                     text = 'Правая граница интервала (b): ')
        self.stepsplitlabel = Label(self.root,
                                     text = 'Шаг разбиения: ')
        self.accuracylabel = Label(self.root,
                                     text = 'Точность: ')
        self.maxittlabel = Label(self.root,
                                     text = 'Максимальное кол-во итераций: ')

        self.leftborderentry = Entry(self.root)
        self.rightborderentry = Entry(self.root)
        self.stepsplitentry = Entry(self.root)
        self.accuracyentry = Entry(self.root)
        self.accuracyentry.insert(0, '0.0001')
        self.maxittentry = Entry(self.root)
        self.maxittentry.insert(0, '100')

        self.accurcheck1 = IntVar()
        self.accurcheck1.set(1)
        self.accurcheck2 = IntVar()
        self.accuracytitle = Label(text = 'Точность', font = ' 15')
        self.accuracycheck1 = Checkbutton(self.root,text=u'|x1-x2|<eps',
                                        variable = self.accurcheck1,
                                        onvalue = 1 ,offvalue = 0)
        self.accuracycheck2 = Checkbutton(self.root,text=u'f(x0)<eps',
                                        variable = self.accurcheck2,
                                        onvalue = 1, offvalue = 0)


        self.buttoncalculate = Button(text = 'Посчитать',
                                      command = self.GetResults)
        self.show()
        
    def show(self):
        self.Title.grid(row = 0, column = 0, columnspan = 11)
        self.leftborderlabel.grid(row = 1, column = 0, columnspan = 5)
        self.leftborderentry.grid(row = 1, column = 5, columnspan = 5)
        self.rightborderlabel.grid(row = 2, column = 0, columnspan = 5)
        self.rightborderentry.grid(row = 2, column = 5, columnspan = 5)
        self.stepsplitlabel.grid(row = 3, column = 0, columnspan = 5)
        self.stepsplitentry.grid(row = 3, column = 5, columnspan = 5)
        self.accuracylabel.grid(row = 4, column = 0, columnspan = 5)
        self.accuracyentry.grid(row = 4, column = 5, columnspan = 5)
        self.maxittlabel.grid(row = 5, column = 0, columnspan = 5)
        self.maxittentry.grid(row = 5, column = 5, columnspan = 5)
        self.accuracytitle.grid(row = 6, column = 0, columnspan = 11)
        self.accuracycheck1.grid(row = 7, column = 4, sticky = 'w')
        self.accuracycheck2.grid(row = 8, column = 4, sticky = 'w')
        self.buttoncalculate.grid(row = 9, column = 0, columnspan = 11)

    def GetResults(self):
        a = self.leftborderentry.get() 
        b = self.rightborderentry.get()
        sh = self.stepsplitentry.get()
        eps = self.accuracyentry.get()
        maxitt = self.maxittentry.get()
        
        a = Float(a)
        b = Float(b)
        sh = Float(sh)
        eps = Float(eps)
        maxitt = Int(maxitt)

        if a>b:
            a,b = b,a
            print(a,b)
            self.leftborderentry.insert(0, str(int(round(a))))
            self.rightborderentry.insert(0, str(int(round(b))))
        
        results = [a, b, sh, eps, maxitt]
        
        for i in results:
            if i == 'error':
                self.errorlabel = Label(self.root,
                                        text = 'Данные введенны не корректно')
                self.errorlabel.grid(row = 10, column = 0, columnspan = 11)
                return 0
            
        if self.errorlabel:
            self.errorlabel.destroy()
            
        self.results = results
        #self.results = solve(f, self.results)
        
        interval = [a,b]
        DrawGraphic(f, interval)
        
        #Output(self.results)

def f(x):
    y = sin(x)
    return y

def Float(num):
    try:
        num = float(num)
    except:
        num = 'error'
    return num

def Int(num):
    try:
        num = int(num)
    except:
        num = 'error'
    return num  

def DrawGraphic(f, interval):
    x = []
    y = []
    sh = (interval[1] - interval[0])/100
    i = interval[0] - sh
    while i<interval[1]:
        i += sh
        x.append(i)
        y.append(f(i))
    print(x)
    print(y)
    plt.plot(x, y, '.-m', label='График sin(x)' , linewidth = 2)
    plt.axis('equal')
    plt.show()

class WindowTable():
    settings = [15, 65, 50, 40, 30, 50, 15]
    probel = '   '
    form = ['{:^' + str(settings[0]) + '}',
                [('({:^' + str(int((settings[1]-3)/2)) +
                '.1f};{:^' + str(int((settings[1]-3)/2)) +'.1f})'),
                '{:^' + str(settings[1]) + '}'],
                '{:^' + str(settings[2]) + '.7f}',
                '{:^' + str(settings[3]) + '.0e}',
                '{:^' + str(settings[4]) + '}',
                '{:^' + str(settings[5]) + '.8f}',
                '{:^' + str(settings[6]) + '}']
    
    text = [['№', 'Диапазон', 'x = ?', 'y = ?',
            'Кол-во итераций', 'Время','Код ошибки']]
    
    valuebg = 'white'
    background = '#aaaaaa'
    
    def __init__(self):
        self.root = Tk()
        self.root['bg'] = self.background

        self.BuildShapka()
        self.ShowShapka()
        '''self.table = []
        for j, result in enumerate(results):
            string = '{:' + self.settings[i+1] +'}'
            array = [Label(text = j)]
            for i, value in enumerate(result[0]):
                if i == 
                string = '{:' + self.settings[i+1] +'}'
                array.append(Label(text = i))
            self.table.append(array)'''

            
    def BuildShapka(self):
        self.shapka = [[Label(text = '',bg = self.background)]]
        
        for i, array_values in enumerate(self.text):
            shapka_line = [Label(self.root, text = self.probel,
                                         bg = self.background, font = ' 8')]
            print(i, array_values, self.settings)
            for j, value in enumerate(array_values):
                print(j, value)
                string = ('{:^'+str(self.settings[j])+'}').format(
                    '')
                shapka_line.append(Label(self.root, text = string,
                                         bg = self.valuebg, font = ' 8'))
                shapka_line.append(Label(self.root, text = self.probel,
                                         bg = self.background, font = ' 8'))
            self.shapka.append(shapka_line)
            self.shapka.append([Label(text = '',bg = self.background)])

    def ShowShapka(self):
        for i, shapka_line in enumerate(self.shapka):
            for j, shapka_field in enumerate(shapka_line):
                shapka_field.grid(row = i, column = j)

    def BuildTestOfShapka(self):
        self.shapka = [[Label(text = '',bg = self.background)]]
        
        for i, array_values in enumerate(self.text):
            shapka_line = [Label(self.root, text = self.text[i],
                                         bg = self.background, font = ' 8')]
            self.shapka.append(shapka_line)
            self.shapka.append([Label(text = self.probel,
                                      bg = self.background)])
            self.shapka

        
            

        


        



            
'''window = WindowInputData()
window.root.mainloop()'''
window = WindowTable()
window.root.mainloop()
