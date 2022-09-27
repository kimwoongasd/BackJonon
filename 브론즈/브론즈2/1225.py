a, b = map(str, input().split())

aa = 0
bb = 0

for x in a:
    aa += int(x)
for y in b:
    bb += int(y)

print(aa * bb)