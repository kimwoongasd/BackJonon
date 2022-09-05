r, c = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs():
    pass

ch = []
swan = [[0 for i in range(c)] for j in range(r)]
ice = [[0 for i in range(c)] for j in range(r)]

for i in range(r):
    
    tem = list(input().rstrip())
    ch.append(tem)
    
    for j in range(c):
        if tem[j] == "X":
            swan[i][j] = 1
        elif tem[j] == "L":
            swan[i][j] = 2
    
for x in swan:
    print(x)