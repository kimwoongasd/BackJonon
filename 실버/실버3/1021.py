from collections import deque

n, m = map(int, input().split())
tem = list(map(int, input().split()))

d = deque([i for i in range(1, n + 1)])
count = 0
for j in range(m):
    while True:
        if tem[j] == d[0]:
            d.popleft()
            break
        else:
            if d.index(tem[j]) > len(d) // 2:
                while tem[j] != d[0]:
                    d.appendleft(d.pop())
                    count += 1
            else:
                while tem[j] != d[0]:
                    d.append(d.popleft())
                    count += 1
print(count)