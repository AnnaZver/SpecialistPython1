# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = (1,5,7,3,-10,)
sum_numbers = 0

for number in numbers:
    if number > 0:
        sum_numbers += number

print(sum_numbers)
