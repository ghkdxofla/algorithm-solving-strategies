def solve():
    N = int(input())
    MAP = []
    for _ in range(100):
        MAP.append([0 for _ in range(100)])

    for _ in range(N):
        X, Y, D, G = map(int, input().split(" "))
        finder(MAP, [D, ], X, Y, G)

    return checker(MAP)

    

def finder(MAP, curve, X, Y, G):
    if G < 0:
        return
    DIRECT = ((1, 0), (0, -1), (-1, 0), (0, 1))
    if len(curve) == 1:
        curve.append((curve[0] + 1) % 4)
        MAP[Y][X] = 1
        nx = X + DIRECT[curve[0]][0]
        ny = Y + DIRECT[curve[0]][1]
        MAP[ny][nx] = 1
        finder(MAP, curve, nx, ny, G - 1)

    elif len(curve) > 1:
        LENGTH = len(curve)
        nx = X
        ny = Y
        for i in range(LENGTH // 2, LENGTH):
            nx += DIRECT[curve[i]][0]
            ny += DIRECT[curve[i]][1]
            MAP[ny][nx] = 1
        temp_left = [(curve[x] + 2) % 4 for x in range(LENGTH // 2)]
        temp_right = [curve[x] for x in range(LENGTH // 2, LENGTH)]
        curve.extend(temp_left)
        curve.extend(temp_right)
        
        finder(MAP, curve, nx, ny, G - 1)

def checker(MAP):
    cnt = 0
    for i in range(99):
        for j in range(99):
            if MAP[i][j] == 1 and MAP[i][j + 1] == 1 and MAP[i + 1][j] == 1 and MAP[i + 1][j + 1] == 1:
                cnt += 1
    return cnt



if __name__=="__main__":
    print(solve())