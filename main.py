from itertools import combinations
from collections import Counter, deque

def bfs(MAP, VISIT, TIME, N, start_p):
  direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  visit_cnt = 1
  edible_time = -1
  baby = 2
  baby_cnt = 0
  time = 0

  fish_list = deque([])
  fish_list.append(start_p)
  VISIT[start_p[0]][start_p[1]] = visit_cnt
  same_list = deque([])

  while len(fish_list) > 0:
    now_p = fish_list.popleft()

    for d in direct:
      x = now_p[0] + d[0]
      y = now_p[1] + d[1]

      if 0 <= x < N and 0 <= y < N and VISIT[x][y] != visit_cnt:
        if MAP[x][y] == 0 or MAP[x][y] == baby:
          TIME[x][y] = TIME[now_p[0]][now_p[1]] + 1
          VISIT[x][y] = visit_cnt
          fish_list.append((x, y))

        elif MAP[x][y] < baby and (edible_time == -1 or edible_time == TIME[now_p[0]][now_p[1]] + 1) :
          if edible_time == -1:
            time = edible_time = TIME[now_p[0]][now_p[1]] + 1
          
          same_list.append((x, y))

        elif edible_time < TIME[now_p[0]][now_p[1]] + 1:
          continue
        
    
    if len(fish_list) == 0 and len(same_list) > 0:
      same_list = sorted(sorted(same_list, key = lambda x : x[1]), key = lambda x : x[0])
      final_p = same_list[0]
      baby_cnt += 1

      if baby == baby_cnt:
        baby += 1
        baby_cnt = 0

      edible_time = -1
      visit_cnt += 1
      MAP[final_p[0]][final_p[1]] = 9
      MAP[start_p[0]][start_p[1]] = 0
      start_p = final_p
      TIME[final_p[0]][final_p[1]] = time
      VISIT[final_p[0]][final_p[1]] = visit_cnt
      same_list = deque([])
      fish_list.append(start_p)
  
  return time

def main():
  N = int(input())

  answer = -1
  MAP = []
  VISIT = []
  TIME = []
  start_p = ()

  for i in range(N):
    temp_map = list(map(int, input().split(" "))) 
    temp_visit = [x // N for x in range(N)]
    temp_time = [x // N for x in range(N)]
    VISIT.append(temp_visit)
    TIME.append(temp_time)
    MAP.append(temp_map)
    for j in range(N):
      
      if temp_map[j] == 9:
        start_p = (i, j)
  
  answer = bfs(MAP, VISIT, TIME, N, start_p)

  print(answer)
  pass

if __name__=="__main__":
  main()