def dfs(pos):
    global cnt
    x, y, z = pos

    # n,n 도달
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 가로 세로 대각선의 경우 대각선 이동
    if x + 1 < n and y + 1 < n:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, 2))

    # 가로 대각선의 경우 가로 이동
    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))

    # 세로 대각선의 경우 세로 이동
    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

# x,y,현재방향
dfs((0, 1, 0))

print(cnt)

# dp해결
# n = int(input())
# graph = [[] for _ in range(n)]

# # 0은 가로, 1은 세로, 2는 대각선
# dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# # 그래프 정보 입력
# for i in range(n):
#     graph[i] = list(map(int, input().split()))

# dp[0][0][1] = 1  # 첫 시작 위치

# # dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
# for i in range(2, n):
#     if graph[0][i] == 0:
#         dp[0][0][i] = dp[0][0][i - 1]

# for r in range(1, n):
#     for c in range(1, n):
#         # 현재위치가 대각선인 경우
#         if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
#             dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

#         if graph[r][c] == 0:
#             # 현재 위치가 가로인 경우
#             dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
#             # 현재 위치가 세로인 경우
#             dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

# print(sum(dp[i][n - 1][n - 1] for i in range(3)))