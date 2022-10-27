from collections import deque

t = int(input()) # 테스트 수

for i in range(t):
    n, m = map(int, input().split()) # 문서 개수와 프린트 할 번째 수
    p = list(map(int, input().split())) # 중요도
    
    for i in range(n):
        p[i] = (p[i], i)
    d = deque(p)
    max_p = max(p)
    count = 0

    while d:
        point = d[0][1]
        if d[0][0] >= max_p[0]:
            d.popleft()
            count += 1
            
            if point == m:
                print(count)
                break       
        else:
            d.append(d.popleft())
        
        max_p = max(d)