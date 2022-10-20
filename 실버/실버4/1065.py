n = int(input())

count = 0
for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        tem = str(i)
        if (int(tem[0]) - int(tem[1])) == (int(tem[1]) - int(tem[2])):
            count += 1
print(count)