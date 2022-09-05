from collections import deque

r, c = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    pass

ice = []
swan = [[0 for _ in range(c)] for _ in range(r)]
ch = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    
    tem = list(input().rstrip())
    ice.append(tem)
    
    for j in range(c):
        if tem[j] == "X":
            swan[i][j] = 1
        elif tem[j] == "L":
            swan[i][j] = 2

for i in range(r):
    for j in range(c):
        pass

for x in swan:
    print(x)