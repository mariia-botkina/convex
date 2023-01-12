from classes import Vector, Polygon
from values import left, right

def get_convex(points):
    global left, right
    points.sort(key = lambda i: i.x, reverse= True)

    start_point = min(points, key = lambda i: i.y ) #находим самую нижнюю точку (по координате y)
    points.remove(start_point) #убираем из рассмотрения стартовую точку

    points.sort(key = lambda i: start_point.get_vector(i).cosinus(Vector(-1,0))) #сортируем точки по уголу между вектором, соединяющим стартовую точку и вектором (-1, 0) 

    for i in range(len(points) - 1): #находим точки с одинаковым синусом, сортируем повторно по расстоянию до стартовой точки
        if start_point.get_vector(points[i]).cosinus(Vector(-1,0)) == start_point.get_vector(points[i + 1]).cosinus(Vector(-1,0)): #углы одинаковые
            if left == -1: #нашли новую последовательность с одинаковым углом
                left, right = i, i + 1 #запоминаем индексы
            else: #все еще находимся в последовательности с одинаковым углом, меняем только правый индекс
                right += 1 
        else: #углы разные
            if left != -1: #есть что сортировать 
                points[left:right + 1] = sorted(points[left:right + 1], key = lambda i: start_point.get_vector(i).get_len(), reverse = True)
                left, right = -1, -1
    if left != -1: #если точки закончились, но есть, что сортировать по расстоянию – сортируем
        points[left:right + 1] = sorted(points[left:right + 1], key = lambda i: start_point.get_vector(i).get_len(), reverse = True)
    left, right = -1, -1

    polygon = Polygon(start_point)

    for i in points: 
        polygon.check_angle(i)
    polygon.add_vertex(start_point)
    points.append(start_point)

    return polygon.vertexes.head #возврат начальной точки, последовательно соединенной с остальными вершинами многоугольника