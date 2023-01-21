import sys
input = sys.stdin.readline
a = str(0) + input().strip()
b = str(0) + input().strip()
dp = [[""] * (len(b)) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[len(a) - 1][len(b) - 1]))
print(dp[len(a) - 1][len(b) - 1])
