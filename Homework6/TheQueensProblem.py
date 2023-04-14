from random import randint

BOARD_SIZE = 8


def get_coordinates():
    global x, y
    x = []
    y = []
    for i in range(BOARD_SIZE):
        new_x, new_y = [int(s) for s in f'{randint(1, 8)} {randint(1, 8)}'.split()]
        print(f'{new_x}x{new_y}')
        x.append(new_x)
        y.append(new_y)


def check_queens_disposition():
    correct = True
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct is True:
        return True
    else:
        return False


if __name__ == '__main__':
    get_coordinates()
    print(check_queens_disposition())
