from collections import deque
n, k = map(int, input().split())

tem = [x for x in range(1, n + 1)]
d = deque(tem)

print("<", end="")
while d:
    for i in range(k - 1):
        d.append(d.popleft())
    print(d.popleft(), end="")
    
    if d:
        print(",", end=" ")
print(">")