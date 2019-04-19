from collections import deque

def main():
    N, M, K = map(int, input().split(" "))
    MAP = []
    FERT = []
    direct = [(1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    TREE = deque([])
    for i in range(N):
        FERT.append(list(map(int, input().split(" "))))
        MAP.append([5 for _ in range(N)])
    
    for i in range(M):
        temp_list = list(map(int, input().split(" ")))
        TREE.append([temp_list[0] - 1, temp_list[1] - 1, temp_list[2]])

    for _ in range(K):
        dead_tree = 0
        DEAD = deque([])
        # Spring
        length = len(TREE)
        for __ in range(length):
            TREE = deque(sorted(TREE, key=lambda x : x[2]))
            
            tree = TREE.popleft()

            if tree[2] <= MAP[tree[0]][tree[1]]:
                MAP[tree[0]][tree[1]] -= tree[2]
                tree[2] += 1
                TREE.append(tree)
            else:
                DEAD.append(tree)

        # Summer
        length = len(DEAD)
        for __ in range(length):
            tree = DEAD.popleft()
            MAP[tree[0]][tree[1]] += tree[2] // 2

        # Fall
        length = len(TREE)
        for __ in range(length):
            tree = TREE.popleft()
            if tree[2] % 5 == 0:
                for d in direct:
                    x = tree[0] + d[0]
                    y = tree[1] + d[1]

                    if 0 <= x < N and 0 <= y < N:
                        TREE.append([x, y, 1])
            TREE.append(tree)
        # Winter

        for i in range(N):
            for j in range(N):
                MAP[i][j] += FERT[i][j]

    print(len(TREE))
    return

if __name__=="__main__":
    main()