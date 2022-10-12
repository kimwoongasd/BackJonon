n = int(input())
count = 0
for i in range(n):
    tmp = []
    a = input()
    for x in a:
        if len(tmp) == 0:
            tmp.append(x)
        else:
            if x in tmp:
                if tmp[-1] != x:
                    break
                else:
                    tmp.append(x)
            else:
                tmp.append(x)
    else:
        count += 1
print(count)