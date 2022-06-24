# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if len(str(ticket_number)) != 6 or (type(ticket_number) is not int):
        return 'Wrong ticket number'
    else:
        sum_begin = int(ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])
        sum_end = int(ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])
        if sum_begin == sum_end:
            return f'Билет {ticket_number} счастливый'
        else:
            return f'Билет {ticket_number} обычный' 


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
