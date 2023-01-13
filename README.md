# convex_hull
EN:
⚡️A program for constructing a convex hull of a set in two-dimensional space by points.

The user sets points on the plane. This can be done in two ways:
1) by clicking on the place where the point should be, its coordinates are calculated automatically;
2) set using the x and y coordinates separated by a space in the input line and click on the "add point" button.

Using the Graham algorithm, the vertices of a convex polygon will be found. To do this, click on the "build shell" button. Graham 's algorithm:
1) find the point with the smallest y coordinate, if there are several of them, then choose the point with the largest x;
2) sort the points by the cosine of the angle between the vector (-1, 0) and the vectors connecting the starting point with them. To do this, we find the scalar product of vectors in coordinate form and divide by the product of their modules;
3) if several points lie on the same straight line with the starting point, then sort by descending distance from the starting point. To do this, we go through the array of points, construct the same vectors again and compare the modules of vectors that have equal cosine values relative to the vector (-1.0);
4) we start adding one point to the set of vertices of the new polygon;
5) if an angle greater than 180 degrees is formed between adjacent sides, then we remove the point common to these sides from the set of vertices. In order to understand whether the “inner” angle is greater than 180 degrees, it is enough to determine the orientation of the vectors. The oblique product, or rather its sign, will help us in this.;
6) when the vertices are over, add the starting point again.

After that, the sides of the resulting polygon are drawn on the canvas. The convex hull is constructed. Now you can add new points to the existing ones or clear the canvas using the "clear canvas" button.

▪️main.py file to run the program
▪️do_convex.py file with algorithm Graham
▪️classes.py file with classes that are used in the program code
▪️values.py file to store some values of the variables

❗️To run the program, you will need the Tkinter library.

![изображение](https://user-images.githubusercontent.com/104559877/212192669-61971a6d-2feb-4725-91d2-f34ebbc80852.png)

RUS:
⚡️Программа для построения выпуклой оболочки множества в двумерном пространстве по точкам.

Пользователь задает точки на плоскости. Это возможно сделать двумя способами:
1) нажав на место, где должна быть точка, её координаты высчитываются автоматически;
2)	задать с помощью координат x и y через пробел в строке ввода и нажать на кнопку "добавить точку".

С помощью алгоритма Грэхема будут найдены вершины выпуклого многоугольника. Для этого нужно нажать на кнопку "построить оболочку". Алгоритм Грэхема:
1)	находим точку с наименьшей координатой по y, если таких несколько, то выбираем точку с наибольшим x;
2)	сортируем точки по косинусу угла между вектором (-1, 0) и векторами, соединяющими стартовую точку с ними. Для этого находим скалярное произведение векторов в координатном виде и делим на произведение их модулей;
3)	если несколько точек лежат на одной прямой со стартовой точкой, то сортируем по убыванию расстояния от стартовой точки. Для этого проходим по массиву точек, вновь строим те же векторы и сравниваем модули векторов, у которых равны значения косинуса относительно вектора (-1,0);
4)	начинаем добавлять по одной точке к множеству вершин нового многоугольника;
5)	если между соседними сторонами образуется угол больше 180 градусов, то точку общую для этих сторон удаляем из множества вершин. Для того, чтобы понять, больше ли “внутренний” угол 180 градусов, достаточно определить ориентацию векторов. В этом нам поможет косое произведение, а точнее его знак;
6)	когда вершины закончились, добавляем еще раз стартовую точку.

После этого запускается отрисовка сторон получившегося многоугольника на холсте. Выпуклая оболочка построена. Теперь можно добавить новые точки к уже имеющимся или же очистить холст с помощью кнопки "очистить холст".

▪️main.py – файл запуска программы
▪️do_convex.py – файл с алгоритмом Грэхема
▪️classes.py – файл с классами, изпользуемыми в коде программы
▪️values.py – файл для хранения некоторых значений переменных

❗️Для запуска программы понадобится библиотека Tkinter.

![изображение](https://user-images.githubusercontent.com/104559877/212192669-61971a6d-2feb-4725-91d2-f34ebbc80852.png)
