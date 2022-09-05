c = int(input())

for _ in range(c):
    tem = list(map(int, input().split()))
    avg = sum(tem[1:]) / tem[0]
    count = 0
    for i in range(1, len(tem)):
        if tem[i] > avg:
            count += 1
        
    print(f"{(count / tem[0]) * 100:.3f}%")