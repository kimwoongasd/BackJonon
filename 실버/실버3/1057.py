n, x, y = map(int, input().split())

count = 0
while x != y:
    x -= x // 2
    y -= y // 2
    count += 1
print(count)