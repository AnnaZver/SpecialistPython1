# Дано целое число. Определить, заканчивается ли оно число цифрой 5?
# Формат входных данных: Целое положительно число
# Формат выходных данных: Если число оканчивается цифрой 5, вывести «YES», в противном случае — вывести «NO».

number = float(input())  # Считываем вещественное число
if number % 5 == 0 and number % 10 != 0:
	print("заканчивается на 5")

else:
	print("не заканчивается на 5")
