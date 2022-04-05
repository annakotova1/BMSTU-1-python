#Импорт необходимых модулей
from math import sin, log
from tkinter import *
import matplotlib.pyplot as plt
from SolveWithoutDiffMethodsAndEps import solve
#импорт функции, которая будет выдавать results все результаты,
#необходимые для того, чтобы нарисовать таблицу

parametres = ['sin(x)', '-sin(x)', 1, 10, 1, 0.001, 100]

#Функция рисует окно с параметрами
def window_of_parametres():
    #Словарь, хранящий все виджеты по их типам
    global widgets_of_window_of_parametres
    widgets_of_window_of_parametres = {'root': Tk(), 'titles': {},
                                        'labels': [], 'entries': [],
                                        'buttons': {}, 'gaps': [], 'frames':{},
                                        'errors': [], 'number_of_rows': 0,
                                        'current_errors_of_input': []}
    #Цвет фона окна и заголовок окна
    widgets_of_window_of_parametres['root']['bg'] = '#dffddd'
    widgets_of_window_of_parametres['root'].title('Уточнение корней')

    #Рисует виджеты окна
    draw_widgets_parametres(widgets_of_window_of_parametres['root'],
                            widgets_of_window_of_parametres)

    #Размещает виджеты в окне
    place_widgets_on_window_of_parametres(widgets_of_window_of_parametres)

#Функция рисует виджеты окна параметров
def draw_widgets_parametres(root, widgets):
    #Рисует заголовок, и основную информацию
    widgets['titles']['title'] = Label(root, text = 'Уточнение корней',
                                       font = 'Arial 32', bg = '#dffddd')
    widgets['titles']['instruction'] = Label(root, text = 'Введите данные',
                                             font = 'Arial 18', bg = '#dffddd')
    
    #Рисует поля и подписи к ним, и заполняет поля значениями по умолчанию
    text = ['Функция','Вторая производная', 'Левая граница интервала',
            'Правая граница интервала', 'Шаг', 'Точность',
            'Макс. кол-во иттераций']
    
    for i in range(len(text)):
        widgets['labels'].append(
            Label(root, text = text[i], bg ='#dffddd',  font = 'Arial 11'))

    global parametres
    parametres_string_var = []
    for i in range(len(parametres)):
        parametres_string_var.append(StringVar())
        parametres_string_var[i].set(parametres[i])
        
    for i in range(len(text)):
        widgets['entries'].append(
            Entry(root, textvariable = parametres_string_var[i],
                  font = 'Arial 11'))

    #Рисует строки, задающие отступы
    widgets['gaps'].append(Label(root, text = '     ', bg = '#dffddd'))
    widgets['gaps'].append(Label(root, text = '     ', bg = '#dffddd'))
    widgets['gaps'].append(Label(root, text = '     ', bg = '#dffddd',
                                 font = 'Arial 1'))
    widgets['gaps'].append(Label(root, text = '     ', bg = '#dffddd',
                                 font = 'Arial 1'))
    widgets['gaps'].append(Label(root, text = '     ', bg = '#dffddd',
                                 font = 'Arial 1'))
    
    
    #Рисует кнопки
    widgets['buttons']['draw_table'] = Button(root, text = 'Нарисовать таблицу',
                                   bg = '#ffffff', command = draw_table,
                                   font = 'Arial 11')
    widgets['buttons']['draw_graphic'] = Button(root, text = 'Нарисовать график',
                                     bg = '#ffffff', command = draw_graphic,
                                     font = 'Arial 11')

    errors = ['Функция задана некорректно',
              'Вторая производная функции заданна некорректно',
              'Левая граница интервала задана некорректно',
              'Правая граница интервала задана некорректно',
              'Шаг задан некорректно',
              'Точность задана некоректно',
              'Макс. кол-во иттераций заданно некорректно', '']

    #Создает виджеты сообщения об ошибке
    widgets['frames']['box_of_errors'] = Frame(root, bg = '#ff8888')
    for i in range(len(errors)):
        widgets['errors'].append(Label(widgets['frames']['box_of_errors'],
                                       text = errors[i],
                                       bg = '#ff8888', fg = '#ffffff'))
    for i in widgets:
        print(i, widgets[i], '\n')

