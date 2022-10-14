n = int(input())
tem = list(map(int, input().split()))

num = [0 for _ in range(max(tem) + 1)]
num[1] = 1
count = 0
for i in range(2, max(tem) + 1):
    if num[i] == 0:
        for  j in range(i * 2, max(tem) + 1, i):
            num[j] = 1
        if i in tem:
            count += 1
print(count)