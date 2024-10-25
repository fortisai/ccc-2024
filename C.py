for _ in range(int(input())):
    x, y, n = map(int, input().split())
    if x % 3 == 0:
        # normally
        for i in range(y):
            for j in range(x // 3):
                if n > 0:
                    for k in range(3):
                        print(n, end=' ')
                    n -= 1
                else:
                    break
            print()
    else:
        res = [[0 for _ in range(x)] for _ in range(y)]
        for i in range(y):
            for j in range(x // 3):
                if n > 0:
                    for k in range(3):
                        res[i][j * 3 + k] = n
                    n -= 1
                else:
                    break
        if n == 0:
            for i in range(y):
                for j in range(x):
                    print(res[i][j], end=' ')
                print()
        else:
            if x % 3 == 1:
                for i in range(y // 3):
                    if n > 0:
                        for k in range(3):
                            res[i * 3 + k][x - 1] = n
                        n -= 1
                    else:
                        break
            else:  # x % 3 == 2
                for i in range(y // 3):
                    if n > 0 and i * 3 + 2 < y:
                        for k in range(3):
                            res[i * 3 + k][x - 2] = n
                        n -= 1
                    else:
                        break
                if n > 0:
                    for i in range(y // 3):
                        if n > 0 and i * 3 + 2 < y:
                            for k in range(3):
                                res[i * 3 + k][x - 1] = n
                            n -= 1
                        else:
                            break
            for i in range(y):
                for j in range(x):
                    print(res[i][j], end=' ')
                print()
