i = 0
number = -5
while i < 10:
    if i == number:
        print (f'здесь есть число {number}')
        i += 1
        continue
    break
    i += 1
else:
    print (f'здесь нет числа {number}')
