from values import digit 

class Point:
    def __init__(self, array): #инициализация точки 
        self.x = array[0]
        self.y = array[1]

    def print_point(self): #вывод координат точки
        print(f'{self.x} {self.y}')
    
    def get_vector(self, B): #нахождение вектора по координатам точек
        return Vector(B.x - self.x, B.y - self.y)
    
class Vector:
    def __init__(self, x, y): #инициализация вектора
        self.x = x
        self.y = y

    def get_len(self): #нахождение длины вектора
        return (self.x ** 2 + self.y ** 2) ** (1/2)
    
    def get_second_point(self, A): #нахождение второй точки скалярного произведения векторов
        x = round(self.x + A.x, digit)
        y = round(self.y + A.y, digit)
        return Point([x, y])

    def sum_vector(self, b): #нахождение суммы двух векторов
        return Vector(self.x + b.x, self.y + b.y)

    def sub_vector(self, b): #нахождение разности двух векторов
        return Vector(self.x - b.x, self.y - b.y)

    def scalar_product(self, b): #нахождение значения скалярного произведения векторов
        return self.x * b.x + self.y * b.y
    
    def cosinus(self, b): #нахождение косинуса между векторами 
        return self.scalar_product(b) / (self.get_len() * b.get_len())
    
    def cross_product(self, b): #нахождение значения векторного произведения (число)
       c = self.x * b.y - self.y * b.x
       return c

class Polygon:
    def __init__(self, A): #инициализация многоугольника
        self.vertexes = List_of_vertexes()
        self.vertexes.add(Vertex(A))
        self.number_of_vertexes = 1

    def add_vertex(self, A): #добавление вершины
        self.vertexes.add(Vertex(A))
        self.number_of_vertexes += 1

    def remove_vertex(self): #удаление последней вершины
        self.vertexes.delete()
        if self.number_of_vertexes > 0:
            self.number_of_vertexes -= 1

    def check_angle(self, i): #проверка угла между векторами
        if self.number_of_vertexes > 1:
            a = self.vertexes.head.vertex.get_vector(self.vertexes.head.next)
            b = self.vertexes.head.vertex.get_vector(i)
            if b.cross_product(a) < 0:
                self.remove_vertex() 
                self.check_angle(i)
            else:
                self.add_vertex(i)
        else:
            self.add_vertex(i)
    
    def print_vertexes(self): #вывод всех вершин
        self.vertexes.print()

class Vertex:
    def __init__(self,  A): #инициализация вершины
        self.vertex = A
        self.x = A.x
        self.y = A.y
        self.next = None

class List_of_vertexes():
    def __init__(self): #инициализация многоугольника
        self.head = None

    def add(self, A): #добавление вершины
        if self.head == None:
            self.head = A
        else:
            A.next = self.head
            self.head = A
    
    def delete(self): #удаление последней вершины
        if self.head != None:
            self.head = self.head.next
    
    def print(self): #вывод всех вершин
        start = self.head
        while start != None:
            print(f'({start.vertex.x}, {start.vertex.y})' )
            start = start.next