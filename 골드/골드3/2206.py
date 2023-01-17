from collections import deque

def bfs(a, b, c):
    dq = deque()
    dq.append((a, b, c))
    while dq:
        x, y, z = dq.popleft()
        if x == n - 1 and y == m - 1:
            return ch[x][y][z]
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if arr[xx][yy] == 1 and z == 0:
                ch[xx][yy][1] = ch[x][y][0] + 1
                dq.append((xx, yy, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif arr[xx][yy] == 0 and ch[xx][yy][z] == 0:
                ch[xx][yy][z] = ch[x][y][z] + 1
                dq.append((xx, yy, z))
    return -1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input()))
    arr.append(a)

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
ch = [[[0] * 2 for _ in range(m)] for _ in range(n)]
ch[0][0][0] = 1
print(bfs(0, 0, 0))


# 힌트를 보고 풀었지만 중간에 오답
# def bfs(a, b, c):
#     dq = deque()
#     dq.append((a, b, c))
#     while dq:
#         x, y, z = dq.popleft()
#         if x == n - 1 and y == m - 1:
#             return arr[x][y]
        
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 1 and z == 0:
#                 arr[xx][yy] = arr[x][y] + 1
#                 dq.append((xx, yy, 1))
            
#             elif 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
#                 arr[xx][yy] = arr[x][y] + 1
#                 dq.append((xx, yy, z))
#     return -1

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().strip()))
#     arr.append(a)
# arr[0][0] = 1

# print(bfs(0, 0, 0))