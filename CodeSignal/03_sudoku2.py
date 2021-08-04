# lc 036-1
def sudoku2(grid):
    ans = []
    for i, row in enumerate(board):  # i是纵坐标，row是横向的数组
        for j, val in enumerate(row):  # j是横坐标，c是数值
            if val != '.':
                # (i, val), (val, j)这种写法主要是为了把横纵坐标做区分
                # (i // 3, j // 3, val)是类似于(x, y)这种坐标形式标注格子
                ans += [(i, val), (val, j), (i // 3, j // 3, val)]
    return len(set(ans)) == len(ans)
