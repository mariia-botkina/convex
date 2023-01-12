# convex_hull
⚡️A program for constructing a convex hull of a set in two-dimensional space by points.

The user sets points on the plane. This can be done in two ways:
1) by clicking on the place where the dot should be;
2) set using the x and y coordinates separated by a space in the input line and click on the "add point" button.

Using the Graham algorithm, the vertices of a convex polygon will be found. To do this, click on the "build shell" button. Graham 's algorithm:
1) find the point with the smallest y coordinate, if there are several of them, then choose the point with the largest x;
2) sort the points by the angle between the vector (-1, 0) and the vectors connecting the starting point with them;
3) we start adding one point to the set of vertices of the new polygon;
4) if an angle is formed between adjacent sides greater than 180 degrees, then the point common to these sides is removed from the set of vertices;
5) when the vertices are over, add the starting point again.

After that, the sides of the resulting polygon are drawn on the canvas. The convex hull is constructed.
Now you can add new points to the existing ones or clear the canvas using the "clear canvas" button.

▪️main.py – file run the program
▪️do_convex.py – file Graham's algorithm 
▪️classes.py – file with classes, ispolzuemye in the program code
▪️values.py – file to store some values of the variables

❗️To run the program, you will need the Tkinter library.

RUS:
⚡️Программа для построения выпуклой оболочки множества в двумерном пространстве по точкам.

Пользователь задает точки на плоскости. Это возможно сделать двумя способами:
1) нажав на место, где должна быть точка;
2) задать с помощью координат x и y через пробел в строке ввода и нажать на кнопку "добавить точку".

С помощью алгоритма Грэхема будут найдены вершины выпуклого многоугольника. Для этого нужно нажать на кнопку "построить оболочку". Алгоритм Грэхема:
1) находим точку с наименьшей координатой по y, если таких несколько, то выбираем точку с наибольшим x;
2) сортируем точки по углу между вектором (-1, 0) и векторами соединяющими стартовую точку с ними;
3) начинаем добавлять по одной точке к множеству вершин нового многоугольника;
4) если образуется угол между соседними сторонами больше 180 градусов, то точку общую для этих сторон удаляем из множества вершин;
5) когда вершины закончились, добавляем еще раз стартовую точку.

После этого запускается отрисовка сторон получившегося многоугольника на холсте. Выпуклая оболочка построена.
Теперь можно добавить новые точки к уже имеющимся или же очистить холст с помощью кнопки "очистить холст".

▪️main.py – файл запуска программы
▪️do_convex.py – файл с алгоритмом Грэхема
▪️classes.py – файл с классами, изпользуемыми в коде программы
▪️values.py – файл для хранения некоторых значений переменных

❗️Для запуска программы понадобится библиотека Tkinter.
