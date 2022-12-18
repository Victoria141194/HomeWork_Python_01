# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

user_number = int(input('Введите номер четверти: '))

if user_number == 1:
    print('X > 0 and Y > 0')
elif user_number == 2:
    print('X < 0 and Y > 0')
elif user_number == 3:
    print('X < 0 and Y < 0')
elif user_number == 4:
    print('X > 0 and Y < 0')
else:
    print('Ошибка! Введите число от 1 до 4')