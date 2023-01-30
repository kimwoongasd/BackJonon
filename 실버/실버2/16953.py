n, m = map(int, input().split())
cnt = 1
while n != m:
    tem = m
    
    if m % 10 == 1:
        m //= 10
    elif m % 2 == 0:
        m //= 2
        
    cnt += 1
    if tem == m:
        print(-1)
        break
    
else:
    print(cnt)