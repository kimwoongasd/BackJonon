a, b, v = map(int, input().split())
count = 0

if (v - b) % (a - b) == 0:
    count = (v - b) // (a - b)
else:
    count = (v - b) // (a - b) + 1

print(count)