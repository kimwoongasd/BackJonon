from collections import deque

n, k = map(int, input().split())

ch = [0] * 100001
dq = deque()
dq.append(n)

while dq:
    x = dq.popleft()
    if x == k:
        print(ch[k])
        break
    
    for i in (x - 1, x + 1, x * 2):
        if 0<= i < 100001 and ch[i] == 0:
            ch[i] = ch[x] + 1
            dq.append(i)
            