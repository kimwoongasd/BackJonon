# 플로이드–워셜
n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            # i가 k보다 크고 k는 j보다 크다는 뜻 그렇다면 i는 j 보다 크다는 것
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

count = 0
for i in range(n):
    # 자신보다 작은사람과 큰사람의 합
    total = 0
    for j in range(n):
        total += arr[i][j] + arr[j][i]
        
    if total == n - 1:
        count +=1
        
print(count)