# 분할정복 문제
def dfs(x, y, z):
    p = arr[x][y]
    for i in range(x, x + z):
        for j in range(y, y + z):
            if p != arr[i][j]:
                p = -1
                break
    
    # 조건이 맞지 않는 경우 4개로 쪼개서 푼다
    # 시작하기전 ( 넣고 끝날때 ) 넣는다
    if p == -1:
        print("(", end="")
        n = z // 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        print(")", end="")   
         
    elif p == 1:
        print(1, end="")
        
    else:
        print(0, end="")

n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input()))
    arr.append(a)
    
dfs(0, 0, n)