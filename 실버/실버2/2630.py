def dfs(x, y, z):
    global zero, one
    v = arr[x][y]
    for i in range(x, x + z):
        for j in range(y, y + z):
            if v != arr[i][j]:
                for k in range(2):
                    for l in range(2):
                        dfs(x + k * z // 2, y + l * z // 2, z // 2)
                return
    
    if v == 0:
        zero += 1
    else:
        one += 1

n = int(input())
arr = []

for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)
    
zero = 0
one = 0
dfs(0, 0, n)
print(f"{zero}\n{one}")