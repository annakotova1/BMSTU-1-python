from tkinter import *

window = Tk()

def show():
    canv = Canvas(window, width = 500, height = 500, bg = '#FF00F0')
    w1 = Tk()
    m = 'line'
    m.pack()
    w1.mainloop()

canv = Canvas(window, width = 500, height = 500, bg = '#FF00F0')

but1 = Button(text = 'Solve', command = show)

canv.create_text(200,200,text = 'Уточнение корней')
canv.pack()
but1.pack()
window.mainloop()
