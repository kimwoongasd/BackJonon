# DP문제
n = int(input())
num = []
for _ in range(n):
    a, b = map(int, input().split())
    num.append((a, b))
# 새로운 dp라는 행렬을 만들어준다.
# 여기서 행과 열은 오른쪽 위만 쓴다.
# 각 칸의 의미는 i행렬부터 j행렬까지 행렬 곱의 최소값이다.  
dp = [[0] * n for _ in range(n)]

for i in range(1, n): #몇 번째 대각선?
    for j in range(0, n-i): #대각선에서 몇 번째 열?
    
        if i == 1: #차이가 1밖에 나지 않는 칸
            dp[j][j + i] = num[j][0] * num[j][1] * num[j + i][1]
            continue
        
        dp[j][j + i] = 2 ** 32 #최댓값을 미리 넣어줌
        for k in range(j, j + i):
            # dp[첫행렬 위치][k] + dp[k+1][마지막 행렬 위치] + ( matrix[첫행렬 위치][0] * matrix[k][1] * matrix[마지막행렬 위치][1] )
            dp[j][j + i] = min(dp[j][j + i], 
                             dp[j][k] + dp[k+1][j + i] + num[j][0] * num[k][1] * num[j + i][1])
                
print(dp[0][n-1]) #맨 오른쪽 위

# 행렬의 곱을 이해를 잘 못했다.
# 2차원 리스트를 사용할 생각을 못했다