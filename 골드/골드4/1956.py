import sys
import heapq
input = sys.stdin.readline

# 플로이드 와샬 알고리즘 - 시간초과, pyp3 풀림
# v, e = map(int, input().split())
# arr = [[int(1e9)] * (v + 1) for _ in range(v + 1)]

# for _ in range(e):
#     a, b, c = map(int, input().split())
#     arr[a][b] = c
    
# # 1. 모든 정점에서 모든 정점으로 가는 최소 거리 구하기
# for i in range(1, v + 1):
#     for j in range(1, v + 1): # 출발 노드
#         for k in range(1, v + 1): # 도착 노드
#             arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
            
# res = int(1e9)

# for i in range(1, v + 1):
#     res = min(res, arr[i][i])
    
# if res == int(1e9):
#     print(-1)
# else:
#     print(res)

# 다익스트라 (변형)
v, e = map(int, input().split())
arr = [[] for _ in range(v + 1)]
#거리를 저장할 배열을 2차원으로
ch = [[int(1e9)] * (v + 1) for _ in range(v + 1)]

hq = []

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([c, b])
    ch[a][b]= c
    # heap에도 비용, 출발지, 도착지 3개의 값을 넣어준다.
    # 유효한 경로 값을 다 넣어줌
    heapq.heappush(hq, [c, a, b])
    
while hq:
    # 최소 비용의 경로를 먼저 뽑아주고 (d:비용, s:출발, g:도착)
    d, s, g = heapq.heappop(hq)
    
    # 출발지와 도착지가 같다면 사이클!
    # heap을 이용하기 때문에 처음 나온 사이클이 가장 비용이 작은 사이클이므로 break 해버려도 됨! -> 여기서 시간이 굉장히 절약되는 듯 
    if s == g:
        print(d)
        break
    
    # d 값이 이미 저장된 비용보다 크다면 넘겨버림
    if ch[s][g] < d:
        continue
    
    # g에서 갈 수 있는 노드들을 검사
    for nd, ng in arr[g]:
        # s->g->ng로 가는 비용
        new_d = d + nd
        # s->g->ng로 가는게 s->ng보다 빠르다면 값 갱신해주고 heap에 넣어줌
        if new_d < ch[s][ng]:
            ch[s][ng] = new_d
            heapq.heappush(hq, [new_d, s, ng])
            
else:
    # heap 다 돌았는데 없다면 -1
    print(-1)