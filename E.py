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

PLACE_TO_PADDING = {
    (2, 0): ((-1, 3), (-1, 2)),
    (0, 2): ((-1, 2), (-1, 3)),
    (-2, 0): ((-2, 2), (-1, 2)),
    (0, -2): ((-1, 2), (-2, 2)),
}

DIR_TO_POI = {
    (2, 0): ((2, 0), (3, 0)),
    (0, 2): ((0, 2), (0, 3)),
    (-2, 0): ((-2, 0), (-3, 0)),
    (0, -2): ((0, -2), (0, -3))
}

DIR_TO_NEXT_POINT = {
    (2, 0): {
        0: (1, 2),
        1: (2, 2),
        2: (3, 0),
    },
    (0, 2): {
        0: (-2, 1),
        1: (-2, 2),
        2: (0, 3),
    },
    (-2, 0): {
        0: (-1, -2),
        1: (-2, -2),
        2: (-3, 0),
    },
    (0, -2): {
        0: (2, -1),
        1: (2, -2),
        2: (0, -3),
    }
}


def print_res(res, reversed_xy):
    if reversed_xy:
        for i in range(x):
            for j in range(y):
                if res[j][i] == 2:
                    print('x', end='')
                elif res[j][i] == 1:
                    print('o', end='')
                else:
                    print('.', end='')
            print()
    else:
        for i in range(y):
            for j in range(x):
                if res[i][j] == 2:
                    print('x', end='')
                elif res[i][j] == 1:
                    print('o', end='')
                else:
                    print('.', end='')
            print()


def can_place(res, n, m, x, y, dx, dy):
    if x + dx < 0 or x + dx >= len(res[0]) or y + dy < 0 or y + dy >= len(res):
        return False

    for i in range(max(0, x - 1), min(x + dx + 2, n)):
        for j in range(max(0, y - 1), min(y + dy + 2, m)):
            if res[j][i] == 2:
                return False

    return True


def place(res, n, m, x, y, dx, dy):
    # place 2's
    ddx = x + dx if dx else x + 1
    ddy = y + dy if dy else y + 1
    for i in range(x, ddx):
        for j in range(y, ddy):
            res[j][i] = 2
    # place 1's (padding)
    ((px1, px2), (py1, py2)) = PLACE_TO_PADDING[(dx, dy)]
    for i in range(max(0, x + px1), min(x + px2, n)):
        for j in range(max(0, y + py1), min(y + py2, m)):
            if res[j][i] == 0:
                res[j][i] = 1
    return res


def check_valid(res, n, m, x, y, dx, dy):
    if x + dx < 0 or x + dx >= len(res[0]) or y + dy < 0 or y + dy >= len(res):
        return False

    return res[y + dy][x + dx] != 2


def solve_current_move(res, k, n, m, x, y, cur_dir, placed):
    """Returns answer number and answer array"""
    if n == 0:
        return placed, res
    
    print(x, y)

    place(res, n, m, x, y, cur_dir[0], cur_dir[1])

    ptm = PLACE_TO_MOVE[cur_dir]

    print_res(res, False)

    if can_place(res, n, m, x + ptm[0], y + ptm[1], cur_dir[0], cur_dir[1]):
        # can place next the same
        return solve_current_move(res, k - 1, n, m, x + ptm[0], y + ptm[1], cur_dir, placed + 1)
    else:
        # need to change direction
        poi1, poi2 = DIR_TO_POI[cur_dir]
        poi1_valid = check_valid(res, n, m, x, y, poi1[0], poi1[1])
        poi2_valid = check_valid(res, n, m, x, y, poi2[0], poi2[1])
        valid_points_count = poi1_valid + poi2_valid
        print(valid_points_count)
        next_point = DIR_TO_NEXT_POINT[cur_dir][valid_points_count]
        next_dir = NEXT_PLACE[cur_dir]
        return solve_current_move(res, k - 1, n, m, x + next_point[0], y + next_point[1], next_dir, placed + 1)


for _ in range(int(input())):
    x, y, n = map(int, input().split())
    reversed_xy = False
    if y > x:
        x, y = y, x
        reversed_xy = True
    res = [[0 for _ in range(x)] for _ in range(y)]
    ans, res = solve_current_move(res, n, x, y, 0, 0, (2, 0), 0)
    # if ans != n:
    #     ans, res = solve_current_move(res, n, x, y, 1, 0, (0, 2), ans)
    # if ans != n:
    #     ans, res = solve_current_move(res, n, x + 1, y, (2, 0), ans)
    print(ans)
    print_res(res, reversed_xy)
