def dfs(x, y, z):
    global zero, p_one, m_one
    # 시작점 종이의 수
    v = arr[x][y]
    # 반복문을 통해 종이 확인
    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작점 종이와 같은 수인지 확인
            if v != arr[i][j]:
                # 3*3 범위를 재귀적으로 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return
            
    if v == -1:
        m_one += 1
    elif v == 0:
        zero += 1
    else:
        p_one += 1

n = int(input())
arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

zero = 0
p_one = 0
m_one = 0
dfs(0, 0, n)
print(f"{m_one}\n{zero}\n{p_one}")