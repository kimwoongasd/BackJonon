t = int(input())

ch = [0] * 12
ch[1] = 1
ch[2] = 2
ch[3] = 4
for i in range(4, 12):
    ch[i] = ch[i - 3] + ch[i - 2] + ch[i - 1]
    
for i in range(t):
    n = int(input())
    print(ch[n])
