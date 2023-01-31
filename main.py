from tkinter import *  
from classes import Point
from do_convex import get_convex
from values import w, h, const, res, points

def canva_coordinates(x): #перевод из декартовых координат в координаты холста
    return 20 * x + w/ 2

def decart_coordinates(x): #перевод из координат холста в декатовы координаты 
    return (x - w/2) / 20

def see_coordinate(coordinates): #вывод координат на лейбл
    global res
    res = f"{res}{coordinates[0], coordinates[1]}\n"
    lbl_1.configure(text=res) 

def add_to_points(coordinates): #добавление точки в рассматриваемое множество
    global points
    points.append(Point(coordinates))

def the_same_point_message(): #ошибка повтора точки
    global res
    lbl_1.configure(text=f"{res}Уже есть такая точка\n") 

def draw_point(x, y): #отрисовка точки по координатам
    c.create_oval(x,y,x,y,fill="white", width=10)

def draw_coordinate_system(): #отрисовка системы координат
    c.create_line(w / 2, 5 , w / 2, w) #ось x
    c.create_line(0, h / 2, h, h /2) #ось y
    c.create_line(w / 2, 5, w / 2 + const/ 3, const) #стрелка на оси x
    c.create_line(w / 2, 5, w / 2 - const / 3, const)
    c.create_line(h, h / 2, h - const, h /2 + const / 3) #стрелка на оси y
    c.create_line(h, h / 2, h - const, h /2 - const / 3)

def convex(): #построение выпуклой оболочки
    global points
    delete_not_all() #очищение холста
    for i in points: #отрисовка точек
        draw_point(canva_coordinates(i.x), canva_coordinates(-i.y))
    vertex = get_convex(points) #нахождение вершин многоугольника
    while vertex.next != None: #папарное соединение вершин
        prev_vertex = vertex
        vertex = vertex.next
        c.create_line(canva_coordinates(prev_vertex.x), canva_coordinates(-prev_vertex.y),canva_coordinates(vertex.x), canva_coordinates(-vertex.y))

def delete_all(): #полное очищение всех данных в программе
    global points, res
    c.delete('all')
    draw_coordinate_system()
    points = []
    res = ''
    lbl_1.configure(text='Здесь будут координаты точек') 

def delete_not_all(): #очищение холста
    global points, res
    c.delete('all')
    draw_coordinate_system()

def draw_point_with_click(event): #отрисовка точки по клику на холсте
    x=event.x
    y=event.y
    coordinates = [(x - w/2) / 20, (-y + w/ 2) / 20]
    if f'({coordinates[0]}, {coordinates[1]})' not in res:
        draw_point(x, y)
        add_to_points(coordinates)
        see_coordinate(coordinates)
    else:
        the_same_point_message()

def draw_point_with_coordinates(): #отрисовка точки по введенным координатам
    global res
    for i in txt.get().split(): #проверка введенных данных
        try:
            float(i)
        except ValueError:
            lbl_1.configure(text=f'{res}Ошибка ввода') 
    else:
        coordinates = list(map(float, txt.get().split()))
        if len(coordinates) == 2:
            if f'({coordinates[0]}, {coordinates[1]})' not in res:
                draw_point(canva_coordinates(coordinates[0]), canva_coordinates(-coordinates[1]))
                add_to_points(coordinates)
                see_coordinate(coordinates)
            else:
                the_same_point_message()
        else:
            lbl_1.configure(text=f'{res}Ошибка ввода') 
  
window = Tk() #создаем окно программы
window.title("Выпуклая оболочка")  
window.geometry(f'{w + 305}x{h + 305}+400+0') #задаем размер окна
c = Canvas(window, width = w, height = h, bg = 'black') #создаем холст
c.grid(column= 1, row=5)
c.bind('<Button-1>', draw_point_with_click)

lbl = Label(window, text="Введите координаты точки через пробел")  
lbl.grid(column=0, row=0)  
lbl_1 = Label(window, text="Здесь будут координаты точек")  
lbl_1.grid(column=0, row=5) 

txt = Entry(window,width=10) #строка ввода
txt.grid(column=0, row=1)  
txt.focus()

btn = Button(window, text="Добавить точку", command=draw_point_with_coordinates)  
btn.grid(column=0, row=2)  
btn_1 = Button(window, text="Построить оболочку", command=convex)  
btn_1.grid(column=0, row=3)  

btn_2 = Button(window, text="Очистить холст", command=delete_all)  
btn_2.grid(column= 0, row=4)
draw_coordinate_system()
window.mainloop()
