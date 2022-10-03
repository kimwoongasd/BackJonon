n = int(input())
tmp = n
count = 0
while True:

    a = tmp // 10
    b = tmp % 10
    c = (a + b) % 10
    tmp = b * 10 + c

    count += 1

    if tmp == n:
        break
print(count)