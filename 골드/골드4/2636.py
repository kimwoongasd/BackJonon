import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    global time, tem
    ch = [[0] * m for _ in range(n)]
    dq = deque()
    dq.append((a, b))
    ch[a][b] = 1
    cnt = 0
    time += 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
                # 공기와 접촉한 칸은 추가
                if  arr[xx][yy] == 0:
                    dq.append((xx, yy))
                    ch[xx][yy] = 1
                    
                # 공기와 접촉한 칸은 넣지 않는다
                # 치즈 안 구멍에 있는 숫자를 포함하지 않아야 하기 때문에
                elif arr[xx][yy] == 1:
                    arr[xx][yy] = 0
                    ch[xx][yy] = 1
                    cnt += 1
    tem.append(cnt)
    return cnt
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
tem = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

time = 0
while True:   
    cnt = bfs(0, 0)
    if cnt == 0:
        break

# 치즈가 없더라도 최소 한번은 확인하기 때문에 -1
print(time - 1)
print(tem[-2])