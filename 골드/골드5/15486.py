n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])
    
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # 이전까지의 최댓값
    dp[i] = max(dp[i], dp[i - 1])
    d = arr[i - 1][0] + i - 1 # 당일 포함
    if d <= n: # 최종일 안에 일이 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        dp[d] = max(dp[d], dp[i - 1] + arr[i - 1][1])

print(max(dp))