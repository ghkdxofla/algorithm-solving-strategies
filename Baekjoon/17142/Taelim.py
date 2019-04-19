from itertools import combinations
from collections import deque

def main():
    N, M = map(int, input().split(" "))
    MAP = []
    VISIT = []
    VIRUS = []
    DIRECT = ((1, 0), (0, 1), (-1, 0), (0, -1))
    WALL = 0
    time_ans = 2147483647
    time_val = 3
    visit_val = 1

    for i in range(N):
        MAP.append(list(map(int, input().split(" "))))
        VISIT.append([x // N for x in range(N)])
        for j in range(N):
            if MAP[i][j] == 2:
                VIRUS.append((i, j, 0))
            
            elif MAP[i][j] == 1:
                VISIT[i][j] = -1
                WALL += 1

    for sel_virus in combinations(VIRUS, M):
        time_max = 0
        total = 0
        for v in VIRUS:
            MAP[v[0]][v[1]] = 2

        sel_queue = deque(sel_virus)
        for v in sel_queue:
            MAP[v[0]][v[1]] = time_val
            VISIT[v[0]][v[1]] = visit_val
        while len(sel_queue) > 0:
            s = sel_queue.popleft()

            total += 1
            if time_max < MAP[s[0]][s[1]] - time_val:
                time_max = MAP[s[0]][s[1]] - time_val

            for d in DIRECT:
                x = s[0] + d[0]
                y = s[1] + d[1]

                if 0 <= x < N and 0 <= y < N:
                    if VISIT[x][y] != -1 and VISIT[x][y] != visit_val:
                        
                        if MAP[x][y] != 2:
                            

                            MAP[x][y] = MAP[s[0]][s[1]] + s[2] + 1
                            sel_queue.append((x, y, 0))
                        else:
                            is_act = False
                            for d2 in DIRECT:
                                x2 = x + d2[0]
                                y2 = y + d2[1]

                                if 0 <= x2 < N and 0 <= y2 < N:
                                    if VISIT[x2][y2] != -1 and VISIT[x2][y2] != visit_val:
                                        is_act = True
                                        break

                            MAP[x][y] = MAP[s[0]][s[1]]
                            sel_queue.append((x, y, s[2] + 1))

                        
                        VISIT[x][y] = visit_val
        

        time_val += time_max
        visit_val += 1

        if total != N * N - WALL:
            time_max = -1

        if time_ans > time_max and time_max != -1:
            time_ans = time_max

    if time_ans == 2147483647:
        time_ans = -1
    
    return time_ans

if __name__=="__main__":
    answer = main()
    print(answer)