# LCS 문제
a = input()
b = input()
c = input()

# 보기가 3개라 3차원 리스트로 만들었다.
dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(c) + 1):
            if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

res = -1
for x in dp:
    for y in x:
        res = max(res, max(y))
print(res)