from tkinter import *
import matplotlib as plt
import numpy as np
from Solve2 import solve

#result[0]= [diapazon, x_n, y_n, i_n, t_n, e_n]
#results = [result, ...]

root = Tk()

Title = Label(root, font = ' 20', text = 'Введите данные: ')

label1 = Label(root, text = 'Левая граница интервала (а): ')
entry1 = Entry(root)

label2 = Label(root, text = 'Правая граница интервала (b): ')
entry2 = Entry(root)

label3 = Label(root, text = 'Шаг разбиения: ')
entry3 = Entry(root)

label4 = Label(root, text = 'Точность: ')
entry4 = Entry(root)
entry4.insert(0, '0,0001')


label5 = Label(root, text = 'Максимальное кол-во итераций: ')
entry5 = Entry(root)
entry5.insert(0,'100')

Title.grid(row = 0, column = 0, columnspan = 11)

label1.grid(row = 1, column = 0, columnspan = 5)
entry1.grid(row = 1, column = 5, columnspan = 5)

label2.grid(row = 2, column = 0, columnspan = 5)
entry2.grid(row = 2, column = 5, columnspan = 5)

label3.grid(row = 3, column = 0, columnspan = 5)
entry3.grid(row = 3, column = 5, columnspan = 5)

label4.grid(row = 4, column = 0, columnspan = 5)
entry4.grid(row = 4, column = 5, columnspan = 5)

label5.grid(row = 5, column = 0, columnspan = 5)
entry5.grid(row = 5, column = 5, columnspan = 5)

root.update_idletasks()
geo = root.geometry()
print(geo)


root.mainloop()
