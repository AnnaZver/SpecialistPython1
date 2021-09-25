price = float(input("введите цену:"))
n = 1

while n <= 20:
    print(n, round(price, 2), "Rub.")
    price = price / n * (n+1)
    n = n + 1
