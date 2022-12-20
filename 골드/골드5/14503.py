 # 북, 동, 하, 서 ( 시계방향 )
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
r, c, d = map(int, input().split())
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
ch = [[0] * m for _ in range(n)]
ch[r][c] = 1
cnt = 1

while True:
    # 청소 안했을 때
    flag = 0
    for _ in range(4):
        # 왼쪽 방향으로 회전
        # 방향이 0, 1, 2, 3 이렇게 총 4개다.
        # 그리고 왼쪽으로 돌리면 3, 2, 1, 0 이다.
        d = (d+3) % 4
        x = r + dx[d]
        y = c + dy[d]

        if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
            if ch[x][y] == 0:
                ch[x][y] = 1
                cnt += 1
                r = x
                c = y
                flag = 1
                break
    
    if flag == 0:
        # 내가 가지고 있는 방향을 빼주면 그것이 후진을 한 값
        # 네 방향 모두 청소를 할 수 없을 때
        if arr[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        # 만약 뒤가 벽이 아니라면 그 위치를 다시 갱신
        else:
            r, c = r - dx[d], c - dy[d]