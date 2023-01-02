# x 세로줄의 n이 있는지 확인
def row(x, target):
    for i in range(9):
        if target == arr[x][i]:
            return False
    return True

# y 가로줄의 n이 있는지 확인
def col(y, target):
    for i in range(9):
        if target == arr[i][y]:
            return False
    return True

# x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
def box(x, y, target):
    xx = x // 3 * 3
    yy = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if target == arr[xx + i][yy +j]:
                return False
    return True

# dfs + 백트래킹
def dfs(idx):
    # 스도쿠의 빈 칸을 채웠다면
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)
        
    # 반복문을 통해 빈칸에 1부터 9까지 넣어본다.
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if row(x, i) and col(y, i) and box(x, y, i):
            arr[x][y] = i
            dfs(idx + 1)
            arr[x][y] = 0

arr = []
blank = []
for i in range(9):
    a = list(map(int, input().split()))
    arr.append(a)
    for j in range(9):
        if a[j] == 0:
            blank.append((i, j))

dfs(0)