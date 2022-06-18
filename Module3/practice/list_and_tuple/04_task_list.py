# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
numbers = []
n = int(input("Введите число элементов: "))
for _ in range(n):
    number = random.randint(-10, 10)
    numbers.append(number)
print(numbers)
summa = 0
for number in numbers:
    if number > 0:
        summa += number
print(summa)
