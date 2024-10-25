NEXT_PLACE = {
    (2, 0): (0, 2),
    (0, 2): (-2, 0),
    (-2, 0): (0, -2),
    (0, -2): (2, 0)
}

PLACE_TO_MOVE = {
    (2, 0): (3, 0),
    (0, 2): (0, 3),
    (-2, 0): (-3, 0),
    (0, -2): (0, -3)
}


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


def can_place(res, n, m, x, y, dx, dy):
    if x + dx < 0 or x + dx >= len(res[0]) or y + dy < 0 or y + dy >= len(res):
        return False

    for j in range(y, min(y + dy + 2, m)):
        for i in range(x, (min(x + dx + 2, n))):
            if res[j][i]:
                return False

    return True


def place(res, n, m, x, y, dx, dy):
    # place 2's
    for i in range(x, x + dx + 1):
        for j in range(y, y + dy + 1):
            res[j][i] = 2
    # place 1's (padding)
    for i in range(max(0, x - 1), min(x + dx + 2, n)):
        for j in range(max(0, y - 1), min(y + dy + 2, m)):
            if res[j][i] == 0:
                res[j][i] = 1
    return res


def solve_current_move(res, k, n, m, x, y, cur_dir, placed):
    """Returns answer number and answer array"""
    if n == 0:
        return placed, res

    place(res, x, y, cur_dir[0], cur_dir[1])

    ptm = PLACE_TO_MOVE[cur_dir]

    if can_place(res, n, m, x + ptm[0], y + ptm[1], cur_dir[0], cur_dir[1]):
        # can place next the same
        return solve_current_move(res, k - 1, n, m, x + ptm[0], y + ptm[1], cur_dir, placed + 1)
    else:
        # need to change direction
        next_dir = NEXT_PLACE[cur_dir]
        return solve_current_move(res, k - 1, n, m, x, y, next_dir, placed)


for _ in range(int(input())):
    x, y, n = map(int, input().split())
    reversed_xy = False
    if y > x:
        x, y = y, x
        reversed_xy = True
    res = [[0 for _ in range(x)] for _ in range(y)]
    ans, res = solve_current_move(res, n, x, y, 0, 0, (2, 0), 0)
    if ans != n:
        ans, res = solve_current_move(res, n, x, y, 1, 0, (0, 2), ans)
    # if ans != n:
    #     ans, res = solve_current_move(res, n, x + 1, y, (2, 0), ans)
    print(ans)
    print_res(res, reversed_xy)
