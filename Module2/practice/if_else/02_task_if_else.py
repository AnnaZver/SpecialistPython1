# Дано целое число. Определить, заканчивается ли оно число цифрой 5?
# Формат входных данных: Целое положительно число
# Формат выходных данных: Если число оканчивается цифрой 5, вывести «YES», в противном случае — вывести «NO».

number = float(input("введите число:"))
if number < 0:
    print("отрицательное")
else:
    print("положительное")
