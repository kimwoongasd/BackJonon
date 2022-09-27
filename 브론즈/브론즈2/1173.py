N, m, M, T, R = map(int, input().split())

count = 0
time = 0
now = m
tem = True
while count < N:
    if m + T > M:
        tem = False
        break
    
    if now + T <= M:
        now += T
        count += 1
        
    else:
        now = max(now - R, m)
        
    time += 1
    
if tem:
    print(time)
else:
    print(-1)