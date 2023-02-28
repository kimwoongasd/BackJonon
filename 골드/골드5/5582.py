import sys 
input = sys.stdin.readline
a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

res = 0
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            res = max(res, dp[i][j])
            
print(res)

'''
시간초과로 pyp3로 풀어야 한다
'''