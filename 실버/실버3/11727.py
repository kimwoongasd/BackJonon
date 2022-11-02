n = int(input())

ch = [0] * 1002
ch[1] = 1
ch[2] = 3

for i in range(3, 1002):
    ch[i] = ((ch[i - 2] * 2) + ch[i - 1]) % 10007
    
print(ch[n])