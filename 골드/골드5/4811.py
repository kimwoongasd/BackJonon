dp = [[0] * 31 for _ in range(31)]

# w만 먹었다고 가정
# w를 먹어야 h가 생기기 때문이다
for i in range(1, 31):
    dp[0][i] = 1


for i in range(1, 31):
    # h가 w보다 많은면 안된다
    for j in range(i, 31):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])
    
# h가 w보다 많은면 안된다라는 점을 생각 못하여 풀지 못하였다