#Функция размещает виджеты в окне параметров
def place_widgets_on_window_of_parametres(widgets):
    #Размещает заголовок
    widgets['titles']['title'].grid(row = 1, column = 1, columnspan = 2)
    widgets['titles']['instruction'].grid(row = 2, column = 1, columnspan = 2)

    #Размещает поля ввода
    for i in range(len(widgets['labels'])):
        widgets['labels'][i].grid(row = i + 4, column = 1)
        widgets['entries'][i].grid(row = i + 4, column = 2)

    #Размещает пробелы и отступы
    widgets['gaps'][0].grid(row = 3, column = 0)
    widgets['gaps'][1].grid(row = i + 5, column = 4)
    widgets['gaps'][2].grid(row = i + 7)
    widgets['gaps'][3].grid(row = 0)
    widgets['gaps'][4].grid(row = i + 9)

    #Размещает кнопки
    widgets['buttons']['draw_table'].grid(row = i + 6, column = 1)
    widgets['buttons']['draw_graphic'].grid(row = i + 6, column = 2)
    widgets['number_of_rows'] = i + 7
    widgets['frames']['box_of_errors'].grid(row = i + 8, column = 1,
                                            columnspan = 2)

#Функция получает параметры из полей
def get_parametres(entries = []):
    if entries == []:
        entries = widgets_of_window_of_parametres['entries']
    global parametres
    parametres = []
    for i in range(len(entries)):
        parametres.append(entries[i].get())

#Функция проверяет полученные параметры и выводит виджеты ошибок
#Результатом работы является True - сли введенные параметры корректны
#или False - если некорректны, и список выведенных виджетов ошибок
def check_parametres():
    #Получает введенные параметры и виджеты окна
    global parametres, widgets_of_window_of_parametres

    #Убирает сообщения о старых ошибках ввода
    
    widgets_of_window_of_parametres['frames']['box_of_errors'].config(
                                                                bg = '#dffddd')
    n = 0
    for i in widgets_of_window_of_parametres['current_errors_of_input']:
        widgets_of_window_of_parametres['errors'][i].pack_forget()
        n += 1
    
    print('Old Errors:',
              widgets_of_window_of_parametres['current_errors_of_input'], n)
    if n != 0:
        widgets_of_window_of_parametres['number_of_rows'] -= n+1

    #Массив, в котором хранятся коды совершенных пользователем ошибок
    result = []
    
    #Ищет ошибки в параметрах
    for i in range(len(parametres)-1, -1, -1):
        if i < 2:
            if 2 in result:
                result.append(i)
                result.append(i-1)
                print(2 in result)
                break
            try:
                eval(parametres[i])
            except:
                result.append(i)
        elif i != 5:
            try:
                int(parametres[i])
            except:
                result.append(i)
        else:
            try:
                float(parametres[i])
            except:
                result.append(i)
            else:
                x = float(parametres[i])

    print('Errors: ', result, 'Parametres:', parametres)
    result.sort()

    #Выводит сообщения об ошибках
    n = len(result)
    if n != 0:
        widgets_of_window_of_parametres['frames']['box_of_errors'].config(
                                                                bg = '#ff8888')
    
    for i in result:
        widgets_of_window_of_parametres['errors'][i].pack(side = TOP)
    widgets_of_window_of_parametres['number_of_rows'] += n+1
    widgets_of_window_of_parametres['current_errors_of_input'] = result
    return result

def draw_graphic():
    get_parametres(widgets_of_window_of_parametres['entries'])
    print(check_parametres())
    print('')
    
def draw_table():
    print('Table')

widgets_of_window_of_parametres = {}
window_of_parametres()
