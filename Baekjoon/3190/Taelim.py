from collections import deque

def main():
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dir_val = 0
    N = int(input())
    K = int(input())
    MAP = []
    for _ in range(N):
        MAP.append([0 for __ in range(N)])
    MAP[0][0] = 1
    SNAKE = deque([(0, 0)])
    S = [0, 0]

    for _ in range(K):
        x, y = map(int, input().split(" "))
        MAP[x - 1][y - 1] = 2

    L = int(input())

    time = 0
    turn_list = []
    for _ in range(L):
        P, T = input().split(" ")
        P = int(P)
        turn_list.append((P, T))
    turn_list.append((10000, "END"))

    for elm in turn_list:
        P = elm[0] - time
        T = elm[1]
        is_over = False
        temp_time = 0
        nx = S[0] + D[dir_val][0] * P
        ny = S[1] + D[dir_val][1] * P
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            if nx < 0:
                nx = 0
            elif nx >= N:
                nx = N - 1
            elif ny < 0:
                ny = 0
            elif ny >= N:
                ny = N - 1
            is_over = True

        if nx == S[0]:
            if ny > S[1]:
                loop_list = range(S[1] + 1, ny + 1)
                
            else:
                loop_list = range(S[1] - 1, ny - 1, -1)
            for i in loop_list:
                if MAP[nx][i] == 2:
                    pass
                elif MAP[nx][i] == 1:
                    return time + i - S[1] + 1
                elif MAP[nx][i] == 0:
                    pnt = SNAKE.popleft()
                    MAP[pnt[0]][pnt[1]] = 0
                temp_time += 1
                MAP[nx][i] = 1
                SNAKE.append((nx, i))

        elif ny == S[1]:
            if nx > S[0]:
                loop_list = range(S[0] + 1, nx + 1)
                
            else:
                loop_list = range(S[0] - 1, nx - 1, -1)
            for i in loop_list:
                if MAP[i][ny] == 2:
                    pass
                elif MAP[i][ny] == 1:
                    return time + i - S[0] + 1
                elif MAP[i][ny] == 0:
                    pnt = SNAKE.popleft()
                    MAP[pnt[0]][pnt[1]] = 0
                temp_time += 1
                MAP[i][ny] = 1
                SNAKE.append((i, ny))
    
        S = [nx, ny]
        if T == "D":
            dir_val = (dir_val + 1) % 4
        elif T == "L":
            dir_val = (dir_val - 1) % 4

        time += temp_time

        if is_over is True:
            return time + 1


    return time + 1
if __name__=="__main__":
    print(main())