number = int(input())
thousand = number // 1000 # находим первую цифру
hundred = number % 1000 // 100 # находим вторую цифру
ten = number % 100 // 10 # третью
one = number % 10 # четвертую
print(f'Цифра в позиции тысяч равна {thousand}')
print(f'Цифра в позиции сотен равна {hundred}')
print(f'Цифра в позиции десятков равна {ten}')
print(f'Цифра в позиции единиц равна {one}')