# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
numbers = []

for number in range(first_number, second_number):
    if number % 3 ==0:
        numbers.append(number)

print(numbers)
