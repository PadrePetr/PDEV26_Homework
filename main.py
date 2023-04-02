print("Введите 2 числа, означающие X и Y,\nгде X - горизонталь, Y - вертикаль")

field = [[" ", " ", "  "] for i in range(3)]

def square():
    print("    0 | 1 | 2 ")
    print("--------------")
    for i, row in enumerate(field):
        row = map(str, row)
        print(f"{i} | {' | '.join(row)}")
        print("--------------")

def get_cord():
    x, y = map(int, input('Введите координаты ').split())
    if 0 <= x <=2 and 0 <= y <=2:
        return x,y
    else:
        print("Укажите координаты, соответствующие требованиям")

num = 0
while True:
    num += 1

    square()

    x, y = get_cord()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "Y"