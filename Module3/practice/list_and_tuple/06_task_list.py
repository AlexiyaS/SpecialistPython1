# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите второе число: "))    # Второе число
numbers = []
for number in range(first_number, second_number):
    numbers.append(number)
print(numbers)

for number in numbers:
    if number % 3 == 0:
        print(number)
        number += 1
