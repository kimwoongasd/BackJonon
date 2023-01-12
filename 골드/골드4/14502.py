import copy, sys
from collections import deque
input = sys.stdin.readline
def bfs():
    global res
    # 기존 맵 정보 깊은 복사(Deep Copy)
    tem = copy.deepcopy(arr)
    dq = deque()
    for i in range(n):
        for j in range(m):
            if tem[i][j] == 2:
                dq.append((i, j))
    
    # 바이러스마다 전파 끝날 때까지 반복
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and tem[xx][yy] == 0:
                tem[xx][yy] = 2
                dq.append((xx, yy))
    
    # 안전지대 개수 카운팅      
    count = 0
    for i in range(n):
        count += tem[i].count(0)
    
    res = max(res, count)

def dfs(t):
    # 벽 3개 설치 완료 시, 바이러스 전파
    if t == 3:
        bfs()
        return
    
    # 벽을 설치할 수 있는 모든 경우의 수 확인
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(t + 1)
                arr[i][j] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

res = 0
dfs(0)
print(res)