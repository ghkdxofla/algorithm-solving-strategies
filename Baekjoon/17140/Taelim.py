from collections import Counter

def main():
    R, C, K = map(int, input().split(" "))
    max_x = max_y = 3
    time = 0
    MAP = []

    for i in range(100):
        MAP.append([x // 100 for x in range(100)])

    for i in range(3):
        temp_list = list(map(int, input().split(" ")))
        for j in range(3):
            MAP[i][j] = temp_list[j]

    while True:

        if R <= max_x and C <= max_y:
            if MAP[R - 1][C - 1] == K:
                return time
        
        if time > 100:
            return -1

        if max_x >= max_y:
            for i in range(max_x):
                temp_list = [MAP[i][j] for j in range(max_y) if MAP[i][j] > 0]
                
                cnt = Counter(temp_list)

                cnt = sorted(cnt.items(), key=lambda x : x[1])

                for j in range(len(cnt) - 1):
                    for k in range(j + 1, len(cnt)):
                        if cnt[j][1] == cnt[k][1] and cnt[j][0] > cnt[k][0]:
                            cnt[j], cnt[k] = cnt[k], cnt[j]

                if max_y < len(cnt) * 2:
                    max_y = len(cnt) * 2

                idx = 0
                for j in range(len(cnt)):
                    MAP[i][idx] = cnt[j][0]
                    idx += 1
                    MAP[i][idx] = cnt[j][1]
                    idx += 1

                for j in range(idx, max_y):
                    MAP[i][j] = 0
            
        else:
            for i in range(max_y):
                temp_list = [MAP[j][i] for j in range(max_x) if MAP[j][i] > 0]
                
                cnt = Counter(temp_list)

                cnt = sorted(cnt.items(), key=lambda x : x[1])

                for j in range(len(cnt) - 1):
                    for k in range(j + 1, len(cnt)):
                        if cnt[j][1] == cnt[k][1] and cnt[j][0] > cnt[k][0]:
                            cnt[j], cnt[k] = cnt[k], cnt[j]
                
                if max_x < len(cnt) * 2:
                    max_x = len(cnt) * 2

                idx = 0
                for j in range(len(cnt)):
                    MAP[idx][i] = cnt[j][0]
                    idx += 1
                    MAP[idx][i] = cnt[j][1]
                    idx += 1

                for j in range(idx, max_y):
                    MAP[j][i] = 0
        
        

        time += 1




if __name__=="__main__":
    answer = main()
    print(answer)