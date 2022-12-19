from collections import deque

n, k = map(int, input().split())
ch = [0] * 100001

dq = deque()
dq.append(n)

while dq:
    s = dq.popleft()
    if s == k:
        print(ch[s])
        break
    
    for i in (s * 2, s - 1, s + 1):  
        if 0 <= i <= 100000 and ch[i] == 0:
            if i == s * 2:
                ch[i] = ch[s]
                dq.append(i)
            else:
                ch[i] = ch[s] + 1
                dq.append(i)
