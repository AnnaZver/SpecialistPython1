# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(x1, y1, x2, y2):
    dist = ((x2 - x1) **2 + (y2 - y1) ** 2) * 1/2
    return dist

def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    return a + b > c and b + c > a and a + c > b

print (can_triangle((10, 12), (14, 18), (12, 12)))
