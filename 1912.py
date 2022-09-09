n = int(input())
number = list(map(int, input().split()))
ch = [-2147000000] * n
ch[0] = number[0]

for i in range(1, n):
    ch[i] = max(number[i], ch[i- 1] + number[i])
    
print(max(ch))