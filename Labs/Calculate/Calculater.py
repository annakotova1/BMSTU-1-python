from tkinter import *

#Рисует окно калькулятора и основные вижеты
def draw_calculater():
    root = Tk()
    
    widgets = {'titles': [], 'labels': [], 'entries': [], 'button': []}
    
    root.title('Calculator')
    title1 = Label(root, text = "Перевод из 10-ной системы исчесления в 16-ную",
                   font = 20)
    title2 = Label(root, text = "и обратно", font = 20)
    entry_10 = Entry(root)
    label_10 = Label(root, text = "10")
    label_16 = Label(root, text = "16")
    entry_16 = Entry(root)
    button_repeat_activities = Button(root,
                                      text = "Повторение основных действий",
                                      command = repeat)
    button_clean = Button(root, command = clean,
                          text = "Очистка полей")
    button_info = Button(root, command = info,
                         text = "Информация об авторе и о программе")
    button_translate = Button(root, command = translate)

    widgets['titles'] = [title1, title2]
    widgets['labels'] = [label_10, label_16]
    widgets['entries'] = [entry_10, entry_16]
    widgets['button'] = [button_repeat_activities, button_clean, button_info,
                         button_translate]

    min_size = button_info.winfo_reqwidth()
    
    button_repeat_activities.size = min_size
    button_clean.size = min_size

    title1.grid(row = 0, columnspan = 3)
    title2.grid(row = 1, columnspan = 3)
    label_10.grid(row = 2, column = 0)
    label_16.grid(row = 2, column = 2)
    button_translate.grid(row = 3, column = 1, columnspan = 1)
    entry_10.grid(row = 3, column = 0)
    entry_16.grid(row = 3, column = 2)
    button_repeat_activities.grid(row = 4, columnspan = 3)
    button_clean.grid(row = 5, columnspan = 3)
    button_info.grid(row = 6, columnspan = 3)
    
    root.mainloop()

'''
    # get the width of the bigger button
minwidth = max(self.btn1.winfo_reqwidth(), self.btn2.winfo_reqwidth())
for x in range(2):
    Grid.columnconfigure(master, x, weight=1, minsize=minwidth)
'''
def clean(root, widgets):
    widgets['entries'][0] = ''
    widgets['entries'][1] = ''

def info():
    root = Tk()
    root.title('Info')
    t = '''Автор: Боренко Анастасия группа: ИУ7-22Б
Инструкция:
Для перевода из 16-ной системы в 10-ную надо ввести число в поле "10",
Для перевода из 10-ной системы в 16-ную надо ввести число в поле "16"
А после нажать на стрелку

Кнопка повторить основные действия - повторяет несколько последних операций'''
    text = Text(root, width = 25, height = 5, wrap = WORD)

def repeat():
    print("Hello, word!!!")

def translate(value):
    symbols = {'10': ['0','1','2','3','4','5','6','7','8','9'],
               '16': ['0','1','2','3','4','5','6','7','8','9','A',
                      'B','C','D','E','F']}
    'con, value, sys = check_fields(widgets)'
    sys = ['10', '16']
    con = True
    a = sys[0]  #Система исчисления из которой переводят
    b = sys[1]  #Система исчисления в которую переводят
    new_value = ''
    if con:
        while value:
            m = value % int(sys[1])
            new_value = symbols[sys[1]][m] + new_value
            value = value // int(sys[1])
            print(value, symbols[sys[1]][m])
    return new_value

def translate_10_into_16(value):
    symbols = {'10': ['0','1','2','3','4','5','6','7','8','9'],
               '16': ['0','1','2','3','4','5','6','7','8','9','A',
                      'B','C','D','E','F']}
    sys = ['10', '16']
    new_value = ''
    while value:
        m = value % int(sys[1])
        new_value = symbols[sys[1]][m] + new_value
        value = value // int(sys[1])
    return new_value

def translate_16_into_10(value):
    symbols = {'10': ['0','1','2','3','4','5','6','7','8','9'],
               '16': ['0','1','2','3','4','5','6','7','8','9','A',
                      'B','C','D','E','F']}
    sys = ['10', '16']
    new_value = 0 
    for i in value:
        new_value = new_value * 16 + symbols['16'].index(i)
        print(new_value, i)
    return new_value

draw_calculater()
print("draw")

