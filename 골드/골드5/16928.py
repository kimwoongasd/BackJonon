from collections import deque

n, m = map(int, input().split())
arr = [0] * 101
ch = [0] * 101

# 사다리와 뱀
ladder = dict()
snake = dict()

for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
    
for i in range(m):
    a, b = map(int, input().split())
    ladder[a] = b
    
dq = deque([1])

while dq:
    x = dq.popleft()
    
    # 끝까지 도착했다면 종료
    if x == 100:
        print(arr[x])
        break
    
    for i in range(1, 7):
        dx = x + i
        
        # 100칸 이내이면서 방문하지 않는 칸일 떄
        if dx <= 100 and ch[dx] == 0:
            # 이동할 위치에 사다리가 있을 떄
            if dx in ladder.keys():
                dx = ladder[dx]
            # 이동할 위치에 뱀이 있을 때    
            if dx in snake.keys():
                dx = snake[dx]
                
            if ch[dx] == 0:
                ch[dx] = 1
                arr[dx] = arr[x] + 1
                dq.append(dx)