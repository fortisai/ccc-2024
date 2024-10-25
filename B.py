for _ in range(int(input())):
    x, y, n = map(int, input().split())
    for i in range(y):
        for j in range(x // 3):
            if n > 0:
                for l in range(3):
                    print(n, end=' ')
                n -= 1
            else:
                break
        print()
