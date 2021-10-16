# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

sum = 0
with open("log1.txt", "r") as f:
    for line in f:
        if line.strip().isdigit():
            sum += int(line)
print(sum)
