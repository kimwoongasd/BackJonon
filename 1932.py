n = int(input())

ls = []

for _ in range(n):
    ls.append(list(map(int, input().split())))
    
    
for i in range(1, n):
    for j in range(len(ls[i])):
        if j == 0:
            ls[i][j] = ls[i - 1][j] + ls[i][j]
        elif i == j:
            ls[i][j] = ls[i - 1][j - 1] + ls[i][j]
        else:
            ls[i][j] = ls[i][j] + max(ls[i - 1][j], ls[i - 1][j - 1])
            
print(max(ls[n - 1]))