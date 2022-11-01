t = int(input())

ch = [0] * 101
ch[1] = 1
ch[2] = 1
ch[3] = 1

for i in range(4, 101):
    ch[i] = ch[i - 2] + ch[i - 3]

for i in range(t):
    n = int(input())
    
    print(ch[n])