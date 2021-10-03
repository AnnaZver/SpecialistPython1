# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
tup = (2, 4, 6, -4, 12, 0, 5)
long_num = tup[0]
for num in tup:
    if num > long_num:
        long_num = num

print(long_num)
