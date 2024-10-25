def print_res(res, reversed_xy):
    if reversed_xy:
        for i in range(x):
            for j in range(y):
                if res[j][i]:
                    print('X', end='')
                else:
                    print('.', end='')
            print()
    else:
        for i in range(y):
            for j in range(x):
                if res[i][j]:
                    print('X', end='')
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
    
    # Place desks horizontally first
    for i in range(0, y, 2):
        for j in range(0, x, 3):  # Changed from 4 to 3 since desks are now 1x2
            if j + 1 > x - 1:  # Changed from j+2 to j+1 for 1x2 desks
                break
            if n > 0:
                for k in range(2):  # Changed from 3 to 2 for desk size
                    res[i][j + k] = True
                n -= 1
            else:
                break
                
    # If there are remaining desks, place them vertically
    if n > 0:
        for i in range(0, y, 3):  # Changed spacing for vertical placement
            if n > 0 and i + 1 < y:  # Changed from i+2 to i+1 for 1x2 desks
                for k in range(2):  # Changed from 3 to 2 for desk size
                    res[i + k][x - 1] = True
                n -= 1
            else:
                break
                
    print_res(res, reversed_xy)