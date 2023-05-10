import sys
import heapq
input = sys.stdin.readline

# 플로이드 와샬 알고리즘 - 시간초과, pyp3 풀림
v, e = map(int, input().split())
arr = [[int(1e9)] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    
# 1. 모든 정점에서 모든 정점으로 가는 최소 거리 구하기
for i in range(1, v + 1):
    for j in range(1, v + 1): # 출발 노드
        for k in range(1, v + 1): # 도착 노드
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
            
res = int(1e9)

for i in range(1, v + 1):
    res = min(res, arr[i][i])
    
if res == int(1e9):
    print(-1)
else:
    print(res)

