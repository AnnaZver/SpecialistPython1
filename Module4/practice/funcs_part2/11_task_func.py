# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    sum = 0
    n = 0
    for el in args:
        sum  = sum + el
        n += 1
    el_average = sum / n
    return el_average

def gen_list(size, at=-10, to=10):
    import random
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

print(average(*my_list))
print(average(*my_tuple))

