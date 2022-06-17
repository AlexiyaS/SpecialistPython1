# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Введите число элементов: "))
elem_sum = 0
i = 0
while i < n:
    element = random.randint(-100, 100)
    if element >= 0 and element % 2 == 0:
        elem_sum += element
    i += 1
print(elem_sum)
