def print_res(res, reversed_xy):
    if reversed_xy:
        for i in range(x):
            for j in range(y):
                if res[j][i]:
                    print('x', end='')
                else:
                    print('.', end='')
            print()
    else:
        for i in range(y):
            for j in range(x):
                if res[i][j]:
                    print('x', end='')
                else:
                    print('.', end='')
            print()


for _ in range(int(input())):
    x, y, n = map(int, input().split())
    reversed_xy = False
    if y > x:
        x, y = y, x
        reversed_xy = True
    res = [[False for _ in range(x)] for _ in range(y)]
    no_more = False
    for i in range(0, y, 2):
        for j in range(0, x, 4):
            if j + 2 > x - 1:
                break
            if n > 0:
                for k in range(3):
                    res[i][j + k] = True
                n -= 1
            else:
                break
    if n == 0:
        print_res(res, reversed_xy)
    else:
        for i in range(0, y, 4):
            if n > 0 and i + 2 < y:
                for k in range(3):
                    res[i + k][x - 1] = True
                n -= 1
            else:
                break
        print_res(res, reversed_xy)
