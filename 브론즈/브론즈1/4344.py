n = int(input())

for i in range(n):
    tem = list(map(int, input().split())) 
    avg = (sum(tem[1:]) / tem[0])
    count = 0
    for j in range(1, tem[0] + 1):
        if tem[j] > avg:
            count += 1
    res = count / tem[0] * 100
    print(f"{res:.3f}%")