n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

tem_1 = [0] * 10000001
tem_2 = [0] * 10000001

for x in a:
    if x >= 0:
        tem_1[x] = 1
    else:
        x = abs(x)
        tem_2[x] = 1

for y in b:
    y = abs(y)
    if tem_1[y] == 1 or tem_2[y] == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")