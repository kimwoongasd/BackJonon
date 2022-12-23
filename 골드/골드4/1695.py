# pyp3로 풀림
n = int(input())
tem = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 1. 주어진 수열에서 팰린드롬 수열을 구한다.
# 2. 팰린드롬의 정 가운데를 기준으로 수열을 나눈다.
# 3. 팰린드롬이 아닌 수를 반대편에 추가한다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if tem[-i] == tem[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(n - dp[-1][-1])