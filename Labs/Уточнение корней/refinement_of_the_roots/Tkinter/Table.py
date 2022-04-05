from tkinter import *
import matplotlib.pyplot as plt
from Solve2 import solve
from math import sin

#  results 
#
# 
#
#

class WindowTable():
    
    settings = [10, 42, 34, 27, 20, 34, 15] #Sizes of columns
    probel = ' '*3

    tablecolumn = 7
    tablerow = 0

    #ShapkaText
    text = ['№', 'Диапазон', 'x = ?', 'y = ?','Кол-во итер.',
            'Время','Код ош.']

    #Colors
    valuebg = 'white'
    background = '#aaaaaa'

    def __init__(self, results):
        self.root = Tk()
        self.root['bg'] = self.background
        self.result = results
        self.tablerow = len(results)

        self.BuildTable()
        self.ShowTable()
        self.BuieldTextOfShapka()
        self.ShowTextOfShapka()

    def BuildTable(self):
        self.shapka = [[Label(text = '',bg = self.background)]]
        
        for i in range(self.tablerow):
            shapka_line = [Label(self.root, text = self.probel,
                                         bg = self.background, font = ' 8')]
            for j in range(self.tablecolumn):
                string = ('{:^'+str(self.settings[j])+'}').format('')
                shapka_line.append(Label(self.root, text = string,
                                         bg = self.valuebg, font = ' 8'))
                shapka_line.append(Label(self.root, text = self.probel,
                                         bg = self.background, font = ' 8'))
            self.shapka.append(shapka_line)
            self.shapka.append([Label(text = '',bg = self.background)])
    def ShowTable(self):
        for i, shapka_line in enumerate(self.shapka):
            for j, shapka_field in enumerate(shapka_line):
                shapka_field.grid(row = i, column = j)

    def BuieldTextOfShapka(self):
        self.text_shapka = [Label(text = '',bg = self.background)]
        
        for i in range(self.tablecolumn):
            shapka_line = Label(self.root, text = self.text[i],
                                         bg = self.valuebg, font = ' 8')
            self.text_shapka.append(shapka_line)
            self.text_shapka.append(Label(text = self.probel,
                                          bg = self.background))

    def ShowTextOfShapka(self):
        for i, shapka_line in enumerate(self.text_shapka):
            print(self.text_shapka, shapka_line)
            shapka_line.grid(row = 1, column = i)

            
result = [[],[]]    
window = WindowTable(result)
window.root.mainloop()
