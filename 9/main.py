x = 10

def add_to_x(y):
    x = 5
    x = x + y
    print (f'x Внутри функчии: {x}')
    

add_to_x(3)

print(f'x за пределами функции {x}')